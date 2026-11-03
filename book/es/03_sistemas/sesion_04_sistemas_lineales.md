# Sesión 4. Señales a través de sistemas lineales estacionarios y distorsiones

Cada ejercicio de esta sesión lleva delante la teoría que necesitas para hacerlo, y nada más. Trabajarás con los ficheros `rectangular_c.m`, `espectro.m` e `inv_espectro.m` de la sesión 3, y con los nuevos `redRC.m`, `H1.m` a `H5.m`, `leeraudio.m`, `FiltroA.m` y `FiltroB.m`. La notación es la de los apuntes del Tema 2, y se da por sabido lo visto en la {ref}`sesión 3 <integral-ej1>`.

```{admonition} Objetivos de aprendizaje
:class: tip

- Describir un sistema lineal estacionario por su función de transferencia $H(\omega)$ y leer sus espectros en amplitud y fase.
- Obtener el ancho de banda de un sistema y predecir, comparándolo con el de la señal, si habrá distorsión.
- Simular el paso de una señal por un sistema con la relación $G(\omega) = H(\omega)F(\omega)$ y recuperar la salida en el tiempo.
- Aplicar el teorema de respuesta lineal y el principio de superposición a una suma de armónicos.
- Reconocer en los espectros de un sistema la atenuación, el retardo, la distorsión de atenuación y la distorsión de retardo.
- Analizar el efecto de un filtro sobre una señal de audio real.
```

(sistemas-matlab)=
## Las órdenes de MATLAB que vas a usar

```{code-block} matlab
:caption: Órdenes de MATLAB de la sesión.

[t,y,w,coef] = rectangular_c(2.5,1,5,-30,30,50,0);
[w,F1] = espectro(t, y, 5);
sistema1 = redRC(w, 4*pi);       % H(w) evaluada en TODAS las frecuencias de w
plot(w, abs(sistema1))           % espectro en amplitud del sistema
plot(w, angle(sistema1))         % espectro en fase, en radianes
G1 = F1 .* sistema1;             % salida en frecuencia: producto elemento a elemento
[t2,g] = inv_espectro(w, G1, 5); % salida en el tiempo
wk = [2*pi 6*pi 8*pi]; Hk = H1(wk);   % H1.m es una funcion: se evalua donde haga falta
[t,f,tfin] = leeraudio('audio1.wav'); sound(f, 44100)
plot(w/(2*pi), abs(F)); xlim([0 5000]); xlabel('f (Hz)')
```

Fíjate en que `F1 .* sistema1` lleva el punto: es un producto elemento a elemento entre dos vectores del mismo tamaño ({ref}`matlab-ej4`). Las funciones `H1` a `H5`, `redRC`, `FiltroA` y `FiltroB` están en ficheros `.m` y se llaman como cualquier función ({ref}`matlab-ej8`): reciben un vector de frecuencias y devuelven el valor de $H$ en cada una.

(sistemas-ej1)=
## Ejercicio 1. Un tren de pulsos a través de una red RC

### Sistema y función de transferencia

Un **sistema** es cualquier cosa que recibe una señal de entrada $f(t)$ y produce una señal de salida $g(t)$: un cable, un filtro, un amplificador. En esta asignatura se estudian los **sistemas lineales estacionarios**, que cumplen dos propiedades:

- **Superposición.** Si $f_1$ produce $g_1$ y $f_2$ produce $g_2$, entonces $af_1 + bf_2$ produce $ag_1 + bg_2$.
- **Invariancia en el tiempo.** Si $f(t)$ produce $g(t)$, entonces $f(t - t_0)$ produce $g(t - t_0)$.

Un sistema lineal no crea frecuencias nuevas: la salida contiene las mismas frecuencias que la entrada, cada una con otra amplitud y otra fase. Lo que hace el sistema con cada frecuencia lo describe su **función de transferencia** $H(\omega)$, una función compleja que no depende de la entrada y que relaciona las integrales de Fourier de salida y entrada:

$$
H(\omega) = \frac{G(\omega)}{F(\omega)} \qquad\Longleftrightarrow\qquad G(\omega) = H(\omega)\,F(\omega)
$$ (eq-funcion-transferencia)

Esa relación es la clave de toda la sesión. Conocidos el espectro de la entrada y $H(\omega)$, el espectro de la salida es su producto frecuencia a frecuencia, y la señal de salida se recupera con la transformada inversa ({eq}`eq-integral-inversa`). Como las propiedades de la integral valen también para la serie, en una señal periódica cada coeficiente $c_n$ sale multiplicado por $H(\omega_n)$.

### El espectro de un sistema

Como $H(\omega)$ es compleja, se escribe $H(\omega) = |H(\omega)|\,e^{j\theta(\omega)}$ y se dibuja con dos gráficas, igual que una señal ({numref}`tabla-espectros`): el **espectro en amplitud** $|H(\omega)|$, que es siempre par, y el **espectro en fase** $\theta(\omega)$, que es siempre impar. Al conjunto se le llama también **respuesta en frecuencia** del sistema.

### La red RC

La red RC de la práctica es una resistencia $R$ seguida de un condensador $C$, con la salida tomada en el condensador ({numref}`fig-red-rc`).

```{figure} ../../_static/generated/red_rc.png
---
name: fig-red-rc
alt: Red RC con la entrada v0(t) en los terminales de la izquierda, una resistencia R en serie, un condensador C en paralelo con la salida vs(t) y la corriente i(t)
width: 60%
align: center
---
Red RC: la entrada $v_0(t)$ se aplica a la resistencia y la salida $v_s(t)$ se toma entre los extremos del condensador.
```

Sus ecuaciones son $v_0(t) = Ri(t) + \frac{1}{C}\int i\,dt$ y $v_s(t) = \frac{1}{C}\int i\,dt$. Al aplicar la transformada de Fourier a ambas, usando que la integral se transforma en una división por $j\omega$, y dividir la segunda entre la primera, la función de transferencia queda

$$
H(\omega) = \frac{1}{1 + j\,\omega/\omega_0}, \qquad \omega_0 = \frac{1}{RC}
$$ (eq-red-rc)

y su módulo y su fase son

$$
|H(\omega)| = \frac{1}{\sqrt{1 + (\omega/\omega_0)^2}}, \qquad \theta(\omega) = -\arctan\!\left(\frac{\omega}{\omega_0}\right)
$$ (eq-modulo-fase-rc)

En $\omega = 0$ el módulo vale 1 y la fase 0: la componente de continua pasa intacta. Al subir la frecuencia el módulo baja hacia 0 sin llegar nunca a anularse, y la fase baja desde 0 hasta $-\pi/2$. Es un **filtro pasabajas**: deja pasar las frecuencias bajas y atenúa las altas. El único parámetro es $\omega_0$, que marca dónde empieza a atenuar.

### Ancho de banda de un sistema

El **ancho de banda de un sistema** $B_s$ es el intervalo de frecuencias que el sistema deja pasar. Se lee en su espectro en amplitud con dos criterios, análogos a los de las señales:

- **Criterio 1.** Si $|H(\omega)|$ nunca llega a cero, el ancho de banda va de 0 hasta la frecuencia en la que $|H| = \sqrt{2}/2 = 0.707$. A esa frecuencia la potencia de una senoide se reduce a la mitad, lo que se expresa como una caída de 3 dB. Para la red RC, {eq}`eq-modulo-fase-rc` da 0.707 justo en $\omega = \omega_0$, así que $B_s = \omega_0$ rad/s, o $\omega_0/2\pi$ Hz.
- **Criterio 2.** Si $|H(\omega)|$ solo es distinto de cero en un intervalo finito (sistema de banda limitada), el ancho de banda es la diferencia entre la frecuencia más alta y la más baja de ese intervalo. Es el caso de los filtros ideales.

### Estudio cualitativo: comparar $B$ con $B_s$

Sin hacer ninguna cuenta, superponiendo el espectro en amplitud de la señal (ancho de banda $B$) y el del sistema ($B_s$) se puede predecir la salida:

```{list-table} Efecto cualitativo de un sistema según los anchos de banda.
:name: tabla-casos-ancho-banda
:header-rows: 1
:widths: 20 80

* - Caso
  - Salida
* - $B < B_s$
  - Réplica de la entrada, quizá atenuada o amplificada. Todas sus frecuencias se multiplican por casi la misma constante, $G \approx \text{cte}\cdot F$. Sin distorsión.
* - $B \sim B_s$
  - Algo distorsionada, pero reconocible.
* - $B > B_s$
  - Fuertemente distorsionada. Las frecuencias altas se pierden, $G \approx 0\cdot F$ en esa zona, y la salida se queda con el ancho de banda del sistema.
```

```{admonition} Ejemplo resuelto: el tren V = 3, τ = 1, T = 4 por dos redes RC
:class: note

El tren tiene coeficientes $c_n = 3\,\mathrm{sinc}(\pi n/4)$ en $\omega_n = \pi n/2$, primer cero en $2\pi$ rad/s y ancho de banda $B = 1$ Hz. Se evalúa {eq}`eq-modulo-fase-rc` en las frecuencias de los armónicos:

| $n$ | $\omega_n$ (rad/s) | $c_n$ | $\lvert H\rvert$, $\omega_0 = \pi$ | $c_n\lvert H\rvert$ | $\lvert H\rvert$, $\omega_0 = 20\pi$ | $c_n\lvert H\rvert$ |
|---|---|---|---|---|---|---|
| 0 | 0 | 3 | 1 | 3 | 1 | 3 |
| 1 | 1.571 | 2.701 | 0.894 | 2.416 | 1.000 | 2.700 |
| 2 | 3.142 | 1.910 | 0.707 | 1.350 | 0.999 | 1.907 |
| 3 | 4.712 | 0.900 | 0.555 | 0.499 | 0.997 | 0.898 |

- Con $\omega_0 = \pi$ rad/s, $B_s = 0.5$ Hz $< B$. Los armónicos se atenúan cada uno de forma distinta (el tercero pierde casi la mitad) y la forma del pulso cambia: distorsión.
- Con $\omega_0 = 20\pi$ rad/s, $B_s = 10$ Hz $> B$. Todos los armónicos salen multiplicados por un número entre 0.99 y 1: la salida es una réplica de la entrada.
```

### Simular el sistema con `espectro` e `inv_espectro`

El cálculo numérico sigue la relación {eq}`eq-funcion-transferencia` paso a paso: se obtiene el espectro $F$ de la señal con `espectro`, se evalúa $H$ en el **mismo vector de frecuencias** `w`, se multiplican elemento a elemento, `G = F.*H`, y se vuelve al tiempo con `inv_espectro`. Dos detalles importan:

- `w` contiene frecuencias negativas y positivas, y $H$ debe evaluarse en todas. Un sistema real cumple $H(-\omega) = H(\omega)^*$, que es lo mismo que decir que $|H|$ es par y $\theta$ impar. La red RC lo cumple sola.
- El espectro de salida tiene las **mismas líneas** que el de entrada, en las mismas frecuencias, con cada una multiplicada por $|H(\omega_n)|$. Comparar `abs(F1)` con `abs(G1)` es ver qué armónicos han sobrevivido.

```{admonition} Enunciado
:class: important

Se considera una señal temporal compuesta por un **tren de pulsos rectangulares** con periodo $T = 5$, amplitud de los pulsos $V = 2.5$, ancho de pulsos $\tau = 1$ y centrada en $t = 0$.

a) Representarla gráficamente desde $t_{min} = -30$ hasta $t_{max} = 30$ segundos utilizando la función `rectangular_c.m` proporcionada en la sesión 3, y considerando que se suman 50 armónicos.

b) Calcular los valores de los coeficientes (`F1`) de la serie de Fourier y las frecuencias (`w`) utilizando la función `espectro`.

c) Evaluar la función (que representa la función de transferencia de un sistema RC y proporcionada en el fichero `redRC.m`; p. ej. `sistema1 = redRC(w,4*pi)`)

$$
H(\omega) = \frac{1}{1 + \dfrac{\omega}{\omega_0}\,j}
$$

para las frecuencias (`w`) obtenidas en el apartado b). Representar el espectro en amplitud (p. ej. `plot(w,abs(sistema1))`) y fase (p. ej. `plot(w,angle(sistema1))`) para los siguientes valores de $\omega_0$:

- $\omega_0 = 4\pi/6$
- $\omega_0 = 4\pi$
- $\omega_0 = 100\pi$

Analizar en cada una de las situaciones los espectros e interpretar en qué casos se producirán distorsiones de la señal del apartado a) y en cuáles no.

d) Para simular la señal tras pasar por el sistema simplemente hay que hacer uso de la relación $G(\omega) = F(\omega) \cdot H(\omega)$. De esta forma `G1 = F1.*sistema1` nos proporciona el valor de la integral de Fourier de la señal recibida. Representar los espectros en amplitud de la señal antes (`F1`) y después (`G1`) de pasar por los sistemas analizados anteriormente (el que te toque según la entrega). ¿Cuál es el efecto del sistema en el dominio de la frecuencia en cada caso?

e) Para conocer cómo es la señal en el dominio del tiempo solo es necesario evaluar la función `inv_espectro` proporcionada en la sesión 3. Así, obtener y representar las señales en el tiempo tras pasar por los sistemas correspondientes. ¿El resultado es el esperado en cada caso? Justifica tu respuesta.
```

(sistemas-ej2)=
## Ejercicio 2. Tres armónicos y cinco sistemas

### Teorema de respuesta lineal

Si a un sistema lineal estacionario con función de transferencia $H(\omega)$ se le aplica una senoide $f(t) = A\cos(\omega_1 t)$, la salida es

$$
g(t) = A\,|H(\omega_1)|\cos\big(\omega_1 t + \theta(\omega_1)\big)
$$ (eq-respuesta-lineal)

Es decir: la **misma frecuencia**, la amplitud **multiplicada por el módulo** de $H$ en esa frecuencia, y la fase **sumada** a la fase de $H$ en esa frecuencia. Si la senoide de entrada ya tiene una fase $\varphi$, se suma también.

```{admonition} Ejemplo resuelto
:class: note

Entrada $f(t) = 2\cos(4\pi t)$ y un sistema con $|H(4\pi)| = 0.5$ y $\theta(4\pi) = -\pi/3$. La salida es $g(t) = 2 \cdot 0.5\cos(4\pi t - \pi/3) = \cos(4\pi t - \pi/3)$: la amplitud se ha reducido a la mitad y la senoide se ha retrasado.
```

### Superposición: una suma de armónicos

Si la entrada es una suma de senoides, por superposición la salida es la suma de las salidas de cada una:

$$
f(t) = \sum_k A_k\cos(\omega_k t + \varphi_k) \quad\longrightarrow\quad g(t) = \sum_k A_k\,|H(\omega_k)|\cos\big(\omega_k t + \varphi_k + \theta(\omega_k)\big)
$$ (eq-superposicion)

Para aplicarlo solo hace falta conocer $H$ en las frecuencias que contiene la señal, nada más. Una amplitud negativa, como $A_2 = -1/2$ en el enunciado, se deja tal cual en la fórmula: el signo se conserva en la salida. En MATLAB es un bucle de tres vueltas, una por armónico, que acumula cada coseno en un vector.

```{admonition} Cómo evaluar H solo donde importa
:class: tip

Las funciones `H1.m` a `H5.m` reciben un vector de frecuencias. Para las gráficas entre 0 y $10\pi$ se les pasa un vector fino, `w = 0:0.01:10*pi`. Para el teorema de respuesta lineal basta con evaluarlas en las frecuencias de los armónicos, `Hk = H1([2*pi 6*pi 8*pi])`, y leer `abs(Hk)` y `angle(Hk)`.
```

### Perturbaciones: qué dice cada espectro

Al atravesar un sistema, una señal puede sufrir dos perturbaciones **sin distorsión**, que no cambian su forma:

- **Atenuación.** Todos los armónicos se multiplican por la misma constante menor que 1. La señal se encoge, pero su forma es la misma. Si la constante es mayor que 1 hay amplificación.
- **Retardo.** Todos los armónicos se retrasan el **mismo tiempo** $t_d$. La señal sale idéntica, pero más tarde: $g(t) = f(t - t_d)$. Por el teorema de desplazamiento ({eq}`eq-desplazamiento`), eso corresponde a una fase $\theta(\omega) = -\omega t_d$, una recta de pendiente $-t_d$.

Y dos **con distorsión**, que sí cambian la forma:

- **Distorsión de atenuación.** Cada armónico se atenúa de forma distinta, porque $|H|$ varía con la frecuencia.
- **Distorsión de retardo** (o de fase). Cada armónico se retrasa un tiempo distinto, porque la fase no es una recta que pase por el origen.

```{admonition} Retardo no es desfase
:class: warning

Dos armónicos pueden tener desfases distintos y el mismo retardo. El retardo del armónico de frecuencia $\omega_k$ es $t_d = -\theta(\omega_k)/\omega_k$. Si $\theta(2\pi) = -0.2\pi$ y $\theta(6\pi) = -0.6\pi$, los desfases son distintos pero ambos retardos valen 0.1 s: no hay distorsión. Si en cambio $\theta(2\pi) = \theta(6\pi) = -0.2\pi$, los retardos son 0.1 s y 0.033 s: el segundo armónico llega antes que el primero y la forma cambia.
```

Todo esto se lee directamente en las dos gráficas de $H$:

```{list-table} Lectura de las perturbaciones en los espectros de un sistema.
:name: tabla-perturbaciones
:header-rows: 1
:widths: 28 32 40

* - $\lvert H(\omega)\rvert$
  - $\theta(\omega)$
  - Perturbación
* - Constante igual a 1
  - Lineal, pendiente $-t_d$
  - Solo retardo. Medio ideal.
* - Constante menor que 1
  - Lineal
  - Atenuación y retardo, sin distorsión.
* - Constante mayor que 1
  - Lineal
  - Amplificación y retardo, sin distorsión.
* - Variable con $\omega$
  - Cualquiera
  - Distorsión de atenuación.
* - Cualquiera
  - No lineal, o constante distinta de 0
  - Distorsión de retardo.
```

Una fase idénticamente nula es un caso particular de recta con pendiente 0: retardo nulo, sin distorsión de retardo. Ten en cuenta que `angle` devuelve la fase entre $-\pi$ y $\pi$: una recta de pendiente grande aparecerá en la gráfica como dientes de sierra. Si tienes la expresión de $H$, es más fiable leer la fase en ella que en la gráfica.

### Simularlo con `espectro` e `inv_espectro`

La señal del enunciado, con frecuencias de 1, 3 y 4 Hz, es periódica, con el periodo común de sus armónicos ({ref}`fourier-ej1`). Por tanto `espectro` devuelve un espectro de líneas, una por armónico, y multiplicar cada línea por $H(\omega_n)$ es exactamente aplicar {eq}`eq-superposicion` armónico a armónico. Los dos caminos tienen que dar la misma salida. La diferencia práctica es que el camino numérico necesita $H$ definida en **todo** el vector `w`, incluidas las frecuencias negativas, con $H(-\omega) = H(\omega)^*$; si una función solo tiene sentido para $\omega \ge 0$, hay que completar la mitad negativa con el conjugado antes de multiplicar.

```{admonition} Enunciado
:class: important

Construir una señal formada por 3 armónicos en el intervalo de tiempo de 0 a 4 segundos. Las frecuencias de los armónicos serán $\omega_1 = 2\pi$, $\omega_2 = 6\pi$, $\omega_3 = 8\pi$, las correspondientes amplitudes $A_1 = 1$, $A_2 = -1/2$, $A_3 = 1/4$, y en todos los casos la fase igual a 0.

a) Representar gráficamente la señal en el tiempo.

b) Representar el espectro en amplitud y en fase del sistema proporcionado en la función `H1.m` en el intervalo de frecuencias de 0 a $10\pi$. Analizar si producirá algún tipo de distorsión sobre la señal o el efecto que tendrá sobre ella. Utilizando el teorema de respuesta lineal y el principio de superposición, evaluar la señal al pasar por el sistema. Representar las señales en el dominio del tiempo antes y después de pasar por el sistema.

c) Repetir el apartado b) para el sistema proporcionado en la función `H2.m`.

d) Repetir el apartado b) para el sistema proporcionado en la función `H3.m`.

e) Repetir el apartado b) para el sistema proporcionado en la función `H4.m`.

f) Repetir el apartado b) para el sistema proporcionado en la función `H5.m`.

g) ¿Se podría haber hecho la simulación utilizando las funciones `espectro` e `inv_espectro` como en el ejercicio 1? Justifica la respuesta y, si es posible, realízalo en MATLAB.
```

(sistemas-ej3)=
## Ejercicio 3. Filtros sobre una señal de audio

### Filtros y frecuencia de corte

Un **filtro** es un sistema diseñado para dejar pasar unas frecuencias y eliminar otras. Se clasifica por la forma de su espectro en amplitud:

- **Pasabajas:** $|H| \approx 1$ desde 0 hasta una frecuencia $\omega_c$, y $\approx 0$ por encima. La red RC es un pasabajas poco abrupto.
- **Pasaaltas:** $|H| \approx 0$ por debajo de $\omega_c$ y $\approx 1$ por encima. Elimina la continua y los graves.
- **Pasabanda:** $|H| \approx 1$ solo entre dos frecuencias $\omega_1$ y $\omega_2$.

La **frecuencia de corte** $\omega_c$ separa la zona que pasa de la que no. En esta práctica se identifica con el ancho de banda del sistema, leído con el criterio del primer corte por cero del espectro en amplitud. Para saber de qué tipo es un filtro basta con dibujar `abs(H)` y mirar en qué zona vale 1 y en cuál 0.

```{admonition} Ejemplo resuelto
:class: note

Una señal tiene dos componentes, de 500 Hz y 3000 Hz, y pasa por un filtro pasabajas con frecuencia de corte 1000 Hz. En el espectro de salida la línea de 500 Hz se mantiene, porque está dentro de la banda de paso, y la de 3000 Hz desaparece. Con un pasaaltas de la misma frecuencia de corte ocurriría lo contrario.
```

```{admonition} Instala el Signal Processing Toolbox antes de la sesión
:class: warning

Los filtros `FiltroA.m` y `FiltroB.m` se construyen con la función `butter` de MATLAB, que no viene en la instalación básica sino en el complemento **Signal Processing Toolbox**. Si al llamar al filtro aparece un error del tipo *Unrecognized function or variable 'butter'*, instálalo desde la pestaña **Home**, botón **Add-Ons**, **Get Add-Ons**, buscando "Signal Processing Toolbox". Con la licencia de la universidad no tiene coste, pero la descarga tarda unos minutos: hazlo antes de la sesión.
```

### Una señal de audio es una señal muestreada

El fichero `audio1.wav` contiene una señal de sonido muestreada a $f_s = 44100$ muestras por segundo. `leeraudio` devuelve el vector de tiempos `t`, los valores `f` y la duración `tfin`. La señal no es periódica, así que al llamar a `espectro` el argumento del periodo es un parámetro ajustable, y el guion indica usar `tfin`. Las frecuencias que devuelve `espectro` están en rad/s; para interpretarlas en Hz, que es como se habla del sonido, conviene dibujar frente a `w/(2*pi)` y limitar el eje con `xlim`, porque el vector llega hasta decenas de miles de rad/s y lo interesante está en los primeros kilohercios.

El efecto de un filtro sobre el audio se puede ver y oír. En el espectro, al comparar `abs(G)` con `abs(F)` desaparece la zona que el filtro elimina. Al escucharlo con `sound`, un pasabajas deja un sonido apagado, como a través de una pared, porque quita los agudos; un pasaaltas deja un sonido débil y metálico, porque quita los graves, donde está la mayor parte de la energía de la voz. Si la señal filtrada queda muy débil, se puede escalar antes de escucharla, por ejemplo `sound(g/max(abs(g)), 44100)`.

```{admonition} Enunciado
:class: important

En este ejercicio vamos a comprobar el efecto de diversos filtros (sistemas) sobre una señal. Para ello, utilizaremos una señal de sonido proporcionada en el fichero `audio1.wav`.

Para recuperar la señal con MATLAB se ha proporcionado la función `leeraudio.m`. El uso de esta función es el siguiente: `[t,f,tfin] = leeraudio('audio1.wav');`

De esta forma en `t` obtenemos una función de tiempo, en `f` los valores de la señal y en `tfin` cuánto tiempo se está representando. Para escucharla simplemente es necesario ejecutar `sound(f,44100)`.

a) Utilizando la función `espectro`, calcular el espectro de la señal y representar su espectro en amplitud (utilizar en el parámetro del periodo el valor `tfin` obtenido para la señal).

b) En la función `FiltroA.m` se ha implementado una función de transferencia. Representar su espectro en amplitud para las frecuencias de la señal obtenidas en el apartado anterior con la función `espectro`. ¿Cómo es el filtro? ¿Y la frecuencia de corte? NOTA: la frecuencia de corte del filtro es equivalente al ancho de banda del sistema, utilizando el criterio de primer corte por cero de su espectro.

c) Evaluar la integral de Fourier de la señal tras pasar por el sistema del mismo modo que se realizó en el ejercicio 1.d. Representar el espectro en amplitud de la señal resultante y comparar el resultado con el espectro de la señal inicial. A continuación, pasar la señal al dominio del tiempo utilizando la función `inv_espectro` y escuchar la señal para analizar el resultado obtenido.

d) Repetir los pasos b) y c) con la función de transferencia definida en `FiltroB.m`.
```

```{admonition} Resumen de la sesión
:class: seealso

- Un sistema lineal estacionario queda descrito por su función de transferencia $H(\omega) = G(\omega)/F(\omega)$, única para cada sistema e independiente de la entrada. La salida en frecuencia es $G = H\cdot F$, y en el tiempo se recupera con la transformada inversa.
- El espectro de un sistema son dos gráficas: $|H(\omega)|$, par, y $\theta(\omega)$, impar. Un sistema real cumple $H(-\omega) = H(\omega)^*$.
- Red RC: $H = 1/(1 + j\omega/\omega_0)$, pasabajas con $|H(\omega_0)| = 0.707$. Su ancho de banda por el criterio 1 es $B_s = \omega_0$ rad/s.
- Comparar $B$ con $B_s$ predice la salida: $B < B_s$ réplica, $B \sim B_s$ algo distorsionada, $B > B_s$ muy distorsionada y limitada al ancho de banda del sistema.
- Teorema de respuesta lineal: $A\cos(\omega_1 t) \to A|H(\omega_1)|\cos(\omega_1 t + \theta(\omega_1))$. Con superposición, una suma de armónicos se trata armónico a armónico, y es el mismo cálculo que `G = F.*H`.
- Sin distorsión: atenuación ($|H|$ constante) y retardo ($\theta = -\omega t_d$, lineal). Con distorsión: de atenuación ($|H|$ variable) y de retardo ($\theta$ no lineal). Retardo $= -\theta(\omega)/\omega$; si es el mismo para todos los armónicos, no hay distorsión de retardo.
- Un filtro se clasifica por dónde $|H|$ vale 1 y dónde vale 0: pasabajas, pasaaltas, pasabanda. Su frecuencia de corte es su ancho de banda.
- Una señal de audio es una señal muestreada no periódica: en `espectro` se usa `tfin` como periodo y las frecuencias se leen en Hz con `w/(2*pi)`.
```
