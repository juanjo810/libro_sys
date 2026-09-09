# Session 3. Logic Gates

This session moves from bit operators to logic gates instantiated as hardware elements. Each figure appears at the point where it is needed.

```{admonition} Learning objectives
:class: tip

- Instantiate Verilog primitive gates by listing output first and then inputs.
- Check truth tables with `0`, `1`, `x`, and `z`.
- Build combinational functions by connecting gates.
```

## 1. Start with the AND gate

The first gate is written by identifying its output and inputs. {numref}`fig-verilog-en-03-and` shows the gate and {numref}`fig-verilog-en-03-andvar` connects it to the signal names used in the module.

```{figure} ../../_static/verilog/sesion_03/and.png
---
name: fig-verilog-en-03-and
alt: Basic AND gate.
width: 75%
align: center
---
Basic AND gate.
```

```{figure} ../../_static/verilog/sesion_03/andvar.png
---
name: fig-verilog-en-03-andvar
alt: Verilog instantiation of an AND gate.
width: 75%
align: center
---
Verilog instantiation of an AND gate.
```

## 2. Repeat the pattern with other gates

Use the same method for OR, NOT, NAND, NOR, XOR, XNOR, and BUFFER: inspect the figure, write the module, run the truth table, and compare.

```{figure} ../../_static/verilog/sesion_03/or.png
---
name: fig-verilog-en-03-or
alt: OR gate and its conceptual connection.
width: 70%
align: center
---
OR gate and its conceptual connection.
```

```{figure} ../../_static/verilog/sesion_03/not.png
---
name: fig-verilog-en-03-not
alt: NOT gate.
width: 70%
align: center
---
NOT gate.
```

```{figure} ../../_static/verilog/sesion_03/nand.png
---
name: fig-verilog-en-03-nand
alt: NAND gate.
width: 70%
align: center
---
NAND gate.
```

```{figure} ../../_static/verilog/sesion_03/nor.png
---
name: fig-verilog-en-03-nor
alt: NOR gate.
width: 70%
align: center
---
NOR gate.
```

```{figure} ../../_static/verilog/sesion_03/xor.png
---
name: fig-verilog-en-03-xor
alt: XOR gate.
width: 70%
align: center
---
XOR gate.
```

```{figure} ../../_static/verilog/sesion_03/xnor.png
---
name: fig-verilog-en-03-xnor
alt: XNOR gate.
width: 70%
align: center
---
XNOR gate.
```

```{figure} ../../_static/verilog/sesion_03/buf.png
---
name: fig-verilog-en-03-buf
alt: BUFFER gate.
width: 70%
align: center
---
BUFFER gate.
```

## 3. Interconnect gates

Use intermediate wires to connect gate outputs to other gate inputs and build the function in {numref}`fig-verilog-en-03-f2`. {numref}`fig-verilog-en-03-f2var` shows auxiliary variables and {numref}`fig-verilog-en-03-tablaf2` is the truth-table check.

```{figure} ../../_static/verilog/sesion_03/f2.png
---
name: fig-verilog-en-03-f2
alt: Combinational logic function f2.
width: 85%
align: center
---
Combinational logic function f2.
```

```{figure} ../../_static/verilog/sesion_03/f2var.png
---
name: fig-verilog-en-03-f2var
alt: Auxiliary variables for function f2.
width: 85%
align: center
---
Auxiliary variables for function f2.
```

```{figure} ../../_static/verilog/sesion_03/tablaf2.png
---
name: fig-verilog-en-03-tablaf2
alt: Truth table for f2.
width: 85%
align: center
---
Truth table for f2.
```

## 4. Use operators and finish with NAND

Compare gates with relational and logical operators. Then implement the function in {numref}`fig-verilog-en-03-f3for`, first as in {numref}`fig-verilog-en-03-f3` and then using only NAND gates as in {numref}`fig-verilog-en-03-f3nand`.

```{figure} ../../_static/verilog/sesion_03/f3for.png
---
name: fig-verilog-en-03-f3for
alt: Algebraic form of function f3.
width: 85%
align: center
---
Algebraic form of function f3.
```

```{figure} ../../_static/verilog/sesion_03/f3.png
---
name: fig-verilog-en-03-f3
alt: Gate implementation of f3.
width: 85%
align: center
---
Gate implementation of f3.
```

```{figure} ../../_static/verilog/sesion_03/f3nand.png
---
name: fig-verilog-en-03-f3nand
alt: Equivalent implementation using NAND gates.
width: 85%
align: center
---
Equivalent implementation using NAND gates.
```

## Closing checkpoint

Before moving to the next session, save the Verilog file for each exercise and write down what you expected and what the simulation actually printed. That comparison is the quickest way to find mistakes.

## Original Source

Content written and expanded from the class presentation and reference page: <http://avellano.usal.es/~compi/sesion3.htm>.
