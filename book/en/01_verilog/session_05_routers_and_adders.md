# Session 5. Routers and Adders

This session works with buses, tri-state buffers, multiplexers, and adders. The connecting thread is controlling where a signal flows and how carry propagates.

```{admonition} Learning objectives
:class: tip

- Use tri-state buffers and net types to share buses.
- Build multiplexers from smaller blocks.
- Implement adders and reason about propagation delays.
```

## 1. Tri-state buffers

Start with `bufif1` and `bufif0`. {numref}`fig-verilog-en-05-bufif1` and {numref}`fig-verilog-en-05-bufif0` show the difference between active-high and active-low enable.

```{figure} ../../_static/verilog/sesion_05/bufif1.png
---
name: fig-verilog-en-05-bufif1
alt: Active-high tri-state buffer.
width: 75%
align: center
---
Active-high tri-state buffer.
```

```{figure} ../../_static/verilog/sesion_05/bufif0.png
---
name: fig-verilog-en-05-bufif0
alt: Active-low tri-state buffer.
width: 75%
align: center
---
Active-low tri-state buffer.
```

## 2. Share a bus without contention

When several outputs reach one wire, signal contention appears. Build the transceiver in {numref}`fig-verilog-en-05-trans`, name signals as in {numref}`fig-verilog-en-05-transnombres`, and verify it with {numref}`fig-verilog-en-05-transtest`.

```{figure} ../../_static/verilog/sesion_05/trans.png
---
name: fig-verilog-en-05-trans
alt: One-bit bus transceiver.
width: 85%
align: center
---
One-bit bus transceiver.
```

```{figure} ../../_static/verilog/sesion_05/transNombres.png
---
name: fig-verilog-en-05-transnombres
alt: Auxiliary signal names in the transceiver.
width: 85%
align: center
---
Auxiliary signal names in the transceiver.
```

```{figure} ../../_static/verilog/sesion_05/transTest.png
---
name: fig-verilog-en-05-transtest
alt: Transceiver test module.
width: 85%
align: center
---
Transceiver test module.
```

## 3. Assign signals and build multiplexers

Use `assign` for continuous connections. Then build small multiplexers and combine them into the 8-to-1 multiplexer in {numref}`fig-verilog-en-05-mux8x1`; {numref}`fig-verilog-en-05-h4` helps organize selection signals.

```{figure} ../../_static/verilog/sesion_05/mux8x1.png
---
name: fig-verilog-en-05-mux8x1
alt: 8-to-1 multiplexer built from smaller multiplexers.
width: 85%
align: center
---
8-to-1 multiplexer built from smaller multiplexers.
```

```{figure} ../../_static/verilog/sesion_05/h4.png
---
name: fig-verilog-en-05-h4
alt: Auxiliary structure for signal selection.
width: 85%
align: center
---
Auxiliary structure for signal selection.
```

## 4. From half adder to full adder

Implement the half adder in {numref}`fig-verilog-en-05-semisuma`, then add carry-in to obtain the full adder in {numref}`fig-verilog-en-05-sumador1`.

```{figure} ../../_static/verilog/sesion_05/semisuma.png
---
name: fig-verilog-en-05-semisuma
alt: Half adder.
width: 85%
align: center
---
Half adder.
```

```{figure} ../../_static/verilog/sesion_05/sumador1.png
---
name: fig-verilog-en-05-sumador1
alt: One-bit full adder.
width: 85%
align: center
---
One-bit full adder.
```

## 5. Stop, delay, and measure

Use `$finish` to stop the simulation at the right time. Then add delays and estimate how long a four-bit ripple-carry adder such as {numref}`fig-verilog-en-05-propaga4` needs to settle. Compare it with the carry-lookahead option in {numref}`fig-verilog-en-05-anticipa`.

```{figure} ../../_static/verilog/sesion_05/propaga4.png
---
name: fig-verilog-en-05-propaga4
alt: Four-bit ripple-carry adder.
width: 85%
align: center
---
Four-bit ripple-carry adder.
```

```{figure} ../../_static/verilog/sesion_05/anticipa.png
---
name: fig-verilog-en-05-anticipa
alt: Carry-lookahead adder.
width: 85%
align: center
---
Carry-lookahead adder.
```

## Closing checkpoint

Before moving to the next session, save the Verilog file for each exercise and write down what you expected and what the simulation actually printed. That comparison is the quickest way to find mistakes.

## Original Source

Content written and expanded from the class presentation and reference page: <http://avellano.usal.es/~compi/sesion5.htm>.
