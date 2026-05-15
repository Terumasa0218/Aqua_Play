"""Generate a deterministic modular block asset and export GLB/FBX files.

Run from the repository root with:
    blender --background --python blender/scripts/generate_modular_asset.py
"""

from __future__ import annotations

from pathlib import Path

import bpy


REPO_ROOT = Path(__file__).resolve().parents[2]
EXPORT_DIR = REPO_ROOT / "blender" / "exports"
ASSET_NAME = "modular_block"


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def create_material(name: str, color: tuple[float, float, float, float]) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    material.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = color
    material.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.85
    return material


def add_cube(name: str, location: tuple[float, float, float], scale: tuple[float, float, float], material: bpy.types.Material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)
    return obj


def build_asset() -> list[bpy.types.Object]:
    base_material = create_material("AP_Concrete_BlueGrey", (0.36, 0.45, 0.50, 1.0))
    trim_material = create_material("AP_Safety_Yellow", (1.0, 0.72, 0.12, 1.0))

    objects = [
        add_cube("AP_ModularBlock_Base", (0.0, 0.0, 0.25), (4.0, 4.0, 0.5), base_material),
        add_cube("AP_ModularBlock_BackWall", (0.0, 1.85, 1.5), (4.0, 0.3, 2.5), base_material),
        add_cube("AP_ModularBlock_LeftPillar", (-1.75, 0.0, 1.25), (0.35, 0.35, 2.0), trim_material),
        add_cube("AP_ModularBlock_RightPillar", (1.75, 0.0, 1.25), (0.35, 0.35, 2.0), trim_material),
        add_cube("AP_ModularBlock_TopTrim", (0.0, 1.65, 2.85), (4.0, 0.35, 0.3), trim_material),
    ]

    bpy.ops.object.empty_add(type="PLAIN_AXES", location=(0.0, 0.0, 0.0))
    root = bpy.context.object
    root.name = "AP_ModularBlock_Root"

    for obj in objects:
        obj.parent = root

    bpy.context.scene.unit_settings.system = "METRIC"
    bpy.context.scene.unit_settings.scale_length = 1.0
    return objects


def export_asset(objects: list[bpy.types.Object]) -> None:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]

    glb_path = EXPORT_DIR / f"{ASSET_NAME}.glb"
    fbx_path = EXPORT_DIR / f"{ASSET_NAME}.fbx"

    bpy.ops.export_scene.gltf(
        filepath=str(glb_path),
        export_format="GLB",
        use_selection=True,
        export_apply=True,
    )
    bpy.ops.export_scene.fbx(
        filepath=str(fbx_path),
        use_selection=True,
        apply_unit_scale=True,
        bake_space_transform=False,
    )

    print(f"Exported {glb_path}")
    print(f"Exported {fbx_path}")


def main() -> None:
    clear_scene()
    objects = build_asset()
    export_asset(objects)


if __name__ == "__main__":
    main()
