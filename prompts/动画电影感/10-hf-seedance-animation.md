# Seedance HF curated prompts — `动画电影感`

> body: verbatim — full original prompt text only; no summary/teaser.

Source dataset: https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets  
License tag: `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`  
Curation: 2026-09-29 Asia/Shanghai. Prompts are **verbatim** `raw_p` fields. No invention.

Relocated 2026-09-30 (consolidate): entries moved here from other HF files by content; see docs/CURATION-LOG.md.

Count in this file: **5**

---

## 1. Storyboard Panel Animation

- **id:** `SD2_04707`
- **slug:** `storyboard-panel-animation`
- **source URL:** https://x.com/ai_lifehack55/status/2072882708863410216
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=2122; quality_score=22 (HF jsonl has no like/view fields)
- **tags:** storyboard, animation, panels
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 960, "height": 960, "ratio": 1.0, "duration": 15.04, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
Reference @image1 共有用3×3・9コマ参照画像
[CONDITION DEFINITION]
添付した1:1スクエアの3列×3行・全9コマの参照画像を、約15秒の動画を構成する絵コンテとして使用する。参照画像全体を3×3の分割画面のまま動かすのではなく、各コマを1つずつ独立した通常の全画面ショットとして展開する。参照画像内の9コマをすべて使用し、省略、統合、反復、並べ替えを行わない。常に1つのコマだけを全画面表示し、複数のコマを同時に表示しない。参照画像が実写の場合は実写の質感を維持する。アニメまたはイラストの場合は、元の絵柄、線、彩色、陰影、質感を維持する。実写とアニメを相互に変換しない。プロンプト側から特定の衣装、表情、ポーズ、動作、小道具、背景設定を新しく固定しない。各コマに描かれている構図、被写体の状態、姿勢、表情、衣装、背景、雰囲気を基準に、その内容と画風に適した自然な動きを補完する。9コマが同一人物または同一キャラクターを描いている場合は、全ショットを通して顔立ち、髪型、年齢感、体格、衣装、主要な外見的特徴の同一性を維持する。

[SHOT / FLOW]
参照画像の読み込み順は、左上から右方向へ進み、上段、中央段、下段の順とする。
Shot 1｜0.0〜1.5秒
左上のコマを通常の全画面ショットとして展開し、そのコマの構図、画風、被写体の状態に従って自然に動かす。
Shot 2｜1.5〜3.0秒
上中央のコマを通常の全画面ショットとして展開し、そのコマの構図、画風、被写体の状態に従って自然に動かす。
Shot 3｜3.0〜4.5秒
右上のコマを通常の全画面ショットとして展開し、そのコマの構図、画風、被写体の状態に従って自然に動かす。
Shot 4｜4.5〜6.0秒
中央段左のコマを通常の全画面ショットとして展開し、そのコマの構図、画風、被写体の状態に従って自然に動かす。
Shot 5｜6.0〜8.0秒
中央のコマを通常の全画面ショットとして展開し、そのコマの構図、画風、被写体の状態に従って自然に動かす。
Shot 6｜8.0〜9.5秒
中央段右のコマを通常の全画面ショットとして展開し、そのコマの構図、画風、被写体の状態に従って自然に動かす。
Shot 7｜9.5〜11.0秒
左下のコマを通常の全画面ショットとして展開し、そのコマの構図、画風、被写体の状態に従って自然に動かす。
Shot 8｜11.0〜12.5秒
下中央のコマを通常の全画面ショットとして展開し、そのコマの構図、画風、被写体の状態に従って自然に動かす。
Shot 9｜12.5〜15.0秒
右下のコマを通常の全画面ショットとして展開し、そのコマの構図、画風、被写体の状態に従って自然に動かす。最後は短い余韻を残して終える。
各ショットは開始直後から、小さくても視認できる自然な動きを生じさせる。被写体の視線、表情、呼吸、姿勢、髪、衣服、周囲の物体、光、背景などは、各コマの元の状態から自然につながる範囲で動かす。
参照画像と無関係な新しい演技や大きな動作は追加しない。

[CAMERA / EDITING]
各コマの元の構図と距離感を基本として維持し、1:1の通常の全画面ショットとして自然に展開する。
被写体や背景の自然な動きを優先し、カメラは原則として安定させる。必要な場合のみ、ごく軽い寄り、引き、パン、奥行きの変化を加える。ショットの順番と切り替え時刻は、[SHOT / FLOW]で指定した時間軸に従う。
ショット間は明瞭なカットで切り替える。顔、身体、衣装、背景を溶かして次のショットへ変形させるモーフィングは行わない。3×3画像を区切る枠線や余白は、完成映像の固定フレームとして残さない。
各コマ内に元から描かれている装飾、線、記号、エフェクトは、元の画風の一部として自然に維持してよい。ただし、装飾を新しく増殖させたり、形を崩したり、別のショットへ連続させたりしない。

[SOUND]
BGMあり。参照画像全体の画風、雰囲気、映像のテンポに自然に合うインストゥルメンタル音楽を付ける。
歌詞、歌唱、ナレーション、台詞は入れない。必要に応じて、BGMを邪魔しない控えめな環境音や効果音を加える。

[NEGATIVE]
3×3の参照画像全体を分割画面のまま動かさない。
複数画面、分割画面、コラージュ表示にしない。
9コマの一部を省略、統合、反復、並べ替えしない。
指定された読み込み順を変更しない。
指定された時間配分から大きく外れない。
各コマを長い静止状態のまま表示しない。
同一人物または同一キャラクターを別人化させない。
参照内容と無関係な人物、衣装、小道具、背景、演技を新しく追加しない。
元の表情、姿勢、衣装、構図を大幅に変更しない。
実写をアニメ化、アニメやイラストを実写化しない。
ショット間で顔、身体、衣装、背景を溶かして変形させない。
装飾、線、記号、エフェクトを増殖、変形、別ショットへ接続させない。
激しいカメラ移動、極端なズーム、過剰な演技、不要な場面転換を避ける。
```

---

## 2. Anime Style Katsu Don Cooking

- **id:** `SD2_03414`
- **slug:** `anime-katsu-don-cooking`
- **source URL:** https://x.com/tanabe_fragm/status/2064240994070213001
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=6784; quality_score=26 (HF jsonl has no like/view fields)
- **tags:** AnimeFood, KatsuDon, Cooking
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 1280, "height": 720, "ratio": 1.78, "duration": 15.13, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
CRITICAL INSTRUCTION: Do NOT display, reference, or reproduce any storyboard image, panel layout, reference photo, or sketch in the video output. All scenes must be original anime-style animation generated from the text descriptions only. Ignore any visual reference frame entirely. Please turn the storyboard sequence into a fast-paced cooking video following the order of the scenes. ## Style: High-quality Japanese anime film style, cinematic lighting, ultra-detailed food animation, shallow depth of field, soft natural summer lighting, macro close-up shots, slow cinematic camera movement, refreshing and bright summer atmosphere, gourmet cooking animation style with strong emphasis on texture and moisture. ## Editing: Use fast-paced, rhythm-driven cutting as the foundation, ensuring the cooking process is intuitively easy to understand. Apply match cuts (matching shape, motion, composition, and texture) to transition smoothly between scenes. The overall video should feel like an energetic and stylish anime film, with a strong focus on sizzle, freshness, and visual appeal. ### Scene 1 — 豚ロースを叩いて下処理する Close-up of anime-style hands gripping a wooden meat mallet, firmly pounding a thick pink pork loin cutlet on a wooden cutting board. The meat flattens slightly with each strike, fibers visibly loosening. Salt and pepper are sprinkled evenly across the surface. Subtle vibration ripples through the meat on impact. Hyperrealistic anime style, sharp kitchen lighting, cinematic shallow depth of field. ### Scene 2 — パン粉をまぶす Anime-style hands methodically coating a raw pork cutlet: first pressing it into a tray of white flour, then dipping it into beaten egg wash with golden drips falling back, finally pressing it firmly into a tray of coarse white panko breadcrumbs. Each layer adheres visibly. Hyperrealistic anime style, overhead dramatic lighting, close-up food detail. ### Scene 3 — 揚げる A panko-coated pork cutlet submerged in shimmering golden oil in a deep frying pan. Vigorous bubbles erupt around the edges, gradually settling as the crust turns deep amber and crispy. Light refracts through the hot oil surface. Steam rises gently. Hyperrealistic anime style, warm golden lighting, cinematic. ### Scene 4 — 揚げたカツを切る A perfectly fried golden-brown tonkatsu rests on a wooden cutting board. Anime-style hands guide a large sharp knife, slicing the cutlet into even uniform strips. The crispy crust cracks cleanly with each cut, revealing tender white meat inside. Subtle steam escapes the cuts. Hyperrealistic anime style, dramatic top-angle kitchen lighting. ### Scene 5 — 出汁と玉ねぎを煮る Inside a wide shallow pan on a gas stove, thinly sliced onion rings simmer slowly in dashi broth. The onions gradually soften and turn translucent, gently swaying in the amber liquid. Bubbles rise steadily from the bottom. Chopsticks occasionally stir the onions. Warm steam drifts upward. Hyperrealistic anime style, warm stovetop glow, cinematic close-up. ### Scene 6 — カツを出汁の上に置く Anime-style hands use chopsticks to carefully lay sliced tonkatsu strips side by side over the gently simmering onion and dashi broth in a shallow pan. The cutlet sizzles softly as it contacts the liquid. Golden breadcrumbs begin to absorb the broth slightly at the edges. Hyperrealistic anime style, warm amber kitchen lighting, close-up cinematic framing. ### Scene 7 — 溶き卵を回しかける A slow, steady pour of beaten golden egg from a small bowl, spiraling gently over the simmering tonkatsu and onions in the pan. The egg cascades in a thin stream, spreading naturally across the surface, beginning to turn opaque at the edges where it meets heat. Hyperrealistic anime style, warm stovetop light, macro cinematic detail. ### Scene 8 — 卵がゆっくり固まる Inside the shallow pan over low heat, the poured egg slowly coagulates across the surface of the tonkatsu and onions. The edges firm into a soft golden custard while the center remains slightly runny and trembling. Gentle steam rises. No stirring — the egg sets naturally through residual heat. Hyperrealistic anime style, soft warm glow, intimate close-up framing. ### Scene 9 — どんぶり茶碗にご飯を盛る A pristine white ceramic donburi bowl placed on a stainless steel counter. A rice paddle scoops a generous mound of steaming Japanese short-grain rice, placing it carefully into the bowl. The rice grains glisten slightly, tightly packed yet fluffy. Light steam rises from the surface. Hyperrealistic anime style, clean soft kitchen lighting, close-up cinematic. ### Scene 10 — カツと卵をご飯の上に乗せる Anime-style hands use chopsticks to carefully slide the softly set egg-and-tonkatsu mixture from the pan directly onto the mound of white rice in the donburi bowl. The egg settles over the rice in a gentle wave. Broth seeps slightly into the rice at the edges. Steam rises from both layers. Hyperrealistic anime style, warm overhead lighting, close-up cinematic detail. ### Scene 11 — 卵のグレーズが自然に落ち着く The finished katsudon bowl rests still on the counter. The soft golden egg glaze slowly settles and spreads naturally over the tonkatsu strips and rice, pooling gently at the sides. The surface is lightly trembling, semi-set, glossy with broth. No hands visible — pure still life in motion. Hyperrealistic anime style, warm diffused lighting, slow cinematic push-in. ### Scene 12 — 完成したカツ丼を提示する A beautifully finished katsudon is presented in a traditional blue-and-white ceramic donburi bowl on a wooden surface. Golden soft egg drapes over crispy tonkatsu strips atop glossy white rice. A small sprig of green mitsuba garnish is placed delicately on top. Wisps of steam rise gracefully. Camera slowly orbits the bowl in a cinematic arc. Hyperrealistic anime style, warm dramatic food photography lighting, cinematic. ## Audio: Upbeat Japanese city pop melody (80s-inspired, bright and breezy) layered with light Koto plucking and chime-like percussion, evoking a cheerful summer lunch atmosphere. Tempo around 110–120 BPM to match the energetic cooking pace. Crisp, satisfying ASMR cooking sound effects throughout: - Sharp, rhythmic knife chopping on a wooden board - Rapid bubbling and rolling boil of noodle water - Crisp clinking of ice cubes dropping into a glass bowl - Rushing water as noodles are rinsed under cold running water - Soft ceramic clink as the finished bowl is set on the counter - Final sound: a single light wind-chime tone as the completed Hiyashi Chuka is revealed, evoking a refreshing summer breeze ## AVOID: - Do NOT show storyboard panels, panel borders, panel numbers, arrows, camera notes, action notes, captions, subtitles, UI overlays, or any annotations in the final video. - Do NOT replicate or display any reference image or sketch passed as input. - Do NOT show any source material, wireframe, or illustration used as reference.
```

---

## 3. Pastel Mob Beach Dance Party

- **id:** `SD2_05285`
- **slug:** `pastel-mob-beach-dance`
- **source URL:** https://x.com/Toshi_nyaruo_AI/status/2074404732450598955
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=5535; quality_score=26 (HF jsonl has no like/view fields)
- **tags:** kawaii anime, group dance, beach pop
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 1920, "height": 1080, "ratio": 1.78, "duration": 130.65, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
A Japanese full-color anime with no captions, no background music, rapid-fire editing, a high frame count, and 24 FPS. Use 「アット」image1 as the main reference for the overall pastel beach-pop mood, shark-hoodie styling, cute character proportions, and playful summer energy. Use 「アット」image2 as the reference for calm-cute facial rendering, pastel eye design, and soft fashion balance. Use 「アット」image3 as the reference for the brighter pastel shark motif, simplified cute silhouette, and pop color blocking. Use 「アット」image4 as the reference for expressive face variety, comic-style split-panel layouts, and energetic reaction diversity. Use 「アット」image5 as the reference for exaggerated cute-chaotic expressions, candy-like graphic decoration, and playful visual intensity. Reference 「アット」audio1 only for beat timing and rhythm if an audio reference is later provided. Do not generate music. Goal: Create a 15-second 720p anime MV-style sequence showing a small group of cute pastel mob dancers joyfully dancing together. The scene should feel playful, bright, social, and energetic, like a fun crowd dance or kawaii flash-mob moment. Do not lock the performance into one exact choreography. Let Seedance infer the dance naturally from the references: group swaying, bouncing, step-touch rhythms, simple synchronized moves, playful arm gestures, turns, reactions, spacing changes, and cheerful group interaction. Focus on lively group motion, camera play, split-screen rhythm, and a cute party atmosphere. Use camera effects and panel composition actively, but keep the characters readable and fun. 0-3s: Open with a lively group reveal. Show multiple cute mob dancers already in motion, using a wide shot, medium group shot, or fisheye-led opening chosen naturally by the generation. Let the group feel immediately active and upbeat. Use playful camera motion, light fisheye distortion, and buoyant rhythm. The dancers should not hold one fixed pose; they should already be moving together in a casual but coordinated way. Floating bubbles, stars, candy-like shapes, clouds, pastel particles, and beachy pop motifs may move through the frame. 3-6s: Move into a more dance-focused section. Let Seedance infer a variety of cute mob-dance actions: small synchronized steps, side-to-side movement, hand waves, shoulder bounces, light turns, call-and-response gestures, and little formation changes. Use alternating camera sizes: medium group shots, brief close-ups, and occasional fisheye push-ins. Show the group’s fun and shared rhythm rather than one leader doing all the work. The dancers should feel like a cheerful crowd moving together. 6-10s: Introduce split-panel and collage rhythm. Break the frame into multiple angled panels that show different dancers, different moments, or different fragments of the same group dance. Some panels may show close-up expressions, some body movement, some group spacing, some hands or accessories. Do not repeat the same pose across all panels. Let the panels behave like a playful remix of the dance. Use sliding panel borders, snapping cuts, slight rotation, and rhythmic reassembly. Allow occasional prism-like edge duplication, cute glitch fragments, or macro inserts of accessories and eyes, but keep the dance energy central. 10-13s: Escalate the group energy. Let the mob dance become more animated and varied without becoming chaotic noise. Seedance may infer little jumps, spins, bounce accents, quick turns, mirrored motions, or playful interaction between neighboring dancers. Use camera effects more actively here: fisheye close-ups, brief macro flashes, snap zooms, whip-like transitions, and layered panel bursts. The group should feel increasingly joyful and lively, as if the dance is peaking. 13-15s: Do not force a standard final hero pose. Let the ending emerge naturally from the dance. Possible endings may include: the group clustering together while still moving, a playful freeze during motion, a split-panel collapse into one group image, a joyful reaction burst, a cute jump or bounce accent, or a clean energetic cut while the dance is still alive. The final beat should feel fun, spontaneous, and satisfying, without looking mechanically predetermined. Keep: - Keep the overall design language consistent with the references: pastel pink, cyan, mint, yellow, lavender, sky blue, and candy-pop accents. - Keep the characters chibi-cute, stylized, expressive, and visually unified, while allowing some variety between mob dancers. - Keep the shark-hoodie / beach-pop / candy-kawaii styling language from the references. - Keep the mood fun, light, social, and energetic. - Keep the animation group-oriented, with multiple dancers visible across the sequence. - Keep the visual emphasis on cheerful dancing, panel rhythm, cute expressions, and playful camera effects. - Keep the rendering flat, graphic, clean, colorful, and slightly sketchy with lively line energy. - Keep the sequence readable even when the edits become fast. Avoid: - No generated text, no subtitles, no logos, no readable signs. - No dark or horror tone. - No gore, no violent imagery. - No realistic live-action look. - No lonely solo performance for the whole clip; it should clearly feel like a mob dance or group dance. - No rigid repeated loop of the exact same move. - No overcomplicated choreography that looks stiff or mechanical. - No excessive effects that hide the dancers for long periods. - No muddy colors or desaturated lighting. - No off-model redesigns that break the reference style.
```

---

## 4. Anime Girls Luxury Parfait Date

- **id:** `SD2_03667`
- **slug:** `anime-girls-luxury-parfait-date`
- **source URL:** https://x.com/Toshi_nyaruo_AI/status/2060646763502117036
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=6074; quality_score=26 (HF jsonl has no like/view fields)
- **tags:** anime, parfait, cafe
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 864, "height": 496, "ratio": 1.74, "duration": 15.13, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
Use Image A and Image B as the two main characters in all shots. Image A{{image A }}: preserve her exact anime illustration identity, hairstyle, face, blue flower hair accessory, outfit, proportions, and overall design. Image B{{image B }}: preserve her exact anime illustration identity, hairstyle, large striped ribbon, twin-bun hairstyle, face, gothic striped outfit, proportions, and overall design. Both characters must remain anime-style illustrations with crisp clean line art, cel-shaded flat colors, expressive anime eyes, and zero photorealism on the characters. All other elements — the SNS-worthy cafe interior, marble tables, glass parfait cups, fruit, cream, gold leaf, desserts, plates, drinks, windows, lighting, other customers, plants, reflections, and background architecture — are fully photorealistic. Setting: a trendy Instagrammable cafe in the afternoon. Soft natural sunlight through large windows, pastel decor, marble tabletops, elegant dessert displays, hanging plants, glass shelves, warm bokeh lights, stylish customers in the background, cozy but luxurious atmosphere. The mood is cute, fashionable, cheerful, and dreamy. Seating layout must remain fixed in every shot. Image A always sits on the viewer-left / camera-left side of the table, closer to the window side. Image B always sits on the viewer-right / camera-right side of the table, closer to the cafe interior side. They are seated side by side on the same elegant sofa bench, not facing each other across the table. The ultra-luxury oversized parfait is placed on the marble table directly in front of them, centered between Image A and Image B. Do not swap their seats. Do not change their left-right positions. Do not make Image A appear on the right side. Do not make Image B appear on the left side. Maintain the 180-degree rule throughout the video. The camera may push in, pull back, tilt, or gently slide sideways, but it must never cross to the opposite side of the table. Avoid full orbit shots around the table because they may reverse the characters’ positions. The main dessert is an ultra-luxury oversized parfait placed between the two girls: a tall crystal glass filled with many colorful layers of strawberry jelly, vanilla cream, chocolate mousse, fresh strawberries, blueberries, melon, peach slices, macarons, wafer sticks, glossy sauce, whipped cream, edible flowers, sparkling sugar, and delicate gold leaf. The parfait should look huge, premium, photorealistic, and extremely SNS-worthy. 15-second cinematic video, 24fps, smooth motion, clear emotional flow, character consistency across all shots. Shot 1 [CAFE ENTRANCE — DISCOVERY] Image A and Image B enter a beautiful SNS-worthy cafe together. They look around with sparkling eyes, impressed by the stylish interior and dessert display case. The camera tracks backward in front of them as they walk inside. Other customers and cafe staff move naturally in the photorealistic background. Their expressions show curiosity and excitement. Cut to Shot 2 [TABLE SEAT — THE PARFAIT ARRIVES] The two girls sit side by side on the same elegant sofa bench at a marble cafe table near a large sunlit window. Image A is on the viewer-left / camera-left side, closer to the window. Image B is on the viewer-right / camera-right side, closer to the cafe interior. A waiter places an ultra-luxury oversized parfait in the center of the table directly in front of them. Image A leans forward with delighted surprise. Image B’s eyes widen softly, looking amazed. Close-up on the enormous parfait sparkling under the cafe lighting, then cut to their happy faces. Cut to Shot 3 [SNS MOMENT — TAKING PHOTOS] Image A and Image B excitedly admire the parfait before eating. Image A gently adjusts the angle of the parfait slightly, while Image B holds up a smartphone to take a cute photo. The parfait glows beautifully with fruit, cream, macarons, edible flowers, and gold leaf. The camera slowly pushes in and gently slides from left to right without crossing the table axis, keeping Image A on the viewer-left and Image B on the viewer-right at all times. Their mood is playful, stylish, and excited. Cut to Shot 4 [FIRST BITE — SWEET HAPPINESS] Both girls pick up their spoons and take their first bite of the parfait. Image A smiles softly with a calm, elegant expression. Image B reacts with a bright, adorable smile, clearly enjoying the sweetness. Close-up on spoons scooping cream, fruit, jelly, and chocolate layers from the parfait. Their hands should remain natural and correctly drawn. Focus on their expressive anime eyes and joyful reactions. Cut to Shot 5 [CAFE JOY — SHARING THE MOMENT] The two girls continue eating the luxurious parfait together, laughing gently and chatting. Image A points at a cute macaron decoration on top of the parfait. Image B happily reacts and leans in slightly while smiling. The camera pulls back into a wide cinematic shot: the two anime-style girls seated at the center of a dreamy photorealistic cafe, surrounded by warm sunlight, pastel decor, desserts, and soft bokeh lights. End with a gentle crane-out while keeping the camera on the same side of the table so Image A remains on the left and Image B remains on the right. Emotional tone: cute, cheerful, luxurious, stylish, friendly, dreamy, and SNS-worthy. Focus on the girls’ expressions at every beat: curiosity, surprise, delight, sweetness, and relaxed happiness. Keep Image A and Image B visually consistent in every shot. Do not change their outfits, hairstyles, accessories, proportions, or core design. Do not make the characters photorealistic. Do not generate readable text, logos, cafe names, menu text, or distorted signage. Avoid outline jitter, flicker, warped hands, extra fingers, extra limbs, distorted faces, melting desserts, or inconsistent character details. The parfait must remain photorealistic, tall, luxurious, colorful, and visually delicious throughout the video. Background customers should move naturally and realistically, without drawing attention away from the two girls and the parfait.
```

---

## 5. Caffeine Chaos Machine

- **id:** `SD2_00969`
- **slug:** `caffeine-chaos-machine`
- **source URL:** https://x.com/joaquin_arana/status/2036538635399692289
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=4994; quality_score=23 (HF jsonl has no like/view fields)
- **tags:** Rube Goldberg, Pixar Style, Coffee Shop
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"duration": 15.09, "height": 720, "ratio": 1.78, "safety_rating": "Safe for Work", "width": 1280}

### Prompt (verbatim)

```text
SUBJECTS: Subject 1: A frantic barista — small, wiry, early 30s with permanently startled eyes and perpetual five o'clock shadow. Wild curly black hair barely contained under a brown newsboy cap. Wears a wrinkled olive-green apron over a flannel shirt with haphazardly rolled sleeves. Moves like a pinball — bouncing between stations, sliding across the floor, catching things mid-air without looking. Every movement triggers the next part of the machine. His body IS part of the mechanism. Pixar-style 3D rendering: rubbery expressive limbs, exaggerated squash-and-stretch on fast movements, warm skin tones. Subject 2: The café itself — every object is a component of one interconnected Rube Goldberg machine. The espresso machine is the central engine. The sequence involves: a marble track built from bent spoons along the ceiling, balanced cups on saucers that tip like dominoes, a hanging mobile of sugar cubes acting as a counterweight system, a toy train on a track delivering milk from the fridge to the steamer, and a small catapult made from a ruler and napkin holder that launches the finished cup to the counter. Subject 3: The customer — a deadpan woman in a business suit, briefcase in hand, reading glasses on a chain. Completely unfazed by the chaos. She stands at the counter with the patience of someone who has seen this before. ENVIRONMENT: A tiny corner café — barely ten feet wide. Exposed brick walls covered in chalkboard menus with hand-drawn coffee illustrations. Every horizontal surface has a mechanical element: marble tracks on shelves, cup-and-saucer balance chains along the counter, tiny pulleys strung from the ceiling with twine. Warm morning light streams through a single front window catching dust and steam. A small bell hangs above the door. The whole space feels like a brilliant inventor's workshop that serves coffee. MOOD: Manic joy. The barista is in his element — the chaos is intentional, practiced, musical. Every crash, pour, and launch is precisely timed. The punchline deflates the entire spectacle in the best possible way. TIMELINE: 0:00–0:03: The door opens — bell dings. The customer places her briefcase on the counter. Says nothing. The barista points at her, nods — he knows the order. He flicks a marble from his apron pocket onto a ceiling track. The marble rolls — clicking over ridges, banking around a curve, dropping through a funnel into a cup on a saucer on a high shelf. The cup's weight tips the saucer, pulls a string, releases a cabinet latch — coffee beans slide down a ramp into a hand-crank grinder. Audible: bell ding, marble clicking on track, cup clinking, string twang, beans cascading. 0:03–0:06: The barista cranks the grinder with one hand while pulling a lever starting the toy train. The train chugs along a counter-edge track — passes the fridge where a small arm places a milk carton in the car — continues to the steam wand where the track tilts and pours milk into a steaming pitcher. Ground coffee falls through a chute into the portafilter. The barista slams it in with his elbow while catching a falling sugar cube from the overhead mobile with his other hand, dropping it into a cup. Audible: grinder crunching, train chugging and whistling, milk pouring, portafilter clicking, mobile tinkling. 0:06–0:09: Espresso machine fires — rich dark coffee flowing into a porcelain cup. Close-up: crema forming, thick and golden-red, swirling. The barista steams milk — pitcher vibrating, velvety microfoam building. He pours with a practiced wrist flick — a perfect rosetta latte art pattern forms. He tops it with a single coffee bean placed dead center. Camera lingers on the completed drink — perfect, beautiful. Audible: espresso hissing, milk steaming (tearing-paper sound), the gentle pour, the bean placed with a tiny tap. 0:09–0:12: The delivery. The barista places the cup on the ruler catapult and slams his palm down. The cup launches in a perfect arc — camera follows in slow motion as it rotates, latte art intact, not a drop spilled. It lands with a clean clink on a saucer directly before the customer. Steam rises in a perfect spiral. The barista slides into frame behind the counter, slightly breathless, fingers pointing at the drink with showman's pride. Audible: catapult snap, cup whistling through air, clean landing clink, a beat of silence. 0:12–0:15: The customer adjusts her reading glasses. Looks at the latte art. Looks at the barista. "Actually — can I get tea?" The barista's face falls — completely deflated. Shoulders drop. Cap slides askew. A long beat. Then his eyes snap back to life. He pulls out a different marble — a green one — and flicks it onto a completely different track on the opposite wall. The entire café begins moving again — a whole new sequence activating. The customer takes a seat. She's done this before. Cut to black. Audible: her flat delivery, the defeated exhale, then the green marble clicking onto the track and the café machine roaring back to life.
```

---

