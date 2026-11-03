# Session 4. Signals through linear time-invariant systems and distortions

Each exercise in this session is preceded by the theory you need to do it, and nothing more. You will work with the files `rectangular_c.m`, `espectro.m` and `inv_espectro.m` from session 3, and with the new `redRC.m`, `H1.m` to `H5.m`, `leeraudio.m`, `FiltroA.m` and `FiltroB.m`. The notation is that of the Topic 2 lecture notes, and what you saw in {ref}`session 3 <integral-ex1>` is taken for granted.

```{admonition} Learning objectives
:class: tip

- Describe a linear time-invariant system by its transfer function $H(\omega)$ and read its amplitude and phase spectra.
- Obtain the bandwidth of a system and predict, by comparing it with that of the signal, whether there will be distortion.
- Simulate the passage of a signal through a system with the relation $G(\omega) = H(\omega)F(\omega)$ and recover the output in time.
- Apply the linear response theorem and the superposition principle to a sum of harmonics.
- Recognise attenuation, delay, attenuation distortion and delay distortion in the spectra of a system.
- Analyse the effect of a filter on a real audio signal.
```

(sistemas-matlab)=
## The MATLAB commands you will use

```{code-block} matlab
:caption: MATLAB commands for this session.

[t,y,w,coef] = rectangular_c(2.5,1,5,-30,30,50,0);
[w,F1] = espectro(t, y, 5);
sistema1 = redRC(w, 4*pi);       % H(w) evaluated at ALL the frequencies in w
plot(w, abs(sistema1))           % amplitude spectrum of the system
plot(w, angle(sistema1))         % phase spectrum, in radians
G1 = F1 .* sistema1;             % output in frequency: element-by-element product
[t2,g] = inv_espectro(w, G1, 5); % output in time
wk = [2*pi 6*pi 8*pi]; Hk = H1(wk);   % H1.m is a function: evaluate it where needed
[t,f,tfin] = leeraudio('audio1.wav'); sound(f, 44100)
plot(w/(2*pi), abs(F)); xlim([0 5000]); xlabel('f (Hz)')
```

Note that `F1 .* sistema1` has the dot: it is an element-by-element product of two vectors of the same size ({ref}`matlab-ex4`). The functions `H1` to `H5`, `redRC`, `FiltroA` and `FiltroB` live in `.m` files and are called like any function ({ref}`matlab-ex8`): they receive a frequency vector and return the value of $H$ at each frequency.

(sistemas-ex1)=
## Exercise 1. A pulse train through an RC network

### System and transfer function

A **system** is anything that receives an input signal $f(t)$ and produces an output signal $g(t)$: a cable, a filter, an amplifier. In this course we study **linear time-invariant systems**, which satisfy two properties:

- **Superposition.** If $f_1$ produces $g_1$ and $f_2$ produces $g_2$, then $af_1 + bf_2$ produces $ag_1 + bg_2$.
- **Time invariance.** If $f(t)$ produces $g(t)$, then $f(t - t_0)$ produces $g(t - t_0)$.

A linear system creates no new frequencies: the output contains the same frequencies as the input, each with a different amplitude and phase. What the system does with each frequency is described by its **transfer function** $H(\omega)$, a complex function that does not depend on the input and relates the Fourier integrals of output and input:

$$
H(\omega) = \frac{G(\omega)}{F(\omega)} \qquad\Longleftrightarrow\qquad G(\omega) = H(\omega)\,F(\omega)
$$ (eq-transfer-function-en)

That relation is the key to the whole session. Given the spectrum of the input and $H(\omega)$, the spectrum of the output is their product frequency by frequency, and the output signal is recovered with the inverse transform ({eq}`eq-inverse-integral-en`). Since the properties of the integral also hold for the series, in a periodic signal each coefficient $c_n$ comes out multiplied by $H(\omega_n)$.

### The spectrum of a system

Since $H(\omega)$ is complex, it is written $H(\omega) = |H(\omega)|\,e^{j\theta(\omega)}$ and drawn with two plots, just like a signal ({numref}`table-spectra`): the **amplitude spectrum** $|H(\omega)|$, which is always even, and the **phase spectrum** $\theta(\omega)$, which is always odd. Together they are also called the **frequency response** of the system.

### The RC network

The RC network in the lab is a resistor $R$ followed by a capacitor $C$, with the output taken across the capacitor ({numref}`fig-rc-network`).

```{figure} ../../_static/generated/red_rc.png
---
name: fig-rc-network
alt: RC network with the input v0(t) at the left terminals, a series resistor R, a capacitor C in parallel with the output vs(t) and the current i(t)
width: 60%
align: center
---
RC network: the input $v_0(t)$ is applied to the resistor and the output $v_s(t)$ is taken across the capacitor.
```

Its equations are $v_0(t) = Ri(t) + \frac{1}{C}\int i\,dt$ and $v_s(t) = \frac{1}{C}\int i\,dt$. Applying the Fourier transform to both, using that the integral becomes a division by $j\omega$, and dividing the second by the first, the transfer function is

$$
H(\omega) = \frac{1}{1 + j\,\omega/\omega_0}, \qquad \omega_0 = \frac{1}{RC}
$$ (eq-rc-network-en)

and its modulus and phase are

$$
|H(\omega)| = \frac{1}{\sqrt{1 + (\omega/\omega_0)^2}}, \qquad \theta(\omega) = -\arctan\!\left(\frac{\omega}{\omega_0}\right)
$$ (eq-rc-modulus-phase-en)

At $\omega = 0$ the modulus is 1 and the phase 0: the DC component passes unchanged. As the frequency rises the modulus falls towards 0 without ever vanishing, and the phase falls from 0 to $-\pi/2$. It is a **low-pass filter**: it lets low frequencies through and attenuates high ones. Its only parameter is $\omega_0$, which marks where it starts to attenuate.

### Bandwidth of a system

The **bandwidth of a system** $B_s$ is the range of frequencies the system lets through. It is read on its amplitude spectrum with two criteria, analogous to those for signals:

- **Criterion 1.** If $|H(\omega)|$ never reaches zero, the bandwidth goes from 0 to the frequency at which $|H| = \sqrt{2}/2 = 0.707$. At that frequency the power of a sinusoid is halved, which is expressed as a 3 dB drop. For the RC network, {eq}`eq-rc-modulus-phase-en` gives 0.707 exactly at $\omega = \omega_0$, so $B_s = \omega_0$ rad/s, or $\omega_0/2\pi$ Hz.
- **Criterion 2.** If $|H(\omega)|$ is non-zero only on a finite interval (band-limited system), the bandwidth is the difference between the highest and the lowest frequency of that interval. This is the case of ideal filters.

### Qualitative study: comparing $B$ with $B_s$

Without any calculation, overlaying the amplitude spectrum of the signal (bandwidth $B$) and that of the system ($B_s$) lets you predict the output:

```{list-table} Qualitative effect of a system according to the bandwidths.
:name: table-bandwidth-cases
:header-rows: 1
:widths: 20 80

* - Case
  - Output
* - $B < B_s$
  - A replica of the input, perhaps attenuated or amplified. All its frequencies are multiplied by almost the same constant, $G \approx \text{const}\cdot F$. No distortion.
* - $B \sim B_s$
  - Somewhat distorted, but recognisable.
* - $B > B_s$
  - Strongly distorted. The high frequencies are lost, $G \approx 0\cdot F$ in that region, and the output is left with the bandwidth of the system.
```

```{admonition} Worked example: the train V = 3, τ = 1, T = 4 through two RC networks
:class: note

The train has coefficients $c_n = 3\,\mathrm{sinc}(\pi n/4)$ at $\omega_n = \pi n/2$, first zero at $2\pi$ rad/s and bandwidth $B = 1$ Hz. Evaluate {eq}`eq-rc-modulus-phase-en` at the harmonic frequencies:

| $n$ | $\omega_n$ (rad/s) | $c_n$ | $\lvert H\rvert$, $\omega_0 = \pi$ | $c_n\lvert H\rvert$ | $\lvert H\rvert$, $\omega_0 = 20\pi$ | $c_n\lvert H\rvert$ |
|---|---|---|---|---|---|---|
| 0 | 0 | 3 | 1 | 3 | 1 | 3 |
| 1 | 1.571 | 2.701 | 0.894 | 2.416 | 1.000 | 2.700 |
| 2 | 3.142 | 1.910 | 0.707 | 1.350 | 0.999 | 1.907 |
| 3 | 4.712 | 0.900 | 0.555 | 0.499 | 0.997 | 0.898 |

- With $\omega_0 = \pi$ rad/s, $B_s = 0.5$ Hz $< B$. The harmonics are each attenuated differently (the third loses almost half) and the shape of the pulse changes: distortion.
- With $\omega_0 = 20\pi$ rad/s, $B_s = 10$ Hz $> B$. All harmonics come out multiplied by a number between 0.99 and 1: the output is a replica of the input.
```

### Simulating the system with `espectro` and `inv_espectro`

The numerical computation follows relation {eq}`eq-transfer-function-en` step by step: obtain the spectrum $F$ of the signal with `espectro`, evaluate $H$ on the **same frequency vector** `w`, multiply element by element, `G = F.*H`, and go back to time with `inv_espectro`. Two details matter:

- `w` contains negative and positive frequencies, and $H$ must be evaluated at all of them. A real system satisfies $H(-\omega) = H(\omega)^*$, which is the same as saying that $|H|$ is even and $\theta$ is odd. The RC network satisfies this by itself.
- The output spectrum has the **same lines** as the input one, at the same frequencies, each multiplied by $|H(\omega_n)|$. Comparing `abs(F1)` with `abs(G1)` shows which harmonics have survived.

```{admonition} Statement
:class: important

Consider a time signal made of a **rectangular pulse train** with period $T = 5$, pulse amplitude $V = 2.5$, pulse width $\tau = 1$ and centred at $t = 0$.

a) Plot it from $t_{min} = -30$ to $t_{max} = 30$ seconds using the function `rectangular_c.m` provided in session 3, summing 50 harmonics.

b) Compute the values of the Fourier series coefficients (`F1`) and the frequencies (`w`) using the function `espectro`.

c) Evaluate the function (which represents the transfer function of an RC system and is provided in the file `redRC.m`; e.g. `sistema1 = redRC(w,4*pi)`)

$$
H(\omega) = \frac{1}{1 + \dfrac{\omega}{\omega_0}\,j}
$$

at the frequencies (`w`) obtained in part b). Plot the amplitude spectrum (e.g. `plot(w,abs(sistema1))`) and phase spectrum (e.g. `plot(w,angle(sistema1))`) for the following values of $\omega_0$:

- $\omega_0 = 4\pi/6$
- $\omega_0 = 4\pi$
- $\omega_0 = 100\pi$

Analyse the spectra in each situation and interpret in which cases the signal of part a) will be distorted and in which it will not.

d) To simulate the signal after passing through the system you only need to use the relation $G(\omega) = F(\omega) \cdot H(\omega)$. Thus `G1 = F1.*sistema1` gives the value of the Fourier integral of the received signal. Plot the amplitude spectra of the signal before (`F1`) and after (`G1`) passing through the systems analysed above (the one assigned to you for the submission). What is the effect of the system in the frequency domain in each case?

e) To find out what the signal looks like in the time domain you only need to evaluate the function `inv_espectro` provided in session 3. Obtain and plot the time signals after passing through the corresponding systems. Is the result the expected one in each case? Justify your answer.
```

(sistemas-ex2)=
## Exercise 2. Three harmonics and five systems

### Linear response theorem

If a sinusoid $f(t) = A\cos(\omega_1 t)$ is applied to a linear time-invariant system with transfer function $H(\omega)$, the output is

$$
g(t) = A\,|H(\omega_1)|\cos\big(\omega_1 t + \theta(\omega_1)\big)
$$ (eq-linear-response-en)

That is: the **same frequency**, the amplitude **multiplied by the modulus** of $H$ at that frequency, and the phase **added** to the phase of $H$ at that frequency. If the input sinusoid already has a phase $\varphi$, it is added as well.

```{admonition} Worked example
:class: note

Input $f(t) = 2\cos(4\pi t)$ and a system with $|H(4\pi)| = 0.5$ and $\theta(4\pi) = -\pi/3$. The output is $g(t) = 2 \cdot 0.5\cos(4\pi t - \pi/3) = \cos(4\pi t - \pi/3)$: the amplitude has halved and the sinusoid has been delayed.
```

### Superposition: a sum of harmonics

If the input is a sum of sinusoids, by superposition the output is the sum of the outputs of each one:

$$
f(t) = \sum_k A_k\cos(\omega_k t + \varphi_k) \quad\longrightarrow\quad g(t) = \sum_k A_k\,|H(\omega_k)|\cos\big(\omega_k t + \varphi_k + \theta(\omega_k)\big)
$$ (eq-superposition-en)

To apply it you only need to know $H$ at the frequencies the signal contains, nothing more. A negative amplitude, such as $A_2 = -1/2$ in the statement, is left as it is in the formula: the sign is preserved in the output. In MATLAB this is a loop with three iterations, one per harmonic, that accumulates each cosine into a vector.

```{admonition} How to evaluate H only where it matters
:class: tip

The functions `H1.m` to `H5.m` receive a frequency vector. For the plots between 0 and $10\pi$ pass them a fine vector, `w = 0:0.01:10*pi`. For the linear response theorem it is enough to evaluate them at the harmonic frequencies, `Hk = H1([2*pi 6*pi 8*pi])`, and read `abs(Hk)` and `angle(Hk)`.
```

### Impairments: what each spectrum tells you

When passing through a system, a signal may suffer two impairments **without distortion**, which do not change its shape:

- **Attenuation.** All harmonics are multiplied by the same constant smaller than 1. The signal shrinks, but its shape is the same. If the constant is greater than 1 there is amplification.
- **Delay.** All harmonics are delayed by the **same time** $t_d$. The signal comes out identical, but later: $g(t) = f(t - t_d)$. By the shift theorem ({eq}`eq-shift-en`), that corresponds to a phase $\theta(\omega) = -\omega t_d$, a straight line with slope $-t_d$.

And two **with distortion**, which do change the shape:

- **Attenuation distortion.** Each harmonic is attenuated differently, because $|H|$ varies with frequency.
- **Delay distortion** (or phase distortion). Each harmonic is delayed by a different time, because the phase is not a straight line through the origin.

```{admonition} Delay is not phase shift
:class: warning

Two harmonics can have different phase shifts and the same delay. The delay of the harmonic with frequency $\omega_k$ is $t_d = -\theta(\omega_k)/\omega_k$. If $\theta(2\pi) = -0.2\pi$ and $\theta(6\pi) = -0.6\pi$, the phase shifts differ but both delays equal 0.1 s: no distortion. If instead $\theta(2\pi) = \theta(6\pi) = -0.2\pi$, the delays are 0.1 s and 0.033 s: the second harmonic arrives before the first and the shape changes.
```

All of this is read directly on the two plots of $H$:

```{list-table} Reading the impairments on the spectra of a system.
:name: table-impairments
:header-rows: 1
:widths: 28 32 40

* - $\lvert H(\omega)\rvert$
  - $\theta(\omega)$
  - Impairment
* - Constant equal to 1
  - Linear, slope $-t_d$
  - Delay only. Ideal medium.
* - Constant smaller than 1
  - Linear
  - Attenuation and delay, no distortion.
* - Constant greater than 1
  - Linear
  - Amplification and delay, no distortion.
* - Varying with $\omega$
  - Any
  - Attenuation distortion.
* - Any
  - Non-linear, or constant other than 0
  - Delay distortion.
```

An identically zero phase is a particular case of a straight line with slope 0: zero delay, no delay distortion. Keep in mind that `angle` returns the phase between $-\pi$ and $\pi$: a line with a large slope will appear on the plot as a sawtooth. If you have the expression of $H$, it is more reliable to read the phase from it than from the plot.

### Simulating it with `espectro` and `inv_espectro`

The signal in the statement, with frequencies of 1, 3 and 4 Hz, is periodic, with the common period of its harmonics ({ref}`fourier-ex1`). Therefore `espectro` returns a line spectrum, one line per harmonic, and multiplying each line by $H(\omega_n)$ is exactly applying {eq}`eq-superposition-en` harmonic by harmonic. Both routes must give the same output. The practical difference is that the numerical route needs $H$ defined on the **whole** vector `w`, including negative frequencies, with $H(-\omega) = H(\omega)^*$; if a function only makes sense for $\omega \ge 0$, the negative half has to be completed with the conjugate before multiplying.

```{admonition} Statement
:class: important

Build a signal made of 3 harmonics on the time interval from 0 to 4 seconds. The harmonic frequencies are $\omega_1 = 2\pi$, $\omega_2 = 6\pi$, $\omega_3 = 8\pi$, the corresponding amplitudes $A_1 = 1$, $A_2 = -1/2$, $A_3 = 1/4$, and in all cases the phase equals 0.

a) Plot the signal in time.

b) Plot the amplitude and phase spectra of the system provided in the function `H1.m` on the frequency interval from 0 to $10\pi$. Analyse whether it will produce any kind of distortion on the signal, or the effect it will have on it. Using the linear response theorem and the superposition principle, evaluate the signal after passing through the system. Plot the signals in the time domain before and after passing through the system.

c) Repeat part b) for the system provided in the function `H2.m`.

d) Repeat part b) for the system provided in the function `H3.m`.

e) Repeat part b) for the system provided in the function `H4.m`.

f) Repeat part b) for the system provided in the function `H5.m`.

g) Could the simulation have been done using the functions `espectro` and `inv_espectro` as in exercise 1? Justify your answer and, if possible, do it in MATLAB.
```

(sistemas-ex3)=
## Exercise 3. Filters on an audio signal

### Filters and cut-off frequency

A **filter** is a system designed to let some frequencies through and remove others. It is classified by the shape of its amplitude spectrum:

- **Low-pass:** $|H| \approx 1$ from 0 up to a frequency $\omega_c$, and $\approx 0$ above it. The RC network is a gentle low-pass filter.
- **High-pass:** $|H| \approx 0$ below $\omega_c$ and $\approx 1$ above it. It removes the DC component and the bass.
- **Band-pass:** $|H| \approx 1$ only between two frequencies $\omega_1$ and $\omega_2$.

The **cut-off frequency** $\omega_c$ separates the region that passes from the one that does not. In this lab it is identified with the bandwidth of the system, read with the first-zero-crossing criterion on the amplitude spectrum. To tell what type a filter is, it is enough to plot `abs(H)` and look at where it equals 1 and where it equals 0.

```{admonition} Worked example
:class: note

A signal has two components, at 500 Hz and 3000 Hz, and passes through a low-pass filter with cut-off frequency 1000 Hz. In the output spectrum the 500 Hz line remains, because it is inside the pass band, and the 3000 Hz line disappears. With a high-pass filter of the same cut-off frequency the opposite would happen.
```

```{admonition} Install the Signal Processing Toolbox before the session
:class: warning

The filters `FiltroA.m` and `FiltroB.m` are built with MATLAB's `butter` function, which is not part of the basic installation but of the **Signal Processing Toolbox** add-on. If calling the filter gives an error such as *Unrecognized function or variable 'butter'*, install it from the **Home** tab, **Add-Ons** button, **Get Add-Ons**, searching for "Signal Processing Toolbox". With the university licence it is free of charge, but the download takes a few minutes: do it before the session.
```

### An audio signal is a sampled signal

The file `audio1.wav` contains a sound signal sampled at $f_s = 44100$ samples per second. `leeraudio` returns the time vector `t`, the values `f` and the duration `tfin`. The signal is not periodic, so when calling `espectro` the period argument is an adjustable parameter, and the handout says to use `tfin`. The frequencies returned by `espectro` are in rad/s; to interpret them in Hz, which is how sound is described, plot against `w/(2*pi)` and limit the axis with `xlim`, because the vector reaches tens of thousands of rad/s and the interesting part lies in the first few kilohertz.

The effect of a filter on the audio can be both seen and heard. On the spectrum, comparing `abs(G)` with `abs(F)` shows the region the filter removes. When listening with `sound`, a low-pass filter leaves a muffled sound, as if through a wall, because it removes the treble; a high-pass filter leaves a weak, metallic sound, because it removes the bass, where most of the energy of a voice lies. If the filtered signal is very weak, it can be scaled before listening, for example `sound(g/max(abs(g)), 44100)`.

```{admonition} Statement
:class: important

In this exercise we are going to check the effect of several filters (systems) on a signal. To do so, we will use a sound signal provided in the file `audio1.wav`.

To load the signal in MATLAB the function `leeraudio.m` is provided. It is used as follows: `[t,f,tfin] = leeraudio('audio1.wav');`

This way we get in `t` a time vector, in `f` the values of the signal and in `tfin` how much time is represented. To listen to it you only need to run `sound(f,44100)`.

a) Using the function `espectro`, compute the spectrum of the signal and plot its amplitude spectrum (use the value `tfin` obtained for the signal as the period parameter).

b) A transfer function has been implemented in the function `FiltroA.m`. Plot its amplitude spectrum at the signal frequencies obtained in the previous part with the function `espectro`. What kind of filter is it? And what is its cut-off frequency? NOTE: the cut-off frequency of the filter is equivalent to the bandwidth of the system, using the first-zero-crossing criterion on its spectrum.

c) Evaluate the Fourier integral of the signal after passing through the system in the same way as in exercise 1.d. Plot the amplitude spectrum of the resulting signal and compare the result with the spectrum of the initial signal. Then bring the signal back to the time domain using the function `inv_espectro` and listen to it to analyse the result.

d) Repeat steps b) and c) with the transfer function defined in `FiltroB.m`.
```

```{admonition} Session summary
:class: seealso

- A linear time-invariant system is described by its transfer function $H(\omega) = G(\omega)/F(\omega)$, unique to each system and independent of the input. The output in frequency is $G = H\cdot F$, and in time it is recovered with the inverse transform.
- The spectrum of a system is two plots: $|H(\omega)|$, even, and $\theta(\omega)$, odd. A real system satisfies $H(-\omega) = H(\omega)^*$.
- RC network: $H = 1/(1 + j\omega/\omega_0)$, a low-pass filter with $|H(\omega_0)| = 0.707$. Its bandwidth by criterion 1 is $B_s = \omega_0$ rad/s.
- Comparing $B$ with $B_s$ predicts the output: $B < B_s$ replica, $B \sim B_s$ somewhat distorted, $B > B_s$ strongly distorted and limited to the bandwidth of the system.
- Linear response theorem: $A\cos(\omega_1 t) \to A|H(\omega_1)|\cos(\omega_1 t + \theta(\omega_1))$. With superposition, a sum of harmonics is handled harmonic by harmonic, and it is the same computation as `G = F.*H`.
- Without distortion: attenuation ($|H|$ constant) and delay ($\theta = -\omega t_d$, linear). With distortion: attenuation distortion ($|H|$ varying) and delay distortion ($\theta$ non-linear). Delay $= -\theta(\omega)/\omega$; if it is the same for all harmonics, there is no delay distortion.
- A filter is classified by where $|H|$ equals 1 and where it equals 0: low-pass, high-pass, band-pass. Its cut-off frequency is its bandwidth.
- An audio signal is a non-periodic sampled signal: in `espectro` use `tfin` as the period and read the frequencies in Hz with `w/(2*pi)`.
```
