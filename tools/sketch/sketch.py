"""Trazo "a mano" para SVG: líneas temblorosas con doble pasada, estilo birome."""
import math
import random

INK = "#2b2b2b"


def _smooth(pts, closed=False):
    """Catmull-Rom → Bézier cúbicas, para que el temblor quede curvo y no quebrado."""
    if closed:
        pts = pts[-1:] + pts + pts[:2]
    else:
        pts = pts[:1] + pts + pts[-1:]
    d = f"M{pts[1][0]:.1f},{pts[1][1]:.1f}"
    for i in range(1, len(pts) - 2):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[i + 1], pts[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d


def _jitter(pts, amp, rnd):
    return [(x + rnd.uniform(-amp, amp), y + rnd.uniform(-amp, amp)) for x, y in pts]


def stroke(pts, rnd, amp=1.6, width=2.2, passes=2, closed=False, color=INK):
    """Una línea a mano: cada pasada tiembla distinto, como repasar con birome."""
    out = []
    for k in range(passes):
        w = width * (1 if k == 0 else 0.7)
        op = 0.95 if k == 0 else 0.55
        out.append(f'<path d="{_smooth(_jitter(pts, amp, rnd), closed)}" fill="none" stroke="{color}" '
                   f'stroke-width="{w:.2f}" stroke-linecap="round" stroke-linejoin="round" opacity="{op}"/>')
    return "\n".join(out)


def ellipse_pts(cx, cy, rx, ry, rot_deg, n=26, wobble=0.04, rnd=None, overshoot=0.12):
    """Óvalo dibujado de un trazo: no cierra perfecto, se pasa un poco del punto de inicio."""
    rot = math.radians(rot_deg)
    start = rnd.uniform(0, 2 * math.pi)
    pts = []
    total = 2 * math.pi * (1 + overshoot)
    for i in range(n + 1):
        t = start + total * i / n
        r = 1 + rnd.uniform(-wobble, wobble)
        x, y = rx * r * math.cos(t), ry * r * math.sin(t)
        pts.append((cx + x * math.cos(rot) - y * math.sin(rot), cy + x * math.sin(rot) + y * math.cos(rot)))
    return pts


def rotate(pts, cx, cy, deg):
    a = math.radians(deg)
    return [(cx + (x - cx) * math.cos(a) - (y - cy) * math.sin(a),
             cy + (x - cx) * math.sin(a) + (y - cy) * math.cos(a)) for x, y in pts]
