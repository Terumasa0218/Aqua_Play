# Aqua_Play Art Direction Research

Reviewed: 2026-05-15 13:01 JST  
Phase: 0A - visual direction research only  
Repository source of truth: https://github.com/Terumasa0218/Aqua_Play

## Purpose

Before producing Blender assets, this report organizes possible visual directions for the first 1-tile waterway parts. The goal is not to copy AquaPlay, a specific game, or a demo video. The goal is to extract useful design principles, then create original waterway parts that can be judged in Unity from a top-down or isometric camera.

The user-provided references emphasize:

- AquaPlay-like modular water toys: blue waterways, colored gates, locks, pumps, wheels, boats, and connector logic.
- Cozy digital dioramas and builder demos: grid-aware terrain, low-poly/soft materials, asset-sheet workflows, small readable structures.
- Nostalgic or real-world water scenes: painted concrete drainage, moats, sand, aquaculture paddle wheels, and practical water machinery.

## Constraints

- Copyright and trade dress: do not reproduce exact AquaPlay color blocking, part silhouettes, icons, connector shapes, character/boat designs, or product layouts.
- Production limits: create assets in small batches. The default batch is 5 waterway variants, with a maximum of 20 variants before selecting a direction.
- Codex work limits: if the next batch is likely to be interrupted by context, time, or tool limits, stop at a clean boundary after committing/merging the completed batch.
- Unity-first use: the parts should remain readable in Unity, even if they are authored in Blender.
- Phase gate: after this report is merged to main, stop and discuss before creating assets.

## Direction Summary

Recommended anchor direction:

**Nostalgic sand-and-water diorama.**

This keeps the tactile appeal of AquaPlay but moves away from toy-like primary colors. It can combine sun-warmed sand, damp canal edges, small concrete or stone retaining walls, simple valves, and miniature water machinery. The mood should feel handmade, real, and slightly nostalgic, while the module boundaries remain clear for gameplay.

The first asset batch should intentionally test five different moods:

1. Sunbaked Sand Canal
2. Weathered Concrete U-Channel
3. Garden Stone Runnel
4. Muted Aquaculture Trough
5. Painted Urban Drain

These five are broad enough to compare mood, readability, originality, and Blender/Unity production cost.

## Reference Clusters

### 1. Modular Water Toy Systems

Examples: AquaPlay official product/about pages and the user-provided AquaPlay screenshots.

Good points:

- Very clear modular logic: water channels, locks, pumps, gates, cranes, boats, and connectors are immediately understandable.
- Strong cause-and-effect readability: players can infer where water flows and what interactive parts do.
- Raised rims and bright moving pieces make gameplay affordances visible.

Risks:

- The exact blue/yellow/red palette and part silhouettes are strongly tied to AquaPlay.
- A child-toy look may conflict with the desired nostalgic, real, or artful mood.
- Too much plastic gloss can make the game feel like a branded toy simulator instead of an original waterway builder.

What to borrow safely:

- Modular water logic.
- Raised canal walls.
- Simple gate/paddle/pump affordances.
- Clear connection points between tiles.

What to avoid:

- AquaPlay's exact color scheme, connector geometry, boat forms, labeled feature layout, and product-set composition.

### 2. Sandcastle And Beach-Moat Craft

Examples: Sandcastle on Steam and the user's stated interest in a SandCastle-like atmosphere.

Good points:

- Sand and water are naturally connected; moats, channels, erosion, and damp edges are intuitive.
- The mood can be nostalgic without looking like a toy.
- Small decorations such as shells, pebbles, driftwood, and seaweed can make repeated tiles feel handmade.

Risks:

- Sand colors can become low contrast, especially when viewed from above.
- Realistic erosion/detail can become expensive or noisy for early assets.
- A pure beach theme might narrow the world too early.

What to borrow safely:

- Compacted sand berms as channel walls.
- Damp darker sand near water.
- Small embedded objects, subtle footprints, and hand-shaped irregularity.
- Warm color temperature and soft surf-like water highlights.

### 3. Nostalgic Concrete Waterways

Examples: user-provided painted concrete waterway image, Japanese drainage/irrigation canal mood, and urban water-channel references.

Good points:

- Feels more real and memorable than plastic.
- Patina, moss, chipped paint, mineral streaks, and old repair marks can add history.
- Concrete U-channel geometry is readable and easy to modularize.

Risks:

- Can become too dark, dirty, or industrial.
- If it leans too realistic, it may clash with cozy diorama assets.
- Long straight concrete channels may look repetitive without small variations.

What to borrow safely:

- Rounded or chamfered concrete troughs.
- Faded blue/green painted surfaces.
- Hairline cracks, moss seams, water stains, and worn edges.
- Warm sunlight and shallow water reflections to keep the mood inviting.

### 4. Real Water Machinery And Aquaculture

Examples: user-provided paddle-wheel aerator image and real irrigation/aquaculture equipment.

Good points:

- Functional machinery makes water movement credible.
- Floats, paddles, simple frames, bolts, pipes, and mesh baskets can create distinctive silhouettes.
- Good source for later interactive props, not just static canal walls.

Risks:

- Industrial equipment can overpower the garden/diorama feeling.
- Bright blue/yellow industrial colors may accidentally drift back toward toy aesthetics.
- Complex wheel assemblies are better as later accessory assets than the first simple tile.

What to borrow safely:

- Muted utility colors.
- Simple paddle-wheel or float motifs as secondary details.
- Bolted frames, small pipe outlets, and practical water-control language.

### 5. Cozy Diorama Builders

Examples: Tiny Glade, Townscaper, Dorfromantik, SUMMERHOUSE, ISLANDERS, and Tiny World Builder.

Good points:

- Strong readability from an elevated camera.
- Soft silhouettes and procedural detail make simple pieces feel rich.
- Tile or grid awareness is useful for Aqua_Play's modular waterway design.
- These works show how a small asset vocabulary can create a large emotional range.

Risks:

- The cozy diorama look is familiar; copying the surface style too closely would feel derivative.
- Some references prioritize mood over functional water readability.
- Over-softening geometry could hide exact water path connections.

What to borrow safely:

- Readable silhouettes.
- Small detail clusters around functional structures.
- Hand-placed but grid-compatible composition.
- Controlled color palettes instead of loud primary colors.

### 6. Nature Restoration And Overgrowth

Examples: Cloud Gardens and Open Land-style nature restoration references.

Good points:

- Water can visually reward the player: damp soil, moss growth, reeds, small flowers, or restored ground.
- Adds progression fantasy without needing many mechanical parts.
- Works well with nostalgic concrete and garden canal directions.

Risks:

- Plants can visually obscure the waterway path.
- The restoration theme may become a second game concept if introduced too early.
- Too much foliage increases asset complexity.

What to borrow safely:

- Small moss seams and reed clusters near wet edges.
- Visual difference between dry, damp, and flowing states.
- Overgrowth as a later variant or upgrade layer.

### 7. Map And Terrain Style Playgrounds

Examples: Mapbox Standard Style Playground and similar 3D map customization demos.

Good points:

- Clear terrain color zoning and readable feature classes.
- Real-time lighting and theme changes suggest a useful Unity review setup.
- Roads/water/land/building separation is instructive for top-down legibility.

Risks:

- A map-style look can feel sterile or tool-like.
- Terrain colors alone do not provide tactile material charm.

What to borrow safely:

- Palette testing workflow.
- Separation of water, canal wall, land, and interactable accent colors.
- Checking every asset under day/dusk lighting before choosing a direction.

### 8. Art Playgrounds, Gardens, And Water Landscapes

Examples: Isamu Noguchi playscapes, Japanese garden motifs, stone paths, water basins, raked sand, and the user-provided Japanese garden/asset-sheet style screenshots.

Good points:

- Turns functional play space into sculpture and landscape.
- Sand, stone, water, bridges, basins, and abstract landforms can support a more mature mood.
- Strong fit for a modular garden-like water system.

Risks:

- Cultural motifs can become decorative shorthand if used without care.
- Too many theme-specific objects early may lock the project into a Japanese garden direction.
- Abstract sculpture can reduce gameplay clarity if it hides the water path.

What to borrow safely:

- Stone edging, raked sand hints, small bridges, and basin-like water details.
- Playful landform geometry.
- Calm asymmetry and restrained detail density.

## Candidate First Batch: 5 One-Tile Waterway Parts

All five should be the same functional type at first: a straight 1-tile waterway segment. Only the visual treatment changes. This keeps the comparison fair.

### A. Sunbaked Sand Canal

- Geometry: shallow dug channel with compacted sand berms and slightly uneven handmade edges.
- Palette: warm tan, damp ochre, pale blue-green water, tiny shell/pebble accents.
- Detail: darker wet rim, subtle footprints/tool marks, one or two embedded shells.
- Strength: closest to the SandCastle-like mood.
- Risk: may need contrast tuning so the water path stays clear.

### B. Weathered Concrete U-Channel

- Geometry: rounded U-shaped concrete trough with chipped edges and simple seams.
- Palette: faded gray concrete, moss green, mineral white, muted blue water.
- Detail: cracks, moss in corners, small rust stain or repair plate.
- Strength: nostalgic and original compared with toy waterways.
- Risk: can feel gloomy unless lighting and color warmth are controlled.

### C. Garden Stone Runnel

- Geometry: narrow water runnel bordered by irregular stones or cut stone blocks.
- Palette: muted stone gray, moss, dark wet soil, clear water, small plant accents.
- Detail: pebbles, tiny reeds, one stepping stone or edge stone variation.
- Strength: cozy, natural, and compatible with future garden assets.
- Risk: stone detail can get visually noisy in small tiles.

### D. Muted Aquaculture Trough

- Geometry: practical trough or channel with floats/pipes implied at the edges.
- Palette: desaturated blue-gray, off-white plastic, dull yellow utility accent, dark water.
- Detail: bolt heads, small pipe outlet, simple bracket, scuffed material.
- Strength: references real water machinery without copying AquaPlay.
- Risk: too much blue/yellow can become toy-like again.

### E. Painted Urban Drain

- Geometry: concrete channel with faded painted sides or mural-like water strokes.
- Palette: blue-green paint, gray concrete, sun-faded cream, dark shadowed water.
- Detail: worn paint, graffiti-like abstract flow lines, moss and stains.
- Strength: visually distinctive and nostalgic.
- Risk: stylized paint could distract from actual water direction.

## Evaluation Criteria

After rendering/importing the first 5 parts, compare them using:

- Water path readability at gameplay camera distance.
- Originality and distance from AquaPlay trade dress.
- Fit with the confirmed Unity-first direction.
- Modeling time in Blender.
- Material/shader cost in Unity.
- Ability to expand into turns, T-junctions, crosses, gates, pumps, and decorative props.
- Emotional fit: nostalgic, tactile, real, and slightly playful without becoming a direct toy clone.

## Recommended Next Step

Proceed to Phase 0B only after discussion.

Recommended Phase 0B scope:

- Produce the 5 straight 1-tile Blender waterway variants listed above.
- Export/import in a Unity-friendly structure.
- Capture preview images from a consistent camera angle.
- Commit, push, open a PR with `YYYY-MM-DD HH:mm JST` in the title, merge to main, then stop for user review.

Do not create turn pieces, intersections, gates, boats, wheels, or pumps until the visual direction is chosen.

## Source Notes

Web references checked during this report:

- AquaPlay official about page: https://www.aquaplay.com/aquaplay_en/about-aquaplay/
- AquaPlay official categories page: https://www.aquaplay.com/aquaplay_en/categories/
- Sandcastle on Steam: https://store.steampowered.com/app/3216520/Sandcastle/
- Tiny Glade on Steam: https://store.steampowered.com/app/2198150/Tiny_Glade/
- Townscaper on Steam: https://store.steampowered.com/app/1291340/Townscaper/
- Dorfromantik on Steam: https://store.steampowered.com/app/1455840/
- Cloud Gardens on Steam: https://store.steampowered.com/app/1372320/Cloud%20Gardens
- ISLANDERS on Steam: https://store.steampowered.com/app/1046030/ISLANDERS/
- SUMMERHOUSE on Steam: https://store.steampowered.com/app/2533960/SUMMERHOUSE/
- Tiny World Builder: https://tinyworld.build/
- Mapbox Standard Style Playground: https://docs.mapbox.com/playground/standard-style/
- Noguchi's Playscapes, The Noguchi Museum: https://www.noguchi.org/museum/exhibitions/view/noguchis-playscapes/
- Open Land Demo on Steam: https://store.steampowered.com/app/4623880/Open_Land_Demo/

User-provided image references are treated as visual direction inputs only and are not copied directly.
