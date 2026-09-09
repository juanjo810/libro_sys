# Session 7. Registers

This session builds registers from flip-flops and introduces an essential debugging tool: waveforms with GTKWave.

```{admonition} Learning objectives
:class: tip

- Build SISO and SIPO registers from flip-flops.
- Generate waveform files with `$dumpfile` and `$dumpvars`.
- Use timing traces to debug sequential circuits.
```

## 1. Start from a D flip-flop

Begin with the D flip-flop in {numref}`fig-verilog-en-07-d`. Check that the output updates only when the clock allows it.

```{figure} ../../_static/verilog/sesion_07/d.png
---
name: fig-verilog-en-07-d
alt: D flip-flop.
width: 85%
align: center
---
D flip-flop.
```

## 2. Chain flip-flops: SISO register

Connect several flip-flops to form a serial-in, serial-out register. {numref}`fig-verilog-en-07-siso` shows how information shifts from one stage to the next.

```{figure} ../../_static/verilog/sesion_07/siso.png
---
name: fig-verilog-en-07-siso
alt: SISO register.
width: 85%
align: center
---
SISO register.
```

## 3. Debug with GTKWave

Before continuing, add `$dumpfile` and `$dumpvars` to the test module. {numref}`fig-verilog-en-07-gtkwave` shows the waveform style you should obtain.

```{figure} ../../_static/verilog/sesion_07/gtkwave.png
---
name: fig-verilog-en-07-gtkwave
alt: Signal waveform viewed with GTKWave.
width: 85%
align: center
---
Signal waveform viewed with GTKWave.
```

## 4. Change the output: SIPO register

Keep the serial input but expose the content in parallel. Use {numref}`fig-verilog-en-07-sipo` to distinguish input, clock, and parallel outputs.

```{figure} ../../_static/verilog/sesion_07/sipo.png
---
name: fig-verilog-en-07-sipo
alt: SIPO register.
width: 85%
align: center
---
SIPO register.
```

## 5. Combine registers and adders

The final exercise chains input registers, an adder, and an output register. {numref}`fig-verilog-en-07-pisiso` helps organize the parallel-to-serial and serial-to-parallel conversion.

```{figure} ../../_static/verilog/sesion_07/pisiso.png
---
name: fig-verilog-en-07-pisiso
alt: Register structure with parallel-serial and serial-parallel conversion.
width: 85%
align: center
---
Register structure with parallel-serial and serial-parallel conversion.
```

## Closing checkpoint

Before moving to the next session, save the Verilog file for each exercise and write down what you expected and what the simulation actually printed. That comparison is the quickest way to find mistakes.

## Original Source

Content written and expanded from the class presentation and reference page: <http://avellano.usal.es/~compi/sesion7.htm>.
