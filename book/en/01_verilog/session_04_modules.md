# Session 4. Modules

This session turns the gates from the previous session into reusable blocks. The route is progressive: interface, comparator, hierarchy, ports, and extension exercises.

```{admonition} Learning objectives
:class: tip

- Define modules with `input`, `output`, and `inout`.
- Build hierarchical circuits from small modules.
- Prepare test modules that verify every input combination.
```

## 1. Understand the module as a box

A module has a name and an interface. Before writing internal gates, draw which signals enter and which signals leave. {numref}`fig-verilog-en-04-modulo` summarizes this idea.

```{figure} ../../_static/verilog/sesion_04/mOdulo.png
---
name: fig-verilog-en-04-modulo
alt: General diagram of a module with ports.
width: 80%
align: center
---
General diagram of a module with ports.
```

## 2. Build a one-bit comparator

Identify inputs and outputs in {numref}`fig-verilog-en-04-compar1`; then implement the internal circuit shown in {numref}`fig-verilog-en-04-compar11`.

```{figure} ../../_static/verilog/sesion_04/compar1.png
---
name: fig-verilog-en-04-compar1
alt: One-bit comparator.
width: 80%
align: center
---
One-bit comparator.
```

```{figure} ../../_static/verilog/sesion_04/compar11.png
---
name: fig-verilog-en-04-compar11
alt: Internal implementation of the one-bit comparator.
width: 85%
align: center
---
Internal implementation of the one-bit comparator.
```

## 3. Verify with a test module

Do not accept the comparator until all input combinations have been checked. {numref}`fig-verilog-en-04-testcomp1` shows the testing-module idea.

```{figure} ../../_static/verilog/sesion_04/TestComp1.png
---
name: fig-verilog-en-04-testcomp1
alt: Comparator test module.
width: 85%
align: center
---
Comparator test module.
```

## 4. Move up one level

Use the working one-bit comparator as a building block for a two-bit comparator. {numref}`fig-verilog-en-04-comp2` shows how several instances cooperate inside a larger module.

```{figure} ../../_static/verilog/sesion_04/comp2.png
---
name: fig-verilog-en-04-comp2
alt: Two-bit comparator built hierarchically.
width: 85%
align: center
---
Two-bit comparator built hierarchically.
```

## 5. Ports, priority, and larger gates

Practice leaving unused ports visibly disconnected. Then move to the priority encoder in {numref}`fig-verilog-en-04-priocod` and the four-input gate in {numref}`fig-verilog-en-04-and4`.

```{figure} ../../_static/verilog/sesion_04/priocod.png
---
name: fig-verilog-en-04-priocod
alt: Priority encoder.
width: 85%
align: center
---
Priority encoder.
```

```{figure} ../../_static/verilog/sesion_04/and4.png
---
name: fig-verilog-en-04-and4
alt: Four-input AND gate.
width: 70%
align: center
---
Four-input AND gate.
```

## Closing checkpoint

Before moving to the next session, save the Verilog file for each exercise and write down what you expected and what the simulation actually printed. That comparison is the quickest way to find mistakes.

## Original Source

Content written and expanded from the class presentation and reference page: <http://avellano.usal.es/~compi/sesion4.htm>.
