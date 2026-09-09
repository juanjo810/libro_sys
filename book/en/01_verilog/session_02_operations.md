# Session 2. Bit Operations

This session moves from a simple idea, changing selected bits in a register, to more compact operations such as reduction, concatenation, and replication.

```{admonition} Learning objectives
:class: tip

- Use masks to set, clear, toggle, and inspect bits.
- Apply reduction operators to obtain global information from a register.
- Combine signals through concatenation and replication.
```

## 1. Work on specific bits

Start with a 16-bit register whose binary value is easy to read. The guiding question is always which bits change and which stay the same. Work it out on paper before simulating.

## 2. One's complement

The `~` operator inverts every bit. Test it on a small register and print the result in binary with `$display`.

## 3. Set bits

Use bitwise OR (`|`) with a mask that has ones exactly where the target bits must be set. Test one bit first, then several bits at once.

## 4. Clear bits

Use bitwise AND (`&`) with a mask that has zeros where bits must be cleared. A common pattern is to write the positive mask and invert it.

## 5. Toggle and inspect bits

Bitwise XOR (`^`) toggles only the positions marked with ones in the mask. To inspect a bit, isolate it with a mask and compare the result.

## 6. Reduce, concatenate, and replicate

Reduction operators condense many bits into one result, for example parity. Concatenation joins signals with `{a, b}` and replication repeats a pattern with `{4{bit}}`.

## Closing checkpoint

Before moving to the next session, save the Verilog file for each exercise and write down what you expected and what the simulation actually printed. That comparison is the quickest way to find mistakes.

## Original Source

Content written and expanded from the class presentation and reference page: <http://avellano.usal.es/~compi/sesion2.htm>.
