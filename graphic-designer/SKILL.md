---
name: graphic-designer
description: Designs graphics for thumbnails, social media, banners, and presentations. Applies design principles (hierarchy, balance, contrast) to create effective visual communication. Integrates with /geometric-elements for decorative assets. Use when creating layouts, choosing typography/colors, or designing any graphic assets. For photography/cinematography prompts, use /art-director instead.
---

# Graphic Designer

Create effective visual communication through design principles.

## Core Philosophy

**Design = Communication + Aesthetics**

Good design is invisible — it guides the eye, conveys the message, and feels "right" without effort.

---

## Design Principles (CRAP + HRP)

### Primary: CRAP
| Principle | What | How |
|-----------|------|-----|
| **Contrast** | Make differences obvious | Size, color, weight, shape |
| **Repetition** | Create consistency | Reuse colors, fonts, elements |
| **Alignment** | Connect elements visually | Grid, edges, centers |
| **Proximity** | Group related items | Spacing, containers |

### Secondary: HRP
| Principle | What | How |
|-----------|------|-----|
| **Hierarchy** | Guide attention order | Size = importance |
| **Balance** | Visual weight distribution | Symmetrical / Asymmetrical |
| **White Space** | Let design breathe | Don't fill every pixel |

---

## Quick Workflow

```
1. PURPOSE   — What should viewer DO after seeing this?
2. HIERARCHY — What's #1, #2, #3 in importance?
3. LAYOUT    — Sketch placement (thumbnail first)
4. COLORS    — 60-30-10 rule (dominant, secondary, accent)
5. TYPE      — Max 2 fonts (1 display + 1 body)
6. ELEMENTS  — Add graphics, icons, photos
7. REFINE    — Remove until it breaks, then add back
```

---

## Layout Templates

### Thumbnail (16:9)
```
┌─────────────────────────────┐
│  [FACE/SUBJECT]    HEADLINE │
│                     ─────── │
│                    subtext  │
└─────────────────────────────┘
```
- Face on left (viewers scan left→right)
- Big text, readable at small size
- 3-4 colors max

### Social Post (1:1)
```
┌─────────────────┐
│    HEADLINE     │
│   ───────────   │
│                 │
│  [Visual/Icon]  │
│                 │
│    Call to      │
│    Action →     │
└─────────────────┘
```

### Banner (Wide)
```
┌─────────────────────────────────────────┐
│ Logo    HEADLINE TEXT           [CTA]   │
└─────────────────────────────────────────┘
```

---

## Color Selection

### 60-30-10 Rule
| % | Role | Example |
|---|------|---------|
| 60% | Dominant | Background |
| 30% | Secondary | Containers, cards |
| 10% | Accent | CTAs, highlights |

### Quick Palettes
| Mood | Colors |
|------|--------|
| Professional | Navy + White + Gold |
| Energetic | Orange + Black + White |
| Calm | Blue + Light Gray + White |
| Premium | Black + Gold + White |
| Fresh | Green + White + Light Gray |

### Color Psychology
| Color | Feeling | Use For |
|-------|---------|---------|
| Red | Urgency, passion | Sales, warnings |
| Blue | Trust, calm | Corporate, tech |
| Green | Growth, nature | Health, eco |
| Yellow | Optimism, attention | Highlights |
| Black | Premium, power | Luxury |
| White | Clean, space | Backgrounds |

---

## Typography

### Font Pairing Rules
1. **Contrast** — Pair serif with sans-serif
2. **1 display + 1 body** — Max 2 fonts
3. **Hierarchy via size** — Not font changes

### Size Hierarchy
| Element | Size Ratio |
|---------|------------|
| Headline | 2-3x body |
| Subhead | 1.5x body |
| Body | Base (16-18px) |
| Caption | 0.8x body |

### Safe Font Pairs
| Display | Body | Mood |
|---------|------|------|
| Montserrat Bold | Open Sans | Modern |
| Playfair Display | Lato | Elegant |
| Bebas Neue | Roboto | Bold |
| Kanit Bold | Sarabun | Thai-friendly |

---

## Tools Integration

### /geometric-elements — Decorative Assets

**Use for:** Corners, dividers, frames, shapes, patterns, mandalas

```bash
# Basic shapes (circle, star, heart, hexagon, arrow, etc.)
python scripts/generate.py shape --style star --color "#D4A84B" --size 100 --fill
python scripts/generate.py shape --style heart --color "#FF6B6B" --size 80

# Corner decorations (for slide/banner corners)
python scripts/generate.py corner-accent --color "#D4A84B" --size 150 --stroke 4

# Line dividers (with gradient fade)
python scripts/generate.py line-divider --color "#D4A84B" --color2 "#FFFFFF" --gradient linear --width 800

# Frame borders (4-corner brackets)
python scripts/generate.py frame-border --color "#D4A84B" --size 60 --width 400 --height 300

# Patterns (dots, crosses, diamonds)
python scripts/generate.py pattern --style dots --color "#D4A84B" --size 30

# Sacred geometry / Mandala
python scripts/generate.py mandala --color "#CCCCCC" --bg "#0A0A0A" --size 400 --rings 8

# Custom: ส่ง reference image ให้ Claude วิเคราะห์แล้วสร้างตาม
```

**Workflow with geometric-elements:**
1. กำหนด design layout ก่อน
2. ระบุตำแหน่งที่ต้องการ decorative elements
3. เลือก element type ที่เหมาะสม (corner, divider, pattern)
4. Generate ด้วย brand colors
5. วาง element ใน design

### AI Image Generation

```bash
# Nano Banana Pro (cloud) — สำหรับ graphics ที่ต้องการ AI generate
python tools/generate_image.py "prompt" -o media/output/image.png

# ComfyUI (local) — สำหรับ style-specific generation
# Use /art-director skill สำหรับเขียน prompt ที่ดี
```

### Presentations & Documents

```
/pptx — สร้าง/แก้ไข PowerPoint
/thepexcel-brand-guidelines — ThepExcel brand colors & typography
```

---

## Checklist Before Export

- [ ] Hierarchy clear? (Squint test — can you see #1?)
- [ ] Readable at target size? (Thumbnail = small!)
- [ ] Colors consistent? (Max 3-4)
- [ ] Aligned to grid?
- [ ] White space breathing?
- [ ] CTA stands out?

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Too many fonts | Max 2 |
| No hierarchy | Make #1 thing 2x bigger |
| Centered everything | Use left-align + proximity |
| Rainbow colors | Pick 1 accent color |
| Filled every space | Add 20% more white space |
| Text on busy photo | Add overlay or text box |

---

## References

| Topic | File |
|-------|------|
| Color theory deep dive | [references/color-theory.md](references/color-theory.md) |
| Typography guide | [references/typography.md](references/typography.md) |
| Layout patterns | [references/layouts.md](references/layouts.md) |

---

## Related Skills

| Need | Skill | Use For |
|------|-------|---------|
| **Decorative elements** | `/geometric-elements` | Shapes, corners, dividers, patterns, mandalas |
| Photo/video prompts | `/art-director` | Cinematic lighting, composition, storytelling |
| PowerPoint slides | `/pptx` | Create/edit presentations |
| ThepExcel brand | `/thepexcel-brand-guidelines` | Brand colors, typography |
| Creative ideas | `/generate-creative-ideas` | Brainstorm design concepts |

### Typical Workflow

```
1. /graphic-designer  → Plan layout, colors, typography
2. /geometric-elements → Generate decorative assets
3. /art-director      → Write prompts for AI images (if needed)
4. /pptx              → Assemble into presentation (if needed)
```
