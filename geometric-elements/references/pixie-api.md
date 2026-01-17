# Pixie-python API Reference

Quick reference for creating custom geometric elements.

## Setup

```python
import pixie
import math

# Create canvas
image = pixie.Image(width, height)  # width, height must be int

# Create drawing context
ctx = image.new_context()
```

## Colors & Paints

```python
# Solid color
paint = pixie.Paint(pixie.SOLID_PAINT)
paint.color = pixie.Color(r, g, b, a)  # 0.0-1.0 range

# Linear gradient
paint = pixie.Paint(pixie.LINEAR_GRADIENT_PAINT)
paint.gradient_handle_positions.append(pixie.Vector2(x1, y1))
paint.gradient_handle_positions.append(pixie.Vector2(x2, y2))
paint.gradient_stops.append(pixie.ColorStop(color1, 0))  # position 0-1
paint.gradient_stops.append(pixie.ColorStop(color2, 1))

# Radial gradient
paint = pixie.Paint(pixie.RADIAL_GRADIENT_PAINT)
paint.gradient_handle_positions.append(pixie.Vector2(cx, cy))      # center
paint.gradient_handle_positions.append(pixie.Vector2(cx+r, cy))    # edge X
paint.gradient_handle_positions.append(pixie.Vector2(cx, cy+r))    # edge Y
```

## Drawing with Context

```python
ctx.stroke_style = paint
ctx.fill_style = paint
ctx.line_width = 2.0
ctx.line_cap = pixie.ROUND_CAP    # or BUTT_CAP, SQUARE_CAP
ctx.line_join = pixie.ROUND_JOIN  # or MITER_JOIN, BEVEL_JOIN

# Draw line segment
ctx.stroke_segment(x1, y1, x2, y2)
```

## Paths (SVG-style)

```python
# Parse SVG path string
path = pixie.parse_path("M 10 10 L 100 100 Z")

# SVG path commands:
# M x y     - Move to
# L x y     - Line to
# H x       - Horizontal line
# V y       - Vertical line
# A rx ry rotation large-arc sweep x y - Arc
# Q cx cy x y - Quadratic bezier
# C c1x c1y c2x c2y x y - Cubic bezier
# Z         - Close path

# Stroke path
image.stroke_path(path, paint, pixie.Matrix3(), stroke_width)

# Fill path
image.fill_path(path, paint)
```

## Shapes via Path

```python
path = pixie.Path()

# Circle/Ellipse
path.ellipse(cx, cy, rx, ry)

# Rectangle
path.rect(x, y, width, height)

# Rounded rectangle
path.rounded_rect(x, y, w, h, radius_nw, radius_ne, radius_se, radius_sw)

# Then stroke or fill
image.stroke_path(path, paint, pixie.Matrix3(), stroke_width)
image.fill_path(path, paint)
```

## Common Patterns

### Circle at position
```python
circle = pixie.Path()
circle.ellipse(cx, cy, radius, radius)
image.stroke_path(circle, paint, pixie.Matrix3(), stroke)
```

### Polygon (n sides)
```python
points = []
for i in range(n_sides):
    angle = (2 * math.pi / n_sides) * i + rotation
    x = cx + radius * math.cos(angle)
    y = cy + radius * math.sin(angle)
    points.append((x, y))

path_str = f"M {points[0][0]} {points[0][1]}"
for x, y in points[1:]:
    path_str += f" L {x} {y}"
path_str += " Z"

path = pixie.parse_path(path_str)
image.stroke_path(path, paint, pixie.Matrix3(), stroke)
```

### Points arranged in circle
```python
for i in range(n_points):
    angle = (2 * math.pi / n_points) * i
    x = cx + radius * math.cos(angle)
    y = cy + radius * math.sin(angle)
    # draw something at (x, y)
```

### Arc (quarter circle)
```python
# SVG arc: A rx ry x-rotation large-arc-flag sweep-flag x y
path_str = f"M {start_x} {start_y} A {radius} {radius} 0 0 1 {end_x} {end_y}"
```

### Bezier curve
```python
# Quadratic: Q control_x control_y end_x end_y
path_str = f"M {x1} {y1} Q {cx} {cy} {x2} {y2}"

# Cubic: C c1x c1y c2x c2y end_x end_y
path_str = f"M {x1} {y1} C {c1x} {c1y} {c2x} {c2y} {x2} {y2}"
```

## Output

```python
image.write_file("output.png")
```

## Full Example: Star

```python
import pixie
import math

size = 400
image = pixie.Image(size, size)

paint = pixie.Paint(pixie.SOLID_PAINT)
paint.color = pixie.Color(0.83, 0.66, 0.29, 1.0)  # Gold

cx, cy = size/2, size/2
outer_r, inner_r = 150, 60
points = 5

path_parts = []
for i in range(points * 2):
    angle = (math.pi / points) * i - math.pi/2
    r = outer_r if i % 2 == 0 else inner_r
    x = cx + r * math.cos(angle)
    y = cy + r * math.sin(angle)
    cmd = "M" if i == 0 else "L"
    path_parts.append(f"{cmd} {x} {y}")
path_parts.append("Z")

path = pixie.parse_path(" ".join(path_parts))
image.stroke_path(path, paint, pixie.Matrix3(), 3)
image.write_file("star.png")
```

## Tips

1. **Transparent bg**: Default, no fill needed
2. **Anti-aliasing**: Built-in, always on
3. **Coordinates**: Top-left is (0,0)
4. **Matrix3()**: Identity transform, use for no transform
5. **Path reuse**: Create once, draw multiple times
