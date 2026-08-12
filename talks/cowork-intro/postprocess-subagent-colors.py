#!/usr/bin/env python3
"""Post-proceso del render html-strict de clase2 (pedido del presentador, 2026-08-12):
en la lamina "Un subagente propio, por dentro", cada campo del frontmatter del ejemplo
lleva un color distinto (name rojo, description azul, tools verde) para identificarlos
al leer. Correr DESPUES de cada build_html.py; es idempotente."""
import sys
from pathlib import Path

P = Path(__file__).parent / "output" / "html" / "index.html"
s = P.read_text()
if 'data-subagent-colors="1"' in s:
    print("ya aplicado")
    sys.exit(0)

pairs = [
    ("name: revisor-de-seguridad",
     '<span style="color:#DA1B2E" data-subagent-colors="1">name: revisor-de-seguridad</span>'),
    ("description: Revisa un diff buscando secretos, credenciales y datos",
     '<span style="color:#005CC5">description: Revisa un diff buscando secretos, credenciales y datos</span>'),
    ("  sensibles. Usar antes de cada commit importante.",
     '<span style="color:#005CC5">  sensibles. Usar antes de cada commit importante.</span>'),
    ("tools: Read, Grep, Glob",
     '<span style="color:#1a7f37">tools: Read, Grep, Glob</span>'),
]
missing = [a for a, _ in pairs if a not in s]
if missing:
    print("no encontrado en el HTML (¿cambio el ejemplo?):", missing)
    sys.exit(1)
for a, b in pairs:
    s = s.replace(a, b, 1)
P.write_text(s)
print("colores aplicados")
