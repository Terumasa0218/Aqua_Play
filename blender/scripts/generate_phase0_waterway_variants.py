"""Generate Phase 0B straight waterway visual variants.

Run from the repository root with:
    blender --background --python blender/scripts/generate_phase0_waterway_variants.py
"""

from __future__ import annotations

from math import radians
from pathlib import Path

import bpy


REPO_ROOT = Path(__file__).resolve().parents[2]
EXPORT_DIR = REPO_ROOT / "blender" / "exports" / "phase0_waterway_variants"
BLEND_PATH = EXPORT_DIR / "phase0_waterway_variants.blend"
PREVIEW_PATH = EXPORT_DIR / "phase0_waterway_variants_overview.png"
TILE_SIZE = 4.0


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def create_material(
    name: str,
    color: tuple[float, float, float, float],
    *,
    roughness: float = 0.85,
    metallic: float = 0.0,
    alpha: float | None = None,
) -> bpy.types.Material:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    if alpha is not None:
        bsdf.inputs["Alpha"].default_value = alpha
        material.blend_method = "BLEND"
        material.use_screen_refraction = True
        material.show_transparent_back = True
    return material


def add_cube(
    name: str,
    location: tuple[float, float, float],
    scale: tuple[float, float, float],
    material: bpy.types.Material,
    *,
    bevel: float = 0.0,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)
    if bevel > 0:
        modifier = obj.modifiers.new(f"{name}_soft_edges", "BEVEL")
        modifier.width = bevel
        modifier.segments = 3
        modifier.affect = "EDGES"
        obj.modifiers.new(f"{name}_weighted_normals", "WEIGHTED_NORMAL")
    return obj


def add_cylinder(
    name: str,
    location: tuple[float, float, float],
    radius: float,
    depth: float,
    material: bpy.types.Material,
    *,
    rotation: tuple[float, float, float] = (0.0, 0.0, 0.0),
    vertices: int = 24,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=location, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    obj.modifiers.new(f"{name}_weighted_normals", "WEIGHTED_NORMAL")
    return obj


def add_uv_sphere(
    name: str,
    location: tuple[float, float, float],
    scale: tuple[float, float, float],
    material: bpy.types.Material,
    *,
    segments: int = 16,
    rings: int = 8,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=1.0, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(material)
    obj.modifiers.new(f"{name}_weighted_normals", "WEIGHTED_NORMAL")
    return obj


def add_water(name: str, material: bpy.types.Material) -> list[bpy.types.Object]:
    water = add_cube(name, (0.0, 0.0, 0.19), (1.12, 3.72, 0.035), material, bevel=0.08)
    highlight_a = add_cube(f"{name}_highlight_a", (-0.22, -0.75, 0.22), (0.05, 0.95, 0.012), material, bevel=0.04)
    highlight_b = add_cube(f"{name}_highlight_b", (0.28, 0.55, 0.22), (0.045, 0.80, 0.012), material, bevel=0.04)
    return [water, highlight_a, highlight_b]


def collect_variant(name: str, objects: list[bpy.types.Object]) -> bpy.types.Collection:
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    for obj in objects:
        for existing in obj.users_collection:
            existing.objects.unlink(obj)
        collection.objects.link(obj)
    return collection


def move_collection(collection: bpy.types.Collection, offset_x: float) -> None:
    for obj in collection.objects:
        obj.location.x += offset_x


def add_label(text: str, x: float) -> bpy.types.Object:
    bpy.ops.object.text_add(location=(x, -2.75, 0.04), rotation=(0.0, 0.0, 0.0))
    obj = bpy.context.object
    obj.name = f"Label_{text.replace(' ', '_')}"
    obj.data.body = text
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    obj.data.size = 0.26
    obj.data.materials.append(MATS["label"])
    return obj


def create_sunbaked_sand() -> bpy.types.Collection:
    m = MATS
    objects = [
        add_cube("sand_tile_base", (0.0, 0.0, -0.08), (TILE_SIZE, TILE_SIZE, 0.16), m["sand"], bevel=0.12),
        add_cube("sand_left_berm", (-0.82, 0.0, 0.20), (0.52, 3.70, 0.34), m["sand_berm"], bevel=0.22),
        add_cube("sand_right_berm", (0.82, 0.0, 0.20), (0.50, 3.62, 0.31), m["sand_berm"], bevel=0.22),
        *add_water("sand_water", m["water_soft"]),
    ]
    for i, (x, y, sx, sy) in enumerate(
        [(-1.45, -1.18, 0.08, 0.11), (-1.25, -0.98, 0.07, 0.10), (1.34, 1.14, 0.06, 0.10), (1.53, 1.30, 0.07, 0.11)]
    ):
        objects.append(add_uv_sphere(f"sand_footprint_{i}", (x, y, 0.035), (sx, sy, 0.010), m["sand_wet"], segments=12, rings=6))
    for i, (x, y, scale) in enumerate([(-1.35, 0.95, 0.08), (1.32, -0.72, 0.06), (1.55, -1.42, 0.05)]):
        objects.append(add_uv_sphere(f"sand_pebble_shell_{i}", (x, y, 0.10), (scale, scale * 0.65, 0.025), m["shell"], segments=12, rings=6))
    return collect_variant("sunbaked_sand_canal", objects)


def create_weathered_concrete() -> bpy.types.Collection:
    m = MATS
    objects = [
        add_cube("concrete_tile_base", (0.0, 0.0, -0.10), (TILE_SIZE, TILE_SIZE, 0.20), m["concrete"], bevel=0.08),
        add_cube("concrete_channel_floor", (0.0, 0.0, 0.04), (1.36, 3.82, 0.12), m["concrete_dark"], bevel=0.06),
        add_cube("concrete_left_wall", (-0.86, 0.0, 0.35), (0.36, 3.88, 0.70), m["concrete"], bevel=0.09),
        add_cube("concrete_right_wall", (0.86, 0.0, 0.35), (0.36, 3.88, 0.70), m["concrete"], bevel=0.09),
        *add_water("concrete_water", m["water_clear"]),
        add_cube("concrete_moss_left", (-0.64, -0.80, 0.73), (0.08, 1.00, 0.045), m["moss"], bevel=0.03),
        add_cube("concrete_moss_right", (0.64, 0.82, 0.73), (0.08, 0.82, 0.045), m["moss"], bevel=0.03),
        add_cube("concrete_repair_plate", (1.12, -1.05, 0.25), (0.42, 0.56, 0.035), m["rust_plate"], bevel=0.02),
    ]
    for i, (x, y, rot) in enumerate([(-1.10, 0.35, 16), (1.22, 1.18, -20), (-0.20, -1.48, 6)]):
        crack = add_cube(f"concrete_hairline_crack_{i}", (x, y, 0.035), (0.035, 0.60, 0.012), m["crack"], bevel=0.01)
        crack.rotation_euler.z = radians(rot)
        objects.append(crack)
    return collect_variant("weathered_concrete_u_channel", objects)


def create_garden_stone() -> bpy.types.Collection:
    m = MATS
    objects = [
        add_cube("garden_tile_base", (0.0, 0.0, -0.08), (TILE_SIZE, TILE_SIZE, 0.16), m["soil"], bevel=0.08),
        add_cube("garden_grass_patch_a", (-1.35, 1.10, 0.02), (0.96, 0.82, 0.045), m["grass"], bevel=0.18),
        add_cube("garden_grass_patch_b", (1.38, -1.15, 0.02), (0.90, 0.76, 0.045), m["grass"], bevel=0.18),
        *add_water("garden_water", m["water_green"]),
    ]
    stone_positions = [
        (-0.78, -1.50, 0.20, 0.15), (-0.82, -0.78, 0.16, 0.12), (-0.78, 0.00, 0.18, 0.14), (-0.84, 0.82, 0.15, 0.13), (-0.76, 1.55, 0.22, 0.15),
        (0.78, -1.58, 0.17, 0.14), (0.84, -0.86, 0.20, 0.13), (0.79, -0.05, 0.16, 0.12), (0.86, 0.75, 0.21, 0.14), (0.78, 1.48, 0.18, 0.13),
    ]
    for i, (x, y, sx, sy) in enumerate(stone_positions):
        objects.append(add_uv_sphere(f"garden_edge_stone_{i}", (x, y, 0.22), (sx, sy, 0.085), m["stone"], segments=16, rings=8))
    for i, (x, y) in enumerate([(-1.30, -0.32), (-1.20, -0.18), (1.26, 1.15), (1.36, 1.30)]):
        objects.append(add_cylinder(f"garden_reed_{i}", (x, y, 0.23), 0.025, 0.50, m["reed"], rotation=(0.0, 0.0, 0.0), vertices=8))
    objects.append(add_cube("garden_stepping_stone", (0.0, 0.98, 0.29), (0.78, 0.32, 0.08), m["stone_light"], bevel=0.12))
    return collect_variant("garden_stone_runnel", objects)


def create_aquaculture_trough() -> bpy.types.Collection:
    m = MATS
    objects = [
        add_cube("aqua_tile_base", (0.0, 0.0, -0.09), (TILE_SIZE, TILE_SIZE, 0.18), m["utility_base"], bevel=0.08),
        add_cube("aqua_trough_floor", (0.0, 0.0, 0.04), (1.40, 3.78, 0.14), m["off_white"], bevel=0.06),
        add_cube("aqua_left_wall", (-0.86, 0.0, 0.34), (0.34, 3.86, 0.68), m["blue_grey"], bevel=0.08),
        add_cube("aqua_right_wall", (0.86, 0.0, 0.34), (0.34, 3.86, 0.68), m["blue_grey"], bevel=0.08),
        *add_water("aqua_water", m["water_dark"]),
        add_cylinder("aqua_pipe_cross", (0.0, -1.20, 0.56), 0.08, 2.10, m["pipe"], rotation=(0.0, radians(90), 0.0), vertices=20),
        add_cube("aqua_utility_bracket_left", (-1.10, -1.20, 0.56), (0.18, 0.26, 0.34), m["utility_yellow"], bevel=0.03),
        add_cube("aqua_utility_bracket_right", (1.10, -1.20, 0.56), (0.18, 0.26, 0.34), m["utility_yellow"], bevel=0.03),
    ]
    for i, x in enumerate([-1.28, 1.28]):
        objects.append(add_cube(f"aqua_side_float_{i}", (x, 1.05, 0.18), (0.36, 0.98, 0.24), m["float_blue"], bevel=0.16))
    for i, (x, y) in enumerate([(-0.82, 1.55), (0.82, 1.55), (-0.82, -1.55), (0.82, -1.55)]):
        objects.append(add_cylinder(f"aqua_bolt_{i}", (x, y, 0.72), 0.045, 0.025, m["metal"], vertices=12))
    return collect_variant("muted_aquaculture_trough", objects)


def create_painted_urban() -> bpy.types.Collection:
    m = MATS
    objects = [
        add_cube("urban_tile_base", (0.0, 0.0, -0.10), (TILE_SIZE, TILE_SIZE, 0.20), m["urban_concrete"], bevel=0.08),
        add_cube("urban_channel_floor", (0.0, 0.0, 0.035), (1.42, 3.82, 0.11), m["urban_shadow"], bevel=0.05),
        add_cube("urban_left_wall", (-0.88, 0.0, 0.36), (0.36, 3.88, 0.72), m["urban_paint"], bevel=0.08),
        add_cube("urban_right_wall", (0.88, 0.0, 0.36), (0.36, 3.88, 0.72), m["urban_paint_green"], bevel=0.08),
        *add_water("urban_water", m["water_inky"]),
        add_cube("urban_faded_panel", (-1.18, 0.62, 0.60), (0.035, 1.15, 0.34), m["faded_cream"], bevel=0.02),
        add_cube("urban_moss_shadow", (0.64, -0.92, 0.73), (0.10, 0.98, 0.045), m["moss_dark"], bevel=0.03),
    ]
    for i, (x, y, length, rot, mat) in enumerate(
        [(-0.95, -0.98, 0.90, 18, m["flow_line"]), (0.95, 0.45, 1.00, -14, m["flow_line"]), (-0.18, 1.08, 0.72, 6, m["flow_line_green"])]
    ):
        line = add_cube(f"urban_painted_flow_line_{i}", (x, y, 0.76), (0.045, length, 0.030), mat, bevel=0.03)
        line.rotation_euler.z = radians(rot)
        objects.append(line)
    return collect_variant("painted_urban_drain", objects)


def export_collection(collection: bpy.types.Collection) -> None:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    bpy.ops.object.select_all(action="DESELECT")
    for obj in collection.objects:
        obj.select_set(True)
    active = next(iter(collection.objects))
    bpy.context.view_layer.objects.active = active

    slug = collection.name
    glb_path = EXPORT_DIR / f"{slug}.glb"
    fbx_path = EXPORT_DIR / f"{slug}.fbx"

    bpy.ops.export_scene.gltf(filepath=str(glb_path), export_format="GLB", use_selection=True, export_apply=True)
    bpy.ops.export_scene.fbx(filepath=str(fbx_path), use_selection=True, apply_unit_scale=True, bake_space_transform=False)
    print(f"Exported {glb_path}")
    print(f"Exported {fbx_path}")


def setup_preview() -> None:
    bpy.ops.object.light_add(type="AREA", location=(0.0, -5.5, 8.0))
    light = bpy.context.object
    light.name = "Preview_Key_Area_Light"
    light.data.energy = 700.0
    light.data.size = 8.0

    bpy.ops.object.camera_add(location=(0.0, -0.35, 18.0), rotation=(0.0, 0.0, 0.0))
    camera = bpy.context.object
    camera.name = "Preview_Orthographic_Camera"
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 28.0
    bpy.context.scene.camera = camera

    bpy.context.scene.render.engine = "BLENDER_EEVEE"
    bpy.context.scene.eevee.taa_render_samples = 64
    bpy.context.scene.render.resolution_x = 2200
    bpy.context.scene.render.resolution_y = 1000
    bpy.context.scene.view_settings.view_transform = "Filmic"
    bpy.context.scene.view_settings.look = "Medium High Contrast"


def save_preview() -> None:
    bpy.context.scene.render.filepath = str(PREVIEW_PATH)
    bpy.ops.render.render(write_still=True)
    print(f"Rendered {PREVIEW_PATH}")


MATS: dict[str, bpy.types.Material] = {}


def create_materials() -> None:
    MATS.update(
        {
            "sand": create_material("AP0_Sand_Dry", (0.76, 0.58, 0.34, 1.0)),
            "sand_berm": create_material("AP0_Sand_Berm_DampEdge", (0.66, 0.49, 0.27, 1.0)),
            "sand_wet": create_material("AP0_Sand_Wet_Footprint", (0.43, 0.31, 0.18, 1.0)),
            "shell": create_material("AP0_Shell_Pebble", (0.86, 0.78, 0.62, 1.0)),
            "concrete": create_material("AP0_Concrete_WarmGrey", (0.50, 0.50, 0.45, 1.0)),
            "concrete_dark": create_material("AP0_Concrete_WetFloor", (0.32, 0.34, 0.33, 1.0)),
            "crack": create_material("AP0_Concrete_HairlineCrack", (0.10, 0.10, 0.09, 1.0)),
            "moss": create_material("AP0_Moss_Green", (0.22, 0.36, 0.18, 1.0)),
            "rust_plate": create_material("AP0_RepairPlate_Rust", (0.45, 0.23, 0.13, 1.0), metallic=0.2),
            "soil": create_material("AP0_Garden_DarkSoil", (0.30, 0.24, 0.17, 1.0)),
            "grass": create_material("AP0_Garden_MossGrass", (0.35, 0.54, 0.29, 1.0)),
            "stone": create_material("AP0_Garden_Stone", (0.45, 0.45, 0.40, 1.0)),
            "stone_light": create_material("AP0_Garden_LightStone", (0.58, 0.56, 0.49, 1.0)),
            "reed": create_material("AP0_Garden_Reed", (0.36, 0.42, 0.19, 1.0)),
            "utility_base": create_material("AP0_Utility_Base", (0.43, 0.47, 0.47, 1.0)),
            "off_white": create_material("AP0_Utility_OffWhite", (0.78, 0.77, 0.68, 1.0)),
            "blue_grey": create_material("AP0_Utility_BlueGrey", (0.25, 0.39, 0.48, 1.0)),
            "float_blue": create_material("AP0_Utility_MutedFloatBlue", (0.18, 0.34, 0.48, 1.0)),
            "utility_yellow": create_material("AP0_Utility_DullYellow", (0.74, 0.56, 0.20, 1.0)),
            "pipe": create_material("AP0_Utility_DarkPipe", (0.16, 0.18, 0.18, 1.0), metallic=0.1),
            "metal": create_material("AP0_Utility_Bolts", (0.32, 0.33, 0.32, 1.0), metallic=0.3),
            "urban_concrete": create_material("AP0_Urban_Concrete", (0.38, 0.39, 0.36, 1.0)),
            "urban_shadow": create_material("AP0_Urban_ShadowedFloor", (0.13, 0.16, 0.17, 1.0)),
            "urban_paint": create_material("AP0_Urban_FadedBluePaint", (0.20, 0.42, 0.50, 1.0)),
            "urban_paint_green": create_material("AP0_Urban_FadedGreenPaint", (0.42, 0.53, 0.35, 1.0)),
            "faded_cream": create_material("AP0_Urban_FadedCream", (0.74, 0.70, 0.52, 1.0)),
            "moss_dark": create_material("AP0_Urban_DarkMoss", (0.13, 0.25, 0.16, 1.0)),
            "flow_line": create_material("AP0_Urban_PaleFlowLine", (0.78, 0.86, 0.86, 1.0)),
            "flow_line_green": create_material("AP0_Urban_GreenFlowLine", (0.65, 0.78, 0.44, 1.0)),
            "water_soft": create_material("AP0_Water_SoftBeach", (0.43, 0.78, 0.88, 0.72), roughness=0.25, alpha=0.72),
            "water_clear": create_material("AP0_Water_ClearConcrete", (0.30, 0.62, 0.72, 0.70), roughness=0.18, alpha=0.70),
            "water_green": create_material("AP0_Water_GardenGreen", (0.31, 0.60, 0.55, 0.72), roughness=0.23, alpha=0.72),
            "water_dark": create_material("AP0_Water_DeepUtility", (0.13, 0.33, 0.42, 0.75), roughness=0.20, alpha=0.75),
            "water_inky": create_material("AP0_Water_InkyUrban", (0.10, 0.28, 0.33, 0.76), roughness=0.22, alpha=0.76),
            "label": create_material("AP0_Label_WarmLight", (0.88, 0.84, 0.70, 1.0)),
        }
    )


def main() -> None:
    clear_scene()
    create_materials()

    collections = [
        create_sunbaked_sand(),
        create_weathered_concrete(),
        create_garden_stone(),
        create_aquaculture_trough(),
        create_painted_urban(),
    ]

    for collection in collections:
        export_collection(collection)

    for index, collection in enumerate(collections):
        x = (index - 2) * 5.0
        move_collection(collection, x)
        add_label(collection.name.replace("_", " "), x)

    bpy.context.scene.unit_settings.system = "METRIC"
    bpy.context.scene.unit_settings.scale_length = 1.0

    setup_preview()
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    save_preview()


if __name__ == "__main__":
    main()
