# Sesión 3. Espectros de señales periódicas y no periódicas: integral de Fourier

Cada ejercicio de esta sesión lleva delante la teoría que necesitas para hacerlo, y nada más. Trabajarás con los ficheros `rectangular_c.m`, `espectro.m` e `inv_espectro.m` que se proporcionan en la práctica. La notación es la de los apuntes del Tema 2, y se da por sabido lo visto en la {ref}`sesión 2 <fourier-ej2>`.

```{admonition} Objetivos de aprendizaje
:class: tip

- Entender cómo la serie de Fourier se convierte en la integral de Fourier cuando el periodo tiende a infinito.
- Obtener la integral de Fourier de un pulso a partir de los coeficientes de su tren periódico.
- Distinguir un espectro discreto de uno continuo, y leer en ambos el ancho de banda y la componente de continua.
- Calcular espectros numéricamente con `espectro` y recuperar la señal con `inv_espectro`.
- Reconocer cuándo se puede dibujar el espectro en frecuencia y cuándo hay que dibujar el de amplitud.
```

(integral-matlab)=
## Las órdenes de MATLAB que vas a usar

```{code-block} matlab
:caption: Órdenes de MATLAB de la sesión.

[t,y,w,coef] = rectangular_c(5,1,8,-40,40,50,0);  % tren de pulsos; el último argumento es t0
[w1,F1] = espectro(t, y, 8);     % espectro numérico de la señal y, con periodo 8
figure; plot(w1, F1); hold on; stem(w, coef)   % curva y líneas en la misma figura
plot(w1, abs(F1))                % módulo: espectro en amplitud
plot(w1, angle(F1))              % fase, en radianes
max(abs(imag(F1)))               % ¿tiene F1 parte imaginaria apreciable?
[t2,y2] = inv_espectro(w1, F1, 8);  % vuelta al tiempo
xlim([-20 20]); legend('espectro','coef')
```

Las funciones `abs`, `angle`, `real` e `imag` se aplican elemento a elemento, como las de la sesión 1 ({ref}`matlab-ej4`). Para evaluar una fórmula sobre un vector de frecuencias se usan `./` y `.^`, igual que en la sesión 2 ({ref}`fourier-matlab`). El orden exacto de los argumentos de cada función de la práctica está en la primera línea de su fichero `.m`: ábrelo antes de llamarla ({ref}`matlab-ej8`).

```{admonition} La fórmula del sinc en MATLAB
:class: warning

Si escribes `F2 = 5*sin(w/2)./(w/2)` y el vector `w` contiene el 0, en esa posición MATLAB calcula $0/0$ y devuelve `NaN`, y ese punto desaparece de la gráfica. Pon el valor a mano con `F2(w==0) = 5`. No uses la función `sinc` de MATLAB sin pensarlo: está definida como $\sin(\pi x)/(\pi x)$, no como $\sin(x)/x$, de modo que $\sin(\omega/2)/(\omega/2)$ se escribe `sinc(w/(2*pi))`.
```

(integral-ej1)=
## Ejercicio 1. Espectro del tren de pulsos y del pulso único

### De la serie a la integral de Fourier

En la sesión 2 viste que un tren de pulsos de periodo $T$ tiene un espectro **discreto**: solo hay coeficientes en las frecuencias $\omega_n = 2\pi n/T$, separadas entre sí $\Delta\omega = 2\pi/T$. Si el periodo crece, los pulsos se alejan unos de otros y las líneas del espectro se juntan, porque $\Delta\omega$ se hace más pequeño. En el límite $T \to \infty$ queda un único pulso, que ya no es periódico, y las líneas se funden en una curva **continua**. Esa curva es la **integral de Fourier** $F(\omega)$:

$$
F(\omega) = \int_{-\infty}^{\infty} f(t)\,e^{-j\omega t}\,dt
$$ (eq-integral-fourier)

Es la misma integral que daba los coeficientes $c_n$ ({eq}`eq-coef-integral`), con dos cambios: se integra en todo el eje de tiempos en lugar de en un periodo, y la frecuencia $\omega$ ya no está restringida a los valores $\omega_n$, sino que puede tomar cualquier valor. Por eso una señal no periódica contiene **todas** las frecuencias y una periódica solo los múltiplos de su fundamental. A $F(\omega)$ también se le llama **transformada de Fourier** de $f(t)$, y se escribe $f(t) \leftrightarrow F(\omega)$.

```{list-table} Serie e integral de Fourier, lado a lado.
:name: tabla-serie-integral
:header-rows: 1
:widths: 30 35 35

* -
  - Señal periódica (serie)
  - Señal no periódica (integral)
* - Frecuencias
  - $\omega_n = 2\pi n/T$, separadas $2\pi/T$
  - $\omega$ continua, separación $\to 0$
* - Espectro
  - Coeficientes $c_n$
  - Función $F(\omega)$
* - Cálculo
  - $c_n = \int_{-T/2}^{T/2} f(t)\,e^{-j\omega_n t}\,dt$
  - $F(\omega) = \int_{-\infty}^{\infty} f(t)\,e^{-j\omega t}\,dt$
* - Tipo de espectro
  - Discreto, se dibuja con `stem`
  - Continuo, se dibuja con `plot`
```

### La integral de Fourier del pulso rectangular

Para un pulso de altura $V$ y anchura $\tau$ centrado en $t = 0$, la integral {eq}`eq-integral-fourier` se resuelve igual que la de los coeficientes del tren, y el resultado es

$$
F(\omega) = V\tau\,\frac{\sin(\omega\tau/2)}{\omega\tau/2} = V\tau\,\mathrm{sinc}(\omega\tau/2)
$$ (eq-pulso-rect)

Compárala con {eq}`eq-coef-rect`: es la misma expresión con $\omega_n$ sustituida por $\omega$. Ese es el atajo de los apuntes: **si conoces los $c_n$ del tren, obtienes $F(\omega)$ del pulso cambiando $\omega_n$ por $\omega$**, sin resolver ninguna integral. Vale para cualquier señal de la que conozcas los coeficientes de su versión periódica. Al revés, los coeficientes del tren son muestras de la curva del pulso, $c_n = F(\omega_n)$, y por eso al superponer `stem(w, coef)` y la curva $F(\omega)$ las líneas caen exactamente sobre ella.

```{admonition} Ejemplo resuelto: V = 3, τ = 1
:class: note

El pulso único tiene $F(\omega) = 3\,\mathrm{sinc}(\omega/2)$. El tren con $T = 4$ del ejemplo de la sesión 2 tenía $c_n = 3\,\mathrm{sinc}(\pi n/4)$ en $\omega_n = \pi n/2$. Al evaluar la curva en esas frecuencias salen los mismos números:

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $\omega_n$ (rad/s) | 0 | 1.571 | 3.142 | 4.712 | 6.283 | 7.854 |
| $F(\omega_n)$ | 3 | 2.701 | 1.910 | 0.900 | 0 | $-0.540$ |
| $c_n$ del tren | 3 | 2.701 | 1.910 | 0.900 | 0 | $-0.540$ |

Con $T = 40$ habría diez veces más líneas en el mismo tramo de frecuencias, y seguirían cayendo sobre la misma curva.
```

### Espectros, ancho de banda y componente de continua

Las definiciones de la sesión 2 ({numref}`tabla-espectros`) se extienden al caso continuo sin cambios: el **espectro en amplitud** es $|F(\omega)|$, el **espectro en fase** es $\theta(\omega)$, con $F(\omega) = |F(\omega)|\,e^{j\theta(\omega)}$, y el **espectro en frecuencia** reúne los dos en una sola gráfica, lo que solo es posible cuando $F(\omega)$ es real pura (el signo lleva la fase, 0 o $\pi$) o imaginaria pura. La expresión {eq}`eq-pulso-rect` es real, así que para el pulso centrado sí se puede dibujar el espectro en frecuencia.

El **ancho de banda** por el primer criterio es la frecuencia del primer cero del espectro. Se obtiene resolviendo $F(\omega) = 0$: el primer cero de $\sin(\omega\tau/2)$ con $\omega > 0$ está en $\omega\tau/2 = \pi$, es decir,

$$
\omega_{AB} = \frac{2\pi}{\tau}\ \text{rad/s}, \qquad f_{AB} = \frac{1}{\tau}\ \text{Hz}
$$ (eq-ancho-banda)

Fíjate en que solo depende de $\tau$, no de $T$. Hay una **relación inversa** entre la anchura del pulso y el ancho de banda: un pulso más estrecho necesita un intervalo de frecuencias más ancho. En un espectro discreto el primer cero se lee sobre la envolvente, y puede coincidir o no con una línea.

La **componente de continua** es el valor del espectro en $\omega = 0$. Como $e^{0} = 1$, la integral {eq}`eq-integral-fourier` en $\omega = 0$ es simplemente $\int f(t)\,dt$: el **área** bajo la señal. Para el pulso rectangular, $F(0) = V\tau$, el área del rectángulo. Para el tren, $c_0 = V\tau$ es el área de un solo periodo, y el nivel de continua que aparece en la señal es $c_0/T$, como viste en {ref}`fourier-ej3`.

```{admonition} Ejemplo resuelto: ancho de banda y continua con V = 3, τ = 1
:class: note

- Pulso único: primer cero en $\omega = 2\pi/1 = 6.28$ rad/s, es decir, 1 Hz. Componente de continua $F(0) = 3 \cdot 1 = 3$.
- Tren con $T = 4$: el mismo primer cero, $2\pi$ rad/s, que coincide con la línea $n = 4$ porque $T/\tau = 4$ es entero. $c_0 = 3$, y el nivel de continua del tren es $c_0/T = 0.75$.
- Si el pulso pasa a $\tau = 0.5$, la expresión es $F(\omega) = 1.5\,\mathrm{sinc}(\omega/4)$: la mitad de alto en $\omega = 0$ y con el primer cero en $4\pi = 12.57$ rad/s (2 Hz), el doble de ancho de banda.
```

### Cálculo numérico: la función `espectro`

La integral de Fourier se puede calcular numéricamente a partir de las muestras de cualquier señal, sin resolver nada a mano. Eso hace `[w, F] = espectro(t, y, T)`: recibe el vector de tiempos `t`, la señal `y` y un periodo `T`, y devuelve un vector de frecuencias `w` y los valores del espectro `F`. Si `y` es periódica, `F` son sus coeficientes $c_n$; si no lo es, `F` son los valores de la integral de Fourier, y `T` es un parámetro ajustable. Es lo que hace un analizador de espectros con una señal real.

Al ser un cálculo numérico, `F` sale como un vector de números complejos, con pequeñas diferencias respecto a la fórmula exacta. Donde la fórmula da 0 exacto, `F` dará algo del orden de $10^{-15}$, y la parte imaginaria de una señal centrada será de ese mismo orden. Comprueba su tamaño con `max(abs(imag(F)))` antes de decidir si el espectro es real.

### Desplazar el pulso en el tiempo

El **teorema de desplazamiento** de la sesión 2 vale igual con $\omega$ en lugar de $\omega_n$: si $f(t) \leftrightarrow F(\omega)$, entonces

$$
f(t - t_0) \leftrightarrow e^{-j\omega t_0}\,F(\omega)
$$ (eq-desplazamiento)

El factor $e^{-j\omega t_0}$ tiene módulo 1, así que **el espectro en amplitud no cambia** al retrasar la señal: $|e^{-j\omega t_0} F(\omega)| = |F(\omega)|$. Lo que cambia es la fase, que pasa a ser $\theta(\omega) - \omega t_0$, y con ella $F(\omega)$ deja de ser real: cada valor adquiere parte real e imaginaria. Entonces ya no se puede dibujar el espectro en frecuencia, y hay que dibujar por separado el de amplitud, `abs(F)`, y el de fase, `angle(F)`.

```{admonition} Ejemplo resuelto: V = 3, τ = 1, T = 4, retraso t₀ = 0.5 s
:class: note

Aquí $\omega_n t_0 = \pi n/4$. Son los mismos giros que en el ejemplo de la sesión 2, ahora leídos como espectros:

| $n$ | 1 | 2 | 3 |
|---|---|---|---|
| $c_n$ sin desplazar | 2.701 | 1.910 | 0.900 |
| $c_n$ desplazado | $1.910 - 1.910j$ | $-1.910j$ | $-0.637 - 0.637j$ |
| $\lvert c_n \rvert$ | 2.701 | 1.910 | 0.900 |
| $\theta_n$ | $-\pi/4$ | $-\pi/2$ | $-3\pi/4$ |

El espectro en amplitud es idéntico al de la señal centrada. Los $c_n$ desplazados tienen parte real e imaginaria no nulas, y ni siquiera comparten tipo entre sí: $c_2$ es imaginario puro y $c_1$ no. No hay un solo número por frecuencia que recoja toda la información.
```

```{admonition} Enunciado
:class: important

Se considera una señal temporal compuesta por un **tren de pulsos rectangulares** con periodo $T = 8$, amplitud de los pulsos $V = 5$, ancho de pulsos $\tau = 1$ y centrada en $t = 0$.

a) Representarla gráficamente desde $t_{min} = -40$ hasta $t_{max} = 40$ segundos utilizando la función `rectangular_c.m` proporcionada en esta práctica, y considerando que se suman 50 armónicos.

b) Calcular los valores de los coeficientes de la serie de Fourier utilizando la función `espectro` proporcionada en esta práctica y comprobar que son aproximadamente los mismos que se obtienen en el vector `coef` que proporciona `rectangular_c.m`. Para ello representar gráficamente los espectros mediante `plot(w,F1)` y `stem(w,coef)` y comprobarlo superponiéndolos. Mostrar la gráfica con los espectros superpuestos.

La función `[w, F1] = espectro(t, y, T)` es de uso general: sirve para calcular los coeficientes de la serie de Fourier si la señal `y` que se le suministra es periódica, o los valores de la integral de Fourier si se le suministra una señal `y` no periódica. `t` es el vector de tiempos, `y` es un vector con los valores de la señal temporal de la que se quiere calcular los coeficientes (o la integral de Fourier) y `T` es el periodo de la señal (si la señal es no periódica, este es un parámetro ajustable). La función devuelve un vector de frecuencias `w` y los correspondientes valores de los coeficientes o de la integral de Fourier `F`.

c) Superponer a los espectros del apartado anterior la representación gráfica de la siguiente función, que es la integral de Fourier de un **único pulso rectangular (no periódico)**. Utilizar como vector de frecuencias el proporcionado por la función `espectro` en el apartado anterior.

$$
F_2(\omega) = 5\,\frac{\mathrm{sen}(\omega/2)}{\omega/2}
$$

¿Por qué este último espectro es continuo y los del apartado anterior son discretos?

¿Cuál es el ancho de banda de la señal del tren de pulsos rectangulares y del pulso rectangular único (no periódico)? Obtener su valor directamente de los espectros y comprobar que coincide con el valor que se obtendría analíticamente.

¿Cuál es la componente de continua (valor del coeficiente $c_0$) de cada una de las señales?

¿Cómo se modificaría la expresión de $F_2(\omega)$ si el pulso rectangular tuviera una duración de 0.3 segundos? (Simplemente escribir la nueva $F_2(\omega)$; no se trata de repetir el ejercicio con 0.3.)

d) Considerar ahora la señal periódica del tren de pulsos rectangulares con las mismas características que en a) pero **retrasada en el tiempo** una cantidad $t_0 = 2$. Utilizar la función `rectangular_c.m` para crearla y calcular los valores de los coeficientes de la serie de Fourier utilizando la función `espectro`. Representar el espectro en **amplitud** y comprobar y explicar por qué no es posible representar el espectro en frecuencia.
```

(integral-ej2)=
## Ejercicio 2. Transformada de Fourier inversa

### Volver del espectro a la señal

La integral de Fourier no pierde información: a partir de $F(\omega)$ se recupera $f(t)$ con la **transformada inversa**,

$$
f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega)\,e^{j\omega t}\,d\omega
$$ (eq-integral-inversa)

Es la versión continua de la serie {eq}`eq-serie-compleja`: la suma de exponenciales $e^{j\omega_n t}$ pesadas por $c_n/T$ se convierte en una integral de exponenciales $e^{j\omega t}$ pesadas por $F(\omega)/2\pi$. Las dos descripciones de la señal, en el tiempo y en la frecuencia, son equivalentes, y se puede pasar de una a otra en los dos sentidos. En la práctica ese paso lo da `inv_espectro`, que recibe el vector de frecuencias, los valores del espectro y un periodo, y devuelve el vector de tiempos y la señal reconstruida.

Como el cálculo es numérico, la señal reconstruida tiene una parte imaginaria residual del orden de $10^{-15}$. Dibuja `real(y)`, como hacías con `rectangular_b.m`.

### Leer los parámetros del pulso en su espectro

Para comprobar que la señal recuperada es la correcta basta con mirar dos cosas en la fórmula {eq}`eq-pulso-rect`:

- La altura del espectro en $\omega = 0$ es $F(0) = V\tau$, el área del pulso.
- El primer cero está en $\omega = 2\pi/\tau$, lo que fija $\tau$.

Con esos dos datos salen $\tau$ y $V$, y deben coincidir con la anchura y la altura del pulso que aparece en la gráfica temporal.

```{admonition} Ejemplo resuelto
:class: note

Un espectro vale 6 en $\omega = 0$ y tiene su primer cero en $\omega = \pi$ rad/s. Entonces $2\pi/\tau = \pi$ da $\tau = 2$ s, y $V\tau = 6$ da $V = 3$. La señal en el tiempo debe ser un pulso de altura 3 y anchura 2.
```

```{admonition} Enunciado
:class: important

Obtener las señales en el tiempo cuyas integrales de Fourier son las del ejercicio anterior, $F_1(\omega)$ y $F_2(\omega)$, utilizando la función proporcionada en esta sesión `inv_espectro` para el cálculo de la transformada de Fourier inversa, y representarlas gráficamente. Comprobar que, como es lógico, la transformada de Fourier inversa de $F_1(\omega)$ es la señal temporal del tren de pulsos original que se utilizó para calcular $F_1(\omega)$, y la transformada inversa de $F_2(\omega)$ es un único pulso rectangular no periódico.

Comprobar en ambas representaciones gráficas que las amplitudes y duraciones de los pulsos rectangulares sobre las figuras son coherentes con los valores numéricos de los parámetros que aparecen en las integrales de Fourier.

NOTA: en la función `inv_espectro` utilizar como vector de frecuencias el proporcionado por la función `espectro` en el apartado b) del ejercicio anterior.

NOTA: cuando se aplica la función `inv_espectro` a la integral de Fourier $F_2(\omega)$, puesto que se trata de una señal temporal no periódica, utilizar el valor de $T = 80$ en el argumento de la función correspondiente al periodo, para una mejor visualización de los resultados.
```

(integral-ej3)=
## Ejercicio 3. Pulso y tren de pulsos triangulares

### El pulso triangular y su espectro

El pulso triangular tiene altura $V$ en $t = 0$ y base $2\tau$, de $-\tau$ a $\tau$. Su integral de Fourier se obtiene del coeficiente del tren triangular de la sesión 2 ({eq}`eq-coef-tri`) con el mismo atajo de antes, cambiar $\omega_n$ por $\omega$:

$$
F(\omega) = V\tau\,\mathrm{sinc}^2(\omega\tau/2) = V\tau\left[\frac{\sin(\omega\tau/2)}{\omega\tau/2}\right]^2
$$ (eq-pulso-tri)

Es el mismo sinc del pulso rectangular, elevado al cuadrado. Eso tiene tres consecuencias que verás en la gráfica: nunca es negativo, así que fase y amplitud coinciden; los lóbulos laterales son mucho más pequeños, porque los valores menores que 1 se hacen aún menores al elevarlos al cuadrado; y los ceros están en los mismos sitios, de modo que el ancho de banda sigue siendo $2\pi/\tau$. La componente de continua es $F(0) = V\tau$, que es el área del triángulo, $\tfrac12 \cdot 2\tau \cdot V$.

```{admonition} Ejemplo resuelto: V = 3, τ = 1, T = 4
:class: note

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $\mathrm{sinc}(\pi n/4)$ | 1 | 0.900 | 0.637 | 0.300 | 0 | $-0.180$ |
| $c_n$ rectangular $= 3\,\mathrm{sinc}$ | 3 | 2.701 | 1.910 | 0.900 | 0 | $-0.540$ |
| $c_n$ triangular $= 3\,\mathrm{sinc}^2$ | 3 | 2.432 | 1.216 | 0.270 | 0 | 0.097 |

Los dos espectros arrancan en 3 y se anulan en $n = 4$, pero el triangular cae mucho más deprisa y no cambia de signo.
```

### Qué hay que tocar en `rectangular_c.m`

El cambio es el mismo que hiciste en la sesión 2 con `rectangular.m` ({ref}`fourier-ej4`): guardar una copia con otro nombre, cambiar el nombre de la función en la primera línea y sustituir la línea que calcula cada coeficiente por la expresión {eq}`eq-coef-tri`, elevando el sinc al cuadrado. Revisa también el coeficiente del armónico 0, que sigue valiendo $V\tau$. El resto del fichero, incluido el desplazamiento $t_0$, no cambia.

Para generar un **pulso único** con una función que suma una serie, el truco del guion es usar un periodo $T$ mucho mayor que el intervalo de representación: con $T = 80$ y el tiempo de $-40$ a $40$ solo cabe un pulso en pantalla. El espectro que calcula `espectro` sigue siendo discreto, con líneas cada $2\pi/80 \approx 0.079$ rad/s, pero están tan juntas que `plot` dibuja una curva prácticamente continua: es la transición $T \to \infty$ de la {numref}`tabla-serie-integral` vista en la práctica.

### Simetrías y desplazamiento

Los apuntes dan tres propiedades de paridad que explican todo lo que vas a ver en las gráficas:

- Si $f(t)$ es **par**, con $f(-t) = f(t)$, su integral de Fourier es **real pura y par**. El pulso centrado, rectangular o triangular, es par.
- Si $f(t)$ es **impar**, con $f(-t) = -f(t)$, su integral de Fourier es **imaginaria pura e impar**.
- Para cualquier señal, el espectro en amplitud $|F(\omega)|$ es siempre **par** y el espectro en fase $\theta(\omega)$ es siempre **impar**.

Al desplazar el pulso en el tiempo deja de ser par, y según {eq}`eq-desplazamiento` su espectro adquiere el factor $e^{-j\omega t_0}$: el espectro en amplitud sigue siendo el mismo, pero $F(\omega)$ ya tiene parte real e imaginaria, y solo se puede dibujar el de amplitud.

### Variar τ

La relación inversa entre tiempo y frecuencia de los apuntes se escribe $f(t/a) \leftrightarrow a\,F(a\omega)$: estirar la señal en el tiempo comprime su espectro, y al revés. Para el triángulo, cambiar $\tau$ mueve el primer cero a $2\pi/\tau$ y la altura en $\omega = 0$ a $V\tau$, tanto en el pulso único como en el tren, porque ninguno de los dos valores depende de $T$. Ten en cuenta que la base del triángulo es $2\tau$: si mides el ancho del pulso en la gráfica temporal y obtienes 2, es que $\tau = 1$.

```{admonition} Ejemplo resuelto: V = 3, tres valores de τ
:class: note

| $\tau$ | Base $2\tau$ | $F(0) = V\tau$ | Primer cero $2\pi/\tau$ (rad/s) | Ancho de banda (Hz) |
|---|---|---|---|---|
| 0.5 | 1 | 1.5 | $4\pi = 12.57$ | 2 |
| 1 | 2 | 3 | $2\pi = 6.28$ | 1 |
| 2 | 4 | 6 | $\pi = 3.14$ | 0.5 |

Pulso el doble de ancho, mitad de ancho de banda. En un tren con $T = 10$ la línea que se anula es $n = T/\tau$: 20, 10 y 5.
```

```{admonition} Enunciado
:class: important

Representar gráficamente el **espectro en amplitud de un pulso triangular (no periódico)** y de **un tren de pulsos triangulares periódico** utilizando la función `espectro` proporcionada en la práctica.

Para ello, en primer lugar hay que generar la señal temporal modificando la función `rectangular_c.m` introduciendo el coeficiente de Fourier para la señal triangular, y para el caso de pulso **no periódico** utilizar un periodo $T$ grande para que únicamente se genere un pulso. Concretamente, considerar para la señal temporal: $T = 80$, amplitud de los pulsos $V = 5$, ancho de pulsos $\tau = 1$, dominio de representación desde $t_{min} = -40$ hasta $t_{max} = 40$, centrada en $t = 0$ y sumar 400 armónicos. Para el caso de un **tren de pulsos periódicos**, se puede utilizar $T = 10$, manteniendo el resto de parámetros constantes.

Una vez generada la señal temporal, a continuación hay que llamar a la función `espectro`, y finalmente hacer `plot(w,abs(F))` para representar gráficamente el espectro en amplitud. Comparar ambos espectros e indicar las simetrías que presentan y si son continuos o discretos.

¿Qué ocurre si tanto la señal periódica como la no periódica se desplazan temporalmente respecto a $t = 0$? Crearlas y representar nuevamente los espectros en amplitud. ¿Es posible ahora representar el espectro en frecuencia? ¿Por qué?

Manteniendo el resto de parámetros constantes, variar el $\tau$ (hacer tres variaciones) y comentar su influencia en el ancho de banda de la señal.
```

```{admonition} Resumen de la sesión
:class: seealso

- La integral de Fourier $F(\omega) = \int f(t)\,e^{-j\omega t}\,dt$ es el límite de la serie cuando $T \to \infty$: las líneas separadas $2\pi/T$ se funden en una curva continua. Una señal no periódica contiene todas las frecuencias.
- Si conoces los $c_n$ del tren, $F(\omega)$ del pulso sale cambiando $\omega_n$ por $\omega$. Al revés, $c_n = F(\omega_n)$: las líneas del tren caen sobre la curva del pulso.
- Pulso rectangular: $F(\omega) = V\tau\,\mathrm{sinc}(\omega\tau/2)$. Pulso triangular: $F(\omega) = V\tau\,\mathrm{sinc}^2(\omega\tau/2)$, con base $2\tau$.
- Ancho de banda (primer criterio): $\omega_{AB} = 2\pi/\tau$ rad/s, o $1/\tau$ Hz. Depende de $\tau$ y no de $T$; pulso estrecho, mucho ancho de banda.
- Componente de continua: $F(0)$, el área bajo la señal. Vale $V\tau$ para el pulso rectangular y para el triangular. En el tren, $c_0 = V\tau$ es el área de un periodo.
- `espectro(t, y, T)` calcula el espectro numéricamente: coeficientes si `y` es periódica, integral de Fourier si no. `inv_espectro` hace el camino inverso con $f(t) = \frac{1}{2\pi}\int F(\omega)\,e^{j\omega t}\,d\omega$.
- Retrasar $t_0$ multiplica el espectro por $e^{-j\omega t_0}$: el espectro en amplitud no cambia, la fase sí, y $F(\omega)$ deja de ser real.
- El espectro en frecuencia solo se puede dibujar si $F(\omega)$ es real pura o imaginaria pura. Si tiene parte real e imaginaria, se dibujan `abs(F)` y `angle(F)` por separado.
- Señal par: espectro real y par. Señal impar: espectro imaginario puro e impar. Siempre: $|F(\omega)|$ par y $\theta(\omega)$ impar.
```
