# Session 3. Spectra of periodic and non-periodic signals: the Fourier integral

Each exercise in this session is preceded by the theory you need to do it, and nothing more. You will work with the files `rectangular_c.m`, `espectro.m` and `inv_espectro.m` provided with the lab. The notation is that of the Topic 2 lecture notes, and what you saw in {ref}`session 2 <fourier-ex2>` is taken for granted.

```{admonition} Learning objectives
:class: tip

- Understand how the Fourier series turns into the Fourier integral when the period tends to infinity.
- Obtain the Fourier integral of a pulse from the coefficients of its periodic train.
- Tell a discrete spectrum from a continuous one, and read the bandwidth and the DC component on both.
- Compute spectra numerically with `espectro` and recover the signal with `inv_espectro`.
- Recognise when the frequency spectrum can be drawn and when the amplitude spectrum must be drawn instead.
```

(integral-matlab)=
## The MATLAB commands you will use

```{code-block} matlab
:caption: MATLAB commands for this session.

[t,y,w,coef] = rectangular_c(5,1,8,-40,40,50,0);  % pulse train; the last argument is t0
[w1,F1] = espectro(t, y, 8);     % numerical spectrum of signal y, with period 8
figure; plot(w1, F1); hold on; stem(w, coef)   % curve and lines on the same figure
plot(w1, abs(F1))                % modulus: amplitude spectrum
plot(w1, angle(F1))              % phase, in radians
max(abs(imag(F1)))               % does F1 have a noticeable imaginary part?
[t2,y2] = inv_espectro(w1, F1, 8);  % back to the time domain
xlim([-20 20]); legend('espectro','coef')
```

The functions `abs`, `angle`, `real` and `imag` work element by element, like those in session 1 ({ref}`matlab-ex4`). To evaluate a formula on a frequency vector use `./` and `.^`, as in session 2 ({ref}`fourier-matlab`). The exact order of the arguments of each lab function is in the first line of its `.m` file: open it before calling it ({ref}`matlab-ex8`).

```{admonition} The sinc formula in MATLAB
:class: warning

If you write `F2 = 5*sin(w/2)./(w/2)` and the vector `w` contains 0, at that position MATLAB computes $0/0$ and returns `NaN`, and that point disappears from the plot. Set the value by hand with `F2(w==0) = 5`. Do not use MATLAB's `sinc` function without thinking: it is defined as $\sin(\pi x)/(\pi x)$, not as $\sin(x)/x$, so $\sin(\omega/2)/(\omega/2)$ is written `sinc(w/(2*pi))`.
```

(integral-ex1)=
## Exercise 1. Spectrum of the pulse train and of the single pulse

### From the series to the Fourier integral

In session 2 you saw that a pulse train with period $T$ has a **discrete** spectrum: there are coefficients only at the frequencies $\omega_n = 2\pi n/T$, spaced $\Delta\omega = 2\pi/T$ apart. If the period grows, the pulses move away from each other and the spectral lines get closer, because $\Delta\omega$ becomes smaller. In the limit $T \to \infty$ a single pulse remains, which is no longer periodic, and the lines merge into a **continuous** curve. That curve is the **Fourier integral** $F(\omega)$:

$$
F(\omega) = \int_{-\infty}^{\infty} f(t)\,e^{-j\omega t}\,dt
$$ (eq-fourier-integral-en)

It is the same integral that gave the coefficients $c_n$ ({eq}`eq-coef-integral-en`), with two changes: it is integrated over the whole time axis instead of over one period, and the frequency $\omega$ is no longer restricted to the values $\omega_n$, but can take any value. That is why a non-periodic signal contains **all** frequencies and a periodic one only the multiples of its fundamental. $F(\omega)$ is also called the **Fourier transform** of $f(t)$, written $f(t) \leftrightarrow F(\omega)$.

```{list-table} Fourier series and Fourier integral, side by side.
:name: table-series-integral
:header-rows: 1
:widths: 30 35 35

* -
  - Periodic signal (series)
  - Non-periodic signal (integral)
* - Frequencies
  - $\omega_n = 2\pi n/T$, spaced $2\pi/T$ apart
  - Continuous $\omega$, spacing $\to 0$
* - Spectrum
  - Coefficients $c_n$
  - Function $F(\omega)$
* - Computation
  - $c_n = \int_{-T/2}^{T/2} f(t)\,e^{-j\omega_n t}\,dt$
  - $F(\omega) = \int_{-\infty}^{\infty} f(t)\,e^{-j\omega t}\,dt$
* - Type of spectrum
  - Discrete, drawn with `stem`
  - Continuous, drawn with `plot`
```

### The Fourier integral of the rectangular pulse

For a pulse of height $V$ and width $\tau$ centred at $t = 0$, the integral {eq}`eq-fourier-integral-en` is solved just like the one for the coefficients of the train, and the result is

$$
F(\omega) = V\tau\,\frac{\sin(\omega\tau/2)}{\omega\tau/2} = V\tau\,\mathrm{sinc}(\omega\tau/2)
$$ (eq-rect-pulse-en)

Compare it with {eq}`eq-coef-rect-en`: it is the same expression with $\omega_n$ replaced by $\omega$. That is the shortcut in the lecture notes: **if you know the $c_n$ of the train, you get $F(\omega)$ of the pulse by replacing $\omega_n$ with $\omega$**, without solving any integral. It works for any signal whose periodic version has known coefficients. Conversely, the coefficients of the train are samples of the pulse curve, $c_n = F(\omega_n)$, which is why, when you overlay `stem(w, coef)` and the curve $F(\omega)$, the lines fall exactly on it.

```{admonition} Worked example: V = 3, τ = 1
:class: note

The single pulse has $F(\omega) = 3\,\mathrm{sinc}(\omega/2)$. The train with $T = 4$ from the session 2 example had $c_n = 3\,\mathrm{sinc}(\pi n/4)$ at $\omega_n = \pi n/2$. Evaluating the curve at those frequencies gives the same numbers:

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $\omega_n$ (rad/s) | 0 | 1.571 | 3.142 | 4.712 | 6.283 | 7.854 |
| $F(\omega_n)$ | 3 | 2.701 | 1.910 | 0.900 | 0 | $-0.540$ |
| $c_n$ of the train | 3 | 2.701 | 1.910 | 0.900 | 0 | $-0.540$ |

With $T = 40$ there would be ten times as many lines over the same frequency range, and they would still fall on the same curve.
```

### Spectra, bandwidth and DC component

The definitions from session 2 ({numref}`table-spectra`) extend to the continuous case unchanged: the **amplitude spectrum** is $|F(\omega)|$, the **phase spectrum** is $\theta(\omega)$, with $F(\omega) = |F(\omega)|\,e^{j\theta(\omega)}$, and the **frequency spectrum** combines both in a single plot, which is only possible when $F(\omega)$ is purely real (the sign carries the phase, 0 or $\pi$) or purely imaginary. Expression {eq}`eq-rect-pulse-en` is real, so for the centred pulse the frequency spectrum can indeed be drawn.

The **bandwidth** by the first criterion is the frequency of the first zero of the spectrum. It is obtained by solving $F(\omega) = 0$: the first zero of $\sin(\omega\tau/2)$ with $\omega > 0$ is at $\omega\tau/2 = \pi$, that is,

$$
\omega_{AB} = \frac{2\pi}{\tau}\ \text{rad/s}, \qquad f_{AB} = \frac{1}{\tau}\ \text{Hz}
$$ (eq-bandwidth-en)

Note that it depends only on $\tau$, not on $T$. There is an **inverse relationship** between the pulse width and the bandwidth: a narrower pulse needs a wider range of frequencies. On a discrete spectrum the first zero is read on the envelope, and it may or may not coincide with a line.

The **DC component** is the value of the spectrum at $\omega = 0$. Since $e^{0} = 1$, the integral {eq}`eq-fourier-integral-en` at $\omega = 0$ is simply $\int f(t)\,dt$: the **area** under the signal. For the rectangular pulse, $F(0) = V\tau$, the area of the rectangle. For the train, $c_0 = V\tau$ is the area of a single period, and the DC level that appears in the signal is $c_0/T$, as you saw in {ref}`fourier-ex3`.

```{admonition} Worked example: bandwidth and DC with V = 3, τ = 1
:class: note

- Single pulse: first zero at $\omega = 2\pi/1 = 6.28$ rad/s, that is, 1 Hz. DC component $F(0) = 3 \cdot 1 = 3$.
- Train with $T = 4$: the same first zero, $2\pi$ rad/s, which coincides with line $n = 4$ because $T/\tau = 4$ is an integer. $c_0 = 3$, and the DC level of the train is $c_0/T = 0.75$.
- If the pulse changes to $\tau = 0.5$, the expression is $F(\omega) = 1.5\,\mathrm{sinc}(\omega/4)$: half as high at $\omega = 0$ and with the first zero at $4\pi = 12.57$ rad/s (2 Hz), twice the bandwidth.
```

### Numerical computation: the `espectro` function

The Fourier integral can be computed numerically from the samples of any signal, without solving anything by hand. That is what `[w, F] = espectro(t, y, T)` does: it receives the time vector `t`, the signal `y` and a period `T`, and returns a frequency vector `w` and the spectrum values `F`. If `y` is periodic, `F` are its coefficients $c_n$; if it is not, `F` are the values of the Fourier integral, and `T` is an adjustable parameter. It is what a spectrum analyser does with a real signal.

Being a numerical computation, `F` comes out as a vector of complex numbers, with small differences from the exact formula. Where the formula gives an exact 0, `F` will give something of order $10^{-15}$, and the imaginary part of a centred signal will be of that same order. Check its size with `max(abs(imag(F)))` before deciding whether the spectrum is real.

### Shifting the pulse in time

The **shift theorem** from session 2 holds equally with $\omega$ in place of $\omega_n$: if $f(t) \leftrightarrow F(\omega)$, then

$$
f(t - t_0) \leftrightarrow e^{-j\omega t_0}\,F(\omega)
$$ (eq-shift-en)

The factor $e^{-j\omega t_0}$ has modulus 1, so **the amplitude spectrum does not change** when the signal is delayed: $|e^{-j\omega t_0} F(\omega)| = |F(\omega)|$. What changes is the phase, which becomes $\theta(\omega) - \omega t_0$, and with it $F(\omega)$ stops being real: each value acquires a real and an imaginary part. The frequency spectrum can then no longer be drawn, and the amplitude spectrum, `abs(F)`, and the phase spectrum, `angle(F)`, must be drawn separately.

```{admonition} Worked example: V = 3, τ = 1, T = 4, delay t₀ = 0.5 s
:class: note

Here $\omega_n t_0 = \pi n/4$. These are the same rotations as in the session 2 example, now read as spectra:

| $n$ | 1 | 2 | 3 |
|---|---|---|---|
| $c_n$ without shift | 2.701 | 1.910 | 0.900 |
| Shifted $c_n$ | $1.910 - 1.910j$ | $-1.910j$ | $-0.637 - 0.637j$ |
| $\lvert c_n \rvert$ | 2.701 | 1.910 | 0.900 |
| $\theta_n$ | $-\pi/4$ | $-\pi/2$ | $-3\pi/4$ |

The amplitude spectrum is identical to that of the centred signal. The shifted $c_n$ have non-zero real and imaginary parts, and they do not even share a type among themselves: $c_2$ is purely imaginary and $c_1$ is not. There is no single number per frequency that carries all the information.
```

```{admonition} Statement
:class: important

Consider a time signal made of a **rectangular pulse train** with period $T = 8$, pulse amplitude $V = 5$, pulse width $\tau = 1$ and centred at $t = 0$.

a) Plot it from $t_{min} = -40$ to $t_{max} = 40$ seconds using the function `rectangular_c.m` provided with this lab, summing 50 harmonics.

b) Compute the values of the Fourier series coefficients using the function `espectro` provided with this lab and check that they are approximately the same as those obtained in the vector `coef` returned by `rectangular_c.m`. To do so, plot the spectra with `plot(w,F1)` and `stem(w,coef)` and check it by overlaying them. Show the plot with the overlaid spectra.

The function `[w, F1] = espectro(t, y, T)` is general purpose: it computes the Fourier series coefficients if the signal `y` supplied to it is periodic, or the values of the Fourier integral if a non-periodic signal `y` is supplied. `t` is the time vector, `y` is a vector with the values of the time signal whose coefficients (or Fourier integral) you want to compute, and `T` is the period of the signal (if the signal is non-periodic, this is an adjustable parameter). The function returns a frequency vector `w` and the corresponding values of the coefficients or of the Fourier integral `F`.

c) Overlay on the spectra of the previous part the plot of the following function, which is the Fourier integral of a **single rectangular pulse (non-periodic)**. Use as frequency vector the one returned by the function `espectro` in the previous part.

$$
F_2(\omega) = 5\,\frac{\sin(\omega/2)}{\omega/2}
$$

Why is this last spectrum continuous while those of the previous part are discrete?

What is the bandwidth of the rectangular pulse train signal and of the single (non-periodic) rectangular pulse? Obtain its value directly from the spectra and check that it matches the value that would be obtained analytically.

What is the DC component (value of the coefficient $c_0$) of each of the signals?

How would the expression of $F_2(\omega)$ change if the rectangular pulse lasted 0.3 seconds? (Just write the new $F_2(\omega)$; this is not about repeating the exercise with 0.3.)

d) Now consider the periodic rectangular pulse train signal with the same characteristics as in a) but **delayed in time** by an amount $t_0 = 2$. Use the function `rectangular_c.m` to create it and compute the values of the Fourier series coefficients using the function `espectro`. Plot the **amplitude** spectrum and check and explain why it is not possible to plot the frequency spectrum.
```

(integral-ex2)=
## Exercise 2. Inverse Fourier transform

### Back from the spectrum to the signal

The Fourier integral loses no information: from $F(\omega)$ you recover $f(t)$ with the **inverse transform**,

$$
f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega)\,e^{j\omega t}\,d\omega
$$ (eq-inverse-integral-en)

It is the continuous version of the series {eq}`eq-complex-series`: the sum of exponentials $e^{j\omega_n t}$ weighted by $c_n/T$ becomes an integral of exponentials $e^{j\omega t}$ weighted by $F(\omega)/2\pi$. The two descriptions of the signal, in time and in frequency, are equivalent, and you can go from one to the other in both directions. In the lab that step is taken by `inv_espectro`, which receives the frequency vector, the spectrum values and a period, and returns the time vector and the reconstructed signal.

Since the computation is numerical, the reconstructed signal has a residual imaginary part of order $10^{-15}$. Plot `real(y)`, as you did with `rectangular_b.m`.

### Reading the pulse parameters on its spectrum

To check that the recovered signal is the right one it is enough to look at two things in formula {eq}`eq-rect-pulse-en`:

- The height of the spectrum at $\omega = 0$ is $F(0) = V\tau$, the area of the pulse.
- The first zero is at $\omega = 2\pi/\tau$, which fixes $\tau$.

From those two values you get $\tau$ and $V$, and they must match the width and height of the pulse that appears on the time plot.

```{admonition} Worked example
:class: note

A spectrum equals 6 at $\omega = 0$ and has its first zero at $\omega = \pi$ rad/s. Then $2\pi/\tau = \pi$ gives $\tau = 2$ s, and $V\tau = 6$ gives $V = 3$. The time signal must be a pulse of height 3 and width 2.
```

```{admonition} Statement
:class: important

Obtain the time signals whose Fourier integrals are those of the previous exercise, $F_1(\omega)$ and $F_2(\omega)$, using the function `inv_espectro` provided in this session to compute the inverse Fourier transform, and plot them. Check that, as expected, the inverse Fourier transform of $F_1(\omega)$ is the time signal of the original pulse train that was used to compute $F_1(\omega)$, and the inverse transform of $F_2(\omega)$ is a single non-periodic rectangular pulse.

Check on both plots that the amplitudes and durations of the rectangular pulses in the figures are consistent with the numerical values of the parameters that appear in the Fourier integrals.

NOTE: in the function `inv_espectro` use as frequency vector the one returned by the function `espectro` in part b) of the previous exercise.

NOTE: when applying the function `inv_espectro` to the Fourier integral $F_2(\omega)$, since it is a non-periodic time signal, use the value $T = 80$ in the function argument corresponding to the period, for a better visualisation of the results.
```

(integral-ex3)=
## Exercise 3. Triangular pulse and triangular pulse train

### The triangular pulse and its spectrum

The triangular pulse has height $V$ at $t = 0$ and base $2\tau$, from $-\tau$ to $\tau$. Its Fourier integral is obtained from the coefficient of the triangular train in session 2 ({eq}`eq-coef-tri-en`) with the same shortcut as before, replacing $\omega_n$ with $\omega$:

$$
F(\omega) = V\tau\,\mathrm{sinc}^2(\omega\tau/2) = V\tau\left[\frac{\sin(\omega\tau/2)}{\omega\tau/2}\right]^2
$$ (eq-tri-pulse-en)

It is the same sinc as the rectangular pulse, squared. That has three consequences you will see on the plot: it is never negative, so phase and amplitude coincide; the side lobes are much smaller, because values below 1 become even smaller when squared; and the zeros are in the same places, so the bandwidth is still $2\pi/\tau$. The DC component is $F(0) = V\tau$, which is the area of the triangle, $\tfrac12 \cdot 2\tau \cdot V$.

```{admonition} Worked example: V = 3, τ = 1, T = 4
:class: note

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $\mathrm{sinc}(\pi n/4)$ | 1 | 0.900 | 0.637 | 0.300 | 0 | $-0.180$ |
| Rectangular $c_n = 3\,\mathrm{sinc}$ | 3 | 2.701 | 1.910 | 0.900 | 0 | $-0.540$ |
| Triangular $c_n = 3\,\mathrm{sinc}^2$ | 3 | 2.432 | 1.216 | 0.270 | 0 | 0.097 |

Both spectra start at 3 and vanish at $n = 4$, but the triangular one falls much faster and does not change sign.
```

### What to change in `rectangular_c.m`

The change is the same one you made in session 2 with `rectangular.m` ({ref}`fourier-ex4`): save a copy under another name, change the function name in the first line and replace the line that computes each coefficient with expression {eq}`eq-coef-tri-en`, squaring the sinc. Also review the coefficient of harmonic 0, which is still $V\tau$. The rest of the file, including the shift $t_0$, does not change.

To generate a **single pulse** with a function that sums a series, the trick in the handout is to use a period $T$ much larger than the plotting interval: with $T = 80$ and time from $-40$ to $40$ only one pulse fits on screen. The spectrum computed by `espectro` is still discrete, with lines every $2\pi/80 \approx 0.079$ rad/s, but they are so close together that `plot` draws a practically continuous curve: it is the transition $T \to \infty$ of {numref}`table-series-integral` seen in practice.

### Symmetries and shift

The lecture notes give three parity properties that explain everything you will see on the plots:

- If $f(t)$ is **even**, with $f(-t) = f(t)$, its Fourier integral is **purely real and even**. The centred pulse, rectangular or triangular, is even.
- If $f(t)$ is **odd**, with $f(-t) = -f(t)$, its Fourier integral is **purely imaginary and odd**.
- For any signal, the amplitude spectrum $|F(\omega)|$ is always **even** and the phase spectrum $\theta(\omega)$ is always **odd**.

When the pulse is shifted in time it stops being even, and by {eq}`eq-shift-en` its spectrum acquires the factor $e^{-j\omega t_0}$: the amplitude spectrum stays the same, but $F(\omega)$ now has real and imaginary parts, and only the amplitude spectrum can be drawn.

### Varying τ

The inverse relationship between time and frequency in the lecture notes is written $f(t/a) \leftrightarrow a\,F(a\omega)$: stretching the signal in time compresses its spectrum, and vice versa. For the triangle, changing $\tau$ moves the first zero to $2\pi/\tau$ and the height at $\omega = 0$ to $V\tau$, both for the single pulse and for the train, because neither value depends on $T$. Keep in mind that the base of the triangle is $2\tau$: if you measure the pulse width on the time plot and get 2, then $\tau = 1$.

```{admonition} Worked example: V = 3, three values of τ
:class: note

| $\tau$ | Base $2\tau$ | $F(0) = V\tau$ | First zero $2\pi/\tau$ (rad/s) | Bandwidth (Hz) |
|---|---|---|---|---|
| 0.5 | 1 | 1.5 | $4\pi = 12.57$ | 2 |
| 1 | 2 | 3 | $2\pi = 6.28$ | 1 |
| 2 | 4 | 6 | $\pi = 3.14$ | 0.5 |

Twice the pulse width, half the bandwidth. In a train with $T = 10$ the line that vanishes is $n = T/\tau$: 20, 10 and 5.
```

```{admonition} Statement
:class: important

Plot the **amplitude spectrum of a (non-periodic) triangular pulse** and of a **periodic triangular pulse train** using the function `espectro` provided with the lab.

To do so, first generate the time signal by modifying the function `rectangular_c.m`, introducing the Fourier coefficient for the triangular signal, and for the **non-periodic** pulse case use a large period $T$ so that only one pulse is generated. Specifically, consider for the time signal: $T = 80$, pulse amplitude $V = 5$, pulse width $\tau = 1$, plotting domain from $t_{min} = -40$ to $t_{max} = 40$, centred at $t = 0$, and sum 400 harmonics. For the **periodic pulse train** case, $T = 10$ can be used, keeping the remaining parameters constant.

Once the time signal has been generated, call the function `espectro`, and finally do `plot(w,abs(F))` to plot the amplitude spectrum. Compare both spectra and state the symmetries they show and whether they are continuous or discrete.

What happens if both the periodic and the non-periodic signals are shifted in time with respect to $t = 0$? Create them and plot the amplitude spectra again. Is it now possible to plot the frequency spectrum? Why?

Keeping the remaining parameters constant, vary $\tau$ (make three variations) and comment on its influence on the bandwidth of the signal.
```

```{admonition} Session summary
:class: seealso

- The Fourier integral $F(\omega) = \int f(t)\,e^{-j\omega t}\,dt$ is the limit of the series when $T \to \infty$: the lines spaced $2\pi/T$ apart merge into a continuous curve. A non-periodic signal contains all frequencies.
- If you know the $c_n$ of the train, $F(\omega)$ of the pulse follows by replacing $\omega_n$ with $\omega$. Conversely, $c_n = F(\omega_n)$: the lines of the train fall on the curve of the pulse.
- Rectangular pulse: $F(\omega) = V\tau\,\mathrm{sinc}(\omega\tau/2)$. Triangular pulse: $F(\omega) = V\tau\,\mathrm{sinc}^2(\omega\tau/2)$, with base $2\tau$.
- Bandwidth (first criterion): $\omega_{AB} = 2\pi/\tau$ rad/s, or $1/\tau$ Hz. It depends on $\tau$ and not on $T$; narrow pulse, large bandwidth.
- DC component: $F(0)$, the area under the signal. It equals $V\tau$ for both the rectangular and the triangular pulse. In the train, $c_0 = V\tau$ is the area of one period.
- `espectro(t, y, T)` computes the spectrum numerically: coefficients if `y` is periodic, Fourier integral if not. `inv_espectro` goes the other way with $f(t) = \frac{1}{2\pi}\int F(\omega)\,e^{j\omega t}\,d\omega$.
- Delaying by $t_0$ multiplies the spectrum by $e^{-j\omega t_0}$: the amplitude spectrum does not change, the phase does, and $F(\omega)$ stops being real.
- The frequency spectrum can only be drawn if $F(\omega)$ is purely real or purely imaginary. If it has real and imaginary parts, draw `abs(F)` and `angle(F)` separately.
- Even signal: real, even spectrum. Odd signal: purely imaginary, odd spectrum. Always: $|F(\omega)|$ even and $\theta(\omega)$ odd.
```
