---
name: graphic-designer
description: Designs graphics for thumbnails, social media, banners, and presentations. Applies design principles (CRAP, Gestalt, visual hierarchy) with research-backed techniques. Integrates with /geometric-elements for decorative assets. Use when creating layouts, choosing typography/colors, or designing any graphic assets. For photography/cinematography prompts, use /art-director instead.
---

# Graphic Designer

Create effective visual communication through research-backed design principles.

**Design = Communication + Aesthetics** — Good design is invisible: it guides the eye, conveys the message, and feels "right" without effort.

---

## Quick Workflow

```
1. PURPOSE   — What should viewer DO after seeing this?
2. AUDIENCE  — Who? What culture? What device?
3. HIERARCHY — What's #1, #2, #3 in importance?
4. LAYOUT    — Sketch placement (Z or F pattern)
5. COLORS    — 60-30-10 rule (check cultural meaning!)
6. TYPE      — Max 2 fonts (1 display + 1 body)
7. ELEMENTS  — Add graphics, icons, photos
8. REFINE    — Remove until it breaks, then add back
9. CHECK     — Squint test, mobile test, contrast check
```

---

## Design Principles (Summary)

### CRAP Principles

| Principle | What | How |
|-----------|------|-----|
| **Contrast** | Make differences obvious | Size, color, weight |
| **Repetition** | Create consistency | Reuse colors, fonts |
| **Alignment** | Connect visually | Grid, edges |
| **Proximity** | Group related items | Spacing |

→ Details: [references/gestalt.md](references/gestalt.md)

### Visual Hierarchy (order of impact)

1. **Size** — Larger = more important
2. **Color/Contrast** — Bright catches eye first
3. **Position** — Top-left (Western), top-right (RTL)
4. **White Space** — Isolation creates emphasis
5. **Weight** — Bold stands out

### Reading Patterns

| Pattern | Best For | Flow |
|---------|----------|------|
| **Z-Pattern** | Visual/marketing | Top-L → Top-R → Bottom-L → Bottom-R |
| **F-Pattern** | Text-heavy | Horizontal scans + vertical down left |

---

## Color System

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
| **2025 Trend** | Dark + Neon accent |

### Cultural Color Meanings (Check First!)

| Color | Western | East Asia | Thai Context |
|-------|---------|-----------|--------------|
| **Red** | Danger, urgency | Luck, joy | Auspicious |
| **White** | Pure, clean | Mourning | Formal/Mourning |
| **Yellow** | Optimism | Sacred | Royal |
| **Gold** | Luxury | Prosperity | Premium |

→ Full guide: [references/color-theory.md](references/color-theory.md)

### Accessibility (WCAG)

| Standard | Normal Text | Large Text (18pt+) |
|----------|-------------|-------------------|
| **AA (Minimum)** | 4.5:1 | 3:1 |
| **AAA (Enhanced)** | 7:1 | 4.5:1 |

Tool: [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

---

## Typography

### Quick Rules

- **Max 2 fonts** — 1 display + 1 body
- **Hierarchy via size** — Not font changes
- **Line height** — 1.4-1.6 for body, 1.1-1.2 for headlines

### Safe Font Pairs

| Display | Body | Mood |
|---------|------|------|
| Montserrat Bold | Open Sans | Modern |
| Playfair Display | Lato | Elegant |
| **Kanit Bold** | **Sarabun** | Thai-friendly |

→ Full guide: [references/typography.md](references/typography.md)

---

## Layout

### 8px Spacing System

| Size | Use |
|------|-----|
| 8px | Within groups |
| 16px | Between elements |
| 24-32px | Sections |
| 48px | Page margins |

### Social Media Dimensions

| Platform | Ratio | Size |
|----------|-------|------|
| YouTube Thumbnail | 16:9 | 1280×720 |
| Instagram Post | 1:1 | 1080×1080 |
| Instagram Story | 9:16 | 1080×1920 |
| Facebook/LinkedIn | 1.91:1 | 1200×630 |

→ Layout templates: [references/layouts.md](references/layouts.md)

---

## Presentation Slides

### Core Rules

| Rule | Guideline |
|------|-----------|
| **One idea per slide** | Single focused message |
| **Rule of 4** | Max 4 bullets, 4 words each |
| **Don't compete** | Audience can't read AND listen |

### Font Sizes

| Context | Titles | Body | Captions |
|---------|--------|------|----------|
| **Large room** | 60pt+ | 40pt+ | 24pt+ |
| **Virtual** | 44pt+ | 32pt+ | 20pt+ |

→ Full guide: [references/presentation-design.md](references/presentation-design.md)

---

## YouTube Thumbnails

| Element | Recommendation |
|---------|----------------|
| **Faces** | Use expressive faces (+20-30% CTR) |
| **Text** | Minimal, bold, curiosity |
| **Colors** | High contrast, 3-4 max |
| **Mobile** | Readable at small size |

**Layout:** Face 40%+ height, eye contact, blur background

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Too many fonts | Max 2 |
| No hierarchy | Make #1 thing 2x bigger |
| Centered everything | Use left-align + proximity |
| Rainbow colors | Pick 1 accent color |
| Filled every space | Add 20% more white space |
| Text on busy photo | Add overlay or blur |
| Ignoring culture | Check color meanings |

---

## Checklists

### Before Designing

- [ ] What's the ONE message?
- [ ] Who's the audience? (culture, device)
- [ ] What emotion should it evoke?

### Quality Check

- [ ] Clear hierarchy? (squint test)
- [ ] Readable at target size?
- [ ] Max 3-4 colors, 2-3 fonts?
- [ ] Contrast 4.5:1+? (WCAG AA)
- [ ] Aligned to grid?
- [ ] Enough white space?

---

## Tools Integration

### /geometric-elements — Decorative Assets

```bash
python scripts/generate.py shape --style star --color "#D4A84B" --size 100
python scripts/generate.py corner-accent --color "#D4A84B" --size 150
python scripts/generate.py line-divider --color "#D4A84B" --width 800
```

### Related Skills

| Need | Skill |
|------|-------|
| Decorative elements | `/geometric-elements` |
| Photo/video prompts | `/art-director` |
| PowerPoint slides | `/pptx` |
| ThepExcel brand | `/thepexcel-brand-guidelines` |

---

## References

| Topic | File |
|-------|------|
| Color theory | [references/color-theory.md](references/color-theory.md) |
| Typography | [references/typography.md](references/typography.md) |
| Layouts | [references/layouts.md](references/layouts.md) |
| Presentation design | [references/presentation-design.md](references/presentation-design.md) |
| Gestalt principles | [references/gestalt.md](references/gestalt.md) |
