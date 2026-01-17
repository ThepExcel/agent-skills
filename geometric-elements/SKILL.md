---
name: geometric-elements
description: Generate decorative geometric elements (corners, lines, arcs, frames) with precise control over colors, gradients, and transparency. Use when creating design assets, slide decorations, or any vector-like graphics programmatically. Can also analyze reference images and recreate geometric patterns.
---

# Geometric Elements Generator

Create decorative geometric elements with code using Pixie-python.

## Quick Start

```bash
# Install dependency (first time only)
pip install pixie-python

# Generate element
python .claude/skills/geometric-elements/scripts/generate.py corner-accent \
  --color "#D4A84B" \
  --size 200 \
  --output media/output/corner.png
```

## Available Elements

| Element | Command | Description |
|---------|---------|-------------|
| **Basic Shapes** | `shape` | circle, star, heart, hexagon, arrow, etc. |
| Corner Accent | `corner-accent` | L-shaped corner decoration |
| Line Divider | `line-divider` | Horizontal divider with gradient |
| Arc Accent | `arc-accent` | Curved arc |
| Frame Border | `frame-border` | 4-corner bracket frame |
| Pattern | `pattern` | Repeating dots/crosses/diamonds |
| Mandala | `mandala` | Sacred geometry / complex patterns |

## Common Options

| Option | Description | Default |
|--------|-------------|---------|
| `--color` | Primary color (hex) | `#D4A84B` |
| `--color2` | Secondary color for gradient | None |
| `--size` | Element size in pixels | 200 |
| `--width` | Canvas width | 400 |
| `--height` | Canvas height | 400 |
| `--stroke` | Stroke width | 4 |
| `--output` | Output file path | `output.png` |
| `--gradient` | Gradient type: `linear`, `radial` | None |
| `--opacity` | Opacity 0.0-1.0 | 1.0 |

## Examples

### Basic Shapes
```bash
# Circle (stroke)
python .claude/skills/geometric-elements/scripts/generate.py shape \
  --style circle --color "#D4A84B" --size 100 --stroke 3 \
  --output media/output/circle.png

# Star (filled)
python .claude/skills/geometric-elements/scripts/generate.py shape \
  --style star --color "#D4A84B" --size 100 --sides 5 --fill \
  --output media/output/star.png

# Available styles: circle, ellipse, rectangle, square, rounded-rect,
#   triangle, polygon, star, diamond, ring, cross, arrow, arrow-up,
#   heart, hexagon, octagon, crescent
```

### Gold Corner Accent (ThepExcel Brand)
```bash
python .claude/skills/geometric-elements/scripts/generate.py corner-accent \
  --color "#D4A84B" \
  --size 150 \
  --stroke 4 \
  --output media/output/gold-corner.png
```

### Gradient Line Divider
```bash
python .claude/skills/geometric-elements/scripts/generate.py line-divider \
  --color "#D4A84B" \
  --color2 "#FFFFFF" \
  --gradient linear \
  --width 800 \
  --stroke 3 \
  --output media/output/divider.png
```

### Arc with Radial Gradient
```bash
python .claude/skills/geometric-elements/scripts/generate.py arc-accent \
  --color "#D4A84B" \
  --gradient radial \
  --size 200 \
  --output media/output/arc.png
```

### Sacred Geometry Mandala
```bash
python .claude/skills/geometric-elements/scripts/generate.py mandala \
  --color "#CCCCCC" \
  --bg "#0A0A0A" \
  --size 400 \
  --stroke 1.5 \
  --rings 8 \
  --layers 4 \
  --output media/output/mandala.png
```

## Element Details

See [references/element-catalog.md](references/element-catalog.md) for:
- Visual examples of each element type
- Detailed parameter options
- Design guidelines

## Brand Colors (ThepExcel)

| Name | Hex | Usage |
|------|-----|-------|
| Gold | `#D4A84B` | Primary accent |
| Black | `#0A0A0A` | Text, contrast |
| White | `#FFFFFF` | Background |
| Light Gray | `#F5F5F5` | Subtle BG |

## Tips

1. **Transparent background**: All outputs have transparent background by default
2. **High DPI**: Use `--size` 2x for retina displays
3. **Gradients**: Combine `--gradient linear` with `--color` and `--color2`
4. **Batch generation**: Script supports multiple outputs in one call

---

## Custom Elements (On-the-fly)

For complex or custom geometric patterns not covered by predefined commands, write Python code directly using pixie-python.

### Quick Start

```python
import pixie
import math

# Create canvas
image = pixie.Image(400, 400)

# Create paint
paint = pixie.Paint(pixie.SOLID_PAINT)
paint.color = pixie.Color(0.83, 0.66, 0.29, 1.0)  # Gold #D4A84B

# Draw using context
ctx = image.new_context()
ctx.stroke_style = paint
ctx.line_width = 2
ctx.stroke_segment(50, 50, 350, 350)

# Or using paths
path = pixie.parse_path("M 100 100 L 300 100 L 200 300 Z")
image.stroke_path(path, paint, pixie.Matrix3(), 2)

# Save
image.write_file("output.png")
```

### When to Use Custom Code

- Complex sacred geometry / mandalas
- Spirograph / mathematical curves
- Unique patterns not in predefined commands
- Animated sequences (generate frames)

### API Reference

See [references/pixie-api.md](references/pixie-api.md) for:
- Color & gradient setup
- Path commands (SVG-style)
- Common patterns (polygons, arcs, beziers)
- Full working examples

---

## From Reference Image

User สามารถส่ง reference image มาให้ Claude วิเคราะห์และสร้างตามได้

### Workflow

1. **User ส่งรูป** — screenshot, design reference, หรือ pattern ที่ต้องการ
2. **Claude วิเคราะห์** — ระบุ shapes, colors, proportions, layout
3. **Claude เขียน code** — ใช้ pixie-python API สร้าง element ตาม reference
4. **Output** — PNG พร้อมใช้งาน

### Example Request

```
"สร้าง geometric pattern ตามรูปนี้" + [แนบรูป]
```

Claude จะ:
- วิเคราะห์ว่ารูปมี circles, polygons, lines อะไรบ้าง
- ประมาณสัดส่วน, ระยะห่าง, สี
- เขียน Python code สร้างตาม
- Run และ output PNG

### Tips for Good Reference

- **ชัด** — รูปไม่เบลอ เห็น detail
- **Simple** — geometric patterns ทำได้ดี, realistic photos ยาก
- **บอกสี** — ถ้าต้องการสีเฉพาะ บอก hex code
