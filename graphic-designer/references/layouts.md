# Layout Patterns

## Grid Systems

### 12-Column Grid
Most flexible, divisible by 2, 3, 4, 6.

```
|1|2|3|4|5|6|7|8|9|10|11|12|
├─────────┼─────────────────┤  8+4 (sidebar layout)
├─────┼─────┼─────┼─────────┤  3+3+3+3 (cards)
├───────────┼───────────────┤  5+7 (asymmetric)
├───────────────────────────┤  12 (full width)
```

### Common Divisions
| Columns | Use |
|---------|-----|
| 12 | Full-width hero |
| 8+4 | Content + sidebar |
| 6+6 | Two equal columns |
| 4+4+4 | Three cards |
| 3+3+3+3 | Four items grid |

## Layout Templates

### Z-Pattern (Scanning)
```
┌─────────────────────────┐
│ LOGO          [NAV NAV] │  ← Eye starts here
│                         │
│ HEADLINE                │
│        ───────────      │  ← Diagonal scan
│                         │
│ Supporting text    [CTA]│  ← Ends at CTA
└─────────────────────────┘
```
Best for: Landing pages, simple content

### F-Pattern (Reading)
```
┌─────────────────────────┐
│ HEADLINE HEADLINE HEAD  │  ← First scan
│ ────────────────────    │
│ Subhead text text text  │  ← Second scan
│ ────────────────        │
│ Body text text text     │  ← Vertical scan down
│ Body text text          │
│ Body text               │
└─────────────────────────┘
```
Best for: Text-heavy content, blogs

### Rule of Thirds
```
┌─────────┬─────────┬─────────┐
│         │         │         │
│    ●────┼────●    │         │
│         │         │         │
├─────────┼─────────┼─────────┤
│         │         │         │
│    ●────┼────●    │         │
│         │         │         │
└─────────┴─────────┴─────────┘
```
Place key elements at intersections (●)

## Thumbnail Layouts

### Face + Text (YouTube)
```
┌─────────────────────────────┐
│                             │
│ [FACE]     BIG HEADLINE     │
│            ─────────────    │
│            smaller text     │
│                             │
└─────────────────────────────┘
```
- Face fills 40% height minimum
- Eye contact if possible
- Text on contrasting area

### Before/After
```
┌─────────────────────────────┐
│  BEFORE   │    AFTER        │
│           │                 │
│  [old]    │    [new]        │
│           │                 │
└─────────────────────────────┘
```
- Clear visual difference
- Arrow or divider line

### Listicle
```
┌─────────────────────────────┐
│    7 WAYS TO...             │
│    ────────────             │
│                             │
│    [Icons/Preview]          │
│                             │
└─────────────────────────────┘
```
- Number prominent
- Curiosity gap

## Social Media Dimensions

| Platform | Format | Size |
|----------|--------|------|
| YouTube Thumbnail | 16:9 | 1280×720 |
| Instagram Post | 1:1 | 1080×1080 |
| Instagram Story | 9:16 | 1080×1920 |
| Facebook Post | 1.91:1 | 1200×630 |
| Twitter Post | 16:9 | 1200×675 |
| LinkedIn Post | 1.91:1 | 1200×627 |

## Spacing System

### 8px Base Grid
```
4px   — Tight (icons, inline)
8px   — Small (within groups)
16px  — Medium (between elements)
24px  — Large (sections)
32px  — XL (major sections)
48px  — XXL (page margins)
```

### Margin Rules
- Consistent on all sides
- More space = more importance
- White space is not "empty"

## Visual Hierarchy Checklist

1. [ ] Can you identify #1 in 1 second?
2. [ ] Clear path from #1 → #2 → #3?
3. [ ] Eye flows naturally to CTA?
4. [ ] No competing elements same size?
5. [ ] Grouped items use proximity?
