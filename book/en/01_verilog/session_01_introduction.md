# Session 1. Introduction to Verilog

This session follows the order of the original page: first Verilog is introduced, then the environment is prepared, and only then do we write small programs to check formats, registers, operations, and wires.

```{admonition} Learning objectives
:class: tip

- Understand Verilog as a hardware description language.
- Create, compile, and run a first `.v` file.
- Use constants, registers, wires, and `$display` to check results.
```

## 1. Present Verilog

Verilog is a hardware description language. In these labs we are not writing instructions for a processor to execute one after another: we describe a circuit and observe its behavior through simulation.

## 2. Prepare the environment

Work always starts in a practice folder. Open a terminal, enter your working directory, and check that `iverilog` is available.

```bash
iverilog -V
```

## 3. Write and run `hello.v`

Create a file named `hello.v` with a minimal module, then compile and run it.

```verilog
module hello;
  initial
    $display("Hello, world");
endmodule
```

```bash
iverilog hello.v -o hello
./hello
```

## 4. Comments, strings, and constants

Verilog uses C-like comments: `//` for one line and `/* ... */` for blocks. Numeric constants can be written in binary with `'b`, octal with `'o`, decimal with `'d`, and hexadecimal with `'h`.

## 5. Types, registers, and blocks

A block with several instructions is enclosed between `begin` and `end`. Declare an integer, a real, and a 16-bit register, then assign simple values and print them.

## 6. Check values with `$display`

Use `$display` to print the same value in decimal, binary, octal, and hexadecimal. {numref}`fig-verilog-en-01-ej-1-9` shows an expected output for this first checking exercise.

```{figure} ../../_static/verilog/sesion_01/ej_1_9.png
---
name: fig-verilog-en-01-ej-1-9
alt: Expected output for an initial conversion and data-display exercise.
width: 85%
align: center
---
Expected output for an initial conversion and data-display exercise.
```

## 7. Read the full program structure

Once the example prints values, read the code by zones: module name, definition area, `initial` block, instructions, and `endmodule`. {numref}`fig-verilog-en-01-ej-1-9-comentado` helps locate those parts.

```{figure} ../../_static/verilog/sesion_01/ej_1_9_comentado.png
---
name: fig-verilog-en-01-ej-1-9-comentado
alt: Commented version of the same example, useful for locating each instruction.
width: 85%
align: center
---
Commented version of the same example, useful for locating each instruction.
```

## 8. Solve conversions and register exercises

Solve several base conversions by hand and then check them with Verilog. Repeat the same pattern with 16-bit registers, unsigned limits, and two's-complement representation.

## 9. Finish with shifts, nets, and special values

Close the session by testing bit shifts and `wire` connections. Record that `x` means unknown value and `z` means high impedance.

## Closing checkpoint

Before moving to the next session, save the Verilog file for each exercise and write down what you expected and what the simulation actually printed. That comparison is the quickest way to find mistakes.

## Original Source

Content written and expanded from the class presentation and reference page: <http://avellano.usal.es/~compi/sesion1.htm>.
