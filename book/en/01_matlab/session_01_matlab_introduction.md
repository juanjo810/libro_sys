# Session 1. Introduction to MATLAB

This is the reference guide for the first lab session. If you already know how to program in C, you will find that MATLAB has a different syntax but a familiar logic. Use this page together with the exercise handout: each section corresponds to one of the exercises.

```{admonition} Learning objectives
:class: tip

- Recognise the most important syntax differences between C and MATLAB.
- Use the environment: Command Window, Workspace, script editor and current folder.
- Define scalars, complex numbers, vectors and matrices, and access their elements.
- Distinguish matrix operations (`*`, `/`, `^`) from element-wise operations (`.*`, `./`, `.^`).
- Plot signals with `plot` and label the figures properly.
- Write `for` loops and functions in `.m` files.
```

(matlab-from-c)=
## Coming from C

MATLAB is not a general-purpose language: it is designed for matrix and numerical computation. Many things that need libraries and loops in C are a single line here. The price is a syntax with several differences that cause errors at first. {numref}`table-c-matlab` summarises the ones you will notice on day one.

```{list-table} Basic equivalences between C and MATLAB.
:name: table-c-matlab
:header-rows: 1
:widths: 30 30 40

* - In C you write…
  - In MATLAB it is…
  - Why does it change?
* - `int a = 5;`
  - `a = 5;`
  - No type declarations. Everything is `double` by default.
* - `// comment`
  - `% comment`
  - `%` starts a comment. The remainder of a division is computed with `mod(a, b)`.
* - `printf("x=%d\n", x);`
  - `disp(x)` or just `x`
  - Without a trailing `;`, MATLAB prints the result automatically. `fprintf`, almost identical to `printf`, also exists.
* - `v[0] = 1;`
  - `v(1) = 1;`
  - Indices start at 1, not 0, and are written in parentheses.
* - `a * b` (two numbers)
  - `a .* b` (two vectors)
  - `*` is the matrix product. Element-wise multiplication uses `.*`.
* - `#include <math.h>`
  - (nothing)
  - There are no includes: `sin`, `cos`, `exp`, `sqrt`… are always available.
* - `}` (closes a block)
  - `end`
  - `for`, `if`, `while` and `function` blocks are closed with `end`.
* - `;` (ends a statement)
  - `;` (suppresses output)
  - The `;` is optional: leave it out when you want to see the value in the console.
```

```{admonition} The most common day-one mistake
:class: warning

Using `*` instead of `.*` when operating on two vectors. If MATLAB answers `Error using * Incorrect dimensions for matrix multiplication`, that is the problem.
```

The two snippets below do the same thing: fill a vector with the numbers 1 to 10. Notice the starting index, the `for` header and the `end` that replaces the closing brace.

```{code-block} c
:caption: `for` loop in C.

int v[10];
for (int k = 0; k < 10; k++) {
    v[k] = k + 1;
}
```

```{code-block} matlab
:caption: The same loop in MATLAB.

v = zeros(1, 10);
for k = 1:10
    v(k) = k;
end
```

(matlab-environment)=
## The MATLAB environment

When you open MATLAB you will see several work areas:

- **Command Window (console)**: type a command, press Enter and see the result immediately.
- **Workspace**: lists the variables in memory, with their size and value.
- **Editor**: where you write scripts and functions in `.m` files.
- **Current Folder**: the current working folder. MATLAB only finds your `.m` files if they are in it (or on the path).

A few commands keep the environment clean and you will use them constantly:

```{code-block} matlab
:caption: Essential clean-up commands.

clc        % clear the console (like cls in Windows)
clear      % delete all variables from the Workspace
clear a b  % delete only a and b
who        % list the variables that currently exist
whos       % list variables with their type and size

% Good habit: start every script with
clc; clear;
```

```{admonition} Script or console
:class: note

You can type directly in the console or save the code in a `.m` file and run it with **F5** (or the *Run* button). In this session use scripts: that way you can fix and rerun your code easily.
```

(matlab-ex1)=
## Exercise 1. Scalar variables

```{admonition} Statement
:class: important

Define variables, with any name, that store the values given in the handout table: numbers, fractions, roots, trigonometric functions, logarithms and complex numbers.
```

### Assignment

Assignment works as in C (`variable = value`), with two differences: there are no types, and the trailing `;` only stops MATLAB from printing the result.

```{code-block} matlab
:caption: Assignment and predefined constants.

a = 3;          % silent
b = -5.7;       % silent
b = -5.7        % no ; -> prints "b = -5.7000" in the console

% Predefined constants (do not use them as variable names)
c = pi;         % 3.14159...
d = exp(1);     % number e = 2.71828...
```

### Fractions and roots

MATLAB evaluates `*` and `/` from left to right, just like C. That is why `5/2*7` equals $(5/2)\cdot 7 = 17.5$ and not $5/14$. Always use parentheses when a fraction has several factors in the denominator.

```{code-block} matlab
:caption: Fractions, roots and powers.

f1 = 5 / (2*7);     % 5/14 = 0.3571
f2 = 1/3;           % 0.3333...

r1 = sqrt(2);       % square root of 2 = 1.4142...
r2 = 2^(1/3);       % cube root of 2: ^ is the power (pow in C)
r3 = 8^(2/3);       % = 4
```

### Trigonometry

Trigonometric functions **always work in radians**, just like those in `math.h`.

```{code-block} matlab
:caption: Trigonometric functions and their inverses.

s1 = sin(pi/4);     % 0.7071
s2 = cos(pi/3);     % 0.5
s3 = tan(pi/4);     % 1

s4 = asin(0.5);     % pi/6
s5 = atan2(1, 1);   % pi/4 (arctangent with the correct quadrant)
```

### Logarithms and exponential

```{code-block} matlab
:caption: Logarithms in different bases and exponential.

l1 = log(exp(1));   % natural logarithm: ln(e) = 1
l2 = log10(100);    % base-10 logarithm -> 2
l3 = log2(8);       % base-2 logarithm  -> 3
e1 = exp(-2);       % e^(-2) = 0.1353
```

### Complex numbers

Complex numbers are essential in Signals and Systems. A complex number can be written in rectangular form, $z = a + jb$, or in polar form, $z = r\,e^{j\theta}$, where $r = |z|$ is the magnitude and $\theta$ the argument. In MATLAB the imaginary unit is written `i` or `j`; the safest form is `1i` or `1j`.

```{code-block} matlab
:caption: Defining and operating with complex numbers.

z1 = 3 + 4i;               % rectangular form
z2 = 2*exp(1i*pi/3);       % polar form: r = 2, theta = pi/3

magnitude = abs(z1);       % |z1| = 5
phase     = angle(z1);     % argument = atan2(4, 3) = 0.9273 rad
conjugate = conj(z1);      % conjugate: 3 - 4i
real_part = real(z1);      % real part: 3
imag_part = imag(z1);      % imaginary part: 4
```

```{admonition} Do not use i or j as counters
:class: warning

`i` and `j` represent the imaginary unit. If you use them as loop variables they will no longer equal $\sqrt{-1}$, and your complex computations will give wrong results without any warning. Use `k`, `n` or `m` for indices.
```

(matlab-ex2)=
## Exercise 2. Vectors and matrices

```{admonition} Statement
:class: important

Define the given vectors and matrices. For the last three (very long vectors) it is **mandatory** to use the `:` operator notation; you cannot type every element by hand.
```

### Explicit definition

Elements are written between square brackets. A space (or comma) separates columns and a semicolon separates rows.

```{code-block} matlab
:caption: Row vectors, column vectors and matrices.

% Row vector: elements separated by spaces or commas
v = [1 2 3 4 5];
v = [1, 2, 3, 4, 5];      % equivalent

% Column vector: elements separated by semicolons
c = [1; 2; 3; 4; 5];

% 3x3 matrix: rows are separated by ;
A = [1 2 3; 4 5 6; 7 8 9];

% Transpose: the ' operator turns row <-> column
ct = c';                  % column -> row
```

### The `:` operator

The `:` (colon) operator generates vectors with a regular pattern. Its syntax is `start:step:end`; if you omit the step, it is 1. The step can be fractional or negative.

```{code-block} matlab
:caption: Vectors generated with the `:` operator and with `linspace`.

v1 = 1:10;          % [1 2 3 4 5 6 7 8 9 10]
v2 = 0:0.5:3;       % [0 0.5 1 1.5 2 2.5 3]
v3 = 10:-1:1;       % countdown: [10 9 8 ... 1]
v4 = 0:2:20;        % even numbers from 0 to 20

% linspace(a, b, N): N equally spaced points between a and b
t = linspace(0, 10, 1000);   % 1000 points in [0, 10]

% In Signals, this is how the time axis is defined
t = 0:0.001:10;     % from 0 to 10 with step 0.001 (10001 points)
```

```{admonition} When to use : and when to use linspace
:class: tip

Use `start:step:end` when the **step** matters (for example, the sampling period). Use `linspace(a, b, N)` when the **number of points** matters. Both create row vectors.
```

### Accessing elements

Remember that the first element has index 1. The word `end` inside an index means "the last one".

```{code-block} matlab
:caption: Indexing vectors and matrices.

v = [10 20 30 40 50];

v(1)            % first element: 10   (v[0] in C)
v(3)            % third element: 30   (v[2] in C)
v(end)          % last element: 50
v(2:4)          % elements 2, 3 and 4: [20 30 40]
v(end-1:end)    % second-to-last and last: [40 50]

% Matrices: A(row, column)
A(1, 2)         % row 1, column 2
A(2, :)         % the whole row 2
A(:, 3)         % the whole column 3
```

(matlab-ex3)=
## Exercise 3. The `size` function

```{admonition} Statement
:class: important

Obtain the number of rows and columns of a matrix and of a row vector with the `size` function, and store those values in two variables.
```

The `size` function returns the dimensions of a variable. Called as `[m, n] = size(A)` it returns rows and columns at once; called as `size(A, dim)` it returns a single dimension (`dim = 1` for rows, `dim = 2` for columns). For vectors, `length(v)` directly gives the number of elements.

```{code-block} matlab
:caption: Three ways to query dimensions.

A = [1 2 3; 4 5 6];        % 2x3 matrix

% Way 1: rows and columns at once (what the exercise asks for)
[rows, cols] = size(A);    % rows = 2, cols = 3

% Way 2: a single dimension
rows = size(A, 1);         % number of rows
cols = size(A, 2);         % number of columns

% Way 3: for vectors, length is more convenient
v = 1:10;
n = length(v);             % n = 10
n = numel(v);              % total number of elements
```

```{admonition} Check your result
:class: note

For a row vector such as `v = 1:10`, `size(v)` returns `[1 10]`: one row and ten columns. If transposing it (`v'`) gives `[10 1]`, you have understood the difference between a row vector and a column vector.
```

(matlab-ex4)=
## Exercises 4 and 5. Element-wise operations

```{admonition} Statement
:class: important

- **Exercise 4.** Multiply two vectors element by element using `.*`.
- **Exercise 5.** Divide element by element with `./` and square each element with `.^`.
```

This is one of the most important differences from C. In MATLAB, `*` is **matrix** multiplication. To operate on two vectors position by position you add a dot before the operator, as summarised in {numref}`table-element-wise`.

```{list-table} Element-wise operators and their C equivalent.
:name: table-element-wise
:header-rows: 1
:widths: 15 40 45

* - Operator
  - Action
  - "By hand" equivalent in C
* - `.*`
  - `c(k) = a(k) * b(k)` for every `k`
  - `for (k=0; k<n; k++) c[k] = a[k]*b[k];`
* - `./`
  - `c(k) = a(k) / b(k)` for every `k`
  - `for (k=0; k<n; k++) c[k] = a[k]/b[k];`
* - `.^`
  - `c(k) = a(k)^p` for every `k`
  - `for (k=0; k<n; k++) c[k] = pow(a[k], p);`
* - `*`
  - **Matrix product** (a different concept)
  - Not the same: the number of columns of `a` must match the number of rows of `b`.
```

````{admonition} Proposed solution for exercises 4 and 5
:class: dropdown

```matlab
v = [1 2 3 4 5];
z = [2 4 1 3 6];

% Exercise 4: element-wise product
prod_ew = v .* z;       % [2 8 3 12 30]

% Exercise 5a: element-wise division
div_ew = v ./ z;        % [0.5 0.5 3 1.3333 0.8333]

% Exercise 5b: square of each element of v
squared = v .^ 2;       % [1 4 9 16 25]
```
````

Why does this matter in Signals? Because a signal in MATLAB is a vector with thousands of samples. To compute, for example, the damped sine $y(t) = \sin(2\pi t)\, e^{-t}$ you must multiply sample by sample:

```{code-block} matlab
:caption: Damped sine: element-wise product of two signals.

t = 0:0.001:10;
y = sin(2*pi*t) .* exp(-t);
```

```{admonition} Careful
:class: warning

`sin(t) * exp(-t)` produces the error `Incorrect dimensions for matrix multiplication`, because it tries to multiply two row vectors as matrices. Always use `.*` when operating on two vectors point by point. Multiplying a vector by a **scalar** (`2*t`) does work with `*`.
```

(matlab-ex6)=
## Exercise 6. Plotting

```{admonition} Statement
:class: important

Plot several functions for $t \in [0, 10]$ (the last one for $t \in [-10, 10]$) using `plot`. Use `figure` to show them in separate windows.
```

The pattern is always the same:

1. Define the vector `t` with the domain required by the exercise and a small step (0.001 gives good resolution).
2. Compute the signal with element-wise operations on `t`.
3. Open a new window with `figure` and draw with `plot(t, y)`.
4. Add labels. A plot without a title and labelled axes is an incomplete plot.

```{code-block} matlab
:caption: Complete pattern for plotting a signal.

% Step 1: time axis
t = 0:0.001:10;

% Step 2: signal
y = sin(2*pi*t);

% Step 3: open a window and draw
figure;             % new window (avoids overwriting the previous plot)
plot(t, y);

% Step 4: labels
xlabel('t (s)');
ylabel('y(t)');
title('Sine signal');
grid on;
```

The following signals are typical examples of the kind of functions the exercise asks for. Adapt them to the specific expressions in your handout.

```{code-block} matlab
:caption: Example signals for exercise 6.

t  = 0:0.001:10;
t2 = -10:0.001:10;      % domain [-10, 10] for the last function

% Decaying exponential
figure; plot(t, exp(-t));
title('e^{-t}'); xlabel('t'); grid on;

% Damped cosine
figure; plot(t, exp(-0.5*t) .* cos(2*pi*t));
title('e^{-0.5t} cos(2\pi t)'); xlabel('t'); grid on;

% Square wave (sign of a sine)
figure; plot(t, sign(sin(pi*t)));
title('Square wave'); xlabel('t'); grid on;

% Sinc on [-10, 10]: sinc(x) = sin(pi x)/(pi x)
figure; plot(t2, sinc(t2));
title('sinc(t)'); xlabel('t'); grid on;
```

```{admonition} If sinc is not available in your installation
:class: note

The `sinc` function belongs to the *Signal Processing Toolbox*. If you do not have it, compute `y = sin(pi*t2)./(pi*t2);` and fix the point $t = 0$, where the division gives `NaN`, with `y(t2 == 0) = 1;`.
```

Some `plot` options that will save you time:

```{code-block} matlab
:caption: Line styles, several curves and axis limits.

% Styles: 'colour' + 'line' + 'marker'
plot(t, y, 'b-');       % blue, solid line
plot(t, y, 'r--');      % red, dashed line
plot(t, y, 'go');       % green, circle at each point

% Several curves in the same figure
figure;
hold on;
plot(t, sin(t));
plot(t, cos(t));
legend('sin(t)', 'cos(t)');
hold off;

% Set the axis limits
xlim([0 10]);
ylim([-1.5 1.5]);
```

```{admonition} Mathematical notation in titles
:class: tip

In `title`, `xlabel` and `ylabel` you can use basic TeX notation: `'e^{-t}'` shows an exponent, `'\pi'` shows the Greek letter and `'f_0'` shows a subscript.
```

(matlab-ex7)=
## Exercise 7. The `for` loop

```{admonition} Statement
:class: important

Using a `for` loop, create a vector made up of the natural numbers from 1 to 10.
```

MATLAB's `for` is different from C's: it does not control a counter with a condition and an increment, it **iterates over the elements of a vector**. On each pass, the loop variable takes the next value of the vector.

```{code-block} matlab
:caption: General structure of the `for` loop.

for variable = vector_of_values
    % block of statements (no braces)
end
```

Some common iteration vectors (only the headers are shown):

```{code-block} matlab
:caption: Examples of loop headers.

for k = 1:10          % k = 1, 2, ..., 10
for k = 0:2:20        % k = 0, 2, 4, ..., 20
for k = 10:-1:1       % k = 10, 9, 8, ..., 1
for x = [3 7 -1]      % x = 3, then 7, then -1
```

````{admonition} Proposed solution for exercise 7
:class: dropdown

```matlab
v = zeros(1, 10);     % preallocate the vector
for k = 1:10
    v(k) = k;
end
disp(v)               % 1 2 3 4 5 6 7 8 9 10
```
````

```{admonition} Preallocation
:class: tip

Before a loop that fills a vector, create it with `zeros(1, n)`. Without preallocation MATLAB resizes the vector on every iteration: it works, but it is much slower for large vectors.
```

(matlab-ex8)=
## Exercise 8. Functions in `.m` files

```{admonition} Statement
:class: important

Write a MATLAB function that returns the product of all the elements of a vector passed as an argument.
```

A MATLAB function is saved in a `.m` file whose name must be **exactly the same** as the function name. The first line defines the outputs, the name and the inputs: `function output = name(input)`. There is no `return` with a value: the function returns whatever the output variable holds when it reaches `end`.

Compare the C version with the MATLAB version. In MATLAB there is no need to pass the size of the vector, because the function can find it with `length`.

```{code-block} c
:caption: Product of the elements of a vector in C.

double product(double *v, int n) {
    double r = 1.0;
    for (int k = 0; k < n; k++)
        r *= v[k];
    return r;
}
```

````{admonition} Proposed solution: file product_elements.m
:class: dropdown

```matlab
function result = product_elements(v)
% PRODUCT_ELEMENTS  Returns the product of all the elements of v.
%
%   result = product_elements(v)
%
%   Input:   v      - numeric vector (row or column)
%   Output:  result - scalar with the accumulated product

    result = 1;                     % identity element of the product
    for k = 1:length(v)
        result = result * v(k);
    end
end
```
````

Once the file is saved, the function can be called from the console or from any script:

```{code-block} matlab
:caption: Calling the function and checking it with `prod`.

p = product_elements([1 2 3 4 5]);   % p = 120
p = product_elements(1:10);          % p = 3628800 = 10!

% Check: MATLAB includes the prod function
prod([1 2 3 4 5])                    % = 120
```

```{admonition} MATLAB cannot find my function
:class: warning

The file `product_elements.m` must be in the current folder (*Current Folder*). Check where you are with `pwd` and change folder with `cd` or from MATLAB's address bar. Also check that the file name matches the function name.
```

A function can return several outputs. They are declared in square brackets and collected the same way:

```{code-block} matlab
:caption: Function with two outputs (file my_max.m).

function [mx, idx] = my_max(v)
% Returns the maximum of v and its position
    [mx, idx] = max(v);
end
```

```{code-block} matlab
:caption: Calling a function with several outputs.

[m, n] = my_max([3 8 2 5]);   % m = 8, n = 2
m      = my_max([3 8 2 5]);   % only the maximum
```

(matlab-elementary-signals)=
## Reference: elementary signals

These are the signals that will appear most often throughout the course, ready to copy and adapt. The unit step, the rectangular pulse of width $a$ and the ramp are defined as

$$
u(t) = \begin{cases} 1, & t \ge 0 \\ 0, & t < 0 \end{cases}
\qquad
\Pi_a(t) = \begin{cases} 1, & |t| < a/2 \\ 0, & \text{otherwise} \end{cases}
\qquad
r(t) = t\,u(t)
$$ (eq-elementary-signals)

In MATLAB, the expressions in {eq}`eq-elementary-signals` are built with comparisons: `(t >= 0)` equals 1 where the condition holds and 0 where it does not.

```{code-block} matlab
:caption: Elementary signals built with logical comparisons.

t = -5:0.001:5;

% Unit step u(t)
u = (t >= 0);

% Rectangular pulse of width a centred at 0
a = 2;
rect = (t >= -a/2) & (t < a/2);

% Ramp r(t) = t u(t)
ramp = t .* (t >= 0);

% Causal damped sine (typical response of a 2nd-order system)
y_am = exp(-0.5*t) .* sin(2*pi*t) .* (t >= 0);
```

With these signals you can compute properties and apply basic transformations. The energy of a signal, $E = \int |x(t)|^2\,dt$, is approximated numerically by summing the squared samples and multiplying by the step $\Delta t$.

```{code-block} matlab
:caption: Energy, time shift and time reversal.

dt = t(2) - t(1);              % sampling step

% Signal energy (numerical integration)
E = sum(abs(y_am).^2) * dt;

% Time shift: y(t - t0)
t0 = 1;
y_del = exp(-0.5*(t-t0)) .* sin(2*pi*(t-t0)) .* (t >= t0);

% Time reversal: y(-t)
y_rev = exp(0.5*t) .* sin(-2*pi*t) .* (t <= 0);
```

```{admonition} Session summary
:class: seealso

- In MATLAB there are no type declarations, indices start at 1 and blocks are closed with `end`.
- Vectors are created with `[ ]`, with `start:step:end` or with `linspace`.
- Between two vectors, always use `.*`, `./` and `.^`.
- Every plot needs `figure`, `plot`, a title and labelled axes.
- A function lives in a `.m` file with the same name, in the current folder.
```
