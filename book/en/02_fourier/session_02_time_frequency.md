# Session 2. Signals in the time and frequency domains

Each exercise in this session is preceded by the theory you need to do it, and nothing more. You will work with the files `rectangular.m` and `rectangular_b.m` provided with the lab. The notation is that of the Topic 2 lecture notes.

```{admonition} Learning objectives
:class: tip

- Identify the amplitude, period, frequency and phase of a sinusoid, and obtain the period of a sum of sinusoids.
- Represent a rectangular pulse train through its Fourier series and read its coefficients.
- Interpret the effect of a time shift on the coefficients.
- Plot and read the spectra of a pulse train: bandwidth and DC level.
- Modify the lab function for a triangular pulse train.
```

(fourier-matlab)=
## The MATLAB commands you will use

```{code-block} matlab
:caption: MATLAB commands for this session.

t = 0:0.001:5;                 % time vector, from 0 to 5 in steps of 0.001
y = sin(2*pi*t);               % functions on vectors, element by element
figure; plot(t, y); grid on    % opens a new figure and plots the signal
hold on; plot(t, 0.5*y)        % hold on overlays the next plot
subplot(2,1,1)                 % several plots in one figure (rows, columns, position)
stem(w, coef)                  % vertical lines, for discrete spectra
xlabel('t (s)'); ylabel('f(t)'); legend('a','b'); xlim([0 5])
[t,y,w,coef] = rectangular(4,1,2,-5,5,400);   % how a lab function is called
```

Between vectors of the same size use `.*`, `./` and `.^`, as in session 1 ({ref}`matlab-ex4`). The full pattern for plotting and labelling a signal is in {ref}`matlab-ex6`, and how to call a function with several outputs, in {ref}`matlab-ex8`.

(fourier-ex1)=
## Exercise 1. Sum of a constant and two sinusoids

### The sinusoid and its parameters

A sinusoid is written

$$
f(t) = A \sin(\omega t + \theta)
$$ (eq-sinusoid)

where $A$ is the **amplitude** (peak value), $T$ the **period** in s, $f = 1/T$ the **frequency** in Hz, $\omega = 2\pi/T$ the **angular frequency** in rad/s and $\theta$ the **phase** in rad.

```{admonition} Worked example
:class: note

$f(t) = 3\sin(4\pi t)$. Here $A = 3$ and $\omega = 4\pi$ rad/s, so $f = \omega/2\pi = 2$ Hz and $T = 1/f = 0.5$ s. In 0.5 s the signal completes one full cycle.
```

The phase $\theta$ shifts the curve in time without changing its shape. If $\theta$ is positive, the curve moves to the left, and if it is negative, to the right. For example, $\sin(\omega t)$ starts at 0 and $\sin(\omega t + \pi/2)$ starts at 1, because it is the same curve moved to the left. That second signal is a cosine, since $\cos(x) = \sin(x + \pi/2)$.

```{admonition} rad/s versus Hz
:class: warning

Both units appear in the lab. $\omega = 2\pi$ rad/s is equivalent to $f = 1$ Hz. In MATLAB you write `w1 = 2*pi` and work with $\omega$.
```

### Sum of signals: period and harmonics

A sum of periodic signals repeats when **all** its terms repeat at the same time. A constant term does not change the period, because it does not oscillate. The constant is called the **DC level**, or zero-frequency component.

```{admonition} Worked examples
:class: note

- $\sin(2t) + \sin(3t)$. The periods are $T_1 = \pi$ s and $T_2 = 2\pi/3$ s, and the period of the sum is $2\pi \approx 6.28$ s.
- $\cos(6\pi t) + \cos(8\pi t)$. The periods are $T_1 = 1/3$ s and $T_2 = 1/4$ s, and the period of the sum is 1 s.
- $\sin(t) + \sin(\pi t)$. The periods are $2\pi$ s and 2 s, and the sum is not periodic.
```

When the sum is periodic, its components have frequencies that are multiples of a **fundamental frequency** $f_0 = 1/T$. Those components are called **harmonics**, and harmonic $n$ is the one with frequency $n f_0$. In $\cos(2\pi t) + \tfrac{1}{3}\cos(6\pi t + \pi)$, for example, $T = 1$ s and $f_0 = 1$ Hz. The 1 Hz component is the first harmonic (the fundamental) and the 3 Hz one is the third, because $3\text{ Hz} = 3 f_0$. The second harmonic, at 2 Hz, does not appear in this signal.

```{admonition} Measuring the period on a plot
:class: tip

Find two identical, equivalent points on the curve, for example two consecutive maxima, and subtract their times. A data cursor on the figure (*Data Tips*) gives you those coordinates.
```

```{admonition} Statement
:class: important

Given a signal defined by $f(t) = 1 + A_1\sin(\omega_1 t) + A_2\cos(2\omega_1 t + \theta)$, plot it between 0 and 5 seconds for $A_1 = 1$, $A_2 = 1/2$, $\omega_1 = 2\pi$ rad/s and $\theta = \pi/3$. Obtain the approximate period of the signal from the plot. How many harmonics does it have? What happens to the **shape** of the signal if the DC level is removed?
```

(fourier-ex2)=
## Exercise 2. Rectangular pulse train

### From the Fourier series to the lab formula

A periodic signal with period $T$ can be written as a sum of cosines whose frequencies are multiples of the fundamental, $\omega_n = 2\pi n/T$ with $n = 1, 2, 3\ldots$ That is the **Fourier series**. The pulse train in the lab has amplitude $V$, width $\tau$ and period $T$, and its pulses are centred at $t = 0$. Since the signal is symmetric about $t = 0$, only cosines appear, and the series becomes:

$$
f(t) = \frac{1}{T}\left[c_0 + 2\sum_{n=1}^{\infty} c_n \cos(\omega_n t)\right], \qquad \omega_n = \frac{2\pi n}{T}
$$ (eq-fourier-series)

The numbers $c_n$ are called the **coefficients of the series**. The amplitude of harmonic $n$ is $2|c_n|/T$. If $c_n$ is negative, the cosine of that harmonic is inverted.

Each coefficient is obtained from the signal with an integral over one period, in which the signal equals $V$ inside the pulse and 0 outside it:

$$
c_n = \int_{-T/2}^{T/2} f(t)\,e^{-j\omega_n t}\,dt
$$ (eq-coef-integral-en)

Solving it for the rectangular pulse train gives

$$
c_n = V\tau\,\frac{\sin(\omega_n\tau/2)}{\omega_n\tau/2} = V\tau\,\mathrm{sinc}(\omega_n\tau/2)
$$ (eq-coef-rect-en)

where $\mathrm{sinc}(x) = \sin(x)/x$.

This expression cannot be used as it stands for $n = 0$, because $\omega_n = 0$ gives $\sin(0)/0$. In that case you take the limit, which is $\mathrm{sinc}(0) = 1$, and the result is $c_0 = V\tau$. That is why $c_0$ goes separately in the series and in the code. Substituting $c_0$ and $c_n$ into the series gives the formula in the lab handout:

$$
f(t) = \frac{V\tau}{T} + \frac{2}{T}\sum_{n=1}^{\infty} V\tau\,\mathrm{sinc}(\omega_n\tau/2)\cos(\omega_n t)
$$ (eq-rect-series)

```{admonition} Worked example: V = 3, τ = 1, T = 4
:class: note

Here $\omega_n = \pi n/2$, so the argument of the sinc is $\omega_n\tau/2 = \pi n/4$ and $c_n = 3\,\mathrm{sinc}(\pi n/4)$.

| $n$ | $\pi n/4$ | $\mathrm{sinc}(\pi n/4)$ | $c_n$ | Amplitude $2\lvert c_n\rvert/T$ |
|---|---|---|---|---|
| 1 | $\pi/4$ | 0.900 | 2.701 | 1.350 |
| 2 | $\pi/2$ | 0.637 | 1.910 | 0.955 |
| 3 | $3\pi/4$ | 0.300 | 0.900 | 0.450 |
| 4 | $\pi$ | 0 | **0** | 0 |
| 5 | $5\pi/4$ | $-0.180$ | $-0.540$ | 0.270 |

Harmonic 4 vanishes because $\sin(\pi) = 0$. In general, $c_n = 0$ when $\omega_n\tau/2$ is a multiple of $\pi$.
```

### How the files store the data

The function is called as `[t,y,w,coef] = rectangular(V,tau,T,tmin,tmax,m)`. It computes the series with $m$ harmonics, that is, with $n$ from 1 to $m$ plus the term $c_0$. It returns the time `t`, the signal `y`, the frequencies `w` and the coefficients `coef`.

The order of `coef` is `coef(1)` $= c_0$, `coef(2)` $= c_1$, `coef(3)` $= c_2$… Note that `coef` stores the $c_n$ of {eq}`eq-coef-rect-en`. The division by $T$ and the factor 2 are applied in the last line of the function.

A series with $m$ harmonics is an approximation of the signal. The more terms are added, the more faithful it should be, and it is worth looking carefully at what happens at the points where the signal has jumps.

### Shifting the signal in time

Delaying the signal by a time $t_0$ gives $f(t - t_0)$. The function `rectangular_b(V,tau,T,tmin,tmax,m,t0)` performs that shift. To do so it uses the complex form of the series, with complex numbers $z = a + bj$, of modulus $r = \sqrt{a^2 + b^2}$ and phase $\varphi$ (review {ref}`matlab-ex1` to work with them in MATLAB). In polar form, $z = r\,e^{j\varphi}$, and multiplying by $e^{j\alpha}$ rotates the number by an angle $\alpha$ without changing its modulus.

$$
e^{j\varphi} = \cos\varphi + j\sin\varphi
$$ (eq-euler-en)

A positive real coefficient has phase 0 and a negative real one has phase $\pi$. A positive pure imaginary number has phase $\pi/2$ and a negative one, $-\pi/2$.

In the complex series

$$
f(t) = \frac{1}{T}\sum_{n=-m}^{m} c_n\,e^{j\omega_n t}
$$ (eq-complex-series)

the sum runs over $n = -m \ldots m$. The coefficient of harmonic $n$ is in `coef(m+1+n)`, so harmonic 0 is in `coef(m+1)` and harmonics 1, 2, 3… are in `coef(m+2)`, `coef(m+3)`, `coef(m+4)`… The signal `y` comes out with a negligible imaginary part, of order $10^{-15}$, so you plot `real(y)`.

The **shift theorem** in the lecture notes states that if $f(t)$ has coefficients $c_n$, then $f(t - t_0)$ has coefficients $e^{-j\omega_n t_0}\,c_n$.

```{admonition} Worked example: V = 3, τ = 1, T = 4, t₀ = 0.5 s
:class: note

Here $\omega_n t_0 = \pi n/4$, and each coefficient is multiplied by $e^{-j\pi n/4}$.

| $n$ | $c_n$ without shift | Rotation $-\omega_n t_0$ | Shifted $c_n$ |
|---|---|---|---|
| 1 | 2.701 | $-45^\circ$ | $1.910 - 1.910j$ |
| 2 | 1.910 | $-90^\circ$ | $-1.910j$ |
| 3 | 0.900 | $-135^\circ$ | $-0.637 - 0.637j$ |

The modulus of each coefficient has not changed; only its phase has rotated.
```

```{admonition} Do not use i as a variable
:class: warning

`rectangular_b.m` uses `i` as the imaginary unit. If you have used `i` as a loop counter in your session, the function will give wrong results. Fix it with `clear i`.
```

```{admonition} Statement
:class: important

Plot a periodic signal made of **rectangular pulses** using the function `rectangular.m` provided with the lab. This function implements the sum of a finite number of terms of the Fourier series expansion of that signal, which corresponds to expression {eq}`eq-rect-series`, where $V$ is the pulse amplitude, $\tau$ the pulse width, $T$ the period of the signal and $\omega_n$ the frequency of the harmonics.

a) Setting $V = 4$, $\tau = 1$, $T = 2$ and the time interval from $t_{min} = -5$ to $t_{max} = 5$ seconds, plot the series for 400 harmonics.

b) Plot the series for a number of terms (number of harmonics) of 5, 15, 50, 100, 400 and 1000. Explain the behaviour observed as the number of harmonics increases.

c) Keeping the plotting interval of the previous part and 400 harmonics, vary the remaining parameters ($V$, $\tau$, $T$) and observe how the signal changes. Note how each parameter affects the final result.

d) Since the function `rectangular.m` returns the Fourier series coefficients, what is the value of the first 5 coefficients, corresponding to the first 5 harmonics, if the signal parameters are $V = 4$, $\tau = 1$, $T = 2$? Does any harmonic vanish? Why? What is the value of the coefficient $c_0$ and what does it represent physically? NOTE: the first value of the vector `coef` is the harmonic $c_0$.

e) Now using the function `rectangular_b.m`, which allows the signal to be shifted in time, observe the influence of $t_0$ on the rectangular pulse train, keeping the remaining parameters constant. What is now the value of the coefficients for the first 5 harmonics? What is the fundamental difference from the coefficients of the unshifted signal? NOTE: since this function internally uses the complex form of the Fourier series, in this part the harmonic $c_0$ (DC component) is in the middle of the vector `coef`, because there are negative and positive frequencies.

f) Looking at the code of the function `rectangular_b.m`, where does the time shift of the signal appear and why is it expressed that way?
```

(fourier-ex3)=
## Exercise 3. Spectra of the pulse train

### The three spectra

Each coefficient $c_n$ is a complex number, with a modulus $|c_n|$ and a phase $\theta_n$, so that $c_n = |c_n|\,e^{j\theta_n}$. To describe at which frequencies a signal has energy, three plots are used, all with the frequency $\omega_n = 2\pi n/T$ on the horizontal axis:

```{list-table} The three spectra of a periodic signal.
:name: table-spectra
:header-rows: 1
:widths: 20 35 45

* - Spectrum
  - What is plotted
  - What it is for
* - **Amplitude**
  - $|c_n|$ against $\omega_n$
  - How much each harmonic weighs. All lines point upwards.
* - **Phase**
  - $\theta_n$ against $\omega_n$
  - How each harmonic is shifted in time.
* - **Frequency**
  - Amplitude and phase together, that is, the $c_n$ themselves
  - Combines the two previous ones in a single plot.
```

In the rectangular pulse train all the $c_n$ are real numbers, positive or negative. The phase can then only be 0 (positive $c_n$) or $\pi$ (negative $c_n$), and the frequency spectrum is drawn in a single plot with `stem(w, coef)`. Negative $c_n$ point downwards, which is equivalent to phase $\pi$. With `stem(w, abs(coef))` you plot the amplitude spectrum, and all lines point upwards.

```{admonition} Worked example: the coefficients of the exercise 2 example (V = 3, τ = 1, T = 4)
:class: note

| $n$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $\omega_n$ (rad/s) | 1.57 | 3.14 | 4.71 | 6.28 | 7.85 |
| $c_n$ (frequency spectrum) | 2.701 | 1.910 | 0.900 | 0 | $-0.540$ |
| $\lvert c_n\rvert$ (amplitude spectrum) | 2.701 | 1.910 | 0.900 | 0 | 0.540 |
| $\theta_n$ (phase spectrum) | 0 | 0 | 0 | not applicable | $\pi$ |

The first two plots have the same lines, but in the frequency spectrum the line $n = 5$ hangs downwards. That shows that the sign of the $c_n$ has changed.
```

The spectrum of a periodic signal is **discrete**. There are values only at the frequencies $\omega_n = 2\pi n/T$, with $n = 0, 1, 2\ldots$, and that is why it is drawn as separate lines using `stem`. Between two lines there is nothing.

### Bandwidth and DC level

The **bandwidth** according to the first criterion is the frequency of the first zero of the coefficients. It is computed by setting $V\tau\,\mathrm{sinc}(\omega\tau/2)$ equal to zero and taking the first solution with $\omega > 0$. The answer comes out in rad/s, and is converted to Hz with $f = \omega/2\pi$. It may or may not coincide with the frequency of a particular harmonic.

```{admonition} Worked example: first criterion with another expression
:class: note

The expression $A\sin(\omega a)/(\omega a)$, with $a = 0.5$ s, vanishes when $\sin(\omega a) = 0$. The first solution with $\omega > 0$ is $\omega a = \pi$, that is, $\omega = \pi/a = 2\pi$ rad/s, or 1 Hz.
```

The **DC level** of the signal is the constant term of the series, which comes from formula {eq}`eq-rect-series` without any cosine. It is not the same as the value of `coef(1)`: harmonic 0 is the one stored in `coef(1)`, and the DC level is the one that appears in the signal.

```{admonition} Statement
:class: important

Using the function `rectangular.m` again to obtain the Fourier series coefficients and their corresponding frequencies, now plot the **spectra of the rectangular pulse train**, which by definition are the graphical representation of these coefficients. To represent each value by a vertical line, use MATLAB's `stem` function, with syntax `stem(w,coef)`.

Consider a signal on the interval $t_{min} = -50$, $t_{max} = 50$, with $V = 4$, $\tau = 1$ and $T = 2$.

a) Plot the frequency spectra for periods $T = 2$, 5 and 20, using 50 harmonics, and observe the influence of $T$ on the spectrum, on the spacing between harmonics. What happens when $T$ becomes very large? State the bandwidth (using the first criterion) and the value of harmonic 0 (DC level) in each case, from the plots. To compare spectra it is useful to overlay the plots with `hold on`.

b) State the bandwidth of this signal and its DC level analytically, and compare those values with the ones obtained from the plots.

c) Vary the pulse width $\tau$ (keeping the remaining parameters) and observe the influence on the bandwidth. Check that there is an inversely proportional relationship between the pulse width and the bandwidth of the signal.
```

(fourier-ex4)=
## Exercise 4. Triangular pulse train

### The triangular pulse and its coefficient

The triangular pulse has height $V$ at $t = 0$ and falls linearly to 0 at $t = -\tau$ and at $t = \tau$. Its base is therefore $2\tau$ long. The coefficients of the train, according to the handout, are

$$
c_n = V\tau\,\mathrm{sinc}^2(\omega_n\tau/2) = V\tau\left[\frac{\sin(\omega_n\tau/2)}{\omega_n\tau/2}\right]^2, \qquad \omega_n = \frac{2\pi n}{T}
$$ (eq-coef-tri-en)

The series is summed as in exercise 2, with {eq}`eq-fourier-series`.

The term $c_0$ is still the coefficient of harmonic 0, that is, the value of the integral {eq}`eq-coef-integral-en` with $n = 0$, which is now computed over the triangle. It has to be set by hand in `coef(1)`, as `rectangular.m` does.

```{admonition} What to change in rectangular.m
:class: tip

Save a copy under another name, for example `triangular.m`, and change the function name in the first line (remember from {ref}`matlab-ex8` that the file name and the function name must match). Then review the line that computes `coef(n+1)` and the one that assigns `coef(1)`. Apart from that, the structure of the file is the same.
```

```{admonition} Statement
:class: important

Modify the code of the function `rectangular.m` so that it represents a periodic triangular pulse train, given that the Fourier series coefficients for that signal are those in {eq}`eq-coef-tri-en`, where $V$ is the pulse amplitude, $2\tau$ is the pulse width (base of the triangles), $T$ is the period of the signal and $\omega_n$ is the frequency of the harmonics.

Plot the **signal in the time domain** and the **spectrum of the signal** for the following parameter values: $V = 5$, $\tau = 2$, $T = 5$, $t_{min} = -10$, $t_{max} = 10$, using 5, 10 and 50 harmonics. Check on the time-domain plot that the pulse width is correct.
```

```{admonition} Session summary
:class: seealso

- A sinusoid $A\sin(\omega t + \theta)$ is defined by its amplitude, its frequency ($\omega = 2\pi/T$) and its phase, which shifts the curve without changing its shape.
- A sum of periodic signals repeats when all its terms repeat at the same time. Its components are harmonics with frequency $n f_0$, and the constant is the DC level.
- The Fourier series writes a periodic signal as $\frac{1}{T}\left[c_0 + 2\sum c_n\cos(\omega_n t)\right]$, with $\omega_n = 2\pi n/T$. The amplitude of harmonic $n$ is $2|c_n|/T$.
- For the rectangular pulse train, $c_n = V\tau\,\mathrm{sinc}(\omega_n\tau/2)$ and $c_0 = V\tau$. In `rectangular.m`, `coef(1)` is $c_0$.
- Delaying the signal by $t_0$ multiplies each coefficient by $e^{-j\omega_n t_0}$. In `rectangular_b.m`, harmonic 0 is in the middle of `coef`.
- The spectrum of a periodic signal is discrete and is drawn with `stem`: amplitude ($|c_n|$), phase ($\theta_n$) or frequency (the $c_n$ themselves).
- The bandwidth (first criterion) is the frequency of the first zero of the coefficients. The DC level is the constant term of the series, not the value of `coef(1)`.
- The triangular pulse train has $c_n = V\tau\,\mathrm{sinc}^2(\omega_n\tau/2)$ and base $2\tau$.
```
