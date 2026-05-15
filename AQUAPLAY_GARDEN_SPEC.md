# Aqua_Play Game Design Spec v0.6

Unity / C# / 3D top-down / grid placement / toy waterway garden simulation

## 0. Purpose

This document defines the game design, MVP scope, core systems, and implementation phases for Aqua_Play.

The active engine direction is Unity. Earlier Godot references are considered superseded. The project may be renamed later, but `Aqua_Play` is the working project name for now.

The MVP is fixed around the following baseline:

- canal placement,
- pump activation,
- symbolic water amount,
- water level display,
- overflow,
- wetness,
- water wheel coin generation,
- light wind effect,
- gradual part purchasing and garden growth.

Buckets, shishi-odoshi, dams, waterfalls, large basins, terrain digging, and advanced water events are attractive future ideas, but they are not part of the minimum MVP.

## 1. Game Concept

Aqua_Play is a small 3D garden simulation about assembling toy-like plastic waterway parts.

The player starts with a small garden grid. They place canals, pumps, water wheels, and decorations to design a visible water flow. Flowing water turns wheels, creates coins, and lets the player buy more parts and expand the garden.

This is not a realistic fluid simulation. The important experience is understandable, charming, toy-like water behavior that feels good to watch.

Core feelings:

- connecting waterways is satisfying,
- water movement is readable,
- water levels visibly rise and fall,
- overflow leaves wet ground behind,
- water wheels feel rewarding,
- wind gives the garden a living atmosphere,
- coins slowly grow the garden,
- appearance matters as much as efficiency.

## 2. Experience Target

One-line experience:

```text
Build a small toy water garden and grow it into a personal water-powered diorama.
```

The player should feel:

- "I understand where the water is going."
- "This little system is alive."
- "I want to make it prettier and more efficient."
- "One more part will make the network better."

## 3. Visual Direction

The visual target is toy garden diorama, not industrial simulator.

Direction:

- low-poly,
- stylized,
- bright garden,
- soft lighting,
- top-down 3D camera,
- readable grid,
- plastic toy waterway feel,
- clear water level feedback,
- wet ground feedback,
- small dense diorama composition.

Theme candidates for later:

- plastic toy waterway,
- western garden,
- Japanese garden,
- sandbox,
- science museum experiment kit,
- wooden waterway,
- stone waterway,
- tiny greenhouse,
- summer backyard.

Early theme differences should be visual only. Mechanical differences can wait until balance is stable.

## 4. Core Game Loop

Minimum loop:

```text
place waterway parts
start pump
water flows
water level rises
overflow wets ground
water wheel rotates
coins increase
buy new parts
expand the garden
build a more interesting flow
```

Long-term loop:

```text
build small flow
earn from water wheels
expand waterways
add branches, storage, wind, and decorations
balance appearance and efficiency
unlock themes and advanced water events
```

## 5. Technical Direction

Use Unity and C#.

Primary implementation style:

- 3D top-down camera,
- grid-based placement,
- tile-connected waterway parts,
- symbolic water simulation,
- data-driven part definitions,
- prefab-based visuals,
- Unity editor tooling for generated asset import.

Do not use real fluid simulation for MVP.

Why symbolic water:

- easier to implement,
- easier to debug,
- easier to tune,
- clear for players,
- stable for AI-assisted development,
- well matched to toy-like water behavior.

## 6. World Units

### 6.1 Water Unit

Water is measured in WU.

Example:

```text
100 WU = one second of base pump output
```

### 6.2 Flow Rate

Flow rate is measured in WU/sec.

### 6.3 Tick

Simulation should use a fixed tick. MVP can use:

```text
0.25 sec/tick
```

### 6.4 Grid Unit

One grid cell represents one part footprint. MVP starts with a 10x10 garden.

### 6.5 Height

Height is future scope. MVP can store height as `0` everywhere or omit it entirely until waterfalls and terrain matter.

## 7. Resources

### Coin

Main MVP currency.

Used for:

- buying canals,
- buying water wheels,
- later buying decorative or advanced parts.

### Water

Water is a gameplay signal, not a strict physical volume in MVP.

MVP does not require strict conservation. Later storage, dams, and tanks may require stricter accounting.

### Energy

Energy is future scope. It may be introduced if wind wheels, drills, gates, or powered devices need a separate resource.

### Soil

Soil is future scope. MVP only needs dry and wet ground states.

### Wind

Wind exists in MVP as a light effect and tiny bonus influence.

Wind should:

- animate the garden,
- lightly affect water wheels,
- provide very small coin income,
- never replace water as the main system.

## 8. Grid and Terrain

MVP grid state:

- empty ground,
- occupied by part,
- wet ground visual,
- blocked cell if needed.

Future terrain state:

- trench,
- mound,
- high ground,
- low ground,
- water pool,
- decorative bed.

MVP should avoid terrain preparation requirements. Placement should be easy first.

## 9. Waterway Parts

Each waterway part has:

- grid position,
- rotation,
- connection directions,
- capacity,
- current water amount,
- water level,
- outgoing flow,
- visual flow intensity,
- overflow behavior.

Connection directions:

- north,
- east,
- south,
- west.

MVP parts:

| Part | Role |
| --- | --- |
| Ground Tile | Base garden cell. |
| Wet Ground Tile | Wet visual state. |
| Straight Canal | Basic straight flow. |
| Corner Canal | Turns flow. |
| Mini Circulation Pump | Initial water source. |
| Water Wheel | Revenue device moved by water and light wind. |

Later part candidates:

| Part | Role |
| --- | --- |
| T Junction | Branching. |
| Cross Junction | Four-way branch. |
| Wind Paddle | Wind-focused wheel. |
| Storage Tank | Temporary storage. |
| Small Dam | Stored water. |
| Gate | Release control. |
| Waterfall Drop | Height and fall effect. |
| Decorative Plant | Atmosphere. |
| Bridge | Decorative crossing. |
| Toy Boat | Flow animation. |

Future-only candidates:

- Tipping Bucket,
- Shishi-odoshi,
- Large Basin,
- Splash Ramp,
- Flow Splitter,
- Drill Car,
- Charging Station.

## 10. Symbolic Water Simulation

### 10.1 Basic Rule

Each tick:

1. Pumps add water to their output cell or connected part.
2. Parts inspect connected neighbors.
3. Flow is distributed to valid outputs.
4. Water amount is updated through a double buffer.
5. Water level is recalculated.
6. Overflow is applied.
7. Wetness is updated.
8. Visual flow intensity is updated.

### 10.2 Double Buffer

Use double buffering to avoid order-dependent results:

```text
currentWater[] -> calculate deltas -> nextWater[]
```

### 10.3 Flow

MVP flow can be intentionally simple:

```text
available = current_water * output_ratio
per_output = available / connected_output_count
```

Apply a small loss rate if needed for stability:

```text
received = sent * (1.0 - loss_rate)
```

### 10.4 Minimum Flow

Very tiny flows can be clamped:

```text
if flow_rate < minimum_flow_rate:
    flow_rate = 0
```

This keeps visuals readable and avoids noisy trickle states.

## 11. Water Level

Water level is visualized from the ratio:

```text
water_level = current_water / capacity
```

Suggested levels:

| Ratio | Visual |
| --- | --- |
| 0 | empty |
| 0.01-0.33 | low |
| 0.34-0.66 | medium |
| 0.67-1.0 | high |
| > 1.0 | overflow |

Unity implementation options:

- scale a water mesh vertically,
- reveal a water surface with shader properties,
- swap simple visual states,
- use particles only as secondary feedback.

MVP should pick the simplest readable option.

## 12. Overflow and Wetness

Overflow occurs when:

```text
current_water > capacity
```

Overflow amount:

```text
overflow_amount = current_water - capacity
current_water = capacity
```

MVP wetness:

- mark the part cell or neighboring ground as wet,
- increase wetness value,
- gradually dry over time.

Wetness visual:

- darker ground material,
- slight shine,
- optional small puddle decal later.

Drying:

```text
wetness -= dry_rate * delta_time
```

MVP does not need weather.

## 13. Water Visuals

Water should be readable before it is realistic.

MVP visual requirements:

- show whether a part contains water,
- show rough level,
- show flow direction or movement,
- show overflow clearly,
- avoid visual clutter.

Possible Unity components:

- simple mesh renderer for water surface,
- material color or alpha changes,
- scrolling normal map later,
- particle splash for overflow later,
- line or arrow debug overlay for early testing.

## 14. Wind System

Wind has:

- `wind_power` from 0 to 100,
- slow variation over time,
- optional gusts later.

Water wheel rotation can combine water and wind:

```text
water_force = current_flow_rate / capacity
wind_force = wind_power / 100
rotation_power = water_force * 0.85 + wind_force * 0.15
```

Wind-only revenue should be tiny:

```text
coin_gain = wind_bonus_coin_rate * rotation_power * delta_time
```

Wind's job is atmosphere and light support, not the main economy.

## 15. Pump System

MVP pump:

- Mini Circulation Pump,
- one initial pump,
- manually activated with Space or UI button,
- fixed output rate,
- simple state machine.

States:

```text
READY
ACTIVE
RECHARGING
```

MVP can use manual activation. Automatic pumps may be added later.

## 16. Water Wheel

Water wheels convert flow into rotation and coins.

MVP behavior:

- rotate from water flow,
- rotate slightly from wind,
- generate coins while rotating,
- visibly communicate power.

Example:

```text
rotation_speed = rotation_power * max_rotation_speed
coin_gain = coin_rate * rotation_power * delta_time
```

The water wheel is the first satisfying reward device.

## 17. Economy and Prices

MVP prices:

| Part | Cost |
| --- | --- |
| Straight Canal | 5 |
| Corner Canal | 5 |
| Water Wheel | 30 |
| Mini Circulation Pump | Initial fixed part |
| Delete | 0 |

Future price candidates:

| Part | Cost |
| --- | --- |
| T Junction | 10 |
| Cross Junction | 15 |
| Wind Paddle | 70 |
| Storage Tank | 40 |
| Small Dam | 25 |
| Gate | 20 |
| Waterfall Drop | 50 |

Prices are provisional. MVP only needs to prove that buying, placing, earning, and expanding feels good.

## 18. UI

MVP UI:

- current coins,
- selected part,
- part cost,
- pump state,
- wind power,
- simple placement/delete mode,
- optional debug toggle.

Debug UI:

- selected cell coordinate,
- part type,
- water amount,
- water level,
- flow rate,
- wetness,
- connections.

Controls:

| Action | Input |
| --- | --- |
| Select part | UI button |
| Place | Left click |
| Rotate | R |
| Delete mode | Delete tool or key |
| Pump | Space or UI button |
| Camera pan/zoom | Standard Unity camera controls for prototype |

## 19. Unity Architecture

Suggested runtime systems:

| System | Responsibility |
| --- | --- |
| GameManager | High-level state and bootstrapping. |
| GridManager | Grid coordinates, occupancy, cell lookup. |
| PlacementController | Selection, preview, rotation, placement, deletion. |
| PartDefinition | Data for part cost, capacity, prefab, connections. |
| WaterPart | Runtime state for placed water-capable parts. |
| WaterSimulation | Tick-based symbolic water updates. |
| WetnessSystem | Wet ground state and drying. |
| EconomyManager | Coins and purchase validation. |
| PumpController | Pump state and water output. |
| WaterWheel | Rotation and coin generation. |
| WindManager | Wind power and visual influence. |
| UIManager | HUD and tool selection. |

Prefer simple C# classes and MonoBehaviours first. Add ScriptableObjects for part definitions when duplication appears.

## 20. Implementation Phases

### Phase 0: Unity Foundation

Purpose: project foundation.

Implement:

- Unity project under `unity/`,
- 10x10 grid,
- top-down 3D camera,
- garden stage,
- cell click detection,
- basic UI display.

Done when:

- grid appears,
- camera can view the garden,
- clicking a cell shows coordinates.

### Phase 1: Part Placement

Purpose: place parts.

Implement:

- Straight Canal,
- Corner Canal,
- Water Wheel,
- Mini Circulation Pump,
- rotation,
- deletion,
- connection directions,
- placed part data.

Done when:

- player can select and place parts,
- R rotates,
- delete works,
- connections are visible in debug data.

### Phase 2: Pump and Water Simulation

Purpose: make symbolic water move.

Implement:

- pump state,
- fixed tick,
- double buffer,
- capacity,
- loss rate,
- water level,
- overflow,
- wetness,
- minimum flow rate.

Done when:

- Space or UI starts the pump,
- water moves through connected canals,
- water level changes visually,
- overflow wets nearby ground.

### Phase 3: Water Wheel and Coin Loop

Purpose: complete the minimum loop.

Implement:

- wheel rotation from water,
- coin rate,
- coin increase,
- part prices,
- insufficient coin feedback.

Done when:

- water flow rotates a wheel,
- rotating wheel increases coins,
- coins buy more canals or wheels.

### Phase 4: Wind

Purpose: add living motion.

Implement:

- wind power,
- slow wind variation,
- small wheel influence,
- tiny wind bonus coin rate,
- wind UI,
- simple grass, leaf, or water movement.

Done when:

- wind is visible in UI,
- strong wind slightly moves wheels,
- water remains the main source of income.

### Phase 5: Junctions and Better Flow

Implement:

- T Junction,
- Cross Junction,
- split flow,
- merge flow,
- loop stability checks.

### Phase 6: Terrain and Soil

Implement later:

- terrain state,
- shovel,
- trench,
- soil,
- mound,
- high ground.

### Phase 7: Storage, Dam, and Gate

Implement later:

- Storage Tank,
- Small Dam,
- Gate,
- gate open ratio,
- release rate.

### Phase 8: Height and Waterfall

Implement later:

- height,
- gravity bonus,
- Waterfall Drop,
- fall bonus,
- waterfall visuals.

### Phase 9: Advanced Water Events

Consider only after prior systems are stable:

- Tipping Bucket,
- Shishi-odoshi,
- Large Basin,
- Splash Ramp,
- Flow Splitter.

### Phase 10: Visual Polish and Themes

Add:

- plastic toy theme,
- western garden theme,
- Japanese garden theme,
- sandbox theme,
- improved water material,
- sounds,
- small ambient animations.

## 21. Recommended Unity File Structure

```text
unity/
└── Assets/
    ├── Scenes/
    │   └── Main.unity
    ├── Scripts/
    │   ├── Core/
    │   ├── Grid/
    │   ├── Parts/
    │   ├── Water/
    │   ├── Economy/
    │   ├── Wind/
    │   └── UI/
    ├── Prefabs/
    │   ├── Parts/
    │   └── UI/
    ├── Materials/
    ├── Art/
    ├── Generated/
    │   ├── Imported/
    │   └── Prefabs/
    └── Editor/
        └── GeneratedAssetPipeline.cs
```

## 22. Blender and Asset Pipeline

Blender supports Unity asset creation.

Pipeline:

```text
Blender source or generator
↓
blender/exports/*.fbx
↓
Unity editor import
↓
unity/Assets/Generated/Imported/
↓
unity/Assets/Generated/Prefabs/
```

Rules:

- keep source generation in `blender/scripts/`,
- keep generated exports in `blender/exports/`,
- default to `.fbx` for Unity,
- optionally export `.glb` for preview or interchange,
- never overwrite hand-authored Unity assets without review.

## 23. MVP Acceptance Criteria

The MVP succeeds when this is playable:

```text
place canal
place water wheel
start pump
water moves
water level rises
overflow wets ground
wheel rotates
coins increase
coins buy more parts
wind adds light movement
```

The MVP fails if the water is hard to read or the loop does not feel satisfying.

## 24. Known Later Decisions

Decide later:

- exact Unity LTS version,
- strictness of water conservation,
- whether pump activation becomes automatic,
- whether Energy is introduced,
- whether wind direction matters or only wind power,
- garden expansion rules,
- theme unlock rules,
- whether theme parts have stats or only visual differences,
- when to add height and excavation,
- whether the project name changes.

## 25. Design Principles

- Do not build every idea at once.
- First make water feel good.
- Favor player readability over physical accuracy.
- Make every state visible.
- Keep generated and hand-authored assets separate.
- Prefer small, reviewable implementation steps.
- Let MVP feedback decide which advanced systems deserve expansion.

## 26. Summary

Aqua_Play is a Unity-first toy water garden simulation. Its core is not realistic fluid physics; it is the satisfying design of visible water paths, wet ground, turning wheels, coins, and a living garden atmosphere.

The first goal is the minimum loop:

- pump,
- canals,
- water level,
- overflow,
- wetness,
- water wheel,
- coins,
- light wind.

After that loop works, the project can grow into branches, storage, terrain, waterfalls, larger water events, and themed garden parts.
