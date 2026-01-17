#!/usr/bin/env python3
"""
Geometric Elements Generator
Generate decorative geometric elements using Pixie-python.
"""

import argparse
import math
import sys
from pathlib import Path

try:
    import pixie
except ImportError:
    print("Error: pixie-python not installed. Run: pip install pixie-python")
    sys.exit(1)


def hex_to_color(hex_str: str, opacity: float = 1.0) -> pixie.Color:
    """Convert hex color to pixie Color."""
    hex_str = hex_str.lstrip('#')
    r = int(hex_str[0:2], 16) / 255
    g = int(hex_str[2:4], 16) / 255
    b = int(hex_str[4:6], 16) / 255
    return pixie.Color(r, g, b, opacity)


def create_linear_gradient(color1: str, color2: str, x1: float, y1: float, x2: float, y2: float, opacity: float = 1.0) -> pixie.Paint:
    """Create linear gradient paint."""
    paint = pixie.Paint(pixie.LINEAR_GRADIENT_PAINT)
    paint.gradient_handle_positions.append(pixie.Vector2(x1, y1))
    paint.gradient_handle_positions.append(pixie.Vector2(x2, y2))
    paint.gradient_stops.append(pixie.ColorStop(hex_to_color(color1, opacity), 0))
    paint.gradient_stops.append(pixie.ColorStop(hex_to_color(color2, 0), 1))
    return paint


def create_radial_gradient(color1: str, color2: str, cx: float, cy: float, radius: float, opacity: float = 1.0) -> pixie.Paint:
    """Create radial gradient paint."""
    paint = pixie.Paint(pixie.RADIAL_GRADIENT_PAINT)
    paint.gradient_handle_positions.append(pixie.Vector2(cx, cy))
    paint.gradient_handle_positions.append(pixie.Vector2(cx + radius, cy))
    paint.gradient_handle_positions.append(pixie.Vector2(cx, cy + radius))
    paint.gradient_stops.append(pixie.ColorStop(hex_to_color(color1, opacity), 0))
    paint.gradient_stops.append(pixie.ColorStop(hex_to_color(color2, 0), 1))
    return paint


def create_solid_paint(color: str, opacity: float = 1.0) -> pixie.Paint:
    """Create solid color paint."""
    paint = pixie.Paint(pixie.SOLID_PAINT)
    paint.color = hex_to_color(color, opacity)
    return paint


def generate_corner_accent(args):
    """Generate L-shaped corner accent."""
    size = args.size
    stroke = args.stroke
    padding = int(stroke * 2)

    # Canvas size with padding (ensure int)
    width = int(args.width or size + padding * 2)
    height = int(args.height or size + padding * 2)

    image = pixie.Image(width, height)

    # Create paint
    if args.gradient == 'linear' and args.color2:
        paint = create_linear_gradient(args.color, args.color2, padding, padding, size, size, args.opacity)
    elif args.gradient == 'radial' and args.color2:
        paint = create_radial_gradient(args.color, args.color2, padding, padding, size, args.opacity)
    else:
        paint = create_solid_paint(args.color, args.opacity)

    ctx = image.new_context()
    ctx.stroke_style = paint
    ctx.line_width = stroke
    ctx.line_cap = pixie.ROUND_CAP
    ctx.line_join = pixie.ROUND_JOIN

    # Draw L-shape
    # Vertical line
    ctx.stroke_segment(padding, padding, padding, padding + size * 0.7)
    # Horizontal line
    ctx.stroke_segment(padding, padding, padding + size * 0.7, padding)

    # Add decorative accent lines
    ctx.line_width = stroke * 0.5
    accent_offset = size * 0.15

    # Short accent on vertical
    ctx.stroke_segment(
        padding + stroke * 1.5, padding + accent_offset,
        padding + stroke * 1.5, padding + accent_offset + size * 0.2
    )
    # Short accent on horizontal
    ctx.stroke_segment(
        padding + accent_offset, padding + stroke * 1.5,
        padding + accent_offset + size * 0.2, padding + stroke * 1.5
    )

    image.write_file(args.output)
    print(f"Generated: {args.output}")


def generate_line_divider(args):
    """Generate horizontal line divider with gradient fade."""
    width = int(args.width or 400)
    height = int(args.height or 50)
    stroke = args.stroke

    image = pixie.Image(width, height)

    y_center = height / 2
    padding = 20

    # Create gradient paint (fade out at edges)
    if args.gradient == 'linear' and args.color2:
        paint = create_linear_gradient(args.color, args.color2, padding, y_center, width - padding, y_center, args.opacity)
    else:
        paint = create_solid_paint(args.color, args.opacity)

    ctx = image.new_context()
    ctx.stroke_style = paint
    ctx.line_width = stroke
    ctx.line_cap = pixie.ROUND_CAP

    # Main line
    ctx.stroke_segment(padding, y_center, width - padding, y_center)

    # Optional: decorative dots at ends
    if args.style == 'dotted':
        dot_paint = create_solid_paint(args.color, args.opacity)

        # Draw dots as small circles
        dot_path = pixie.Path()
        dot_path.ellipse(padding, y_center, stroke * 1.5, stroke * 1.5)
        image.fill_path(dot_path, dot_paint)

        dot_path2 = pixie.Path()
        dot_path2.ellipse(width - padding, y_center, stroke * 1.5, stroke * 1.5)
        image.fill_path(dot_path2, dot_paint)

    image.write_file(args.output)
    print(f"Generated: {args.output}")


def generate_arc_accent(args):
    """Generate curved arc accent."""
    size = args.size
    padding = 20

    width = int(args.width or size + padding * 2)
    height = int(args.height or size + padding * 2)

    image = pixie.Image(width, height)

    cx = width / 2
    cy = height / 2
    radius = size / 2 - padding

    # Create paint
    if args.gradient == 'radial' and args.color2:
        paint = create_radial_gradient(args.color, args.color2, cx, cy, radius, args.opacity)
    elif args.gradient == 'linear' and args.color2:
        paint = create_linear_gradient(args.color, args.color2, padding, padding, width - padding, height - padding, args.opacity)
    else:
        paint = create_solid_paint(args.color, args.opacity)

    # Draw arc using SVG path
    # Quarter circle from top to right
    start_x = cx
    start_y = cy - radius
    end_x = cx + radius
    end_y = cy

    path_str = f"M {start_x} {start_y} A {radius} {radius} 0 0 1 {end_x} {end_y}"
    path = pixie.parse_path(path_str)
    image.stroke_path(path, paint, pixie.Matrix3(), args.stroke)

    # Second arc (inner) if double style
    if args.style == 'double':
        inner_radius = radius * 0.7
        inner_start_x = cx
        inner_start_y = cy - inner_radius
        inner_end_x = cx + inner_radius
        inner_end_y = cy

        inner_path_str = f"M {inner_start_x} {inner_start_y} A {inner_radius} {inner_radius} 0 0 1 {inner_end_x} {inner_end_y}"
        inner_path = pixie.parse_path(inner_path_str)
        image.stroke_path(inner_path, paint, pixie.Matrix3(), args.stroke * 0.6)

    image.write_file(args.output)
    print(f"Generated: {args.output}")


def generate_frame_border(args):
    """Generate decorative frame border."""
    width = int(args.width or 400)
    height = int(args.height or 300)
    stroke = args.stroke
    padding = int(stroke * 2)
    corner_size = args.size or 40

    image = pixie.Image(width, height)

    paint = create_solid_paint(args.color, args.opacity)

    ctx = image.new_context()
    ctx.stroke_style = paint
    ctx.line_width = stroke
    ctx.line_cap = pixie.SQUARE_CAP
    ctx.line_join = pixie.MITER_JOIN

    # Top-left corner
    ctx.stroke_segment(padding, padding + corner_size, padding, padding)
    ctx.stroke_segment(padding, padding, padding + corner_size, padding)

    # Top-right corner
    ctx.stroke_segment(width - padding - corner_size, padding, width - padding, padding)
    ctx.stroke_segment(width - padding, padding, width - padding, padding + corner_size)

    # Bottom-right corner
    ctx.stroke_segment(width - padding, height - padding - corner_size, width - padding, height - padding)
    ctx.stroke_segment(width - padding, height - padding, width - padding - corner_size, height - padding)

    # Bottom-left corner
    ctx.stroke_segment(padding + corner_size, height - padding, padding, height - padding)
    ctx.stroke_segment(padding, height - padding, padding, height - padding - corner_size)

    image.write_file(args.output)
    print(f"Generated: {args.output}")


def generate_shape(args):
    """Generate basic geometric shapes."""
    size = args.size
    padding = 20

    width = int(args.width or size + padding * 2)
    height = int(args.height or size + padding * 2)

    image = pixie.Image(width, height)

    # Fill background if specified
    if args.bg:
        bg_paint = create_solid_paint(args.bg, 1.0)
        bg_path = pixie.Path()
        bg_path.rect(0, 0, width, height)
        image.fill_path(bg_path, bg_paint)

    # Create paint
    if args.gradient == 'linear' and args.color2:
        paint = create_linear_gradient(args.color, args.color2, padding, padding, width - padding, height - padding, args.opacity)
    elif args.gradient == 'radial' and args.color2:
        paint = create_radial_gradient(args.color, args.color2, width/2, height/2, size/2, args.opacity)
    else:
        paint = create_solid_paint(args.color, args.opacity)

    cx, cy = width / 2, height / 2
    radius = size / 2 - padding

    shape_type = args.style or 'circle'
    fill_mode = args.fill if hasattr(args, 'fill') and args.fill else False

    # Get number of sides for polygons
    sides = args.sides if hasattr(args, 'sides') and args.sides else 5

    path = pixie.Path()

    if shape_type == 'circle':
        path.ellipse(cx, cy, radius, radius)

    elif shape_type == 'ellipse':
        rx = radius
        ry = radius * 0.6
        path.ellipse(cx, cy, rx, ry)

    elif shape_type == 'rectangle' or shape_type == 'rect':
        x = padding
        y = padding + (height - 2*padding - size*0.6) / 2
        w = size
        h = size * 0.6
        path.rect(x, y, w, h)

    elif shape_type == 'square':
        x = cx - radius
        y = cy - radius
        path.rect(x, y, radius * 2, radius * 2)

    elif shape_type == 'rounded-rect' or shape_type == 'roundrect':
        x = padding
        y = padding + (height - 2*padding - size*0.6) / 2
        w = size
        h = size * 0.6
        r = min(w, h) * 0.15
        path.rounded_rect(x, y, w, h, r, r, r, r)

    elif shape_type == 'triangle':
        points = []
        for i in range(3):
            angle = (2 * math.pi / 3) * i - math.pi / 2
            px = cx + radius * math.cos(angle)
            py = cy + radius * math.sin(angle)
            points.append((px, py))
        path = pixie.parse_path(f"M {points[0][0]} {points[0][1]} L {points[1][0]} {points[1][1]} L {points[2][0]} {points[2][1]} Z")

    elif shape_type == 'polygon':
        points = []
        for i in range(sides):
            angle = (2 * math.pi / sides) * i - math.pi / 2
            px = cx + radius * math.cos(angle)
            py = cy + radius * math.sin(angle)
            points.append((px, py))
        path_str = f"M {points[0][0]} {points[0][1]}"
        for px, py in points[1:]:
            path_str += f" L {px} {py}"
        path_str += " Z"
        path = pixie.parse_path(path_str)

    elif shape_type == 'star':
        points = []
        outer_r = radius
        inner_r = radius * 0.4
        for i in range(sides * 2):
            angle = (math.pi / sides) * i - math.pi / 2
            r = outer_r if i % 2 == 0 else inner_r
            px = cx + r * math.cos(angle)
            py = cy + r * math.sin(angle)
            points.append((px, py))
        path_str = f"M {points[0][0]} {points[0][1]}"
        for px, py in points[1:]:
            path_str += f" L {px} {py}"
        path_str += " Z"
        path = pixie.parse_path(path_str)

    elif shape_type == 'diamond' or shape_type == 'rhombus':
        points = [(cx, cy - radius), (cx + radius * 0.7, cy), (cx, cy + radius), (cx - radius * 0.7, cy)]
        path = pixie.parse_path(f"M {points[0][0]} {points[0][1]} L {points[1][0]} {points[1][1]} L {points[2][0]} {points[2][1]} L {points[3][0]} {points[3][1]} Z")

    elif shape_type == 'ring' or shape_type == 'donut':
        # Outer circle
        path.ellipse(cx, cy, radius, radius)
        # Inner circle (creates hole when using even-odd fill)
        inner_r = radius * 0.5
        path.ellipse(cx, cy, inner_r, inner_r)

    elif shape_type == 'cross' or shape_type == 'plus':
        arm_width = radius * 0.35
        # Vertical arm
        path.rect(cx - arm_width, cy - radius, arm_width * 2, radius * 2)
        # Horizontal arm
        path.rect(cx - radius, cy - arm_width, radius * 2, arm_width * 2)

    elif shape_type == 'arrow-right' or shape_type == 'arrow':
        # Arrow pointing right
        shaft_h = radius * 0.4
        head_w = radius * 0.6
        shaft_w = radius * 1.4

        points = [
            (cx - radius, cy - shaft_h/2),  # shaft top-left
            (cx - radius + shaft_w, cy - shaft_h/2),  # shaft top-right
            (cx - radius + shaft_w, cy - radius * 0.5),  # head inner top
            (cx + radius, cy),  # head tip
            (cx - radius + shaft_w, cy + radius * 0.5),  # head inner bottom
            (cx - radius + shaft_w, cy + shaft_h/2),  # shaft bottom-right
            (cx - radius, cy + shaft_h/2),  # shaft bottom-left
        ]
        path_str = f"M {points[0][0]} {points[0][1]}"
        for px, py in points[1:]:
            path_str += f" L {px} {py}"
        path_str += " Z"
        path = pixie.parse_path(path_str)

    elif shape_type == 'arrow-up':
        shaft_w = radius * 0.4
        points = [
            (cx, cy - radius),  # tip
            (cx + radius * 0.5, cy - radius + radius * 0.6),  # head right
            (cx + shaft_w/2, cy - radius + radius * 0.6),  # inner right
            (cx + shaft_w/2, cy + radius),  # shaft bottom-right
            (cx - shaft_w/2, cy + radius),  # shaft bottom-left
            (cx - shaft_w/2, cy - radius + radius * 0.6),  # inner left
            (cx - radius * 0.5, cy - radius + radius * 0.6),  # head left
        ]
        path_str = f"M {points[0][0]} {points[0][1]}"
        for px, py in points[1:]:
            path_str += f" L {px} {py}"
        path_str += " Z"
        path = pixie.parse_path(path_str)

    elif shape_type == 'heart':
        # Heart shape using bezier curves
        scale = radius / 50
        # Move to bottom point, draw left curve, then right curve
        path_str = f"""
            M {cx} {cy + 40*scale}
            C {cx - 10*scale} {cy + 30*scale} {cx - 50*scale} {cy + 10*scale} {cx - 50*scale} {cy - 15*scale}
            C {cx - 50*scale} {cy - 40*scale} {cx - 25*scale} {cy - 50*scale} {cx} {cy - 25*scale}
            C {cx + 25*scale} {cy - 50*scale} {cx + 50*scale} {cy - 40*scale} {cx + 50*scale} {cy - 15*scale}
            C {cx + 50*scale} {cy + 10*scale} {cx + 10*scale} {cy + 30*scale} {cx} {cy + 40*scale}
            Z
        """
        path = pixie.parse_path(path_str)

    elif shape_type == 'hexagon':
        sides = 6
        points = []
        for i in range(sides):
            angle = (2 * math.pi / sides) * i - math.pi / 2
            px = cx + radius * math.cos(angle)
            py = cy + radius * math.sin(angle)
            points.append((px, py))
        path_str = f"M {points[0][0]} {points[0][1]}"
        for px, py in points[1:]:
            path_str += f" L {px} {py}"
        path_str += " Z"
        path = pixie.parse_path(path_str)

    elif shape_type == 'octagon':
        sides = 8
        points = []
        for i in range(sides):
            angle = (2 * math.pi / sides) * i - math.pi / 2 + math.pi / 8
            px = cx + radius * math.cos(angle)
            py = cy + radius * math.sin(angle)
            points.append((px, py))
        path_str = f"M {points[0][0]} {points[0][1]}"
        for px, py in points[1:]:
            path_str += f" L {px} {py}"
        path_str += " Z"
        path = pixie.parse_path(path_str)

    elif shape_type == 'crescent' or shape_type == 'moon':
        # Crescent moon
        path.ellipse(cx, cy, radius, radius)
        # Subtract circle offset to right
        path.ellipse(cx + radius * 0.4, cy, radius * 0.8, radius * 0.9)

    else:
        print(f"Unknown shape: {shape_type}")
        print("Available: circle, ellipse, rectangle, square, rounded-rect, triangle,")
        print("           polygon, star, diamond, ring, cross, arrow, arrow-up, heart,")
        print("           hexagon, octagon, crescent")
        return

    # Draw shape
    if fill_mode:
        image.fill_path(path, paint)
    else:
        image.stroke_path(path, paint, pixie.Matrix3(), args.stroke)

    image.write_file(args.output)
    print(f"Generated: {args.output}")


def generate_mandala(args):
    """Generate sacred geometry / mandala pattern."""
    size = args.size
    padding = 40

    width = int(args.width or size + padding * 2)
    height = int(args.height or size + padding * 2)

    image = pixie.Image(width, height)

    # Fill background if specified
    if args.bg:
        bg_paint = create_solid_paint(args.bg, 1.0)
        bg_path = pixie.Path()
        bg_path.rect(0, 0, width, height)
        image.fill_path(bg_path, bg_paint)

    paint = create_solid_paint(args.color, args.opacity)

    cx = width / 2
    cy = height / 2
    radius = size / 2 - padding

    ctx = image.new_context()
    ctx.stroke_style = paint
    ctx.line_width = args.stroke

    # Number of elements in the ring
    n_circles = int(args.rings) if hasattr(args, 'rings') and args.rings else 8
    n_polygons = int(args.layers) if hasattr(args, 'layers') and args.layers else 3

    # 1. Draw rotated polygons (squares/octagons)
    for i in range(n_polygons):
        poly_radius = radius * (0.95 - i * 0.15)
        rotation = math.pi / (n_polygons * 2) * i  # Offset each layer
        sides = 4 if i % 2 == 0 else 8  # Alternate between square and octagon

        points = []
        for j in range(sides):
            angle = (2 * math.pi / sides) * j + rotation
            px = cx + poly_radius * math.cos(angle)
            py = cy + poly_radius * math.sin(angle)
            points.append((px, py))

        # Draw polygon
        path_parts = [f"M {points[0][0]} {points[0][1]}"]
        for px, py in points[1:]:
            path_parts.append(f"L {px} {py}")
        path_parts.append("Z")
        path_str = " ".join(path_parts)
        path = pixie.parse_path(path_str)
        image.stroke_path(path, paint, pixie.Matrix3(), args.stroke)

    # 2. Draw circles arranged in a ring
    circle_radius = radius * 0.18
    ring_radius = radius * 0.55

    circle_centers = []
    for i in range(n_circles):
        angle = (2 * math.pi / n_circles) * i - math.pi / 2
        circle_cx = cx + ring_radius * math.cos(angle)
        circle_cy = cy + ring_radius * math.sin(angle)
        circle_centers.append((circle_cx, circle_cy))

        # Draw circle
        circle_path = pixie.Path()
        circle_path.ellipse(circle_cx, circle_cy, circle_radius, circle_radius)
        image.stroke_path(circle_path, paint, pixie.Matrix3(), args.stroke)

    # 3. Draw connecting lines between circle centers
    for i in range(n_circles):
        # Connect to next circle
        next_i = (i + 1) % n_circles
        ctx.stroke_segment(
            circle_centers[i][0], circle_centers[i][1],
            circle_centers[next_i][0], circle_centers[next_i][1]
        )

        # Connect to center
        ctx.stroke_segment(cx, cy, circle_centers[i][0], circle_centers[i][1])

        # Connect to opposite circle (creates star pattern)
        if n_circles >= 6:
            opposite_i = (i + n_circles // 2) % n_circles
            ctx.stroke_segment(
                circle_centers[i][0], circle_centers[i][1],
                circle_centers[opposite_i][0], circle_centers[opposite_i][1]
            )

    # 4. Draw central triangle
    triangle_radius = radius * 0.25
    triangle_points = []
    for i in range(3):
        angle = (2 * math.pi / 3) * i - math.pi / 2
        px = cx + triangle_radius * math.cos(angle)
        py = cy + triangle_radius * math.sin(angle)
        triangle_points.append((px, py))

    tri_path_str = f"M {triangle_points[0][0]} {triangle_points[0][1]} L {triangle_points[1][0]} {triangle_points[1][1]} L {triangle_points[2][0]} {triangle_points[2][1]} Z"
    tri_path = pixie.parse_path(tri_path_str)
    image.stroke_path(tri_path, paint, pixie.Matrix3(), args.stroke)

    # 5. Draw center circle
    center_circle = pixie.Path()
    center_circle.ellipse(cx, cy, radius * 0.08, radius * 0.08)
    image.stroke_path(center_circle, paint, pixie.Matrix3(), args.stroke)

    # 6. Draw outer circle
    outer_circle = pixie.Path()
    outer_circle.ellipse(cx, cy, radius, radius)
    image.stroke_path(outer_circle, paint, pixie.Matrix3(), args.stroke * 0.7)

    image.write_file(args.output)
    print(f"Generated: {args.output}")


def generate_pattern(args):
    """Generate repeating geometric pattern."""
    width = int(args.width or 400)
    height = int(args.height or 400)
    cell_size = args.size or 50

    image = pixie.Image(width, height)

    paint = create_solid_paint(args.color, args.opacity)

    ctx = image.new_context()
    ctx.stroke_style = paint
    ctx.line_width = args.stroke

    pattern_type = args.style or 'dots'

    for x in range(0, width, cell_size):
        for y in range(0, height, cell_size):
            cx = x + cell_size / 2
            cy = y + cell_size / 2

            if pattern_type == 'dots':
                path = pixie.Path()
                path.ellipse(cx, cy, args.stroke * 2, args.stroke * 2)
                image.fill_path(path, paint)

            elif pattern_type == 'crosses':
                size = cell_size * 0.3
                ctx.stroke_segment(cx - size, cy, cx + size, cy)
                ctx.stroke_segment(cx, cy - size, cx, cy + size)

            elif pattern_type == 'diamonds':
                size = cell_size * 0.25
                path_str = f"M {cx} {cy - size} L {cx + size} {cy} L {cx} {cy + size} L {cx - size} {cy} Z"
                path = pixie.parse_path(path_str)
                image.stroke_path(path, paint, pixie.Matrix3(), args.stroke)

    image.write_file(args.output)
    print(f"Generated: {args.output}")


def main():
    parser = argparse.ArgumentParser(description='Generate geometric decorative elements')
    subparsers = parser.add_subparsers(dest='command', help='Element type')

    # Common arguments for all commands
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('--color', default='#D4A84B', help='Primary color (hex)')
    common.add_argument('--color2', help='Secondary color for gradient')
    common.add_argument('--size', type=int, default=200, help='Element size in pixels')
    common.add_argument('--width', type=int, help='Canvas width')
    common.add_argument('--height', type=int, help='Canvas height')
    common.add_argument('--stroke', type=float, default=4, help='Stroke width')
    common.add_argument('--output', '-o', default='output.png', help='Output file path')
    common.add_argument('--gradient', choices=['linear', 'radial'], help='Gradient type')
    common.add_argument('--opacity', type=float, default=1.0, help='Opacity 0.0-1.0')
    common.add_argument('--style', help='Style variant')
    common.add_argument('--bg', help='Background color (hex)')
    common.add_argument('--rings', type=int, default=8, help='Number of circles in ring (mandala)')
    common.add_argument('--layers', type=int, default=3, help='Number of polygon layers (mandala)')
    common.add_argument('--fill', action='store_true', help='Fill shape instead of stroke')
    common.add_argument('--sides', type=int, default=5, help='Number of sides (polygon/star)')

    # Subcommands
    subparsers.add_parser('corner-accent', parents=[common], help='L-shaped corner accent')
    subparsers.add_parser('line-divider', parents=[common], help='Horizontal line divider')
    subparsers.add_parser('arc-accent', parents=[common], help='Curved arc accent')
    subparsers.add_parser('frame-border', parents=[common], help='Decorative frame border')
    subparsers.add_parser('pattern', parents=[common], help='Repeating geometric pattern')
    subparsers.add_parser('mandala', parents=[common], help='Sacred geometry / mandala pattern')
    subparsers.add_parser('shape', parents=[common], help='Basic geometric shapes')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Ensure output directory exists
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    # Generate element
    generators = {
        'corner-accent': generate_corner_accent,
        'line-divider': generate_line_divider,
        'arc-accent': generate_arc_accent,
        'frame-border': generate_frame_border,
        'pattern': generate_pattern,
        'mandala': generate_mandala,
        'shape': generate_shape,
    }

    generators[args.command](args)


if __name__ == '__main__':
    main()
