# AquaPlay Garden — Game Design Spec v0.5

Godot 4 / GDScript / 3D俯瞰 / グリッド配置型 / 箱庭水路シミュレーション

---

## 0. この仕様書の目的

このドキュメントは、AquaPlay Garden のゲーム設計、世界観、基本システム、実装フェーズを整理するための仕様書である。

本仕様は最終決定版ではない。  
Codex に技術的判断、矛盾チェック、実装難易度評価、MVP範囲の整理を依頼する前提の作業用仕様書である。

特に現時点では、以下を優先して整理する。

- 最小ゲームループ
- 水路パーツの配置
- 水量、水位、overflow、wetness
- 水車によるコイン獲得
- 風による補助的な演出と微収益
- Godot 4 で実装しやすい段階的な開発順序

バケツ、鹿威し、ダム、滝、大規模プールなどは魅力的な要素だが、現時点ではまだ仕様が固まりきっていないため、MVPからは外し、将来拡張として扱う。

---

## 1. ゲームコンセプト

AquaPlay Garden は、庭にプラスチック製の水路玩具を組み立てるような箱庭シミュレーションゲームである。

プレイヤーは、小さな庭の一角から始める。  
水路パーツ、ポンプ、水車、装飾パーツなどをグリッド上に配置し、水の流れを設計する。

水の流れによって水車を回し、コインやエネルギーを得る。  
得たリソースを使って新しいパーツを購入し、庭を拡張し、より複雑で美しい水流ネットワークを作っていく。

このゲームは、リアルな流体物理を再現するものではない。  
重要なのは、プレイヤーが見て理解できる、気持ちよく眺められる水のふるまいである。

重視する体験：

- 水路をつなげて水の流れを作る楽しさ
- 水位が上がる分かりやすさ
- 水が溢れて地面が湿る箱庭感
- 水車が回る嬉しさ
- 風で世界が少し動く生きている感じ
- コインで少しずつ庭を拡張する成長感
- 眺めているだけでも楽しいジオラマ感

---

## 2. 目指す体験

### 2.1 一言で表す体験

> 庭に水路玩具を組み立て、自分だけの小さな水力庭園を育てるゲーム。

### 2.2 プレイヤーが感じるべきこと

- 水路をつなげるのが楽しい
- 水が流れていることが見た目で分かる
- 水位が変わるのを見るのが楽しい
- overflow が起きると地面が湿って、状態が見た目に残る
- 水車が回ると嬉しい
- 風で葉っぱや水車が少し動くと、庭に空気感が出る
- パーツを買って庭を広げるのが楽しい
- 効率だけでなく、見た目の気持ちよさも追求したくなる

---

## 3. ビジュアル方針

### 3.1 基本方針

ビジュアルは、リアルな工業シミュレーターではなく、箱庭、玩具、ジオラマ方向にする。

方向性：

- ローポリ
- デフォルメ
- 3D俯瞰
- 柔らかいライティング
- 明るい庭
- 視認性の高いパーツ
- プラスチック玩具感
- 水はやや誇張された透明感
- 小さく密度のある庭ジオラマ

### 3.2 参考にしたい雰囲気

- AquaPlay のようなプラスチック水路玩具
- 明るい砂場や庭の箱庭感
- Tiny World Builder 系のグリッド箱庭
- Townscaper / Dorfromantik 系の眺めて楽しいジオラマ感
- 小さな水場、庭、池、温室、和風庭園などへ広げられる雰囲気

### 3.3 アセットの方向性

基本パーツは「おもちゃ風水路」とする。  
ただし将来的には、複数テーマのアセットを用意したい。

想定テーマ：

- おもちゃ風プラスチック
- 洋風庭園
- 和風庭園
- 砂場 / サンドキャッスル
- 科学館の実験装置風
- 木製水路
- 石造り水路
- 小型工業パーツ
- 温室・植物園風
- 夏休みの庭風

テーマ差は、初期段階では性能差ではなく見た目違いを基本とする。  
性能差を付ける場合は、ゲームバランスが固まってから検討する。

---

## 4. 基本ゲームループ

### 4.1 最小ゲームループ

```text
水路を配置する
↓
ポンプを起動する
↓
水が流れる
↓
水位が上がる
↓
水車が回る
↓
コインを得る
↓
新しいパーツを買う
↓
庭を拡張する
↓
より複雑な水流を作る
```

### 4.2 長期ゲームループ

```text
小さな水路を作る
↓
水車で収益を得る
↓
水路を拡張する
↓
分岐、合流、風、装飾を追加する
↓
庭の見た目と効率を整える
↓
より大きな水流ネットワークを作る
↓
テーマアセットや高度な水流ギミックを解放する
```

---

## 5. 技術方針

### 5.1 使用技術

- Godot 4
- GDScript
- 3D
- 俯瞰カメラ
- グリッド配置
- タイル接続型シミュレーション

### 5.2 重要な技術判断

リアルな流体シミュレーションは使わない。

水は以下のような記号化された値で表現する。

- 数値としての水量
- パーツごとの容量
- 水位表示
- 流量の減衰
- overflow
- wetness
- 接続方向
- 見た目用の流れの強さ

### 5.3 リアル流体を使わない理由

- 実装難易度が高い
- パフォーマンス負荷が高い
- デバッグが難しい
- ゲームバランス調整が難しい
- 箱庭玩具風の見た目では、記号化された水の方が分かりやすい
- AI支援開発では、単純で検証しやすいルールの方が扱いやすい

---

## 6. 世界の単位

### 6.1 水量単位

Water Unit = WU

水の量は WU で扱う。

例：

```text
100 WU = 初期ポンプ1秒分の基本水量
```

### 6.2 流量単位

Flow Rate = WU/sec

流れている水の強さは WU/sec で扱う。

今後の混乱を避けるため、以下を分けて考える。

- stored_water: 貯まっている水量 WU
- flow_rate: 流れている水量 WU/sec
- input_flow_rate: 入力流量 WU/sec
- output_flow_rate: 出力流量 WU/sec
- overflow_water: 溢れた水量 WU
- visual_flow: 見た目用の流れの強さ 0.0〜1.0

### 6.3 時間単位

Time = sec

### 6.4 グリッド単位

1 cell = 1 tile

### 6.5 高さ単位

高さは将来的に整数レベルで扱う。

```text
height = -1, 0, +1, +2
```

例：

```text
-1 = 掘削済み水路溝
 0 = 地表
+1 = 盛り土・高台
+2 = 高台上段
```

MVPでは height は未実装でもよい。

### 6.6 シミュレーションtick

基本案：

```text
simulation_tick = 0.2 sec
```

1秒に5回、水量計算を行う。

見た目のアニメーションは毎フレーム更新するが、水量計算は固定tickで処理する。

---

## 7. リソース設計

### 7.1 Coin

パーツ購入、庭拡張、ツール購入に使う基本リソース。

初期値案：

```text
coins = 100
```

### 7.2 Water

水路、ポンプ、水車などを流れる水。

MVPでは厳密な総量保存はしない。  
まずは「ポンプが水を出し、水路を伝わり、減衰し、溢れ、消える」程度でよい。

将来的にダム、タンク、大規模プールを実装する場合は、水量保存に近づける。

### 7.3 Energy

将来リソース。  
ポンプ、自動装置、特殊パーツに使う可能性がある。

MVPでは未実装。

### 7.4 Soil

将来リソース。  
掘削、整地、盛り土、高台作成に使う可能性がある。

MVPでは未実装。

### 7.5 Wind

風量。  
水車やパドルを補助的に回すために使う。

風は水流の代替ではなく、見た目と微収益を支える補助要素とする。

---

## 8. グリッド・地形システム

### 8.1 基本グリッド

初期は 10x10 グリッドから開始する。

各セルは以下を持つ。

- grid_position
- terrain_state
- height
- placed_part
- wetness

### 8.2 MVPでの地形状態

MVPでは地形を単純化する。

```text
ground = 通常地面
trench = 水路設置可能な掘削済みマス
```

最初は trench の制約すら省略し、どの ground にも水路を置ける形でもよい。  
掘削や整地は、基本ループが成立してから追加する。

### 8.3 将来的な地形状態

| 状態 | 説明 | 設置できるもの |
| --- | --- | --- |
| 未開拓地 | 木、岩、雑草がある | 何も置けない |
| 荒れ地 | 凸凹している | 整地が必要 |
| 平地 | 整地済み | ダム、ポンプ、タンクなど |
| 水路溝 | 掘削済み | 水路パーツ |
| 高台 | 盛り土済み | 高所水路、滝、貯水装置 |

---

## 9. 水路パーツの基本構造

各水路パーツは以下を持つ。

- part_type
- grid_position
- rotation_index
- connection_directions
- input_flow_rate
- accepted_flow_rate
- output_flow_rate
- capacity
- loss_rate
- overflow_water
- water_level
- visual_flow
- is_flowing
- height

### 9.1 接続方向

方向は4方向。

- NORTH
- EAST
- SOUTH
- WEST

水が流れる条件：

```text
A が B 側の接続方向を持つ
B が A 側の接続方向を持つ
```

例：

```text
A が EAST を持つ
B が WEST を持つ
→ 接続成立
```

### 9.2 基本パーツ種別

MVPで必要な水路パーツ：

- Straight Canal
- Corner Canal
- Mini Circulation Pump
- Water Wheel

追加候補：

- T Junction
- Cross Junction
- Decorative Water Tile
- Bridge
- Toy Boat

---

## 10. 水量・流量計算

### 10.1 基本方針

水量計算は、リアルな水圧や流体ではなく、接続されたパーツ間で flow_rate を渡す方式にする。

MVPでは以下で十分とする。

```text
accepted_flow_rate = min(input_flow_rate, capacity)
overflow_flow_rate = max(input_flow_rate - capacity, 0)
water_level = accepted_flow_rate / capacity
output_flow_rate = accepted_flow_rate * (1.0 - loss_rate)
```

### 10.2 例

```text
input_flow_rate = 120 WU/sec
capacity = 100 WU/sec
loss_rate = 0.10

accepted_flow_rate = 100 WU/sec
overflow_flow_rate = 20 WU/sec
water_level = 1.0
output_flow_rate = 90 WU/sec
```

### 10.3 最小流量

微小な水が無限に伸びるのを防ぐため、最小流量を設定する。

```text
minimum_flow_rate = 5 WU/sec

if output_flow_rate < minimum_flow_rate:
    output_flow_rate = 0
```

### 10.4 二重バッファ方式

将来的なループ水路、分岐、合流を考えると、水計算は二重バッファ方式にする。

基本手順：

```text
1. 各パーツが current_input_flow_rate を読む
2. 出力流量を計算する
3. 接続先の next_input_flow_rate に加算する
4. overflow / wetness を処理する
5. 最後に next を current に反映する
```

これにより、処理順によって水の結果が変わる問題を減らす。

---

## 11. 水位表示

水位は water_level で表現する。

```text
water_level = accepted_flow_rate / capacity
```

範囲：

```text
0.0 〜 1.0
```

| water_level | 表示 |
| --- | --- |
| 0.0 | 水なし |
| 0.1〜0.4 | 低水位 |
| 0.4〜0.7 | 中水位 |
| 0.7〜0.99 | 高水位 |
| 1.0 | 満水 |

overflow時：

```text
water_level = 1.0
```

---

## 12. Overflow と Wetness

### 12.1 Overflow

容量を超えた水は overflow になる。

```text
overflow_flow_rate = max(input_flow_rate - capacity, 0)
overflow_water = overflow_flow_rate * delta
```

overflowした水は地面に染み出す。

### 12.2 Wetness

各地面セルは wetness を持つ。

```text
wetness = 0.0 〜 100.0
```

overflow時の分配案：

```text
current_cell.wetness += overflow_water * 0.50
north_cell.wetness += overflow_water * 0.125
east_cell.wetness += overflow_water * 0.125
south_cell.wetness += overflow_water * 0.125
west_cell.wetness += overflow_water * 0.125
```

上限：

```text
wetness = clamp(wetness, 0, 100)
```

### 12.3 Wetness の見た目

| wetness | 表示 |
| --- | --- |
| 0〜20 | 乾燥 |
| 20〜50 | やや湿り |
| 50〜80 | 湿り |
| 80〜100 | 水たまり |

### 12.4 乾燥

時間経過で wetness は減る。

```text
wetness -= dry_rate * delta
```

基本値：

```text
dry_rate = 2.0 / sec
```

天候による変化案：

| 天候 | dry_rate |
| --- | --- |
| 晴れ | 3.0 / sec |
| 通常 | 2.0 / sec |
| 曇り | 1.0 / sec |
| 雨 | 0.2 / sec |

天候はMVPでは未実装。

---

## 13. 水流の見た目

水流は数値だけでなく、必ず見た目に出す。

```text
visual_flow = accepted_flow_rate / capacity
```

| visual_flow | 表示 |
| --- | --- |
| 0〜0.2 | 細い水 |
| 0.2〜0.5 | 普通の流れ |
| 0.5〜0.9 | 太い流れ |
| 1.0 | 満水 |
| overflow | 水しぶき + 地面 wetness |

見た目の表現案：

- 水面の高さ
- 水の透明度
- 水の流れる線
- 泡
- 小さな水しぶき
- 地面の湿り色
- 水車の回転速度

---

## 14. 風システム

### 14.1 風量

風量は wind_power で表す。

```text
wind_power = 0 〜 100
```

| 状態 | wind_power |
| --- | --- |
| Calm | 0〜10 |
| Light Wind | 10〜30 |
| Normal Wind | 30〜60 |
| Strong Wind | 60〜100 |

### 14.2 風の変動

通常時はランダムにゆるく変動する。

```text
base_wind = 20
wind_variation = -10 〜 +20
wind_power = clamp(base_wind + wind_variation, 0, 100)
```

風の変化は毎tickではなく、数秒ごとに補間する方が自然。

### 14.3 水車への影響

水車やパドルは、水流と風量の合成で回る。

```text
water_force = current_flow_rate / capacity
wind_force = wind_power / 100

rotation_power = water_force * 0.85 + wind_force * 0.15
rotation_speed = rotation_power * max_rotation_speed
```

基本値：

```text
max_rotation_speed = 360 deg/sec
```

風はあくまで補助。  
水が主役であり、風だけで大きく稼げないようにする。

### 14.4 風だけで回る例

```text
water_force = 0
wind_power = 60

rotation_power = 0 * 0.85 + 0.6 * 0.15
rotation_power = 0.09

rotation_speed = 32.4 deg/sec
```

これにより、水がなくても風が強ければ水車が少し回る。

### 14.5 風による収益

風だけで稼げると水路設計が不要になるため、風による収益は弱くする。

```text
coin_rate = water_coin_rate + wind_bonus_coin_rate
```

wind_bonus_coin_rate:

| wind_power | bonus |
| --- | --- |
| 0〜40 | 0 coin/sec |
| 40〜70 | +0.2 coin/sec |
| 70以上 | +0.5 coin/sec |

風は「回る見た目」と「微収益」程度に留める。

### 14.6 風のゲーム的役割

風は以下の役割を持つ。

- 水車がカタカタ少し回る
- 軽い発電補助になる
- 世界が生きて見える
- 葉っぱ、草、水面などの揺れで空気感を出す
- 将来の風車パーツにつながる

将来候補：

- Wind Vane
- Small Windmill
- Wind Boost Fan
- Wind Paddle

---

## 15. ポンプシステム

### 15.1 基本方針

従来の「無限水源」は使わない。

初期水源の代わりに、デフォルト設備として小型循環ポンプを置く。

### 15.2 Mini Circulation Pump

初期ポンプ。

仕様案：

```text
output_flow_rate = 100 WU/sec
active_duration = 3 sec
recharge_duration = 8 sec
```

状態：

```text
READY
ACTIVE
RECHARGING
```

動作：

```text
READY
↓ 起動
ACTIVE: 3秒間水を出す
↓
RECHARGING: 8秒間待機
↓
READY
```

### 15.3 ポンプの役割

- 最初の水流を作る
- 一定周期の水の波を作る
- 水車を回す
- 水路容量不足を見つける
- overflow を発生させる
- プレイヤーに水量と容量の関係を見せる

### 15.4 自動か手動か

MVPでは手動起動でよい。

```text
Space = ポンプ起動
```

将来的には以下を検討する。

- 一定周期で自動起動
- Energy を消費して起動
- 複数ポンプの同期
- ポンプ出力のアップグレード

---

## 16. 水車・パドル

### 16.1 基本方針

水車・パドルは、水流と風で回る。  
ただし水流が主役で、風は補助。

### 16.2 水量による収益

water_coin_rate:

| current_flow_rate | 状態 | coin_rate |
| --- | --- | --- |
| 0〜20 WU/sec | 停止 | 0 coin/sec |
| 20〜50 WU/sec | 低速 | 1 coin/sec |
| 50〜80 WU/sec | 中速 | 3 coin/sec |
| 80以上 WU/sec | 高速 | 5 coin/sec |

### 16.3 回転速度

```text
water_force = current_flow_rate / capacity
wind_force = wind_power / 100

rotation_power = water_force * 0.85 + wind_force * 0.15
rotation_speed = rotation_power * max_rotation_speed
```

基本値：

```text
max_rotation_speed = 360 deg/sec
```

### 16.4 回転の見た目

水車の回転は、収益計算よりも少し滑らかにする。

推奨：

- current_flow_rate をそのまま使わず、短時間の平均値を使う
- 水が途切れても即停止ではなく、少し慣性で減速する
- 風があると低速でカタカタ回る

これにより、水路が生きているように見える。

---

## 17. パーツ一覧

### 17.1 MVPパーツ

| パーツ | 役割 |
| --- | --- |
| Ground Tile | 地面 |
| Wet Ground Tile | 湿った地面表示 |
| Straight Canal | 直線水路 |
| Corner Canal | 曲がり水路 |
| Mini Circulation Pump | 初期水流発生 |
| Water Wheel | 水流・風で回る収益装置 |

### 17.2 Phase追加パーツ候補

| パーツ | 役割 |
| --- | --- |
| T Junction | 分岐 |
| Cross Junction | 十字分岐 |
| Wind Paddle | 風でも回りやすい軽量パドル |
| Storage Tank | 一時貯水 |
| Small Dam | 貯水 |
| Gate | 放流制御 |
| Waterfall Drop | 落差演出 |
| Decorative Plant | 景観 |
| Bridge | 見た目・水路横断 |
| Toy Boat | 水流に乗る演出 |

### 17.3 未確定・将来検討パーツ

以下は魅力的だが、現時点では仕様を固めすぎない。

| パーツ | 状態 | メモ |
| --- | --- | --- |
| Tipping Bucket | 後回し | 自動水源型にするか、上流水を貯める型にするか未決定 |
| Shishi-odoshi | 後回し | 和風テーマのリズム演出として有力 |
| Large Basin | 後回し | 終盤の大型水流イベント候補 |
| Splash Ramp | 後回し | 放流演出が固まってから検討 |
| Flow Splitter | 後回し | 分岐仕様が安定してから検討 |
| Drill Car | 後回し | 掘削と Energy が必要 |
| Charging Station | 後回し | Drill Car とセット |

---

## 18. 価格案

### 18.1 MVP価格

| パーツ | Cost |
| --- | --- |
| Straight Canal | 5 |
| Corner Canal | 5 |
| Water Wheel | 30 |
| Mini Circulation Pump | 初期固定 |
| Delete | 0 |

### 18.2 将来価格

| パーツ | Cost |
| --- | --- |
| T Junction | 10 |
| Cross Junction | 15 |
| Wind Paddle | 70 |
| Storage Tank | 40 |
| Small Dam | 25 |
| Gate | 20 |
| Waterfall Drop | 50 |

価格は仮。  
MVPでは「買える、置ける、収益で増える」の確認を優先する。

---

## 19. UI設計

### 19.1 基本UI

表示項目：

- Coins
- Water Flow
- Wind
- Selected Part
- Rotation
- Income/sec
- Active Wheels
- Pump State

### 19.2 デバッグUI

開発中は各パーツ上に以下を表示する。

- Water / Flow
- Capacity
- Level
- Overflow
- Wetness
- Connection

例：

```text
Flow: 81.0
Cap: 100
Level: 0.81
Overflow: 0
```

### 19.3 操作

初期操作案：

| 操作 | 内容 |
| --- | --- |
| 左クリック | パーツ配置 |
| R | 回転 |
| 1 | Straight Canal |
| 2 | Corner Canal |
| 3 | Water Wheel |
| 4 | Delete |
| Space | ポンプ起動 |
| Tab | デバッグ表示切替 |

---

## 20. 実装Phase

### Phase 0 — Foundation

目的：プロジェクト土台。

実装：

- Godot 4 project
- 10x10 grid
- 3D俯瞰カメラ
- 庭ステージ
- セルクリック取得
- UI表示

未実装：

- 水
- パーツ
- コイン
- ポンプ

完了条件：

- 画面にグリッド庭が表示される
- カメラで俯瞰できる
- セルをクリックすると座標が取得できる

### Phase 1 — Water Part Placement

目的：パーツを置けるようにする。

実装：

- Straight Canal
- Corner Canal
- Water Wheel
- Mini Circulation Pump
- 回転
- 削除
- 接続方向
- placed_part 管理

完了条件：

- パーツを選んでグリッドに配置できる
- Rキーで回転できる
- 削除できる
- 接続方向が内部データとして確認できる

### Phase 2 — Pump and Water Simulation

目的：水が流れるようにする。

実装：

- Mini Pump
- READY / ACTIVE / RECHARGING
- 固定tick水量計算
- 二重バッファ方式
- capacity
- loss_rate
- water_level
- overflow
- wetness
- minimum_flow_rate

完了条件：

- Spaceでポンプを起動できる
- 水路に水が流れる
- 水位が見た目に反映される
- 容量を超えると overflow する
- overflow した周辺地面が湿る

### Phase 3 — Water Wheel and Coin Loop

目的：最小ゲームループ成立。

実装：

- 水車回転
- 水量による回転速度
- coin_rate
- coins増加
- パーツ価格
- コイン不足時の配置制限

完了条件：

- 水流で水車が回る
- 水車が回るとコインが増える
- コインで水路や水車を追加できる
- 最小ループが遊べる

### Phase 4 — Wind

目的：世界に動きを追加。

実装：

- wind_power
- 風の時間変動
- 水車が風で少し回る
- wind_bonus_coin_rate
- 風の簡易表示
- 葉っぱ、草、水面などの揺れ演出

完了条件：

- UIに風量が表示される
- 水がなくても強風時に水車が少し回る
- 風による収益はごく小さい
- 水路設計の主役が水のまま保たれている

### Phase 5 — Junctions and Better Flow

目的：水路設計の幅を広げる。

実装：

- T Junction
- Cross Junction
- 分岐時の流量分配
- 合流時の流量加算
- ループ時の安定性確認

完了条件：

- 分岐水路を作れる
- 分岐先に流量が分配される
- 合流しても計算が破綻しない
- ループ配置でクラッシュしない

### Phase 6 — Terrain and Soil

目的：掘削・整地による庭づくりを追加。

実装：

- terrain_state
- shovel
- trench
- soil
- mound
- high ground

完了条件：

- 水路を置く前に地形準備が必要になる
- 掘削や整地がゲームプレイに加わる
- ただし操作が面倒になりすぎない

### Phase 7 — Storage / Dam / Gate

目的：貯める、流すを追加。

実装候補：

- Storage Tank
- Small Dam
- Gate
- gate_open_ratio
- release_rate

完了条件：

- 水を一時的に貯められる
- 放流量を調整できる
- overflow の制御に意味が出る

### Phase 8 — Height and Waterfall

目的：高低差設計を追加。

実装候補：

- height
- gravity_bonus
- Waterfall Drop
- fall_bonus
- 滝演出
- 滝直下の水車補正

完了条件：

- 高低差によって水流が変化する
- 滝が見た目に分かる
- 滝の下の水車にボーナスが入る

### Phase 9 — Advanced Water Events

目的：大型ギミックを検討。

候補：

- Tipping Bucket
- Shishi-odoshi
- Large Basin
- Splash Ramp
- Flow Splitter

完了条件：

- 仕様が固まっている
- 既存の水量計算と矛盾しない
- 見た目とゲーム性の両方で意味がある

### Phase 10 — Visual Polish and Asset Themes

目的：世界観強化。

実装候補：

- プラスチックテーマ
- 洋風庭園テーマ
- 和風庭園テーマ
- 砂場テーマ
- 水エフェクト
- 泡
- 水しぶき
- 水たまり
- 音

完了条件：

- 同じ機能でもテーマ違いの見た目を選べる
- 水と庭の状態が見た目で分かりやすい
- 眺めて楽しい箱庭になっている

---

## 21. 将来システム案

この章の内容は、現時点では未確定。  
MVPや初期実装には入れない。

### 21.1 Tipping Bucket

水が一定量溜まると傾き、一気に放流する装置。

未決定点：

- 時間経過で自動的に水が溜まる水源型にするか
- 上流から来た水を貯める変換装置にするか
- どの程度の実用性を持たせるか
- 遊園地風、玩具風、庭園風のどれに寄せるか

### 21.2 Shishi-odoshi

和風庭園テーマの小型放流装置。

役割候補：

- 水が少しずつ溜まる
- 一定量で傾く
- 少量の水を放流する
- 音を鳴らす
- 実用性より雰囲気とリズムを重視する

### 21.3 Dam / Gate

水を貯め、放流量を調整する装置。

将来的には以下を持つ。

- dam_current_water
- dam_capacity
- release_rate
- gate_open_ratio

### 21.4 Waterfall

高低差による水流ブーストと演出。

将来的には以下を検討する。

```text
height_drop = current_height - next_height

if height_drop >= 2:
    is_waterfall = true
```

滝の効果案：

```text
fall_bonus = 1.0 + 0.25 * height_drop
```

### 21.5 Large Basin

大量の水を貯め、一定周期で波や放流を作る終盤施設。

現時点ではまだ後回し。

---

## 22. 推奨ファイル構成

```text
AquaPlayGarden/
├── project.godot
├── PLAN.md
├── AGENTS.md
├── AQUAPLAY_GARDEN_SPEC.md
├── README.md
├── docs/
│   ├── physics_rules.md
│   ├── asset_style_guide.md
│   └── phase_plan.md
├── .logs/
│   ├── phase0.md
│   ├── phase1.md
│   └── phase2.md
├── .prompts/
│   ├── asset_plastic_waterway.md
│   ├── asset_japanese_garden.md
│   └── asset_western_garden.md
├── scenes/
│   ├── Main.tscn
│   ├── parts/
│   └── ui/
├── scripts/
│   ├── GridManager.gd
│   ├── TerrainManager.gd
│   ├── PlacementController.gd
│   ├── WaterPart.gd
│   ├── WaterSimulation.gd
│   ├── Pump.gd
│   ├── WindManager.gd
│   ├── GameManager.gd
│   └── UIManager.gd
├── assets/
│   ├── models/
│   ├── textures/
│   ├── materials/
│   ├── icons/
│   └── audio/
```

---

## 23. Codexに依頼したい技術判断

Codexには、実装前に以下を確認させる。

```text
この仕様書を読み、Godot 4 / GDScript での実装に向けて、以下を整理してください。

1. 仕様上の矛盾
2. 実装難易度が高すぎる箇所
3. MVPから外すべき要素
4. Phase順序の妥当性
5. 必要なファイル構成
6. 各Phaseの完了条件
7. テスト・確認方法
8. Godotで避けるべき実装方針
9. 将来拡張しやすい設計案
10. PLAN.md と AGENTS.md に反映すべきルール
```

---

## 24. MVPで絶対に確認すべきこと

MVPの成功条件は、完成度ではなく以下。

```text
水路を置く
↓
ポンプを起動する
↓
水位が上がる
↓
capacityを超えるとoverflowする
↓
地面が湿る
↓
水車が回る
↓
コインが増える
```

このループが気持ちよくなければ、拡張しても弱い。

---

## 25. 重要な設計方針

### 25.1 最初から全部作らない

以下は後回しにする。

- バケツ
- 鹿威し
- ダム
- 高低差
- 滝
- 蒸発
- 大型プール
- ドリルカー
- Energy
- Soil
- 天候
- 複数テーマアセット

### 25.2 まず水の気持ちよさを見る

最優先は以下。

- 水位変化
- overflow
- wetness
- 水車回転
- ポンプ周期
- コイン獲得

### 25.3 数学的正しさより納得感

リアルさより、プレイヤーが見て理解できることを優先する。

### 25.4 見た目で状態が分かるようにする

数値だけに頼らない。

例：

- 水位で水量を示す
- 地面の色で湿りを示す
- 水車速度で水流を示す
- 風で葉っぱや水車が少し動く
- overflow で水しぶきが出る

### 25.5 仕様は固めすぎない

初期仕様は、実装しながら変える。  
特に放流装置、貯水装置、テーマアセットは、MVPの触り心地を見てから決める。

---

## 26. 現時点の未決定事項

以下は後で決める。

- 水は総量保存するか
- ポンプの起動を自動にするか手動にするか
- バケツを水源型にするか、上流水を貯める型にするか
- 鹿威しを実用パーツにするか、演出パーツにするか
- 風向きを入れるか、風量だけにするか
- 水車の収益を coin 直結にするか、Energy経由にするか
- 庭拡張の条件
- テーマアセットの解放条件
- 和風・洋風パーツを性能差にするか、見た目違いだけにするか
- ダムやタンクの水量保存をどこまで厳密にするか
- 高低差と掘削をいつ導入するか

---

## 27. まとめ

AquaPlay Garden は、リアルな流体シミュレーションではなく、箱庭の中で水、風、貯水、放流、地形、装飾を組み合わせて楽しむ水路設計ゲームである。

最初に目指すべきは、巨大な完成版ではない。

まずは以下だけで遊べる最小ループを作る。

- ポンプ
- 水路
- 水位
- overflow
- wetness
- 水車
- coin
- 風による軽い演出

その後、MVPの触り心地を確認しながら、以下を段階的に検討する。

- 分岐と合流
- 地形と掘削
- ダムと水門
- 滝と高低差
- バケツ
- 鹿威し
- 大型水流イベント
- 和風・洋風・おもちゃ風アセット

このゲームの核は、効率だけではなく、見ていて気持ちいい水の流れを作ることである。
