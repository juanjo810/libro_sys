# Session 8. Counters

This session uses flip-flops to build counters and analyze state transitions. The route goes from a concrete counter to arbitrary-sequence design.

```{admonition} Learning objectives
:class: tip

- Program counters with clock and count mode.
- Recognize transient states in asynchronous counters.
- Design arbitrary-sequence counters through state transitions.
```

## 1. Up/down counter

Program the four-bit counter in {numref}`fig-verilog-en-08-contador`. Use a four-bit variable for the output and test both up and down counting.

```{figure} ../../_static/verilog/sesion_08/contador.png
---
name: fig-verilog-en-08-contador
alt: Counter with up/down count selection.
width: 85%
align: center
---
Counter with up/down count selection.
```

## 2. Control mode changes with HOLD

Change the count mode in the middle of the sequence and observe the jumps. Then add active-low PRESET, CLEAR, and HOLD to freeze the state before changing direction.

## 3. Analyze an asynchronous 10-to-0 counter

Build the counter in {numref}`fig-verilog-en-08-10a0` and observe why the count can pass through transient states. This prepares the formal analysis in {numref}`fig-verilog-en-08-analisis`.

```{figure} ../../_static/verilog/sesion_08/10a0.png
---
name: fig-verilog-en-08-10a0
alt: 10-to-0 counter.
width: 85%
align: center
---
10-to-0 counter.
```

```{figure} ../../_static/verilog/sesion_08/analisis.png
---
name: fig-verilog-en-08-analisis
alt: State and transition analysis.
width: 85%
align: center
---
State and transition analysis.
```

## 4. Compare with a synchronous counter

Repeat the simulation with the synchronous counter in {numref}`fig-verilog-en-08-contsinc`. Compare when outputs change in each design.

```{figure} ../../_static/verilog/sesion_08/contsinc.png
---
name: fig-verilog-en-08-contsinc
alt: Synchronous counter.
width: 85%
align: center
---
Synchronous counter.
```

## 5. Design an arbitrary count

First draw the transition diagram, as in {numref}`fig-verilog-en-08-cont01`. Then use the JK transition table in {numref}`fig-verilog-en-08-transjk`, fill transitions as in {numref}`fig-verilog-en-08-transis`, and simplify with Karnaugh maps like {numref}`fig-verilog-en-08-jkarn`.

```{figure} ../../_static/verilog/sesion_08/cont01.png
---
name: fig-verilog-en-08-cont01
alt: Auxiliary counter circuit.
width: 85%
align: center
---
Auxiliary counter circuit.
```

```{figure} ../../_static/verilog/sesion_08/transJK.png
---
name: fig-verilog-en-08-transjk
alt: JK flip-flop transitions.
width: 85%
align: center
---
JK flip-flop transitions.
```

```{figure} ../../_static/verilog/sesion_08/transis.png
---
name: fig-verilog-en-08-transis
alt: State transition diagram.
width: 85%
align: center
---
State transition diagram.
```

```{figure} ../../_static/verilog/sesion_08/jkarn.png
---
name: fig-verilog-en-08-jkarn
alt: Karnaugh map for JK inputs.
width: 85%
align: center
---
Karnaugh map for JK inputs.
```

## 6. Build and test the final counter

With the simplified equations, assemble the arbitrary-sequence counter. {numref}`fig-verilog-en-08-contarb` shows the final form. Test it in Verilog and check that it follows the intended sequence.

```{figure} ../../_static/verilog/sesion_08/contarb.png
---
name: fig-verilog-en-08-contarb
alt: Arbitrary-sequence counter.
width: 85%
align: center
---
Arbitrary-sequence counter.
```

## Closing checkpoint

Before moving to the next session, save the Verilog file for each exercise and write down what you expected and what the simulation actually printed. That comparison is the quickest way to find mistakes.

## Original Source

Content written and expanded from the class presentation and reference page: <http://avellano.usal.es/~compi/sesion8.htm>.
