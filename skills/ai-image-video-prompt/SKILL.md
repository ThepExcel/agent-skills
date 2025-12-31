---
name: ai-image-video-prompt
description: |
  Professional AI image/video prompt engineering with visual artist's eye. Creates prompts that produce stunning, professional-quality visuals by understanding composition, color theory, lighting, cinematography, and model-specific techniques. Use when: (1) User wants to generate AI images/videos, (2) "create image of...", "generate video...", (3) Needs help with prompts for Nano Banana Pro, Qwen Image, Z-Image Turbo, Wan 2.2, Sora2, or similar models, (4) Wants to improve visual quality of AI outputs.
---

# AI Image & Video Prompt Engineering

Create professional-quality AI visuals with an artist's eye.

## Core Philosophy

**Prompt = Vision + Craft + Syntax**

| Component | What It Is | This Skill Provides |
|-----------|-----------|---------------------|
| **Vision** | What you want to create | Visual judgment, taste |
| **Craft** | Technical knowledge | Composition, color, lighting, cinematography |
| **Syntax** | Model-specific format | Prompt structure per model |

---

## Two Modes

| Mode | Trigger | Workflow |
|------|---------|----------|
| **Generate** | "สร้างภาพ...", "generate image of..." | VISUALIZE → COMPOSE → PROMPT |
| **Critique & Edit** | "ดูรูปนี้หน่อย", "ปรับปรุงรูปนี้", shows image | GOAL → ANALYZE → DIAGNOSE → PRESCRIBE |

---

## Mode 1: Generate

### Workflow: VISUALIZE → COMPOSE → PROMPT

### Step 1: VISUALIZE (What's the final image?)

Before writing any prompt, answer:

```
1. SUBJECT: Who/what is the main focus?
2. MOOD: What emotion should it evoke?
3. STYLE: Photorealistic? Artistic? Cinematic?
4. PURPOSE: Where will this be used?
```

### Step 2: COMPOSE (Apply visual fundamentals)

| Element | Quick Decision |
|---------|----------------|
| **Composition** | Rule of thirds? Symmetry? Leading lines? |
| **Color** | Warm/cool? Complementary? Monochrome? |
| **Lighting** | Golden hour? Studio? Dramatic? |
| **Lens** | Wide (context)? Tele (compression)? |
| **Angle** | Eye level? Low (power)? High (vulnerable)? |

**For thumbnails/social media:** Also consider typography, text placement, visual hierarchy.

→ See **[visual-fundamentals.md](references/visual-fundamentals.md)** for detailed guidance.
→ See **[graphic-design.md](references/graphic-design.md)** for thumbnails & social media.

### Step 3: PROMPT (Model-specific syntax)

| Model | Best For | Prompt Style |
|-------|----------|--------------|
| **Nano Banana Pro** | Text, infographics, editing | Creative Director (ICS) |
| **Qwen Image** | Text rendering, Chinese | Structured paragraphs |
| **Z-Image Turbo** | Fast, budget | Director style, no negatives |
| **Wan 2.2** | Video, motion | 80-120 words, cinematic |
| **Sora2** | Pro video, audio | Storyboard + dialogue |

→ See **[references/models/](references/models/)** for model-specific guides.

---

## Mode 2: Critique & Edit

### Workflow: GOAL → ANALYZE → DIAGNOSE → PRESCRIBE

When user shows an image and wants to improve it:

### Step 1: GOAL (ถามเป้าหมายก่อน)

**ต้องถามก่อนวิจารณ์:**

```
"ภาพนี้จะใช้ทำอะไรคะ?"
"อยากให้ออกมาเป็นแบบไหน?"
"มีอะไรที่รู้สึกว่ายังไม่ใช่ไหม?"
```

| Goal Type | Focus Areas |
|-----------|-------------|
| **Commercial/Product** | Clean, professional, brand consistency |
| **Social Media** | Eye-catching, scroll-stopping, mood |
| **Thumbnail** | Readable text, high contrast, face expression, CTR |
| **Portfolio/Art** | Technical excellence, artistic vision |
| **Editorial** | Story, emotion, narrative |
| **Personal** | Subject flattering, memorable moment |

### Step 2: ANALYZE (วิเคราะห์ 6 มิติ)

Evaluate image against user's goal:

| Dimension | Questions to Ask |
|-----------|------------------|
| **Composition** | Subject placement? Balance? Leading lines? Clutter? |
| **Color** | Harmony? Temperature? Matches mood? Distracting? |
| **Lighting** | Direction? Quality? Flattering? Mood-appropriate? |
| **Focus/DOF** | Sharp where needed? Distracting background? |
| **Technical** | Exposure? Noise? Sharpness? Resolution? |
| **Story/Mood** | Does it convey intended emotion? Authentic? |
| **Typography** | (For thumbnails) Readable? Hierarchy? Contrast? Position? |

### Step 3: DIAGNOSE (ระบุปัญหา + จัดลำดับ)

**Format:**

```
## สิ่งที่ดีแล้ว ✓
- [strength 1]
- [strength 2]

## สิ่งที่ควรปรับ (เรียงตามผลกระทบ)
1. [HIGH IMPACT] [issue] → [why it matters for goal]
2. [MEDIUM] [issue] → [why]
3. [LOW] [issue] → [optional improvement]
```

**Diagnostic Checklist:**

| Issue | Symptoms | Common in |
|-------|----------|-----------|
| **Poor composition** | Subject lost, cluttered, no focus | Snapshots |
| **Bad lighting** | Harsh shadows, flat, wrong mood | Indoor, noon |
| **Color issues** | Cast, muddy, clashing | Mixed light, wrong WB |
| **Soft focus** | Blurry subject, wrong DOF | Low light, wrong aperture |
| **Exposure problems** | Too dark/bright, lost detail | Tricky lighting |
| **Distracting elements** | Objects pulling attention | Busy backgrounds |

### Step 4: PRESCRIBE (แนะนำ + สร้าง Edit Prompt)

**Two paths:**

| Path | When | Output |
|------|------|--------|
| **Reshoot** | Fundamental issues (lighting, angle) | Shot recommendations |
| **Edit** | Fixable post-processing | Edit prompt for AI model |

**Edit Prompt Template:**

```
[ACTION]: [specific change]
[TARGET]: [what to affect]
[PRESERVE]: [what to keep unchanged]
[STYLE]: [desired look after edit]
```

**Example Edit Prompts:**

| Issue | Edit Prompt |
|-------|-------------|
| Distracting background | "Blur the background to create bokeh effect, keep subject sharp" |
| Wrong color temp | "Warm up the image, add golden hour color grading" |
| Flat lighting | "Add dramatic side lighting, increase contrast in shadows" |
| Cluttered | "Remove the [object] in background, extend clean background" |
| Wrong mood | "Make the atmosphere more moody and cinematic, add blue tones" |

### Critique Voice

**เป็นกลาง + สร้างสรรค์:**
- ชมก่อน → บอกจุดแข็ง
- วิจารณ์เพื่อพัฒนา → ไม่ใช่เพื่อ criticize
- ให้ทางออก → ไม่ใช่แค่บอกปัญหา
- เคารพเป้าหมายของ user → ไม่ยัดเยียด taste ของตัวเอง

**ตัวอย่าง Critique:**

```
## วิเคราะห์ภาพ

### สิ่งที่ดีแล้ว ✓
- Subject placement ใช้ rule of thirds ได้ดี
- Expression จับได้ natural มาก

### สิ่งที่ควรปรับ

1. **[HIGH]** Background รก มีสิ่งรบกวนสายตา
   → สำหรับ portfolio, ควร clean กว่านี้
   → **Edit:** "Blur background significantly, remove distracting elements"

2. **[MEDIUM]** แสง flat ไป ขาด dimension
   → เพิ่ม contrast จะทำให้ดู professional ขึ้น
   → **Edit:** "Add subtle side lighting effect, increase shadow depth"

3. **[LOW]** Color cast เหลืองเล็กน้อย
   → ถ้าต้องการ neutral look
   → **Edit:** "Correct yellow color cast, neutral white balance"
```

---

## Quick Reference: Visual Fundamentals

### Composition

| Technique | When | Prompt Keywords |
|-----------|------|-----------------|
| Rule of thirds | Default | "subject positioned off-center" |
| Centered/Symmetry | Power, calm | "centered composition, symmetrical" |
| Leading lines | Depth, guide | "leading lines toward subject" |
| Negative space | Minimalist | "negative space, minimal, clean" |
| Frame in frame | Focus | "framed by doorway/window" |

### Color Harmony

| Type | Effect | Prompt Keywords |
|------|--------|-----------------|
| Complementary | Tension, pop | "orange and teal", "blue and orange contrast" |
| Analogous | Harmony, calm | "cool blue-green palette", "warm earth tones" |
| Monochrome | Mood, focus | "monochromatic blue", "sepia tones" |
| Triadic | Vibrant | "vibrant primary colors" |

### Lighting

| Style | Mood | Prompt Keywords |
|-------|------|-----------------|
| Golden hour | Warm, romantic | "golden hour, warm sunlight, long shadows" |
| Blue hour | Moody, cool | "blue hour, twilight, cool ambient" |
| Rembrandt | Dramatic, artistic | "Rembrandt lighting, triangle shadow" |
| Rim light | Separation | "rim lighting, backlit, edge light" |
| Soft/Diffused | Gentle, beauty | "soft diffused light, overcast" |
| Hard/Direct | Dramatic | "hard light, sharp shadows, direct sun" |

### Lens/Perspective

| Focal Length | Effect | Prompt Keywords |
|--------------|--------|-----------------|
| Ultra wide (14-24mm) | Expansive, distort | "ultra wide angle, expansive view" |
| Wide (24-35mm) | Context, street | "wide angle, environmental" |
| Normal (35-50mm) | Natural | "natural perspective, 50mm" |
| Portrait (85-135mm) | Flattering, bokeh | "85mm portrait lens, shallow depth of field" |
| Telephoto (200mm+) | Compression | "telephoto compression, stacked layers" |

→ Full details: **[visual-fundamentals.md](references/visual-fundamentals.md)**

---

## Quick Reference: Video/Cinematography

### Camera Movement

| Movement | Effect | Prompt Keywords |
|----------|--------|-----------------|
| Static | Stable, observe | "static shot, locked camera" |
| Pan L/R | Survey, follow | "slow pan left revealing..." |
| Tilt Up/Down | Reveal, scale | "tilt up to reveal..." |
| Dolly In/Out | Intimacy/distance | "dolly in slowly toward..." |
| Tracking | Follow action | "tracking shot following subject" |
| Crane | Epic, reveal | "crane shot rising above..." |
| Handheld | Realism, tension | "handheld, documentary style" |

### Shot Types

| Shot | Frame | Use |
|------|-------|-----|
| Establishing | Wide location | Set scene |
| Full | Whole body | Action |
| Medium | Waist up | Dialogue |
| Close-up | Face | Emotion |
| Extreme CU | Detail | Intensity |

### Aspect Ratio

| Ratio | Feel | Prompt Keywords |
|-------|------|-----------------|
| 16:9 | Modern, TV | "16:9 widescreen" |
| 2.35:1 | Cinematic, epic | "anamorphic widescreen, cinemascope" |
| 4:3 | Vintage, intimate | "4:3 academy ratio, vintage" |
| 9:16 | Mobile, vertical | "vertical video, mobile format" |

→ Full details: **[cinematography.md](references/cinematography.md)**

---

## Quick Reference: Styles

### Film Stocks

| Stock | Look | Prompt Keywords |
|-------|------|-----------------|
| Kodak Portra | Warm skin, soft | "Kodak Portra 400, warm tones" |
| Kodak Ektar | Saturated, vibrant | "Kodak Ektar 100, vivid colors" |
| Fuji Pro 400H | Cool, pastel | "Fuji Pro 400H, soft pastels" |
| Cinestill 800T | Tungsten, halation | "Cinestill 800T, neon halation" |

### Art Movements

| Style | Visual Traits | Prompt Keywords |
|-------|---------------|-----------------|
| Impressionism | Soft, light play | "impressionist style, soft focus, painterly" |
| Surrealism | Dreamlike, impossible | "surrealist, dreamscape, impossible geometry" |
| Minimalism | Clean, simple | "minimalist, clean lines, negative space" |
| Film Noir | High contrast B&W | "film noir, high contrast, dramatic shadows" |
| Cyberpunk | Neon, rain, dystopia | "cyberpunk, neon lights, rain-slicked streets" |

### Color Grading

| Look | Description | Prompt Keywords |
|------|-------------|-----------------|
| Teal & Orange | Hollywood blockbuster | "teal and orange color grading" |
| Bleach Bypass | Desaturated, gritty | "bleach bypass, desaturated, high contrast" |
| Cross-process | Color shift | "cross-processed, color shift" |
| Lifted Blacks | Faded, matte | "lifted blacks, faded film look" |

→ Full details: **[styles-glossary.md](references/styles-glossary.md)**

---

## Quick Reference: Graphic Design (Thumbnails/Social)

### Thumbnail Essentials

| Element | Guideline |
|---------|-----------|
| **Text** | 3-5 words max, 30%+ of thumbnail height |
| **Face** | Expressive (surprise, excitement), close-up |
| **Colors** | Saturated, high contrast |
| **Safe zone** | Keep content in center 80% |
| **Test** | Must be readable at 100px width |

### Typography for Images

| Rule | Guideline |
|------|-----------|
| **Fonts** | Max 2 (1 heading + 1 accent) |
| **Contrast** | Use stroke/shadow on busy backgrounds |
| **Hierarchy** | Largest = most important |
| **Position** | Avoid center (reserve for face/subject) |

### Platform Sizes

| Platform | Image Size |
|----------|------------|
| YouTube Thumbnail | 1280 x 720 (16:9) |
| Blog Feature | 1200 x 630 (1.91:1) |
| Instagram Post | 1080 x 1080 (1:1) |
| Instagram Story | 1080 x 1920 (9:16) |

→ Full details: **[graphic-design.md](references/graphic-design.md)**

---

## Model Selection Guide

### Image Generation

| Need | Model | Why |
|------|-------|-----|
| **Text/Typography** | Nano Banana Pro, Qwen Image | Best text rendering |
| **Fast iteration** | Z-Image Turbo | $0.005/MP, sub-second |
| **Image editing** | Qwen Image Edit, Nano Banana Pro | In-painting, style transfer |
| **Budget production** | Z-Image Turbo | Cheapest per image |
| **Premium quality** | Nano Banana Pro | Best semantic understanding |

### Video Generation

| Need | Model | Why |
|------|-------|-----|
| **Open source/Local** | Wan 2.2 | Free, ComfyUI native |
| **Quick clips** | Wan 2.2 5B | Runs on 4090 |
| **Pro quality** | Sora2 Pro | Best fidelity |
| **Audio sync** | Sora2 | Native audio generation |
| **Fast iteration** | Sora2 (standard) | Quick turnaround |

---

## Prompt Templates

### Image: Professional Portrait

```
[SUBJECT]: Professional headshot of [description], [age], [ethnicity]
[LIGHTING]: Rembrandt lighting with soft fill, subtle rim light
[COMPOSITION]: Centered, shallow depth of field, clean background
[STYLE]: Editorial photography, Kodak Portra 400
[TECHNICAL]: 85mm f/1.8, studio lighting, 4K resolution
```

### Image: Cinematic Landscape

```
[SCENE]: [Location description] at [time of day]
[COMPOSITION]: Rule of thirds, leading lines toward [focal point]
[ATMOSPHERE]: [Weather], [mood] atmosphere
[COLOR]: [Color palette], [film stock look]
[TECHNICAL]: Wide angle 24mm, deep focus, anamorphic 2.35:1
```

### Video: Cinematic Scene (Wan 2.2 / Sora2)

```
[OPENING]: Camera [movement] revealing [scene description]
[SUBJECT]: [Character/object] [action with motion verbs]
[ENVIRONMENT]: [Setting] with [atmospheric details]
[CAMERA]: [Shot type], [movement], [speed]
[ATMOSPHERE]: [Lighting], [color palette], [mood]
[STYLE]: Cinematic film scene, [film stock], [director reference]
```

---

## Model-Specific Guides

| Model | Guide |
|-------|-------|
| Nano Banana Pro | [nano-banana-pro.md](references/models/nano-banana-pro.md) |
| Qwen Image / Edit | [qwen-image.md](references/models/qwen-image.md) |
| Z-Image Turbo | [z-image-turbo.md](references/models/z-image-turbo.md) |
| Wan 2.2 | [wan-2-2.md](references/models/wan-2-2.md) |
| Sora2 | [sora2.md](references/models/sora2.md) |

---

## Related Skills (Optional)

| When | Suggest |
|------|---------|
| Generate actual images | `/visualization` - Matplotlib, Manim |
| Research visual references | `/deep-research` - find inspiration |
| Creative ideation | `/creativity` - brainstorm concepts |

---

## Anti-Patterns

| Don't | Do Instead |
|-------|------------|
| "beautiful photo" | Specify what makes it beautiful |
| "high quality" | Describe the quality (sharp, detailed, 4K) |
| "nice lighting" | Name the lighting (Rembrandt, golden hour) |
| Tag soup: "4k, hdr, realistic" | Structured description |
| Vague colors: "colorful" | Specific: "teal and orange palette" |

---

## Iteration Strategy

1. **Start simple** → Core subject + style
2. **Add specifics** → Lighting, composition, color
3. **Test variations** → Different angles, moods, styles
4. **Use seed** → Lock good results, iterate details
5. **Combine strengths** → Image → Video pipeline
