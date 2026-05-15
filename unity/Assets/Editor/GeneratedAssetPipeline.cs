using System.IO;
using UnityEditor;
using UnityEngine;

namespace AquaPlay.Editor
{
    public static class GeneratedAssetPipeline
    {
        private const string GeneratedRoot = "Assets/Generated";
        private const string ImportedRoot = GeneratedRoot + "/Imported";
        private const string PrefabRoot = GeneratedRoot + "/Prefabs";
        private const string BlenderExportRelativePath = "../blender/exports";

        public static void Run()
        {
            EnsureDirectory(GeneratedRoot);
            EnsureDirectory(ImportedRoot);
            EnsureDirectory(PrefabRoot);

            ImportBlenderExports();
            AssetDatabase.Refresh();
            CreatePrefabsForImportedModels();
            AssetDatabase.SaveAssets();
            AssetDatabase.Refresh();

            Debug.Log("Generated asset pipeline completed.");
        }

        private static void ImportBlenderExports()
        {
            string projectRoot = Directory.GetParent(Application.dataPath)!.FullName;
            string exportRoot = Path.GetFullPath(Path.Combine(projectRoot, BlenderExportRelativePath));

            if (!Directory.Exists(exportRoot))
            {
                Debug.LogWarning($"Blender export directory not found: {exportRoot}");
                return;
            }

            foreach (string sourcePath in Directory.EnumerateFiles(exportRoot, "*.*", SearchOption.AllDirectories))
            {
                string extension = Path.GetExtension(sourcePath).ToLowerInvariant();
                if (extension != ".glb" && extension != ".fbx")
                {
                    continue;
                }

                string relativePath = sourcePath.Substring(exportRoot.Length).TrimStart(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar);
                string destinationAssetPath = ToAssetPath(Path.Combine(ImportedRoot, relativePath));
                ValidateGeneratedAssetPath(destinationAssetPath);

                string absoluteDestinationPath = Path.Combine(projectRoot, destinationAssetPath);
                Directory.CreateDirectory(Path.GetDirectoryName(absoluteDestinationPath)!);
                File.Copy(sourcePath, absoluteDestinationPath, overwrite: true);
                Debug.Log($"Copied generated model: {destinationAssetPath}");
            }
        }

        private static void CreatePrefabsForImportedModels()
        {
            string[] modelGuids = AssetDatabase.FindAssets("t:Model", new[] { ImportedRoot });

            foreach (string guid in modelGuids)
            {
                string modelAssetPath = AssetDatabase.GUIDToAssetPath(guid);
                ValidateGeneratedAssetPath(modelAssetPath);

                GameObject model = AssetDatabase.LoadAssetAtPath<GameObject>(modelAssetPath);
                if (model == null)
                {
                    continue;
                }

                string prefabName = Path.GetFileNameWithoutExtension(modelAssetPath) + ".prefab";
                string prefabPath = ToAssetPath(Path.Combine(PrefabRoot, prefabName));
                ValidateGeneratedAssetPath(prefabPath);

                GameObject instance = PrefabUtility.InstantiatePrefab(model) as GameObject;
                if (instance == null)
                {
                    Debug.LogWarning($"Unable to instantiate model: {modelAssetPath}");
                    continue;
                }

                try
                {
                    PrefabUtility.SaveAsPrefabAsset(instance, prefabPath);
                    Debug.Log($"Generated prefab: {prefabPath}");
                }
                finally
                {
                    Object.DestroyImmediate(instance);
                }
            }
        }

        private static void EnsureDirectory(string assetPath)
        {
            ValidateGeneratedAssetPath(assetPath);

            if (AssetDatabase.IsValidFolder(assetPath))
            {
                return;
            }

            string[] parts = assetPath.Split('/');
            string current = parts[0];

            for (int index = 1; index < parts.Length; index++)
            {
                string next = current + "/" + parts[index];
                if (!AssetDatabase.IsValidFolder(next))
                {
                    AssetDatabase.CreateFolder(current, parts[index]);
                }
                current = next;
            }
        }

        private static string ToAssetPath(string path)
        {
            return path.Replace('\\', '/');
        }

        private static void ValidateGeneratedAssetPath(string assetPath)
        {
            string normalized = ToAssetPath(assetPath);
            if (!normalized.StartsWith(GeneratedRoot))
            {
                throw new System.InvalidOperationException($"Refusing to write outside {GeneratedRoot}: {assetPath}");
            }
        }
    }
}
