# Sesión 2. Señales en el dominio del tiempo y la frecuencia

Cada ejercicio de esta sesión lleva delante la teoría que necesitas para hacerlo, y nada más. Trabajarás con los ficheros `rectangular.m` y `rectangular_b.m` que se proporcionan en la práctica. La notación es la de los apuntes del Tema 2.

```{admonition} Objetivos de aprendizaje
:class: tip

- Identificar amplitud, periodo, frecuencia y fase de una sinusoide, y obtener el periodo de una suma de sinusoides.
- Representar un tren de pulsos rectangulares mediante su serie de Fourier y leer sus coeficientes.
- Interpretar el efecto de un desplazamiento temporal sobre los coeficientes.
- Representar y leer los espectros de un tren de pulsos: ancho de banda y nivel de continua.
- Modificar la función de la práctica para un tren de pulsos triangulares.
```

(fourier-matlab)=
## Las órdenes de MATLAB que vas a usar

```{code-block} matlab
:caption: Órdenes de MATLAB de la sesión.

t = 0:0.001:5;                 % vector de tiempos, de 0 a 5 en pasos de 0.001
y = sin(2*pi*t);               % funciones sobre vectores, elemento a elemento
figure; plot(t, y); grid on    % abre una figura nueva y dibuja la señal
hold on; plot(t, 0.5*y)        % hold on superpone la gráfica siguiente
subplot(2,1,1)                 % varias gráficas en una figura (filas, columnas, posición)
stem(w, coef)                  % líneas verticales, para espectros discretos
xlabel('t (s)'); ylabel('f(t)'); legend('a','b'); xlim([0 5])
[t,y,w,coef] = rectangular(4,1,2,-5,5,400);   % así se llama a una función de la práctica
```

Entre vectores del mismo tamaño se usan `.*`, `./` y `.^`, como en la sesión 1 ({ref}`matlab-ej4`). El patrón completo para dibujar y etiquetar una señal está en {ref}`matlab-ej6`, y la forma de llamar a una función con varias salidas, en {ref}`matlab-ej8`.

(fourier-ej1)=
## Ejercicio 1. Suma de una constante y dos sinusoides

### La sinusoide y sus parámetros

Una sinusoide se escribe

$$
f(t) = A \sin(\omega t + \theta)
$$ (eq-sinusoide)

donde $A$ es la **amplitud** (valor de pico), $T$ el **periodo** en s, $f = 1/T$ la **frecuencia** en Hz, $\omega = 2\pi/T$ la **frecuencia angular** en rad/s y $\theta$ la **fase** en rad.

```{admonition} Ejemplo resuelto
:class: note

$f(t) = 3\sin(4\pi t)$. Aquí $A = 3$ y $\omega = 4\pi$ rad/s, luego $f = \omega/2\pi = 2$ Hz y $T = 1/f = 0.5$ s. En 0.5 s la señal hace un ciclo completo.
```

La fase $\theta$ desplaza la curva en el tiempo sin cambiar su forma. Si $\theta$ es positiva, la curva se mueve hacia la izquierda, y si es negativa, hacia la derecha. Por ejemplo, $\sin(\omega t)$ empieza valiendo 0 y $\sin(\omega t + \pi/2)$ empieza valiendo 1, porque es la misma curva movida a la izquierda. Esa segunda señal es un coseno, ya que $\cos(x) = \sin(x + \pi/2)$.

```{admonition} rad/s frente a Hz
:class: warning

Las dos unidades aparecen en la práctica. $\omega = 2\pi$ rad/s equivale a $f = 1$ Hz. En MATLAB se escribe `w1 = 2*pi` y se trabaja con $\omega$.
```

### Suma de señales: periodo y armónicos

Una suma de señales periódicas se repite cuando **todos** sus sumandos se repiten a la vez. Un término constante no cambia el periodo, porque no oscila. A la constante se le llama **nivel de continua**, o componente de frecuencia 0.

```{admonition} Ejemplos resueltos
:class: note

- $\sin(2t) + \sin(3t)$. Los periodos son $T_1 = \pi$ s y $T_2 = 2\pi/3$ s, y el periodo de la suma es $2\pi \approx 6.28$ s.
- $\cos(6\pi t) + \cos(8\pi t)$. Los periodos son $T_1 = 1/3$ s y $T_2 = 1/4$ s, y el periodo de la suma es 1 s.
- $\sin(t) + \sin(\pi t)$. Los periodos son $2\pi$ s y 2 s, y la suma no es periódica.
```

Cuando la suma es periódica, sus componentes tienen frecuencias que son múltiplos de una **frecuencia fundamental** $f_0 = 1/T$. Esas componentes se llaman **armónicos**, y el armónico $n$ es el que tiene frecuencia $n f_0$. En $\cos(2\pi t) + \tfrac{1}{3}\cos(6\pi t + \pi)$, por ejemplo, $T = 1$ s y $f_0 = 1$ Hz. La componente de 1 Hz es el primer armónico (el fundamental) y la de 3 Hz es el tercero, porque $3\text{ Hz} = 3 f_0$. El segundo armónico, de 2 Hz, no aparece en esta señal.

```{admonition} Medir el periodo en una gráfica
:class: tip

Busca dos puntos iguales y equivalentes de la curva, por ejemplo dos máximos consecutivos, y resta sus tiempos. Un cursor de datos en la figura (*Data Tips*) te da esas coordenadas.
```

```{admonition} Enunciado
:class: important

Dada una señal definida por $f(t) = 1 + A_1\sin(\omega_1 t) + A_2\cos(2\omega_1 t + \theta)$, representarla gráficamente entre 0 y 5 segundos para $A_1 = 1$, $A_2 = 1/2$, $\omega_1 = 2\pi$ rad/s y $\theta = \pi/3$. Obtener a partir de la gráfica el valor aproximado del periodo de la señal. ¿Cuántos armónicos tiene? ¿Qué ocurre con la **forma** de la señal si se elimina el nivel de continua?
```

(fourier-ej2)=
## Ejercicio 2. Tren de pulsos rectangulares

### De la serie de Fourier a la fórmula de la práctica

Una señal periódica de periodo $T$ se puede escribir como una suma de cosenos cuyas frecuencias son múltiplos de la fundamental, $\omega_n = 2\pi n/T$ con $n = 1, 2, 3\ldots$ Eso es la **serie de Fourier**. El tren de pulsos de la práctica tiene amplitud $V$, anchura $\tau$ y periodo $T$, y sus pulsos están centrados en $t = 0$. Al ser una señal simétrica respecto a $t = 0$, solo aparecen cosenos, y la serie queda así:

$$
f(t) = \frac{1}{T}\left[c_0 + 2\sum_{n=1}^{\infty} c_n \cos(\omega_n t)\right], \qquad \omega_n = \frac{2\pi n}{T}
$$ (eq-serie-fourier)

Los números $c_n$ se llaman **coeficientes de la serie**. La amplitud del armónico $n$ es $2|c_n|/T$. Si $c_n$ es negativo, el coseno de ese armónico va invertido.

Cada coeficiente se obtiene de la señal con una integral que recorre un periodo, en la que la señal vale $V$ dentro del pulso y 0 fuera de él:

$$
c_n = \int_{-T/2}^{T/2} f(t)\,e^{-j\omega_n t}\,dt
$$ (eq-coef-integral)

Al resolverla para el tren de pulsos rectangulares, el resultado es

$$
c_n = V\tau\,\frac{\sin(\omega_n\tau/2)}{\omega_n\tau/2} = V\tau\,\mathrm{sinc}(\omega_n\tau/2)
$$ (eq-coef-rect)

donde $\mathrm{sinc}(x) = \sin(x)/x$.

Esta expresión no sirve tal cual para $n = 0$, porque $\omega_n = 0$ da $\sin(0)/0$. En ese caso se toma el límite, que es $\mathrm{sinc}(0) = 1$, y resulta $c_0 = V\tau$. Por eso $c_0$ va aparte en la serie y en el código. Sustituyendo $c_0$ y $c_n$ en la serie se llega a la fórmula del enunciado de la práctica:

$$
f(t) = \frac{V\tau}{T} + \frac{2}{T}\sum_{n=1}^{\infty} V\tau\,\mathrm{sinc}(\omega_n\tau/2)\cos(\omega_n t)
$$ (eq-serie-rect)

```{admonition} Ejemplo resuelto: V = 3, τ = 1, T = 4
:class: note

Aquí $\omega_n = \pi n/2$, así que el argumento del sinc es $\omega_n\tau/2 = \pi n/4$ y $c_n = 3\,\mathrm{sinc}(\pi n/4)$.

| $n$ | $\pi n/4$ | $\mathrm{sinc}(\pi n/4)$ | $c_n$ | Amplitud $2\lvert c_n\rvert/T$ |
|---|---|---|---|---|
| 1 | $\pi/4$ | 0.900 | 2.701 | 1.350 |
| 2 | $\pi/2$ | 0.637 | 1.910 | 0.955 |
| 3 | $3\pi/4$ | 0.300 | 0.900 | 0.450 |
| 4 | $\pi$ | 0 | **0** | 0 |
| 5 | $5\pi/4$ | $-0.180$ | $-0.540$ | 0.270 |

El armónico 4 se anula porque $\sin(\pi) = 0$. En general, $c_n = 0$ cuando $\omega_n\tau/2$ es un múltiplo de $\pi$.
```

### Cómo guardan los datos los ficheros

La función se llama `[t,y,w,coef] = rectangular(V,tau,T,tmin,tmax,m)`. Calcula la serie con $m$ armónicos, es decir, con $n$ desde 1 hasta $m$ más el término $c_0$. Devuelve el tiempo `t`, la señal `y`, las frecuencias `w` y los coeficientes `coef`.

El orden de `coef` es `coef(1)` $= c_0$, `coef(2)` $= c_1$, `coef(3)` $= c_2$… Ten en cuenta que `coef` guarda los $c_n$ de {eq}`eq-coef-rect`. La división entre $T$ y el factor 2 se aplican en la última línea de la función.

Una serie con $m$ armónicos es una aproximación de la señal. Cuantos más términos se suman, más fiel debería ser, y conviene mirar con atención qué ocurre en los puntos donde la señal tiene saltos.

### Desplazar la señal en el tiempo

Retrasar la señal un tiempo $t_0$ da $f(t - t_0)$. La función `rectangular_b(V,tau,T,tmin,tmax,m,t0)` hace ese desplazamiento. Para ello usa la serie en forma compleja, con números complejos $z = a + bj$, de módulo $r = \sqrt{a^2 + b^2}$ y fase $\varphi$ (repasa {ref}`matlab-ej1` para trabajar con ellos en MATLAB). En forma polar, $z = r\,e^{j\varphi}$, y multiplicar por $e^{j\alpha}$ gira el número un ángulo $\alpha$ sin cambiar su módulo.

$$
e^{j\varphi} = \cos\varphi + j\sin\varphi
$$ (eq-euler)

Un coeficiente real positivo tiene fase 0 y uno real negativo tiene fase $\pi$. Un imaginario puro positivo tiene fase $\pi/2$ y uno negativo, $-\pi/2$.

En la serie compleja

$$
f(t) = \frac{1}{T}\sum_{n=-m}^{m} c_n\,e^{j\omega_n t}
$$ (eq-serie-compleja)

la suma recorre $n = -m \ldots m$. El coeficiente del armónico $n$ está en `coef(m+1+n)`, de modo que el armónico 0 está en `coef(m+1)` y los armónicos 1, 2, 3… en `coef(m+2)`, `coef(m+3)`, `coef(m+4)`… La señal `y` sale con una parte imaginaria despreciable, del orden de $10^{-15}$, así que se dibuja `real(y)`.

El **teorema de desplazamiento** de los apuntes dice que, si $f(t)$ tiene coeficientes $c_n$, entonces $f(t - t_0)$ tiene coeficientes $e^{-j\omega_n t_0}\,c_n$.

```{admonition} Ejemplo resuelto: V = 3, τ = 1, T = 4, t₀ = 0.5 s
:class: note

Aquí $\omega_n t_0 = \pi n/4$, y cada coeficiente se multiplica por $e^{-j\pi n/4}$.

| $n$ | $c_n$ sin desplazar | Giro $-\omega_n t_0$ | $c_n$ desplazado |
|---|---|---|---|
| 1 | 2.701 | $-45^\circ$ | $1.910 - 1.910j$ |
| 2 | 1.910 | $-90^\circ$ | $-1.910j$ |
| 3 | 0.900 | $-135^\circ$ | $-0.637 - 0.637j$ |

El módulo de cada coeficiente no ha cambiado; solo ha girado su fase.
```

```{admonition} No uses i como variable
:class: warning

`rectangular_b.m` usa `i` como unidad imaginaria. Si en tu sesión has usado `i` como contador de un bucle, la función dará resultados erróneos. Se arregla con `clear i`.
```

```{admonition} Enunciado
:class: important

Representar gráficamente una señal periódica formada por **pulsos rectangulares** utilizando la función `rectangular.m` proporcionada en la práctica. Esta función implementa la suma de un número finito de términos del desarrollo en serie de Fourier de dicha señal, que se corresponde con la expresión {eq}`eq-serie-rect`, donde $V$ es la amplitud de los pulsos, $\tau$ el ancho de los pulsos, $T$ el periodo de la señal y $\omega_n$ la frecuencia de los armónicos.

a) Fijando el valor de $V = 4$, $\tau = 1$, $T = 2$ y el intervalo de tiempo desde $t_{min} = -5$ a $t_{max} = 5$ segundos, representar la serie para 400 armónicos.

b) Representar la serie para un número de términos (número de armónicos) de 5, 15, 50, 100, 400 y 1000. Explicar el comportamiento observado al aumentar el número de armónicos.

c) Manteniendo el intervalo de representación del apartado anterior y un número de armónicos de 400, variar el resto de parámetros ($V$, $\tau$, $T$) y observar cómo se modifica la señal. Anotad cómo afecta cada uno de los parámetros al resultado final.

d) Dado que la función `rectangular.m` devuelve los coeficientes de la serie de Fourier, ¿cuál es el valor de los 5 primeros coeficientes, correspondientes a los 5 primeros armónicos, si los parámetros de la señal son $V = 4$, $\tau = 1$, $T = 2$? ¿Hay algún armónico que se anula? ¿Por qué? ¿Cuánto vale el coeficiente $c_0$ y qué representa físicamente? NOTA: el primer valor del vector `coef` es el armónico $c_0$.

e) Utilizando ahora la función `rectangular_b.m`, que permite el desplazamiento temporal de la señal, observar la influencia de $t_0$ en el tren de pulsos rectangulares, manteniendo constantes el resto de los parámetros. ¿Cuál es ahora el valor de los coeficientes para los 5 primeros armónicos? ¿Cuál es la diferencia fundamental con los coeficientes de la señal sin desplazar? NOTA: dado que esta función utiliza internamente la serie de Fourier en forma compleja, en este apartado el armónico $c_0$ (componente de continua) está en el centro del vector `coef`, ya que hay frecuencias negativas y positivas.

f) Observando el código de la función `rectangular_b.m`, ¿dónde aparece el desplazamiento temporal de la señal y por qué se expresa así?
```

(fourier-ej3)=
## Ejercicio 3. Espectros del tren de pulsos

### Los tres espectros

Cada coeficiente $c_n$ es un número complejo, con un módulo $|c_n|$ y una fase $\theta_n$, de modo que $c_n = |c_n|\,e^{j\theta_n}$. Para describir en qué frecuencias tiene energía una señal se usan tres gráficas, todas con la frecuencia $\omega_n = 2\pi n/T$ en el eje horizontal:

```{list-table} Los tres espectros de una señal periódica.
:name: tabla-espectros
:header-rows: 1
:widths: 20 35 45

* - Espectro
  - Qué se dibuja
  - Para qué sirve
* - **En amplitud**
  - $|c_n|$ frente a $\omega_n$
  - Cuánto pesa cada armónico. Todas las líneas salen hacia arriba.
* - **En fase**
  - $\theta_n$ frente a $\omega_n$
  - Cómo está desplazado cada armónico en el tiempo.
* - **En frecuencia**
  - Amplitud y fase a la vez, es decir, los propios $c_n$
  - Reúne los dos anteriores en una sola gráfica.
```

En el tren de pulsos rectangulares todos los $c_n$ son números reales, positivos o negativos. Entonces la fase solo puede valer 0 ($c_n$ positivo) o $\pi$ ($c_n$ negativo), y el espectro en frecuencia se dibuja en una sola gráfica con `stem(w, coef)`. Los $c_n$ negativos salen hacia abajo, y eso equivale a fase $\pi$. Con `stem(w, abs(coef))` se dibuja el espectro en amplitud, y todas las líneas salen hacia arriba.

```{admonition} Ejemplo resuelto: los coeficientes del ejemplo del ejercicio 2 (V = 3, τ = 1, T = 4)
:class: note

| $n$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $\omega_n$ (rad/s) | 1.57 | 3.14 | 4.71 | 6.28 | 7.85 |
| $c_n$ (espectro en frecuencia) | 2.701 | 1.910 | 0.900 | 0 | $-0.540$ |
| $\lvert c_n\rvert$ (espectro en amplitud) | 2.701 | 1.910 | 0.900 | 0 | 0.540 |
| $\theta_n$ (espectro en fase) | 0 | 0 | 0 | no aplica | $\pi$ |

Las dos primeras gráficas tienen las mismas líneas, pero en la del espectro en frecuencia la línea $n = 5$ cuelga hacia abajo. Ahí se ve que el signo de los $c_n$ ha cambiado.
```

El espectro de una señal periódica es **discreto**. Solo hay valores en las frecuencias $\omega_n = 2\pi n/T$, con $n = 0, 1, 2\ldots$, y por eso se dibuja con líneas sueltas usando `stem`. Entre dos líneas no hay nada.

### Ancho de banda y nivel de continua

El **ancho de banda** según el primer criterio es la frecuencia del primer cero de los coeficientes. Se calcula igualando a cero $V\tau\,\mathrm{sinc}(\omega\tau/2)$ y tomando la primera solución con $\omega > 0$. La respuesta sale en rad/s, que se pasa a Hz con $f = \omega/2\pi$. Puede coincidir o no con la frecuencia de un armónico concreto.

```{admonition} Ejemplo resuelto: primer criterio con otra expresión
:class: note

La expresión $A\sin(\omega a)/(\omega a)$, con $a = 0.5$ s, se anula cuando $\sin(\omega a) = 0$. La primera solución con $\omega > 0$ es $\omega a = \pi$, es decir, $\omega = \pi/a = 2\pi$ rad/s, o 1 Hz.
```

El **nivel de continua** de la señal es el término constante de la serie, que sale de la fórmula {eq}`eq-serie-rect` sin ningún coseno. No es lo mismo que el valor de `coef(1)`: el armónico 0 es el que ocupa `coef(1)`, y el nivel de continua es el que aparece en la señal.

```{admonition} Enunciado
:class: important

Utilizando nuevamente la función `rectangular.m` para obtener los coeficientes de la serie de Fourier y sus correspondientes frecuencias, representar ahora los **espectros del tren de pulsos rectangulares**, que por definición son la representación gráfica de estos coeficientes. Para representar cada valor por una línea vertical, utilizar la función `stem` de MATLAB, con sintaxis `stem(w,coef)`.

Considerar una señal en el intervalo de $t_{min} = -50$, $t_{max} = 50$, con $V = 4$, $\tau = 1$ y $T = 2$.

a) Representar los espectros en frecuencia para periodos $T = 2$, 5 y 20, utilizando 50 armónicos, y observar la influencia del $T$ en el espectro, en la separación entre armónicos. ¿Qué ocurre cuando $T$ se hace muy grande? Indicar cuál es el ancho de banda (utilizando el primer criterio) y el valor del armónico 0 (nivel de continua) en cada caso, a partir de las gráficas. Para la comparación de espectros es útil superponer las gráficas con `hold on`.

b) Indicar el ancho de banda de esta señal y su nivel de continua analíticamente, y comparar dicho valor con el obtenido a partir de las gráficas.

c) Variar el ancho de los pulsos $\tau$ (manteniendo el resto de parámetros) y observar la influencia en el ancho de banda. Comprobar que existe una relación inversamente proporcional entre el ancho del pulso y el ancho de banda de la señal.
```

(fourier-ej4)=
## Ejercicio 4. Tren de pulsos triangulares

### El pulso triangular y su coeficiente

El pulso triangular tiene altura $V$ en $t = 0$ y baja linealmente hasta 0 en $t = -\tau$ y en $t = \tau$. Su base mide, por tanto, $2\tau$. Los coeficientes del tren, según el enunciado, son

$$
c_n = V\tau\,\mathrm{sinc}^2(\omega_n\tau/2) = V\tau\left[\frac{\sin(\omega_n\tau/2)}{\omega_n\tau/2}\right]^2, \qquad \omega_n = \frac{2\pi n}{T}
$$ (eq-coef-tri)

La serie se suma igual que en el ejercicio 2, con {eq}`eq-serie-fourier`.

El término $c_0$ sigue siendo el coeficiente del armónico 0, es decir, el valor de la integral {eq}`eq-coef-integral` con $n = 0$, que ahora se calcula sobre el triángulo. Hay que ponerlo a mano en `coef(1)`, como hace `rectangular.m`.

```{admonition} Qué hay que tocar en rectangular.m
:class: tip

Guarda una copia con otro nombre, por ejemplo `triangular.m`, y cambia el nombre de la función en la primera línea (recuerda de {ref}`matlab-ej8` que el nombre del archivo y el de la función deben coincidir). Después revisa la línea que calcula `coef(n+1)` y la que asigna `coef(1)`. Fuera de eso, la estructura del fichero es la misma.
```

```{admonition} Enunciado
:class: important

Modificar el código de la función `rectangular.m` para que represente una señal periódica de tren de pulsos triangulares, sabiendo que los coeficientes de la serie de Fourier para dicha señal son los de {eq}`eq-coef-tri`, donde $V$ es la amplitud de los pulsos, $2\tau$ es el ancho de los pulsos (base de los triángulos), $T$ es el periodo de la señal y $\omega_n$ es la frecuencia de los armónicos.

Representar gráficamente la **señal en el dominio del tiempo** y el **espectro de la señal** para los siguientes valores de sus parámetros: $V = 5$, $\tau = 2$, $T = 5$, $t_{min} = -10$, $t_{max} = 10$, utilizando un número de armónicos de 5, 10 y 50. Comprobar en la gráfica de la señal en el dominio del tiempo que el ancho de los pulsos es el correcto.
```

```{admonition} Resumen de la sesión
:class: seealso

- Una sinusoide $A\sin(\omega t + \theta)$ queda definida por su amplitud, su frecuencia ($\omega = 2\pi/T$) y su fase, que desplaza la curva sin cambiar su forma.
- Una suma de señales periódicas se repite cuando todos sus sumandos se repiten a la vez. Sus componentes son armónicos de frecuencia $n f_0$, y la constante es el nivel de continua.
- La serie de Fourier escribe una señal periódica como $\frac{1}{T}\left[c_0 + 2\sum c_n\cos(\omega_n t)\right]$, con $\omega_n = 2\pi n/T$. La amplitud del armónico $n$ es $2|c_n|/T$.
- Para el tren de pulsos rectangulares, $c_n = V\tau\,\mathrm{sinc}(\omega_n\tau/2)$ y $c_0 = V\tau$. En `rectangular.m`, `coef(1)` es $c_0$.
- Retrasar la señal $t_0$ multiplica cada coeficiente por $e^{-j\omega_n t_0}$. En `rectangular_b.m`, el armónico 0 está en el centro de `coef`.
- El espectro de una señal periódica es discreto y se dibuja con `stem`: en amplitud ($|c_n|$), en fase ($\theta_n$) o en frecuencia (los propios $c_n$).
- El ancho de banda (primer criterio) es la frecuencia del primer cero de los coeficientes. El nivel de continua es el término constante de la serie, no el valor de `coef(1)`.
- El tren de pulsos triangulares tiene $c_n = V\tau\,\mathrm{sinc}^2(\omega_n\tau/2)$ y base $2\tau$.
```
