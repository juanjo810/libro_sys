# Session 9. ALU

The final session applies modular work to a 74181 ALU. The route is short but integrative: include an external file, study the interface, and chain operations.

```{admonition} Learning objectives
:class: tip

- Use `` `include `` to add an external Verilog module.
- Prepare tests for arithmetic and logic operations in the 74181 ALU.
- Store intermediate results when an operation requires several steps.
```

## 1. Include source files

Verilog can insert another file with `` `include ``. In this session it is used to bring in `74181.v` without copying its contents into the test file.

```verilog
`include "74181.v"
```

## 2. Read the ALU interface

Before testing operations, inspect the module header and locate inputs, outputs, selection lines, and negated carry lines. {numref}`fig-verilog-en-09-74181` shows the ALU diagram.

```{figure} ../../_static/verilog/sesion_09/74181.png
---
name: fig-verilog-en-09-74181
alt: Diagram of the 74181 integrated circuit.
width: 85%
align: center
---
Diagram of the 74181 integrated circuit.
```

## 3. Choose operations from the table

Use {numref}`fig-verilog-en-09-74181t` to find the combinations needed for additions, logic operations, and compound operations.

```{figure} ../../_static/verilog/sesion_09/74181t.png
---
name: fig-verilog-en-09-74181t
alt: Operation table for the 74181 integrated circuit.
width: 85%
align: center
---
Operation table for the 74181 integrated circuit.
```

## 4. Test simple operations

Write a test module for `7+4`, `2+6+1`, AND, XOR, and OR combined with negations. Print inputs, selection, and output in each case.

## 5. Chain compound operations

For `2*7` and `3*5+1`, store intermediate results in registers. Every step should correspond to a concrete ALU configuration.

## Closing checkpoint

Before moving to the next session, save the Verilog file for each exercise and write down what you expected and what the simulation actually printed. That comparison is the quickest way to find mistakes.

## Original Source

Content written and expanded from the class presentation and reference page: <http://avellano.usal.es/~compi/sesion9.htm>.
