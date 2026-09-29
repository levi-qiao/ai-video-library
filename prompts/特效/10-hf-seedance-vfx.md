# Seedance HF curated prompts — `特效`

> body: verbatim — full original prompt text only; no summary/teaser.

Source dataset: https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets  
License tag: `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`  
Curation: 2026-09-29 Asia/Shanghai. Prompts are **verbatim** `raw_p` fields. No invention.

Evening QC 2026-09-29: removed 4 fences cut mid-token (`rem` / `resolutio` / `J` / `b`).

Count in this file: **14**

---

## 1. Night Street Racing Cinematic Sequence

- **id:** `SD2_00006`
- **slug:** `night-street-racing-cinematic`
- **source URL:** https://x.com/CharaspowerAI/status/2039651574297792688
- **model:** Seedance 2.0
- **featured:** True
- **engagement proxy:** dataset featured=True; prompt_len=1497; quality_score=27 (HF jsonl has no like/view fields)
- **tags:** street racing, night driving, cinematic
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"duration": 12.08, "height": 720, "ratio": 1.78, "safety_rating": "Safe for Work", "width": 1280}

### Prompt (verbatim)

```text
cinematic street racing sequence at night, a focused driver inside a high-performance car grips the steering wheel, intense eye focus, city lights reflecting on windshield, tension building before sudden acceleration

camera: rapid multi-angle system with seamless transitions, interior close-up → over-the-shoulder → exterior tracking → low ground shots, ultra dynamic camera movement, whip pans + speed ramp transitions + motion blur masking cuts, continuous flow illusion

(0-2s) interior close-up on driver, hand tightens on gear shift, subtle breathing, dashboard lights glowing
(2-4s) over-the-shoulder shot, road ahead stretching into neon-lit city, engine vibration building
(4-6s) extreme close-up on finger pressing NOS button, instant ignition reaction
(6-8s) explosive acceleration, camera snaps to exterior side tracking shot, car launches forward with violent speed surge
(8-10s) ultra low ground shot near asphalt, wheels spinning at extreme velocity, environment streaking past
(10-12s) high-speed chase through tight streets, sharp turns, camera whip pans between angles, reflections and light trails enhancing speed

Dense urban night environment, wet asphalt reflecting neon lights, tunnel passages, street lights streaking, high-speed city atmosphere
Ultra realistic, fast and furious inspired energy, photorealistic lighting, intense motion blur, high contrast neon reflections, cinematic depth of field, extreme sense of speed, fluid transitions, no distortion, no stretching
```

---

## 2. Cricket Stadium Couple Zoom Shot

- **id:** `SD2_02796`
- **slug:** `cricket-stadium-couple-zoom-shot`
- **source URL:** https://x.com/XSydneyFan/status/2054443409881043384
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=7506; quality_score=26 (HF jsonl has no like/view fields)
- **tags:** IPL, Broadcast, Crowd
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"duration": 15.04, "height": 1080, "ratio": 1.77, "safety_rating": "Safe for Work", "width": 1916}

### Prompt (verbatim)

```text
Create a photorealistic 16:9 live Indian cricket broadcast screenshot of a young couple captured from far away by a stadium zoom camera during an IPL-style night match.
Use the provided face reference image for the man and keep his facial features highly accurate: same face shape, eyes, nose, lips, beard/stubble pattern, skin tone, hairstyle volume, and natural expression. Do not beautify or change his identity. He should look like the same person from the reference, only seated in a cricket stadium.
Use the provided woman reference for the woman, but make her realistic and human, not doll-like. Keep her attractive but grounded with natural skin texture, realistic eyes, subtle imperfections, believable facial proportions, and soft candid expression.
Scene:
The couple is sitting among a dense crowd inside a packed Indian cricket stadium during a night match. They are not posing for the camera. They look like they were unexpectedly picked up by the long-range broadcast camera installed in the stadium. The camera is far away and zoomed in, like real IPL audience reaction shots.
Important camera style:
This should NOT look like a camera is directly in front of them.
This should NOT look like a close DSLR portrait or staged photoshoot.
Make it look like a telephoto broadcast zoom shot from across the stadium.
Use long-lens compression, slightly flattened perspective, medium-wide crowd framing, mild atmospheric haze, subtle broadcast softness, minor motion blur, slight digital zoom artifacts, realistic compression noise, and live TV sharpness.
The couple should be visible clearly, but not overly crisp or perfectly lit.
Composition:
Frame them from the audience section, with other spectators partially blocking the foreground and background. Some heads, shoulders, flags, and jerseys should naturally overlap the frame, making it feel like the broadcast camera is peeking through the crowd. The couple should be seated in the middle rows, not isolated. Keep surrounding fans close to them so they feel integrated in the stadium crowd.
Pose and emotion:
The man has his arm naturally around the woman’s shoulder and holds a red-and-silver soda can in his other hand. He wears a light blue casual shirt or a light checkered shirt, matching the cool blue stadium vibe. The woman wears a blue summer dress. They are looking at each other with shy, warm, candid chemistry, as if they just realized they are on the big screen. Their expressions should be natural, slightly surprised, and sweet, not posed.
Lighting:
Use only ambient stadium lighting and weak spill light from the cricket field. No cinematic spotlight. No dramatic key light. No beauty lighting. The couple should blend into the crowd brightness naturally, like a real live match broadcast. Skin tones should have natural stadium-light shadows and slight unevenness.
Background:
Packed Indian cricket stadium, night match atmosphere, fans in blue jerseys, waving flags, LED ribbon boards, stadium seating, blurred crowd movement, lively but realistic environment. The crowd should feel dense and natural, not generated or empty.
Broadcast overlay:
Add a Star Sports-style Indian cricket broadcast presentation:

channel watermark in the top corner, inspired by Indian sports TV

LIVE tag

modern cricket scoreboard lower-third

fictional team names only

fictional score, overs, wickets

run rate or required run rate

batsman and bowler stats

small commentary ticker

clean layered TV graphics

Do not use real IPL team names, real player names, real sponsors, or real match details. Use fictional teams and fictional players.
Quality:
Ultra-photorealistic, authentic live sports telecast look, realistic human skin texture, natural fabric details, believable stadium zoom-camera perspective, subtle compression artifacts, slightly imperfect broadcast capture, candid audience reaction moment.Negative prompt:
Do not make it look like a professional portrait photoshoot.
Do not make the couple look directly into the camera.
Do not use cinematic lighting.
Do not isolate them from the crowd.
Do not make the faces overly smooth or doll-like.
Do not make the man’s face generic.
Do not change the man’s identity from the reference image.
Do not create fake plastic skin.
Do not use real IPL team names or real player names.
Do not make the scoreboard unreadable or messy.
Do not make it look like a front-facing mobile photo.

---------------------------------------------

Video Generation prompt:

Create a realistic 15-second single-take live IPL-style Indian cricket broadcast crowd cutaway during a packed night match. Telephoto long-lens zoom shot from far away in the stadium, like a professional audience camera operator spotting the couple naturally. Use realistic broadcast lens compression, slight softness, mild motion blur, subtle TV grain, digital compression artifacts, and authentic sports framing. No cuts, no angle changes, single continuous shot only.

The couple must exactly match the reference image: Boyfriend preserves identical facial structure, hairstyle, stubble/beard pattern, skin tone, and natural expression. He wears the same light grey-blue small check shirt. One arm rests naturally around the girl’s shoulder. He holds a silver-and-red soda can in his other hand at the start. Girl matches exact appearance, hairstyle, makeup, and wears the same blue floral summer dress. Both remain seated throughout.

Environment: Dense packed Indian cricket stadium at night, IPL energy, blue jerseys, stadium seats, LED boards, bright floodlights, natural ambient lighting. Couple embedded in crowd with partial heads/shoulders in foreground and background for authentic zoomed-in broadcast feel.

Action timing (natural, subtle, non-staged):

0-4s: Camera lands smoothly on the couple. Boyfriend casually watches the match, relaxed smile reacting to stadium screen. Girl notices they’re on broadcast, smiles shyly, avoids direct eye contact. Slight natural surprise.

4-7s: Boyfriend lifts soda can slightly in playful celebratory gesture (still focused on match). Girl becomes shy, briefly hides part of her smiling face with hands. Surrounding crowd reacts naturally.

7-11s: Boyfriend lowers can, forms half-heart gesture with fingers toward girl. She shyly completes the heart. Subtle, spontaneous, believable. Nearby spectators cheer lightly and laugh.

11-13s: Girl leans in for soft peck on his cheek. Boyfriend responds with proud grin and small laugh, still immersed in match atmosphere.

13-15s: Both slightly embarrassed, soft smiles. Girl shyly hides smile and looks away. Boyfriend returns attention to cricket screen. Both stay seated comfortably.

Do NOT make them look directly at camera often. Minimal eye contact. No exaggerated acting. Feel like genuine live crowd moment.

Broadcast graphics: Static IPL-style scorebug at bottom throughout (no changes). Fictional teams e.g. Mumbai Indians vs Chennai Super Kings, Score: MI 142/4 (16.2 overs), RR 8.75 | RRR 9.2. Batsman & bowler stats. LIVE tag. Top-corner channel watermark (e.g. STAR SPORTS LIVE).

Audio: Natural stadium ambience, distant cheering, crowd murmur, soft laughter during heart & kiss. Two male Indian cricket commentators casually reacting: “Look at that lovely moment in the crowd!” “Aww, heart gesture and a kiss – perfect IPL night!”

No couple dialogue. No whispering. Preserve exact identities and wardrobe. Far-away telephoto broadcast look, not cinematic or close-up. Must feel authentic IPL live cutaway.
```

---

## 3. Anime Girls Luxury Parfait Date

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

## 4. Cinematic Dragon Bond On Alpine Peak

- **id:** `SD2_10776`
- **slug:** `alpine-dragon-bond`
- **source URL:** https://x.com/Just_sharon7/status/2080906169309442468
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=5935; quality_score=26 (HF jsonl has no like/view fields)
- **tags:** cinematic, dragon, photorealistic
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 1280, "height": 720, "ratio": 1.78, "duration": 15.08, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
Create a 15-second hyper-realistic live-action cinematic video in 16:9 with fast-paced, emotionally warm storytelling, spectacular action, and seamless multi-shot transitions. Absolute photorealism with feature-film quality, shot on anamorphic 35mm lenses, realistic camera physics, subtle handheld movement, natural lens breathing, cinematic motion blur, restrained film grain, and physically accurate lighting. The scene takes place entirely on a rugged alpine mountain summit with jagged gray metamorphic rocks, loose gravel, exposed cliff edges, dry golden alpine grass, distant mountain ranges, a deep blue sky with thin cirrus clouds and low white cumulus clouds, illuminated by crisp late-morning sunlight. Maintain perfect environmental continuity throughout every shot. The main character is a beautiful woman, approximately 25 years old, with long thick naturally wavy blonde hair, fair skin, bright blue eyes, and an athletic feminine build. She wears a weathered brown leather medieval explorer outfit consisting of a fitted leather tunic, dark trousers, tall leather boots, leather bracers, a travel satchel, a belt, and a medieval sword. Preserve her exact facial features, hairstyle, clothing, body proportions, and identity consistently throughout the entire video. Her companion is a gigantic biologically realistic pink-red dragon with dusty reptilian scales, amber eyes, curved horns, muscular limbs, powerful claws, a long tail, and large translucent wing membranes with visible veins. The dragon behaves like a real undiscovered animal, with subtle breathing, shifting muscles beneath its scales, moist reflective eyes, realistic weight, and physically accurate interactions with the environment. The dragon always remains vastly larger than the woman. A powerful alpine crosswind acts as a third character throughout the sequence, constantly influencing the woman's flowing blonde hair, clothing, satchel straps, grass, dust, loose gravel, and the dragon's wing membranes and neck spines. Every gust behaves naturally according to the terrain and camera angle, with believable delayed secondary motion. The sequence begins with an extreme ground-level camera hidden between dry grass and sharp rocks. Wind drives dust and gravel across the lens while the woman stands confidently on the exposed ridge. A gigantic dragon shadow sweeps rapidly across the landscape before one enormous wing passes overhead, dramatically darkening the frame and creating a violent pressure gust. Cut to a dynamic forward-moving perspective traveling low toward the woman as the dragon approaches at high speed. The mountain rocks rush past with strong parallax while her long blonde hair and leather clothing whip dramatically in the wind. The dragon's heavy breathing creates subtle camera movement. Transition into a fast lateral tracking shot racing parallel to the rocky ridge. Foreground boulders repeatedly hide and reveal the action while the dragon runs beside the woman with tremendous weight. Massive claws strike loose gravel, sending rocks toward the camera as dust trails behind. The dragon suddenly brakes beside her, carving deep tracks into the rocky ground while a sweeping cloud of dust fills the frame. Move into a close reverse circular orbit around both characters as the dragon gently lowers its enormous head. The woman smiles warmly, steps closer, and softly places one hand against the dragon's snout. Their foreheads gently touch in an intimate emotional moment as the dragon's folded wing temporarily shelters them from the wind. Focus shifts naturally from her fingers resting on the scales to the dragon's amber eye and finally to her genuine smile. Cut to an unusual snout-mounted close-up beside the dragon's muzzle. The dragon gives a playful snort, blasting a gust of wind that sends the woman's long wavy blonde hair, clothing, and satchel flying backward. Laughing naturally, she briefly loses her balance before affectionately pushing the dragon's muzzle away with both hands. The dragon playfully nudges her again while the camera receives a subtle physical bump, creating an authentic documentary feel. Transition to a perfectly vertical top-down aerial shot directly above the rocky clearing. The dragon unfolds its enormous wings around the woman, nearly filling the frame. A single powerful wingbeat creates a visible expanding pressure wave across the terrain, pushing dust, grass, gravel, and clothing outward in physically accurate concentric motion. The woman crouches, shielding her face while laughing as the dragon begins its powerful takeoff run. Finish with a dramatic cliff-edge aerial shot as the dragon launches directly over the camera. Loose stones fall past the lens while one translucent wing passes overhead, revealing veins, scars, and stretched organic membranes illuminated by sunlight. The camera dives backward along the cliff before stabilizing into a sweeping cinematic reveal of the mountain summit and expansive valley. The dragon performs one fast, low fly-by above the woman, whose hair and clothing are once again swept by the powerful wake. End with a wide composition of the woman standing alone on the exposed ridge as the dragon gracefully glides across the open sky above the vast mountain landscape. Maintain absolute live-action realism throughout with consistent lighting, geography, scale, anatomy, wind direction, environmental continuity, and character identity. Negative Prompt: CGI, animation, cartoon, stylized fantasy, magical effects, glowing eyes, fire breathing, supernatural particles, unrealistic physics, weightless movement, plastic textures, synthetic skin, morphing, duplicated characters, anatomy changes, inconsistent scale, extra limbs, deformed wings, inconsistent lighting, random landscape changes, HDR look, oversaturated colors, text, captions, subtitles, logos, watermarks, interface elements, low quality, blur, noise, artifacts.
```

---

## 5. Lazy Boss Lady Diner Comedy

- **id:** `SD2_10990`
- **slug:** `lazy-boss-lady-diner-comedy`
- **source URL:** https://x.com/john87445528/status/2082804507839193581
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=5493; quality_score=26 (HF jsonl has no like/view fields)
- **tags:** diner, boss lady, comedy
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 720, "height": 1280, "ratio": 0.56, "duration": 37.83, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
第一幕：【参考锁定】 参考图1 hf_20260730_044943_833909d3-0181-4d86-b4ad-8fdd91945fbd 为老板娘#1 穿着 hf_20260730_045132_8f945ce1-0e33-4e9c-86c6-5b5bdb0b0185 腿脚比例、薄袜质感、沙发坐姿及黑色高跟鞋位置的最高优先级；保持#1已经预设的脸部、发型、妆容和服装。 参考视频为小饭馆空间、男#2 与食客#3 的外貌、身形、服装和生活化表演节奏的最高优先级。 #1、#2、#3均为成年人，不得换脸、复制、合并或互换身份。 【整体设定】 真实小饭馆生活喜剧。 老板娘#1坐在左后方休息区沙发上刷手机，呈现克制、自然的“海妖风 Pose”：身体斜靠沙发，一侧肩膀略微下沉，腰背形成自然柔和的S形曲线；双腿优雅交叠并略微伸向前方，脚尖放松；头部轻轻侧倾，黑色长发自然落在一侧肩头。姿态具有安静、慵懒、带吸引力的气质，但不主动挑逗食客，不舔嘴、不抛媚眼、不刻意扭动身体。 男#2坐在右前方的第一张绿色旧餐桌吃面。食客#3坐在右后方另一张独立餐桌吃面，两张桌子之间留有清楚的过道，二人绝不坐在同一张桌子旁。 男#2吃面时看老板娘#1短暂发愣，随后叫她拿一瓶橙色饮料。食客#3从餐桌第一次出现时就坐在另一张桌子吃面，为后续反转建立空间位置。 【真实系拍摄】 未经处理的iPhone手持真实视频。9:16竖屏，1080×1920，30fps，26—28mm等效焦段，普通食客站在约1—1.5米外拍摄。 自动曝光、自动对焦、自动白平衡。保留轻微手抖、呼吸起伏、重新取景的半拍延迟、短暂对焦搜索、运动模糊、窗边局部过曝和暗部噪点。 无滤镜、无美颜、无磨皮、无电影布光、无稳定器运镜、无人工浅景深。保留真实皮肤纹理、零散发丝、服装褶皱和薄袜自然反光。 【人物位置】 老板娘#1：左后方米灰色双人沙发。斜靠沙发刷手机，保持自然海妖风坐姿，暂时没有注意食客。 男#2：右前方第一张绿色旧餐桌，独自吃面，是开口叫饮料的人。 食客#3：右后方第二张独立旧餐桌，与男#2相隔约一米，中间有明显过道。他独自吃面，不与男#2同步动作，也不提前说话。 【空间与道具】 左后方：米灰色沙发、老板娘的手机、一双放在脚边的黑色高跟鞋，其中一只更靠近镜头。 中央后方：饮料冰柜、服务台、米黄色记账本。 右前方第一桌：男#2、一碗面、一双筷子、一小碟调料。 右后方第二桌：食客#3、另一碗面、另一双筷子、另一小碟调料。 两名男食客的桌子、面碗、筷子和调料完全独立，不共享、不复制、不交换。 冰柜内只有一瓶橙色饮料：约500毫升透明硬质塑料瓶，内部为自然透光的橙黄色液体，彩色防盗环旋盖。全片只出现这一瓶，不得提前出现在餐桌上。 【15秒严格分镜】 → 0—2秒：低机位脚部建立镜头 镜头从老板娘#1搭在沙发边缘的双腿开始。她维持克制的海妖风坐姿：双腿自然交叠，腿部略向前伸，薄袜有细腻但不过度的真实反光，脚尖自然放松。 一双黑色高跟鞋放在木纹地面，其中一只靠近前景。自动对焦短暂搜索后落在前侧脚部和沙发边缘。镜头只作快速生活化建立，不缓慢扫描腿部。 → 2—4秒：老板娘沙发中景 摄影者自然抬高手臂，镜头快速上移到老板娘上半身。她身体斜靠沙发，一侧肩膀稍低，腰背呈柔和S形曲线，头部轻轻侧倾，长发落在一侧肩头。 她低头用拇指滑动手机，嘴角因手机内容出现很浅的笑意，神态安静慵懒，没有看两名食客。对焦从前景自然漂移到她的脸。 → 4—6.8秒：两张餐桌同框 硬切右侧用餐区稍宽中景。男#2坐在右前方第一张桌子；食客#3清楚出现在右后方第二张桌子。两张桌子之间有明显过道。 男#2吸入一口面，随后抬眼越过面碗，看向左后方的老板娘。筷子停在嘴边，剩余面条短暂悬在筷子与碗之间，他自然走神。 食客#3始终在另一张桌子低头夹面、吹面和咀嚼，不抬头，不与男#2同步。 → 6.8—8.5秒：男#2叫饮料 男#2眨一下眼回过神，把剩余面条吸完，朝老板娘方向抬手喊： “老板娘，再来瓶饮料！” 食客#3仍在右后方自己的桌子吃面，只在听见声音时出现非常轻微的停顿，但不抬头、不说话。 → 8.5—10.5秒：老板娘响应并起身 硬切老板娘中景。她停止滑动手机，抬眼看向男#2，平静回应： “哎，来啦。” 她锁上手机，将手机正面朝下放在沙发扶手上。随后结束斜靠姿态，身体自然前倾，双脚分别滑入地面上的一双黑色高跟鞋并起身。手机必须留在沙发扶手上。 → 10.5—12.5秒：冰柜取饮料 硬切冰柜侧面中景。冰柜侧面中景。老板娘打开老式玻璃冰柜，只取出一瓶密封橙色饮料；左手顺势从服务台拿起米黄色记账本。冰柜关闭后，她立即转入中央过道，行走时身体微侧成S曲线，胯部轻微侧推，双腿前后错位拉长，半垂眼冷感前视。 → 12.5—15秒：送到男#2桌边 手持镜头跟随老板娘从左后方向右前方快步移动，画面产生自然上下晃动和轻微运动模糊。 她停在两桌之间的过道中央，身体微侧朝向画面左侧的男#2，形成流畅S曲线，肩颈拉长，半垂眼冷感直视#2，把橙色饮料放在#2桌面：“来，您的饮料。” 最后一帧：橙色饮料仍然密封，老板娘左手拿着记账本；两个男食客分别坐在两张不同餐桌旁。 【音频】 仅使用饭馆画内自然声：冰柜压缩机、排风扇、远处交谈、吸面声、筷子碰碗声、高跟鞋落地声、柜门开合声、脚步声和饮料瓶接触桌面的声音。 对白带真实饭馆混响，距离改变时音量自然变化。无背景音乐、旁白、罐头笑声和后期音效。 【连续性要求】 老板娘始终从左后方向右前方移动。男#2固定在右前方第一桌，食客#3固定在右后方第二桌，两人不得坐到一起。 #3从用餐区第一次出现时就必须清楚存在。两张餐桌、两碗面、两双筷子各自独立。橙色饮料只能从冰柜取出一次，送到男#2桌边时仍然密封。 老板娘的海妖风 Pose只出现在沙发段落；起身工作后恢复自然、利落的饭馆老板娘动作。 【负面提示】 不要让男#2和食客#3坐在同一张桌子；不要共享面碗、筷子或调料；不要把#3生成成#2的复制人；不要两人同步吃面、同步抬头或同步说话。 不要把海妖风姿态表现成跳舞、扭胯、抛媚眼、舔嘴、夸张挺胸或情色表演；不要色情化腿脚镜头，不要缓慢扫描身体。 不要改变#1的脸、发型、服装、腿脚比例和薄袜质感；不要让手机、高跟鞋、面条、筷子、记账本或饮料漂浮、瞬移、复制。 不要把普通小饭馆变成豪华餐厅；不要HDR、电影调色、强烈光晕、过强虚化、塑料皮肤、稳定器运镜、慢动作、字幕、水印或平台UI。 第二幕：【参考锁定】 参考图1 hf_20260730_044943_833909d3-0181-4d86-b4ad-8fdd91945fbd 为老板娘#1 穿着 hf_20260730_045132_8f945ce1-0e33-4e9c-86c6-5b5bdb0b0185 时的腿脚比例、薄袜质感、身体线条及黑色高跟鞋造型的最高优先级；保持#1预设的脸部、发型、妆容和服装。 参考视频为小饭馆空间、男#2 与食客#3 的外貌、身形、服装和生活化表演节奏的最高优先级。 三人均为成年人，不得换脸、复制、合并或互换身份。 【续写起点】 使用Part A最后一帧 7月30日 ：老板娘#1站在两张餐桌之间的过道位置，身体微侧面对男#2，左手拿米黄色记账本；男#2坐在右前方第一张绿色旧餐桌，右手刚碰到桌上唯一一瓶密封橙色饮料；食客#3坐在右后方第二张独立餐桌，手中拿着筷子，从侧后方观察。 老板娘的手机仍留在左后方沙发扶手。人物、桌椅、餐具、灯光和饭店空间完全延续Part A。 【整体设定】 男#2询问饮料价格，听见六块后只肯出五块。老板娘不争辩，保持克制自然的海妖风Pose，收回饮料，打开后喝一小口，再把喝过的饮料递给男#2。 食客#3看见全过程，停止吃面，看着老板娘说：“这样的，给我来一箱。”老板娘嘴里仍含少量饮料，冷艳表情瞬间破功，用记账本遮住下半张脸，忍不住将饮料笑喷在记账本背面。 【真实系拍摄】 未经处理的iPhone手持真实视频。9:16竖屏，1080×1920，30fps，26—28mm等效焦段，普通食客在约1—1.5米外拍摄。 自动曝光、自动对焦、自动白平衡。镜头在男#2、老板娘与食客#3之间转动时，保留轻微手抖、呼吸起伏、重新取景的半拍延迟、短暂对焦搜索和真实运动模糊。 白平衡在店门自然光、冷白荧光顶灯和冰柜余光之间轻微变化。图像平坦，保留窗边局部过曝、暗部噪点、边缘色差和自然皮肤纹理。无滤镜、美颜、磨皮、电影布光、稳定器运镜和人工浅景深。 【人物位置与表演】 老板娘#1：站在两桌旁的过道位置，主要面对男#2，同时不能遮挡食客#3观察她喝饮料的视线。身体微侧，肩部放松下沉，颈部自然拉长，腰背与胯部形成柔和S形曲线；双腿前后错位，一条腿承重。半垂眼皮，表情冷静、带距离感，但不主动挑逗。 男#2：固定坐在右前方第一张桌，是问价、砍价和接饮料的人。 食客#3：固定坐在右后方第二张独立餐桌，与#2相隔约一米。他只能观察并说最后一句，不能走到#2桌旁。 【空间与道具】 右前方第一桌属于男#2：一碗面、一双筷子、一小碟调料。 右后方第二桌属于食客#3：另一碗面、另一双筷子、另一小碟调料。 两桌餐具完全独立，不共享、不复制、不交换。 全片只有一瓶约500毫升橙色饮料：透明硬质塑料瓶、橙黄色液体、彩色防盗环旋盖。状态严格连续： 密封满瓶 → #2拿起 → 老板娘收回 → 打开 → 喝一口 → 液面下降 → 递给#2 瓶盖和米黄色记账本不能消失、变形或复制。 【15秒严格分镜】 → 0—2秒：问价与回答 男#2拿起密封橙色饮料，看一眼瓶身，抬头问： “这多少钱？” 自动对焦先落在橙色液体和瓶身高光，再稍慢地转到#2的脸。 老板娘微侧面对他，肩部下沉，颈部拉长。她从半垂眼皮下看一眼饮料，再冷静回答： “六块。” 食客#3仍在右后方自己的餐桌吃面，不提前参与。 → 2—3.8秒：男#2砍价 男#2轻轻掂一下饮料，眉头抬起，商量道： “我就五块，五块行不行？” 食客#3夹面的动作出现轻微停顿，眼睛从面碗上方看向两人，但不抬头说话。 → 3.8—5秒：老板娘收回饮料 老板娘不争辩，也不生气。她安静看#2约0.3秒，保持柔和S形站姿，随后伸出右手握住瓶颈。 男#2确认她握稳后松手。饮料完整回到老板娘手中，两人的手不黏连、不穿模，也不长时间接触。 → 5—6.3秒：开瓶 老板娘把记账本夹在左臂与身体之间，左手握住彩色瓶盖，右手固定瓶身，旋开防盗环瓶盖。 传出清楚的“咔”声。瓶盖保留在左手，饮料没有飞溅。对焦短暂落在手指和瓶盖上。 → 6.3—7.8秒：喝一口 老板娘身体微侧，下巴只抬高约8—10度，颈部线条自然拉长。她抬起橙色饮料喝一小口，半垂眼睛越过瓶身短暂看向男#2，随后自然移开。 液面随瓶身倾斜而倾斜。她只咽下一部分，嘴里保留少量饮料，双唇自然闭合，脸颊仅轻微鼓起。瓶内液面真实下降约一口的体积。 她的站位不能遮住食客#3，#3必须清楚看见她喝饮料。 → 7.8—9秒：递给男#2 老板娘把瓶盖松松扣回瓶口，将已经喝过一口的饮料递给男#2。 男#2在自己的桌边接住瓶身中部。老板娘确认他握稳后才松手。瓶内液体因交接产生两次逐渐减弱的晃动。 男#2先看瓶口，再抬眼看老板娘，嘴巴微微张开，表情错愕。 → 9—11.8秒：食客#3说反转台词 食客#3停止吃面，筷子悬在自己的面碗上方。他先看男#2手中已经打开、液面下降的饮料，再抬眼看向老板娘。 摄影者轻微转向#3，自动对焦短暂搜索后稳定在他的脸上。#3坐在原位，用筷子轻轻指向那瓶饮料，一本正经地说： “这样的，给我来一箱。” #3不站起、不靠近#2，不舔嘴、不挑眉、不做猥琐表情。 → 11.8—15秒：老板娘笑喷 镜头迅速转回老板娘。她嘴里仍含着刚才没有完全咽下的少量橙色饮料。 她原本保持半垂眼皮和冷静S形站姿；听见#3的话后，眼睛突然睁大，眉毛抬起，头部转向#3，身体僵住约0.3秒。 随后她立即举起米黄色记账本遮住下半张脸，肩膀控制不住地抖动，忍笑失败。少量橙色细雾和两三滴饮料短促喷在记账本背面，并从上缘和侧缘溅出后向下掉落。 不能喷到#2、#3、两碗面或其他食物。 最后一帧：男#2坐在第一桌拿着喝过的饮料发愣；食客#3坐在第二桌认真等待一箱；老板娘站在过道，用记账本遮脸轻咳、忍笑。 【音频】 仅使用饭馆画内自然声：冰柜压缩机、排风扇、远处交谈、两桌不同方向的吸面声、筷子碰碗声、瓶盖防盗环断裂声、液体晃动声、吞咽声，以及老板娘结尾的短促呛咳和笑声。 对白与口型同步，声音来源唯一。无背景音乐、旁白、罐头笑声和后期反转音效。 【连续性与负面提示】 男#2固定在右前方第一桌，食客#3固定在右后方第二桌；两人不得合桌、换位、共用面碗和筷子。#2负责问价、砍价和接瓶；#3只能观察并说最后一句，不能参与砍价或碰饮料。 不要改变三人的脸、发型、服装和身形；不要饮料瓶、瓶盖、记账本和餐具漂浮、瞬移、穿模或复制；不要饮料变成水、液面不下降或自动回满；不要假喝、嘴唇穿瓶或提前完全咽下后凭空喷出。 不要夸张扭胯、猫步、舔嘴、吐舌或色情化表演；不要女妖角、翅膀、尾巴和奇幻特效；不要把小饭馆变成豪华餐厅或宾馆；不要大口喷射、呕吐或喷到人物和食物；不要HDR、电影调色、过强虚化、塑料皮肤、稳定器运镜、慢动作、字幕、水印或平台UI。
```

---

## 6. Luxury Cinematic Fashion Construction

- **id:** `SD2_04072`
- **slug:** `luxury-cinematic-fashion-construction`
- **source URL:** https://x.com/AIwithAliya/status/2055674114845925710
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=7900; quality_score=23 (HF jsonl has no like/view fields)
- **tags:** luxury fashion, cinematic architecture, material transformation
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 1080, "height": 1350, "ratio": 0.8, "duration": 15.1, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
Ultra-luxury cinematic fashion construction film. STRICTLY follow all 12 storyboard panels sequentially without skipping, merging, shortening, reordering, or improvising any panel. Every shot must transition smoothly into the next in exact numerical order from Panel 1 through Panel 12. Total runtime exactly 155 seconds. Maintain absolute continuity in lighting, material behavior, camera language, scale progression, and object identity throughout the entire film. Only ONE shoe exists during the entire video — never show a pair under any circumstance.

Visual format: 65mm IMAX film aesthetic, macro-capable Panavision anamorphic lens, ultra-sharp macro detail, shallow cinematic depth of field, fine editorial film grain throughout, subtle horizontal anamorphic lens flares ONLY from thread highlights and suede edge speculars. Infinity cyclorama studio environment with seamless pale grey-to-white gradient background where the floor curves upward into the wall with no visible horizon line. Warm-neutral soft key light from above camera-left creating one consistent clean shadow falling back-right in every shot. Lighting inspired by Loewe / Hermès luxury editorial campaigns — soft but directional, warm and premium, never harsh, never blue, never high contrast, never crushed blacks. Stable cinematography only. No jitter, no AI morphing, no flicker, no ghosting.

The entire narrative is a meditative material-transformation journey where a single deep crimson liquid droplet gradually evolves into a handcrafted suede slingback heel through couture construction and hidden comfort engineering. Every material interaction obeys realistic physics. Diegetic sound only — no music, no score.

PANEL 1 — THE VOID (00:00–00:10)
Wide locked-off cinematic shot of an empty infinity cyclorama studio with pale grey-to-white seamless gradient background. Atmospheric dust floating slowly in warm studio light. Exposure breathing subtly. Silence and soft room tone dominate. After several seconds, one tiny deep crimson droplet slowly falls into frame from above in near weightless slow motion, rotating slightly while catching warm highlights. The droplet lands center frame on the polished cyclorama floor with realistic liquid surface tension physics. It briefly holds spherical form before gently flattening outward. One soft shadow falls back-right. Sound: low room tone, elegant bell-like tick on impact, delicate reverb decay.
PANEL 2 — SURFACE TENSION (00:10–00:22)
Cut to macro floor-level close-up. Camera slowly orbits around the flattened crimson liquid pool. Surface tension creates organic rounded edges and subtle thickness variation. Warm key light reflects softly like satin lacquer. Tiny ripples propagate outward and gradually settle. Floating dust visible in the beam of light. The liquid slowly begins thickening microscopically as if memory is forming beneath the surface. Edges transition from glossy wetness toward velvety softness. Sound: soft viscous liquid movement, faint atmospheric resonance.

PANEL 3 — THE FIRST FIBERS (00:22–00:36)
Extreme macro push-in across the crimson surface. Thousands of microscopic suede nap fibers begin extruding upward organically in rhythmic waves. Individual fibers catch warm highlights differently depending on density and angle. The transformation moves naturally across the surface like wind through grass. Matte suede texture gradually replaces liquid gloss entirely. Camera glides slowly across the newly forming velvet landscape. Sound: microscopic fiber rustling, delicate textile friction.
PANEL 4 — MATERIAL MEMORY (00:36–00:50)
Macro tracking shot across fully formed crimson suede terrain. Every velvet strand visible in extreme detail. Invisible pressure waves beneath the suede subtly shift the nap direction, creating tonal changes across the material surface. Warm light rolls gently over the velvet texture. The material gradually lifts upward from the floor, beginning to imply the sculptural shape of a pointed shoe toe. Sound: soft velvet brushing, low warm resonance.

PANEL 5 — THE THREAD ARRIVES (00:50–01:06)
Extreme-extreme macro couture construction sequence. One single crimson thread enters frame illuminated by warm directional light. FPV-style camera flies beside the advancing thread as it stitches into the suede surface. Thread fibers visibly twist under tension. The thread enters the suede, disappears beneath the surface, emerges again at the next stitch peak, pulls taut, and repeats rhythmically. Camera passes over every stitch mountain in sequence. Each stitch slightly reshapes surrounding suede. Sound: couture stitching ticks, thread tension tightening, soft textile compression.
PANEL 6 — CONSTRUCTION OF FORM (01:06–01:20)
Transition from macro to medium scale. Behind the advancing stitch line, the shoe body begins solidifying into recognizable structure. Pointed toe box forms first, then elegant sidewalls rise upward with sculptural precision. The slingback silhouette slowly emerges from previously flat suede terrain. Camera performs a slow floating cinematic arc around the forming structure. Matte crimson suede texture remains perfectly consistent. Sound: restrained structural textile movement, distant stitching continuation.

PANEL 7 — THE INTERIOR (01:20–01:34)
Macro cutaway revealing the inside of the forming shoe. Cream-colored lambskin lining flows organically into place beneath the crimson suede shell. The lining smooths itself naturally against elegant internal curves. Strong visual contrast between warm cream lambskin and deep crimson suede under soft editorial lighting. Materials appear tactile and luxurious. Sound: soft leather settling, delicate tactile friction.
PANEL 8 — ENGINEERED COMFORT (01:34–01:48)
Macro cross-sectional engineering sequence. Internal comfort layers assemble one by one with realistic material physics. Dense foam base layer forms first with subtle porous texture. Softer memory foam settles gently above and compresses naturally under its own weight. Cream lambskin velvet seals the upper layer. The completed cushion compresses once slowly and rebounds naturally, demonstrating softness and resilience. Camera glides across microscopic velvet interior texture. Sound: soft pneumatic settling, muted resonance, cushion compression.

PANEL 9 — THE HEEL SCULPTURE (01:48–02:02)
Macro cinematic focus on the kitten heel gradually forming from the same crimson suede structure beneath the shoe body. Elegant curvature emerges slowly and becomes refined and balanced. Camera tracks upward along the heel contour toward the slingback strap. Warm highlights skim softly across suede edges. Sound: low structural resonance, faint textile shaping.
PANEL 10 — FINAL REFINEMENT (02:02–02:18)
Medium macro editorial beauty detailing. Camera slowly explores completed craftsmanship: stitch consistency, velvet nap direction, edge finishing, cream lambskin softness, seamless slingback geometry. Tiny dust particles drift through warm studio light. The shoe settles microscopically as if materials are naturally relaxing into final form. Sound: quiet room tone, soft textile creaks, near silence.

PANEL 11 — HERO EMERGENCE (02:18–02:32)
Slow cinematic pullback from macro detail into full product reveal. The fully completed deep crimson suede slingback heel stands alone centered on the infinity cyclorama floor. Same warm-neutral key light from above camera-left and same single clean shadow falling back-right for continuity with Panel 1. Camera movement extremely slow and controlled. Every material reads clearly: deep crimson suede upper, cream lambskin interior, sculpted kitten heel, elegant slingback strap. Sound: deep low resonant tone gradually fading into room tone.
PANEL 12 — THE FINAL HOLD (02:32–02:35)
Locked-off front three-quarter hero composition. The single crimson suede slingback heel remains perfectly still at center frame
```

---

## 7. Wolf Saves Child in Stop-Motion Cliff Disaster

- **id:** `SD2_10168`
- **slug:** `wolf-saves-child-cliff`
- **source URL:** https://x.com/ai_animer/status/2078023536992735573
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=7739; quality_score=23 (HF jsonl has no like/view fields)
- **tags:** stop-motion, hand-painted animation, dramatic rescue
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 2206, "height": 946, "ratio": 2.33, "duration": 15.08, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
Style: STOP-MOTION ANIMATION — stepped, frame-by-frame motion brought to a HAND-PAINTED 2D look, a moving oil painting, NOT clay, NOT puppets, NOT 3D. True 12 frames per second, ANIMATED ON TWOS: 12 distinct hand-painted drawings per second, each pose held two frames then snapping to the next, never gliding. Constant painterly BOIL — brushstrokes and outlines subtly alive frame to frame. NO smooth interpolation, NO motion blur, NO morphing, real frame-by-frame animation not AI slop. Style from @[Image 1](image_1), ANA from @[Image 2](image_2), UMAI from @[Image 3](image_3), THE WOLVES from @[Image 4](image_4) — lean steppe wolves, coal-black with cold sheen, pale eyes, the snowy cliff from @[Image 5](image_5). THE INFANT is not a separate reference — render from description: a tightly swaddled baby wrapped in a thick DARK BLUE wool blanket, PRESSED AGAINST ANA'S CHEST in one arm as she clings to the cliff, only a small dark-blue bundle, face barely visible, stirring faintly; NOT a second active child. Heavy weather: drifting FOG, falling and blowing SNOW, gusting WIND. Atmospheric motion (fog, falling and blowing snow, wind-haze, breath-vapor) moves SMOOTHLY; figures, falling rock, wolves and drawn snow-spray step on twos. DIRECTOR'S NOTES: 1. THE SCENE — the catastrophe, the heart of the whole story, and it MUST READ through a precise CHAIN OF CAUSE AND EFFECT, with composition and camera telling the cruel story. As ANA climbs one-armed with her infant, her foot dislodges a rock slab; the slab falls toward little UMAI below; and a WOLF leaps and SHOVES UMAI clear WITH ITS BODY an instant before the slab hits — the wolf SAVES her. Then the pack streams in and carries UMAI away. The wolves do not attack — the first saves her, the pack takes her. This reversal is everything. 2. THE CAUSAL CHAIN — stage each link on screen, cause before effect, on twos: (a) ANA's foot comes down on a ledge high on the cliff, the ledge CRACKS and BREAKS under her weight; (b) a heavy SLAB breaks loose and FALLS straight down toward UMAI — the falling rock the through-line; (c) UMAI stands directly below, looking up; (d) from the side a WOLF LAUNCHES and SLAMS its shoulder and body into UMAI — NOT its jaws, NOT a bite — knocking her sideways clear; (e) the slab CRASHES into the snow exactly where she stood, a burst of powder snow on twos; (f) UMAI tumbles unhurt among the wolves. Every cause visible. 3. THE WOLF SAVES WITH ITS BODY — CRITICAL: the first wolf strikes UMAI with its shoulder/flank, a SHOVE, mouth NOT on her, no bite, no seize — a rescue read as a body-slam. For one instant it LOOKS like an attack — then the rock smashes the empty snow and we understand. Play the shock-reversal. 4. THE PACK TAKES HER — the pack pours in as a fast dark stream from @[Image 4](image_4), varied coats, and SWEEPS UMAI up among them, NOT tearing her, carrying her in the current as they stream away into fog and blizzard. She is small in the dark flowing mass, swept away into the white. The beginning of her life among them. 5. ANA ABOVE SEES AND SCREAMS — high on the cliff, helpless, clinging one-armed with her baby, she SEES and reaches out and SCREAMS her daughter's name. FACIAL ACTING: her held composure SHATTERS — her face breaks open, eyes blown wide in horror, mouth tearing open, all the controlled tenderness from before exploding into raw terror, on twos as snapping held poses of a face coming apart. 6. CAMERA LAW (angle and height tell the cruelty) — SHOT 1 high WITH ANA then a hard VERTIGO TILT DOWN following the falling rock — the height is the cruel mechanism, she is the unwitting cause from above. SHOT 2 LOW at UMAI's level or below — we share the child's helplessness, the rock and the wolf bearing down on us. SHOT 4 the BIG-VERSUS-SMALL angle — ANA tiny and powerless high on the vast cliff, the storm dwarfing her, never powerful, only helpless. Aggressive dynamic handheld throughout, the horizon reeling on the scream, never gimbal-smooth, never tripod-locked. 7. COMPOSITION LAW (the frame tells the story — RUPTURE, the opposite of the vow's affinity) — LINE: the cruel CROSS of forces in the save — the VERTICAL line of doom (the falling rock from above) intersected by the HORIZONTAL line of salvation (the wolf from the side); their crossing on the tiny child IS the story. The pack's flow a DIAGONAL line of dynamics sweeping her off. The vertical gap between mother above and child below now PERMANENT and vast. SHAPE: the angular rock and angular lunging wolf (both read as threat) converging on the small rounded child. TONE: dark masses (rock, wolf, pack) on pale snow and fog, the child the focal point. MOVEMENT: contrast and high intensity — fast violent vertical fall, horizontal slam, diagonal sweep, against the slow helpless reach. CONTRAST & AFFINITY: maximum CONTRAST and PEAK visual intensity — the rupture the vow's affinity has been saving for. SPACE: deep vertical, the cruel distance. 8. FRAMED INK STAGING (read as masses) — FRAME-TRAP the small child between the falling rock above and the lunging wolf from the side, two dark angular masses closing on her. CONCEAL: fog half-swallows the catastrophe, and swallows UMAI as the pack carries her into the white. CAMERA HEIGHT: low and helpless at the child; tiny and powerless at the mother. LARGE VS SMALL: the small child and small distant mother against the vast cliff, the storm, the dark flowing pack. 9. WEATHER — FOG, SNOW, WIND, all smooth: low drifting fog across ground and cliff base, thick snow blown sideways in gusts, gusting wind dragging fog and snow and tearing breath-vapor, the catastrophe half-veiled and swallowed by the storm. 10. SECONDARY ACTION on twos — ANA's and UMAI's clothes hair and breath-vapor whipping, the wolves' fur rippling, the dark-blue swaddled bundle shifting, snow bursting from the rock's impact and the wolves' running as drawn powder on twos; fog and blowing snow smooth. 11. LIGHT — cold grey stormlight in fog and snow, flat soft directionless, no sun, no rays, no beams, no god rays, faces readable. Correct neutral white balance, NOT a blue filter, muted desaturated, snow soft storm-grey white, fog pale grey; nearly BLOODLESS — a rescue not a mauling, any blood dark muted and minimal. SHOT 1 — ON THE CLIFF, ~50mm, aggressive handheld, high on the rock face in fog and blowing snow. COMPOSITION: ANA climbing one-armed in the UPPER frame, the dark-blue swaddled infant pressed to her chest, her boot reaching for a ledge — framed HIGH WITH HER so we feel the drop below. Her foot comes down — the ledge CRACKS and BREAKS away on twos, a SLAB breaking loose. Hard VERTIGO TILT DOWN following the slab as it FALLS down the cliff through the fog toward the tiny figure far below — the vertical line of doom, the height the cruel mechanism. Cut on the falling rock. HARD CUT to SHOT 2 — BELOW THE CLIFF, ~35mm, aggressive handheld, framed LOW at UMAI's level. COMPOSITION (the cross of forces): little UMAI small in frame looking up, fog and snow blowing past — the SLAB falling INTO frame from the TOP straight down at her (vertical line of doom) — and from the SIDE a WOLF LAUNCHES and SLAMS its shoulder and body into her (horizontal line of salvation), the two lines crossing on the tiny child, knocking her sideways clear (jaws NOT on her, a shove not a bite) — and the slab CRASHES into the snow exactly where she stood, a burst of powder on twos. For one beat the two dark angular masses closing on her read as ATTACK — then the empty crater shows the wolf saved her. UMAI tumbles unhurt among arriving wolves. Real weight and impact, all on twos. HARD CUT to SHOT 3 — BELOW, WIDE, ~35mm, aggressive handheld. COMPOSITION (the diagonal sweep): the pack pours
```

---

## 8. Neon Cyberpunk Embrace

- **id:** `SD2_05245`
- **slug:** `neon-cyberpunk-embrace`
- **source URL:** https://higgsfield.ai/community/13efe85e-0712-4e70-ab17-51c50902d41d
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=5364; quality_score=23 (HF jsonl has no like/view fields)
- **tags:** cyberpunk, sci-fi romance, mecha flight
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 3840, "height": 2160, "ratio": 1.78, "duration": 10.04, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
Style: 8K photorealistic, anamorphic widescreen, neon cyberpunk cinematic grade, fine grain.
Lighting: mixed neon key — green and magenta storefront glow from camera-left, cool hazy daylight down the street axis, hot rim from a pink neon strip at frame-right, armor catching colored reflections.
Color: teal-and-magenta neon street as the dominant, the white-and-red armor and the red armor as the saturated subjects, green shop signs and amber banners as secondary accents.
Camera: anamorphic cine optics, horizontal neon flares, real motion blur, weighty operator inertia that turns soaring on the lift.
Skin: armor at material-level realism — brushed metal, scuffed paint, neon reflections sliding across the plates, fine catch-lights on the visors.
Acting: a charged beat before contact — the offered hand held still, her hesitation, then the snap of the grab and the surge upward, bodies reacting to acceleration.
Physics: real mass and inertia — the grab yanks her weight, the lift accelerates against gravity, capes and loose straps trail in the wind, the city falls away below with parallax.
Composition: two-shot profile on the street, then vertical thrust into the cityscape, depth from foreground neon to mid figures to deep hazed skyline.
Continuity: same white-and-red armored figure, same red armored figure, same neon cyberpunk city across all cuts.
Technical: 24fps, ultra high detail, smooth motion accelerating into the flight.
Audio: diegetic only — neon hum and distant city noise, a soft servo whir, the snap of the grab, a building thruster roar, wind rushing on the ascent.

SCENE CONTEXT
On a neon cyberpunk street, a white-and-red armored figure offers his hand to a red-armored figure; the instant she touches it he grips her, pulls her in, and thrusts upward — they fly through the city skyline locked in an embrace.

ACTIVE REFERENCES
<<<image_1>>>: the two figures and the location — left, a slender figure in glossy red armor with a red visored helmet; right, a taller figure in white-and-red armor with a red-striped visored helmet, hand extended; a neon cyberpunk street with green and amber Chinese-character signs, magenta neon, an elevated rail structure and hazed skyline behind. 100% matches the reference.

LOCATION MAP
Foreground: a dark neon-lit doorway edge framing frame-right, magenta strip-light. Midground: the two figures facing each other on the street. Background: the neon storefronts, elevated rail bridge, and hazed city skyline. Camera starts low on the street, then rises with the figures into open sky. Movement runs from a still face-off into a vertical climb.

FIRST FRAME / BLOCKING
<<<image_1>>> exactly — red-armored figure at left in profile, white-and-red figure at right with hand extended toward her, neon street behind, both standing still on the wet pavement.

FORMAT MODE
Sequence of 6 cuts, no timecodes. Cuts only at the specified points, the camera does not cut on its own.

OPTICS
CUT 1 — MS 47° two-shot. CUT 2 — ECU 18° on the hands. CUT 3 — MCU 29° on the grab. CUT 4 — WS 63° low-angle lift. CUT 5 — EWS 84° city flight. CUT 6 — MS 47° embrace in air. No drift mid-segment.

CAMERA
Locked-off street-level two-shot for the offer, a tight insert on the touching hands, a snap-in as he grabs, then a low-angle craning up that releases into a soaring rise tracking them into the skyline, settling close on the embrace mid-air.

ACTION
CUT 1 — the white-and-red figure holds his open hand out, still; the red figure hesitates, then lifts her hand toward his, neon glinting off both plates.
CUT 2 — extreme close on the hands as her fingers touch his palm — the instant of contact, neon reflections catching the metal.
CUT 3 — his hand clamps shut on hers and yanks her in, pulling her against his chest, both helmets close, a soft servo whir.
CUT 4 — a building thruster roar — they launch straight up off the street at 60 km/h, the camera craning to follow, neon signs streaking downward past them.
CUT 5 — wide above the city, the two soaring through the hazed neon skyline, rail bridges and towers sliding below, wind tearing past, locked together.
CUT 6 — close in the air, he holds her wrapped in both arms, both helmets turned toward each other, the city lights rushing soft behind them.

PHYSICS
The grab transfers real weight — her body pulls in with inertia. The lift accelerates against gravity, straps and loose fabric trailing downward in the rush. The city falls away with true parallax. Both armored bodies stay rigid with weight, joints articulating as they move.

LIGHTING
Green and magenta neon key on the street beat, hot pink rim at frame-right; on the ascent cool hazy daylight takes over with neon glow falling away below; WB shifts from 4000K neon street to 6500K open sky, held within each cut.

AUDIO
Neon hum and distant city noise on the street, a soft servo whir on the grab, a building thruster roar on launch, wind rushing through the flight, settling to a low hum on the embrace.

POSITIVE LOCKS
White-and-red armored figure with red-striped visor and red-armored figure with red visor stay identical in every cut. Neon cyberpunk street and hazed skyline consistent throughout. He offers the hand, she touches, he grabs and lifts — the beat reads as protective and close. Neon stays the dominant saturated color. Both stay locked in the embrace through the flight.
```

---

## 9. Seokchon Lake Night Walk Vlog

- **id:** `SD2_10939`
- **slug:** `seokchon-lake-night-walk`
- **source URL:** https://x.com/Shorelyn_/status/2081932710764032063
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=5091; quality_score=23 (HF jsonl has no like/view fields)
- **tags:** nightwalk, cinematic, vlog
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 1080, "height": 1920, "ratio": 0.56, "duration": 15.1, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
Character consistency: The subject is the young female influencer from Reference Image 1. At all times and from all angles, the face shape, facial features, and skin tone must completely match Image 1, and facial deformation is prohibited. Outfit: In all scenes, wear sophisticated and glamorous black dresses, crop tops, jackets, and streetwear. Do not wear the outfits from the character design sheet. Completely replace the styling and hairstyle with entirely different styles for each section. Format: 9:16 vertical screen. Camera and style: Fast editing rhythm with intervals of 0.5 to 1 second. iPhone handheld vertical shooting texture. Mixed digital zoom in, zoom out, and tilt up with natural handheld shake. Autofocus hunting, indoor and outdoor lighting exposure fluctuations, and image quality degradation during zoom adjustment. Maintain real skin texture including pores, baby hairs, and natural skin oil. Beauty filters, excessive skin retouching, CG texture, and cinematic color grading are prohibited. Do not arbitrarily merge cuts or omit scenes. Do not insert subtitles on the screen. Sound: Trendy and sophisticated pop and lo fi background music. Mix ambient sounds of ice glasses clinking, lake water ripples, and footsteps blended with the night breeze. The character does not speak. Jamsil Seokchon Lake night terrace cafe and waterfront night walk. 0 to 2 seconds: At 11 PM, the entrance of a second floor terrace cafe beside Jamsil Seokchon Lake. Low angle wide shot under cold white LED pendant lighting. The character pushes open the glass door with her shoulder, stops after two steps, then rolls up her jacket sleeves to her elbows while adjusting her bag strap with one hand. Autofocus briefly hunts between the door handle and her face before locking onto her face. She makes eye contact with the camera for 0.5 seconds, smiles, then immediately turns her gaze inside. 2 to 4 seconds: At the same terrace table, a macro tight shot of a glass full of ice on a stainless steel tray with water droplets running down the glass. The table spotlight reflects as sharp white highlights on the wet metal and glass. Hard cut to her facial reaction as she lifts the glass with one hand, her fingertips slip, the glass tilts, her eyes widen, her shoulders tense, and she inhales sharply. She reacts only to the cold and slippery sensation. 4 to 6 seconds: In front of the terrace floor to ceiling glass, a tight shot showing the character's upper body reflected in the glass with the nighttime facade lights of Lotte World Tower overlapping behind it, creating a double layered reflection. Hard cut to a direct front facing close up of her face captured by the camera. As the camera pans from the indoor white lighting toward the blue night view outside, the exposure lags for a beat, causing the frame to briefly wash out white before settling. The character looks only at the top of the tower beyond the glass as if she does not know the camera is there. Her face is always captured directly by the camera, never as a reflection. 6 to 8 seconds: In front of an unmanned beverage vending machine on the lakeside walkway, a macro tight shot captures frost patterns on the refrigerated display glass and the moment a can drops into the dispenser. Hard cut to her facial reaction as she suddenly turns from the shoulders toward the sound. The blue white fluorescent light from the refrigerated display shines directly onto her face. She presses an unlabeled silver can against her cheek and tightly closes then opens her eyes from the cold. 8 to 10 seconds: At the west side railing of Seokchon Lake, the purple and turquoise LED lights of Magic Island Castle spread across the dark water, casting rippling light patterns over her face. One second macro close up of water droplets lined along the metal railing, each reflecting an upside down tower light. Then focus shifts from the droplets to her face as she squints one eye against the dazzling lights and holds the expression. During digital zoom in, the image quality briefly becomes blurry. 10 to 12 seconds: On the lakeside night walkway, a low angle detail shot of white streetlights sweeping across the wet deck floor and railing at regular intervals. The character strides down the deck stairs and begins walking while the camera follows behind handheld, with the frame bouncing up and down in sync with her footsteps. One or two people walking at night pass by as blurred silhouettes. As the night breeze blows her hair over her face, the camera moves beside her and captures her shaking her head strongly to brush it away. 12 to 15 seconds: On the wet paving block plaza illuminated from the front by the facade lights of Lotte World Tower, one second macro detail of a puddle reflecting both the tower lights and the character upside down. Then the camera slowly rises as the character stands facing forward in a full body shot with one hand in her jacket pocket. Only during the final 0.5 seconds does she make eye contact with the camera before turning her gaze to the side while holding the full body pose.
```

---

## 10. Caffeine Chaos Machine

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

## 11. Magical Candy Workshop Adventure

- **id:** `SD2_10919`
- **slug:** `magical-candy-workshop`
- **source URL:** https://x.com/Caden_Flux/status/2082060465077981481
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=4639; quality_score=23 (HF jsonl has no like/view fields)
- **tags:** fantasy animation, magical workshop, pixar style
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 1280, "height": 720, "ratio": 1.78, "duration": 15.08, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
Duration: 15 Seconds Aspect Ratio: 16:9 Genre: Whimsical Fantasy Animation Style: Premium animated feature film, ultra-detailed stylized 3D, cinematic lighting, warm golden sunlight streaming through giant candy-glass windows, magical volumetric dust, soft bloom, rich pastel color palette, handcrafted fantasy architecture, highly expressive animation, Pixar-inspired quality (original world and characters), playful orchestral energy, buttery-smooth camera movement, shallow depth of field, subtle magical particles, cozy fantasy atmosphere. Character Reference Use the exact approved character sheets for: Professor Crumble Mochi Whisk Jello Sprinkle STRICT CHARACTER & IDENTITY LOCK Maintain identical facial features, body proportions, hairstyles, clothing, accessories, colors, materials, and personalities exactly as shown in their character sheets throughout every shot. No redesigns or inconsistencies. 0–3 Seconds Camera A sweeping FPV cinematic drone shot glides through enormous candy-colored stained-glass windows before gently diving into the magical workshop. The camera flies between floating cupcake chandeliers, spinning sugar gears, glass tubes carrying glowing syrup, and tiny pastry robots crossing wooden bridges. The workshop feels impossibly huge, alive, and full of wonder. As the camera slows, Professor Crumble comes into view at the center of the room. Characters Professor Crumble is happily humming while carefully sketching a recipe upside down. Whisk quietly polishes copper mixing machines. Mochi floats overhead carrying an enormous bag of sparkling Cloud Flour that's clearly too heavy. Jello secretly peeks from behind a cookie jar with a mischievous grin. Sprinkle flutters through flowering vines, gently waking magical strawberries with glowing fairy dust. 3–6 Seconds Camera A smooth dolly move circles Professor Crumble as he suddenly gasps with excitement. The camera pushes in dramatically as his amber eyes sparkle. His Spectra Goggles rotate automatically. Tiny magical sugar particles begin swirling around him. Action Professor Crumble raises his glowing Wonder Spoon. He smiles warmly. "Now then... let's discover something impossible." Every machine in the workshop softly comes alive. Copper pipes glow. Glass bottles gently vibrate. Tiny lights flicker across the ceiling. 6–9 Seconds Camera Fast overhead crane shot transitions into a rotating close-up around the giant enchanted mixing bowl. Action Mochi excitedly tosses Cloud Flour into the bowl. Sprinkle adds glowing Crystal Berries. Whisk precisely pours shimmering Moon Vanilla. Everything is going perfectly... Until... Jello quietly stretches into a long jelly arm... ...and drops one mysterious sparkling ingredient into the mixture. Nobody notices. The bowl instantly flashes with rainbow light. 9–12 Seconds Camera The camera rapidly orbits the mixing bowl before switching to an extreme slow-motion close-up. Action Rainbow batter floats into the air. Sugar butterflies appear. Miniature constellations swirl inside the mixture. Chocolate ribbons spiral around glowing fruit. Professor Crumble laughs with childlike joy instead of panic. Mochi spins happily in midair. Whisk's eyes widen in astonishment. Jello tries to look innocent. 12–15 Seconds Camera A slow cinematic push-in reveals the finished dessert floating above the workshop. Everyone gathers beneath it. The dessert slowly blossoms like a magical flower. Golden sparkles drift through the room. Professor Crumble takes one tiny bite. His eyes light up. He laughs warmly. "Perfection is delicious... but surprises are unforgettable." The camera gently pulls back through the workshop as all five characters admire the glowing dessert together. The final frame freezes into a beautiful storybook illustration while shimmering golden text appears: "Professor Crumble's Wonder Workshop" Tiny sugar sparkles continue drifting across the screen as the music ends on a magical, uplifting note. 🎥 Cinematic Notes Smooth FPV fly-throughs with graceful, weightless movement. Gentle dolly and crane shots to emphasize scale and wonder. Macro close-ups for magical ingredients and expressive character moments. Warm golden lighting with soft bloom and volumetric sun rays. Rich environmental animation: bubbling syrup, rotating gears, floating flour dust, drifting sparkles, gently swaying vines, and glowing glass tubes. Every character should remain active in the background, making the workshop feel like a living, breathing place where magic is always happening. This makes the world feel endlessly alive and invites viewers to rewatch to catch all the little details.
```

---

## 12. Alien Fly Attack: POV Speed Ramp

- **id:** `SD2_05210`
- **slug:** `alien-fly-pov-speed-ramp`
- **source URL:** https://higgsfield.ai/community/525d7c25-8c53-4fa7-8489-e3478dd2e5cb
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=4461; quality_score=23 (HF jsonl has no like/view fields)
- **tags:** first-person POV, macro cinematography, sci-fi forest
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 4398, "height": 1886, "ratio": 2.33, "duration": 15.04, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
Cinematography: First-person POV (Point-of-View), naturalistic unconstrained human vision. Authentic head movement with organic micro-tremor, subtle wind-shake, and reactive eye-line tracking.

Lighting: Surrealistic alien twilight. High-contrast natural light filtering through a dense canopy. The scene is underlit by vibrant, colorful bioluminescent glow from the fungal forest, casting shifting reflections onto the rider's hands and the vehicle's controls.

Color: 60:30:10 — dominant deep indigo and violet (ambient environment) 60% / secondary neon magenta, cyan, and toxic green (glowing mushrooms & alien insect) 30% / accent warm amber-gold (hoverbike dashboard instruments) 10%.

Camera: Physical wide-angle cine lens (24mm). 180° shutter motion blur. Masterfully executed speed-ramping effect (24fps to 240fps and back). Extreme macro depth-of-field transition.

Physics: Inertia and intense wind resistance felt through the camera movement. Correct depth of field (shallow DOF during the close-up). Particles and spores obey fluid aerodynamic drag.

SUBJECTS:

@rider_pov: Pure, unobstructed first-person vision. No helmet, no visor edges, no HUD. The view is completely clean. At the bottom of the frame, the rider's bare or thin-gloved hands are visible gripping the weathered handlebars of a heavy hoverbike, fingers subtly twitching and adjusting the mechanical throttle.

@alien_fly: A surreal, iridescent macro-insect. It features double-layered translucent wings that shimmer like oil slicks, a neon-cyan segmented body pulsing with internal bioluminescence, and large, multi-faceted magenta eyes.

LOCATION: A bizarre fantasy jungle at twilight. The winding trail is lined with towering, twisted mega-mushrooms pulsing with toxic green and magenta light. Spores drift through the air like glowing ash.

ACTION — ONE CONTINUOUS TAKE, single unbroken POV shot, NO cuts. 15 seconds.

0:00–0:04 — High-Velocity Real-Time POV (24fps): The hoverbike flies low and fast, weaving aggressively through a narrow opening in the giant mushroom forest. The camera tilts and leans realistically as the rider banks into turns. Wind-driven spores streak straight past the screen, emphasizing the extreme speed.

0:04–0:05 — The Jolt / Sudden Speed-Ramp: Without warning, right as the bike clips past a massive glowing stalk, the @alien_fly flashes into the frame from camera-left. It is a sudden, jarring jump-scare moment. The camera performs a sharp, subconscious human flinch (a micro-jerk backward and right). In that exact millisecond of panic, time violently freezes, ramping down into extreme slow-motion.

0:05–0:11 — Ultra Slow-Motion Macro Close-Up (240fps): Motion drops to a near-absolute standstill. The background and the rider's hands blur into a soft, dreamy bokeh. The @alien_fly drifts directly past the camera lens at macro distance, mere centimeters from the eye. Every microscopic detail is hyper-visible: the complex, rapid-yet-frozen vibration of its oil-slick wings scattering the neon forest light, the texture of its glowing body, and drifting spores parting around its frame. Beautiful horizontal anamorphic magenta flares streak across the lens element. Focus pulls razor-sharp onto the insect, then expands.

0:11–0:15 — Instant Speed-Ramp Back to Real-Time (24fps): The fly snaps past camera-right and vanishes into the canopy. Time instantly cracks back to normal speed with a sudden, violent rush of wind. The environment sharpens, the heavy repulsor engine roars back to maximum volume, and the rider aggressively corrects the steering wheel, accelerating deeper into the dark indigo alien forest.

CONSTRAINTS: 16:9 anamorphic widescreen scale. ONE CONTINUOUS POV SHOT — absolutely NO cuts or edits. Real-time motion violently ramping into 240fps slow-mo, then snapping back. Complete absence of any screen borders or helmet graphics. Photoreal throughout.

AUDIO (NO MUSIC): The heavy, resonant mechanical hum and high-RPM whine of the hoverbike's engine. High-speed wind rushing and tearing past the ears. At 0:04, a sharp, caught breath from the rider as the insect appears. During the slow-mo (0:05–0:11), all wind drops into an absolute, muffled vacuum, replaced by the deep, amplified, rhythmic thump-thump-thump of the alien fly’s massive wings and the sound of the rider's rapid, magnified heartbeat. At 0:11, a sharp sonic whoosh as reality snaps back, instantly overtaken by the roaring engine and crashing wind.
```

---

## 13. Nike Emerald Aurora Campaign Film

- **id:** `SD2_05292`
- **slug:** `nike-emerald-aurora-campaign`
- **source URL:** https://x.com/ShamiWeb3/status/2074302311275663589
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=4246; quality_score=23 (HF jsonl has no like/view fields)
- **tags:** Nike, Sneaker, Commercial
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 1920, "height": 1080, "ratio": 1.78, "duration": 15.07, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
VIDEO PROMPT — "EMERALD AURORA" Nike Air Max 95 Big Bubble Campaign Film (15s) Style & Mood Premium athletic fashion campaign film. Monochromatic emerald palette — deep emerald green, jade, mint green, pale sage, warm cream — across every surface, garment, background, and product. Soft diffused studio light with warm emerald ambient fill and dramatic single spotlight for silhouette shots. Fluid emerald liquid-glass splashes, motion blur streaks, and champagne-gloss reflections as recurring visual elements. Confident feminine energy. Every frame is editorial-poster quality. Model: Mid-20s Western female, fair sun-kissed skin, striking emerald-green eyes, long tousled honey-blonde hair in loose waves, toned athletic build. Same face, hair, and styling consistent across every shot — no drift. Dynamic Description Shot 01 — Aurora Bloom (0–2.5s): Wide macro product hero — the Nike Air Max 95 Big Bubble in Emerald Aurora floats at a dynamic diagonal angle above a swirling jade-green liquid surface, the liquid curling upward in slow-motion silk waves on both sides of the shoe, translucent emerald spherical droplets suspended in the air around the sole, the champagne-tinted Air bubble unit sharp at frame bottom. Camera pushes slowly toward the sneaker from a low front angle. Text "AURORA BLOOM" fades in lower left in thin white sans-serif. Hard cut. Shot 02 — Air Max 95 Macro Reveal (2.5–5s): 100mm macro slow right-to-left slide — the heel section fills the frame, the large champagne-tinted Air bubble unit glowing warmly under diffused studio light, the quilted sage-green suede panels with stitching lines sharp in the foreground, the deep emerald leather overlay curving across the upper third. Camera slides slowly revealing the Air bubble left to right, light raking across the suede grain and gradient color transitions. Text "AIR MAX 95" fades in upper left. Hard cut. Shot 03 — In Motion Walk (5–7.5s): Wide stabilized shot — the model in a cream crop top and loose sage-green cargo trousers walks directly toward camera in slow motion, honey-blonde hair flowing behind her as she strides forward, wearing the Emerald Aurora sneakers, a single warm spotlight from above casting a soft shadow ahead of her, background a warm emerald-toned empty studio, soft jade light wrapping her left side. Camera holds at chest height, very slow forward drift. Text "IN MOTION" fades in lower right. Hard cut. Shot 04 — Built to Move (7.5–10s): 35mm dynamic handheld — the model leaps mid-air from left to right in a presidential jump, both feet off the ground, right knee raised, arms swinging, the Emerald Aurora sneakers sharp at the bottom of the frame, motion blur streaks of deep emerald trailing behind her across the frame, hair horizontal in motion, background a gradient of warm cream to deep jade. Camera at mid-body height, slightly handheld, following the arc of the leap. Text "BUILT TO MOVE. / MADE TO STAND OUT." fades in lower left in spaced white caps. Hard cut. Shot 05 — Big Bubble Product Packshot (10–12.5s): Static locked-off center composition — the Nike Air Max 95 Big Bubble sits alone on a minimal pale-sage surface at a clean three-quarter angle, full shoe visible, the oversized champagne-tinted Air bubble unit prominent at the heel, deep emerald lace cage and swoosh logo sharp, small leaf-shaped charm on the lace eyelet catching the light. Soft overhead studio light, no distractions. Camera holds completely still. Text "AIR MAX 95 / BIG BUBBLE" fades in upper center in thin white type. Hard cut. Shot 06 — Just Do It Silhouette End Frame (12.5–15s): 85mm static locked-off — background transitions to a deep rich forest-emerald with a single warm spotlight circle on the wall behind. The model stands in confident pose slightly right of center, one hand on hip, head turned in profile, ponytail falling over one shoulder, the Emerald Aurora sneakers visible on her feet, her silhouette almost entirely in dark shadow against the glowing emerald backdrop with only the edge of the spotlight defining her outline and catching the cream sole of the shoe. The Nike Swoosh logo in solid white appears upper right, beneath it "JUST DO IT." in white spaced tracking. Frame holds locked. Slow fade to black.
```

---

## 14. Cool Girl's Fire-Breathing Birthday Surprise

- **id:** `SD2_10613`
- **slug:** `cool-girl-fire-birthday`
- **source URL:** https://x.com/Chengzilhy/status/2080140918704029967
- **model:** Seedance 2.0
- **featured:** False
- **engagement proxy:** dataset featured=False; prompt_len=2932; quality_score=23 (HF jsonl has no like/view fields)
- **tags:** cinematic, birthday, surprise
- **license:** `CC-BY-4.0 via GokuScraper/seedance-2-prompts-datasets (attribute dataset + original author). Original X author copyright retained unless stated.`
- **spec:** {"width": 2160, "height": 3840, "ratio": 0.56, "duration": 16.03, "safety_rating": "Safe for Work"}

### Prompt (verbatim)

```text
【人物与服装参考】

以当前上传的人物定妆图作为唯一人物身份与服装参考。
上传图片左侧近景用于锁定人物脸型、五官、妆容、发型和神态；中间正面全身与右侧背面用于锁定服装结构、首饰、身体比例和背面造型。

全片必须保持人物身份、发型、服装、首饰 and 身体比例一致，禁止换脸、换装、改变发色或改变服装结构。

【风格】

真实电影感生日派对短视频。前半段是自然、克制、略带反差幽默的生活记录感；后半段在“吹蜡烛”这个正常生日动作中突然升级为喷火反差效果；最后直接收束为高反差黑白生日海报。

人物表情整体延续参考图中的安静、清冷、克制气质，不使用夸张卡通表情。

【时长／画幅】

15秒，9:16竖屏。

【场景】

室内餐厅或酒吧的生日聚会场景。

女主坐在桌后，桌面中央放置一个精致圆形生日蛋糕。背景为深色酒柜、酒瓶陈列与暖黄色圆形灯光，环境偏暗，人物与蛋糕受到柔和暖色光照。

桌面、蛋糕、座椅、背景灯具和酒柜位置全程保持稳定，不改变场景结构。

【核心道具】

银色生日皇冠、圆形生日蛋糕、细长白色弯曲生日蜡烛、打火机。

从递入、嘴边点燃、取下到插入蛋糕，必须始终使用同一根蜡烛，其长度、颜色、弯曲形态和外观不能中途改变。

【摄影机与构图】

摄影机固定在女主正前方，镜头距离女主面部约1.4米，保持稳定正面中景。

画面完整拍到女主头顶、脸部、肩部、上半身、双手活动区域、桌面和完整生日蛋糕，同时保留部分背景酒柜与暖色灯光。

全程不摇镜、不俯仰、不横移、不推拉、不后退、不变焦。人物远近变化只能来自女主自身自然前倾或回正，不能由摄影机制造景别变化。

前七个镜头在同一固定机位和构图下连续完成；镜头8直接使用喷火高潮的当前画面进行黑白定格。

【镜头1：戴上生日皇冠】

开场女主已经坐在桌后，生日蛋糕稳定放在桌面中央。

画面左上方伸入一只手，将银色生日皇冠放到女主头顶，并自然调整至稳定位置。

女主先用眼神观察正在戴皇冠的手，随后重新看向前方。她保持安静自然的表情，只有轻微眨眼和呼吸变化，不要一开始就夸张微笑。

皇冠必须由画外人物戴上，不能开场已经戴好，也不能由女主自己拿起皇冠。

【镜头2：像叼烟一样含住生日蜡烛】

画面右侧伸入一只手，拿着一根细长白色弯曲生日蜡烛，将蜡烛横向送到女主嘴边。

女主保持坐姿，头部基本正对摄影机。她自然张开嘴，将蜡烛靠近身体的一端叼在双唇之间，蜡烛另一端向外伸出。

女主同时抬起右手，用食指和中指夹住嘴边的蜡烛，手势像夹着香烟等待点火。

动作顺序必须清楚：

右侧递入蜡烛
→ 蜡烛横向靠近女主嘴边
→ 女主将蜡烛一端叼住
→ 女主用食指和中指夹稳嘴边蜡烛
→ 递蜡烛的手松开并退出画面。

蜡烛此时必须保持横向或略微倾斜，不能竖直举起，也不能提前插进蛋糕。

这是生日蜡烛，只模仿叼烟点火的动作形态，禁止生成真正的香烟、滤嘴、烟草、烟雾、吸烟或吐烟内容。

【镜头3：像点烟一样点燃嘴边蜡烛】

女主继续将细长蜡烛叼在嘴边，并用食指和中指夹住靠近嘴唇的位置，保持等待点火的姿势。

画面左侧伸入另一只手，手中拿着打火机。打火机移动到蜡烛远离女主嘴部的外露末端。

画外人物按下打火机，火苗出现，并像给人点烟一样，将火苗贴近蜡烛外露的一端，直到生日蜡烛成功点燃。

动作顺序必须清楚：
女主叼住蜡烛并用双指夹稳
→ 打火机从左侧进入
→ 打火机移动到蜡烛外露末端
→ 打火机火苗出现
→ 火苗接触蜡烛末端
→ 蜡烛成功点燃
→ 顶端形成稳定的小火苗。
点火过程中，女主保持一本正经、冷静配合的表情，眼神自然观察靠近嘴边的打火机和火苗，形成轻微反差感。
打火机只能点燃女主嘴边叼着的蜡烛，不能直接去点蛋糕上的蜡烛，也不能烧到女主嘴唇、手指、头发或脸部。
【镜头4：取下刚刚点燃的同一根蜡烛】

蜡烛成功点燃后，拿打火机的手立即退出画面。

女主仍用食指和中指夹住蜡烛，像从嘴边取下刚点燃的香烟一样，将蜡烛从双唇之间自然抽出。

动作顺序必须清楚：

蜡烛在嘴边被点燃
→ 打火机退出画面
→ 女主双唇松开
→ 手指夹着蜡烛从嘴边取下
→ 女主将点燃的蜡烛举到胸前
→ 短暂观察蜡烛顶部的小火苗
→ 视线自然移向桌面蛋糕。

必须始终是同一根细长弯曲生日蜡烛。蜡烛不能跳帧、消失、缩短、变直、折断或更换外观。

【镜头5：将蜡烛插入蛋糕】

女主右手握住已经点燃的同一根蜡烛，将其从胸前自然下降到蛋糕上方。

完整表现以下动作：

蜡烛下降
→ 蜡烛底部接触蛋糕顶部
→ 女主将蜡烛插入蛋糕
→ 指尖调整蜡烛角度
→ 确认稳定后松开右手。
蜡烛插入后仍然保持原有的细长弯曲形态，顶部火焰继续正常燃烧。
禁止蜡烛凭空出现在蛋糕中，禁止蜡烛直接穿透蛋糕，禁止蛋糕因插入动作发生塌陷、位移或变形。
【镜头6：俯身准备吹蜡烛】
女主收回右手，重新坐正，双手自然落在桌面两侧。
她先低头看向蛋糕上的蜡烛火焰，嘴角出现自然、克制的微笑。随后上半身开始朝蛋糕方向自然前倾，脸部逐渐接近蜡烛。
动作顺序必须清楚：

看向蜡烛火焰
→ 双手落在桌面两侧
→ 身体自然向前靠近蛋糕
→ 脸部逐渐接近蜡烛
→ 嘴唇收拢，进入准备吹蜡烛的状态。

女主始终面向蛋糕和摄影机，不左右转头。摄影机保持固定，人物在画面中自然变大只能来身体前倾。

蜡烛火焰继续稳定燃烧，不能提前熄灭。

【镜头7：吹蜡烛时突然喷出火焰】

严格承接上一镜头的俯身吹蜡烛姿势。

女主面向蛋糕，嘴唇收拢，开始像正常吹生日蜡烛一样向前吹气。就在她正式吹气的瞬间，嘴部没有吹出普通气流，而是突然喷出一道真实、强烈、连续的橙黄色火焰。

动作顺序必须明确：

身体前倾靠近蛋糕
→ 眼神看向蜡烛
→ 嘴唇收拢
→ 开始吹气
→ 嘴部突然出现火焰
→ 火焰持续向蛋糕上方与镜头前方喷射
→ 女主保持俯身吹蜡烛的高潮姿势。
火焰要求
火焰只能从女主嘴部中央出现；
火焰必须由吹气动作触发，不能提前出现；
火焰方向必须与女主吹蜡烛的方向一致；
火焰从嘴部向正前方喷出，并略微掠过蛋糕上方；
不能要求女主抬头喷火，不能坐直喷火，也不能转向左右喷火；

必须持续喷射，不能只是一个短促火球；

火焰中心明亮偏黄，外缘为橙红色；

具有真实翻卷、流动、尾焰和轻微热浪扰动；

火光自然照亮女主面部、发丝、皇冠、服装、桌面和蛋糕；

蛋糕表面与桌面出现真实暖色反光；

火焰不能完全遮住蛋糕，不能烧毁蛋糕，不能导致蛋糕和蜡烛融化或变形；
火焰不能导致人物嘴部、牙齿、脸型、头发或五官变形。
女主始终保持双手撑在桌面两侧、身体前倾的吹蜡烛姿势，不能因为喷火突然坐直、后仰、站起或改变动作。
蛋糕始终稳定放在桌面中央，弯曲生日蜡烛仍插在蛋糕上。嘴部火焰出现后，蜡烛上的小火苗可以被强烈气流和火焰覆盖，但蛋糕与蜡烛本体不能消失。
喷火时，人物表情依然保持冷静、克制，形成荒诞反差感，不能惊恐、狰狞、翻白眼或过度用力。

【镜头8：吹蜡烛喷火的黑白生日海报定格】

当女主保持俯身吹蜡烛姿势、嘴部火焰达到最长、最完整、最有冲击力的瞬间时，直接使用当前画面进行黑白生日海报定格。
```

---
