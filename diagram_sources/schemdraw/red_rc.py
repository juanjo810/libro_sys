"""Red RC de la sesion 4: entrada v0(t), salida vs(t) en el condensador.

Genera book/_static/generated/red_rc.png y .svg. Ejecutar desde la raiz:
    python diagram_sources/schemdraw/red_rc.py
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "book" / "_static" / "generated"
OUT_DIR.mkdir(parents=True, exist_ok=True)

with schemdraw.Drawing(show=False) as d:
    d.config(unit=3, fontsize=13)
    # Terminales de entrada
    top_in = d.add(elm.Dot(open=True))
    d.add(elm.Line().right(0.8))
    d.add(elm.Resistor().right().label("$R$"))
    node_top = d.add(elm.Dot())
    d.add(elm.Line().right(1.2))
    top_out = d.add(elm.Dot(open=True))
    # Condensador en paralelo con la salida
    d.add(elm.Capacitor().down().at(node_top.start).label("$C$", loc="bottom"))
    node_bot = d.add(elm.Dot())
    # Linea inferior
    d.add(elm.Line().left().to((top_in.start[0], node_bot.start[1])))
    bot_in = d.add(elm.Dot(open=True))
    d.add(elm.Line().right().at(node_bot.start).to((top_out.start[0], node_bot.start[1])))
    bot_out = d.add(elm.Dot(open=True))
    # Tensiones de entrada y salida
    d.add(elm.Gap().at(bot_in.start).to(top_in.start).label(["$-$", "$v_0(t)$", "$+$"]))
    d.add(elm.Gap().at(bot_out.start).to(top_out.start).label(["$-$", "$v_s(t)$", "$+$"]))
    # Corriente
    d.add(elm.Arrow().at((top_in.start[0] + 0.1, top_in.start[1] + 0.45)).to((top_in.start[0] + 0.7, top_in.start[1] + 0.45)).label("$i(t)$", loc="top"))

    d.save(str(OUT_DIR / "red_rc.png"), dpi=200)
    d.save(str(OUT_DIR / "red_rc.svg"))

print("Generado:", OUT_DIR / "red_rc.png", "y .svg")
