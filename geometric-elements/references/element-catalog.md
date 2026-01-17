# Element Catalog

## Corner Accent

L-shaped corner decoration with optional accent lines.

```bash
# Basic
python scripts/generate.py corner-accent --color "#D4A84B" --size 150

# With gradient
python scripts/generate.py corner-accent --color "#D4A84B" --color2 "#FFFFFF" --gradient linear --size 200
```

**Options:**
- `--size` — Length of L-arms (default: 200)
- `--stroke` — Line thickness (default: 4)

**Positions:** Top-left by default. Rotate/flip in your design tool for other corners.

---

## Line Divider

Horizontal line with optional gradient fade.

```bash
# Solid
python scripts/generate.py line-divider --color "#D4A84B" --width 800

# Gradient fade (recommended)
python scripts/generate.py line-divider --color "#D4A84B" --color2 "#FFFFFF" --gradient linear --width 800

# With decorative dots
python scripts/generate.py line-divider --color "#D4A84B" --style dotted --width 400
```

**Options:**
- `--width` — Line length (default: 400)
- `--stroke` — Line thickness (default: 4)
- `--style dotted` — Add dots at endpoints

---

## Arc Accent

Curved arc for elegant decoration.

```bash
# Single arc
python scripts/generate.py arc-accent --color "#D4A84B" --size 150

# Double arc (recommended)
python scripts/generate.py arc-accent --color "#D4A84B" --size 150 --style double

# With radial gradient
python scripts/generate.py arc-accent --color "#D4A84B" --color2 "#FFFFFF" --gradient radial --size 200
```

**Options:**
- `--size` — Arc diameter (default: 200)
- `--style double` — Add inner arc

---

## Frame Border

Corner brackets for framing content.

```bash
# Default
python scripts/generate.py frame-border --color "#D4A84B" --width 400 --height 300

# Larger corners
python scripts/generate.py frame-border --color "#D4A84B" --size 80 --width 800 --height 600
```

**Options:**
- `--size` — Corner bracket length (default: 40)
- `--width/--height` — Canvas dimensions

---

## Pattern

Repeating geometric patterns.

```bash
# Dots
python scripts/generate.py pattern --color "#D4A84B" --style dots --size 50

# Crosses
python scripts/generate.py pattern --color "#D4A84B" --style crosses --size 40

# Diamonds
python scripts/generate.py pattern --color "#D4A84B" --style diamonds --size 60
```

**Styles:** `dots`, `crosses`, `diamonds`

---

## Mandala

Sacred geometry / complex geometric pattern with circles, polygons, and connecting lines.

```bash
# Basic (white on black)
python scripts/generate.py mandala --color "#CCCCCC" --bg "#0A0A0A" --size 400

# Gold on transparent
python scripts/generate.py mandala --color "#D4A84B" --size 300 --rings 6

# Complex (more layers)
python scripts/generate.py mandala --color "#FFFFFF" --bg "#1A1A2E" --size 500 --rings 12 --layers 5 --stroke 1
```

**Options:**
- `--rings` — Number of circles in the ring (default: 8)
- `--layers` — Number of polygon layers (default: 3)
- `--bg` — Background color (default: transparent)
- `--stroke` — Line thickness (default: 4, use 1-2 for detailed patterns)

**Components:**
- Rotated polygons (squares & octagons)
- Circles arranged in ring
- Connecting lines (radial + cross)
- Central triangle
- Center & outer circles

---

## Brand Colors Reference

| Name | Hex | RGB |
|------|-----|-----|
| Gold | `#D4A84B` | rgb(212,168,75) |
| Black | `#0A0A0A` | rgb(10,10,10) |
| White | `#FFFFFF` | rgb(255,255,255) |
| Light Gray | `#F5F5F5` | rgb(245,245,245) |
| Dark Gray | `#4A4A4A` | rgb(74,74,74) |

## Tips

1. **High DPI:** Use `--size` 2x for retina displays
2. **Gradient direction:** Linear gradient follows color1→color2 direction
3. **Transparency:** All outputs have transparent background
4. **Combining:** Layer multiple elements in your design tool
