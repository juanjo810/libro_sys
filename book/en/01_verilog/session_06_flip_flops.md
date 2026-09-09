# Session 6. Flip-Flops

This session moves from combinational logic to memory. The route is to build a flip-flop, observe timing, add a clock, and finish with behavioral models.

```{admonition} Learning objectives
:class: tip

- Build RS and JK flip-flops.
- Distinguish blocking and non-blocking assignments.
- Use `always`, clocks, edges, loops, and `case` in sequential circuits.
```

## 1. Build the RS flip-flop

Start with the RS flip-flop in {numref}`fig-verilog-en-06-rs`. Program the circuit and check its behavior with {numref}`fig-verilog-en-06-rstabla`.

```{figure} ../../_static/verilog/sesion_06/rs.png
---
name: fig-verilog-en-06-rs
alt: RS flip-flop built with NOR gates.
width: 85%
align: center
---
RS flip-flop built with NOR gates.
```

```{figure} ../../_static/verilog/sesion_06/rstabla.png
---
name: fig-verilog-en-06-rstabla
alt: RS flip-flop behavior table.
width: 85%
align: center
---
RS flip-flop behavior table.
```

## 2. Compare assignments

Replace some blocking assignments with non-blocking assignments and observe when the output changes. Timing is part of the simulated circuit.

## 3. Add a level-controlled clock

Now control the RS flip-flop with a clock. {numref}`fig-verilog-en-06-rsc` shows the circuit and {numref}`fig-verilog-en-06-rsctabla` shows when it should respond.

```{figure} ../../_static/verilog/sesion_06/rsc.png
---
name: fig-verilog-en-06-rsc
alt: Clocked RS flip-flop.
width: 85%
align: center
---
Clocked RS flip-flop.
```

```{figure} ../../_static/verilog/sesion_06/rsctabla.png
---
name: fig-verilog-en-06-rsctabla
alt: Clocked RS flip-flop table.
width: 85%
align: center
---
Clocked RS flip-flop table.
```

## 4. Move to edges and JK

Use the edge detector in {numref}`fig-verilog-en-06-det` so the change happens at a specific instant. Then implement the JK flip-flop in {numref}`fig-verilog-en-06-jk` and check its cases with {numref}`fig-verilog-en-06-jktabla`.

```{figure} ../../_static/verilog/sesion_06/det.png
---
name: fig-verilog-en-06-det
alt: Edge detector.
width: 85%
align: center
---
Edge detector.
```

```{figure} ../../_static/verilog/sesion_06/jk.png
---
name: fig-verilog-en-06-jk
alt: JK flip-flop with control inputs.
width: 85%
align: center
---
JK flip-flop with control inputs.
```

```{figure} ../../_static/verilog/sesion_06/jktabla.png
---
name: fig-verilog-en-06-jktabla
alt: JK flip-flop behavior table.
width: 85%
align: center
---
JK flip-flop behavior table.
```

## 5. Write sequential behavior

Close the session with loops, `case` instructions, and conditional `always` blocks. Compare a structural circuit with a behavioral model and note when each style is clearer.

## Closing checkpoint

Before moving to the next session, save the Verilog file for each exercise and write down what you expected and what the simulation actually printed. That comparison is the quickest way to find mistakes.

## Original Source

Content written and expanded from the class presentation and reference page: <http://avellano.usal.es/~compi/sesion6.htm>.
