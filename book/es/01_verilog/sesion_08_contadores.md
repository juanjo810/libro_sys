# Sesion 8. Contadores

Esta pagina respeta la secuencia de la sesion original: cada apartado aparece en el mismo orden y los ejercicios se mantienen como secciones propias dentro del recorrido.

```{admonition} Objetivos de aprendizaje
:class: tip

- Programar contadores con reloj y modo de cuenta.
- Reconocer estados transitorios.
- Disenar contadores de cuenta arbitraria.
```

## Ejercicio 1
Prográmese en Verilog el siguiente contador con posibilidad de cuenta
ascendente o descendente. Verífiquese. Úsese una variable
de cuatro bits en lugar de cuatro variables de un bit para la salida.

La {numref}`fig-verilog-08-contador` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_08/contador.png
---
name: fig-verilog-08-contador
alt: Contador ascendente/descendente
width: 85%
align: center
---
Contador ascendente/descendente
```

¿Qué se observa si cambiáis a mitad de recorrido
la línea de selección de modo (incremento o decremento), sin
limpiar el contador?

Añadid las líneas PRESET y CLEAR activas por bajo y
asíncronas a los biestables del contador. Modificad el diseño
añadiendo una línea adicional de HOLD, también
activa por bajo, de modo que si esa línea está activa,
el biestable no responda a la señal T. Auxiliaros de las entradas
PRESET y CLEAR para ello, no modifiquéis el interior del biestable
T.

Haced una última simulación en la que, cada vez que
cambiéis de modo de cuenta, activéis previamente HOLD y
la desactivéis después, a fin de que la cuenta cambie
de sentido normalmente, sin producirse saltos.

Soluciones y comentarios

## Ejercicio 2
Modificad ligeramente el circuito del ejercicio anterior para que realice
continuamente una cuenta de 10 a 0, según el esquema de la figura:

La {numref}`fig-verilog-08-10a0` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_08/10a0.png
---
name: fig-verilog-08-10a0
alt: Contador de 10 a 0
width: 85%
align: center
---
Contador de 10 a 0
```

Al realizarlo, observaréis que no realiza la cuenta correctamente,
sino que cuenta 10, 9, 8, 2, 1, 0, 10, 9, 8,... La razón es simple.
Al tratarse de un contador asíncrono, las transiciones tardan
en propagarse a todos los biestables. De hecho, la cuenta que lleva a cabo
es:

- 1010 (10)
- 1011 , 1001 (9)
- 1000 (8)
- 1001 , 1011 , 1111 ,
0111 (7)
- 0110 (6)
- 0111 0101 (5)
- 0100 (4)
- 0101 , 0111 ,
0011 (3)
- 0010 (2)
- 0011 , 0001 (1)
- 0000 (0)
- 0001 , 0011 , 0111 , 1111 (actúa NAND),
1010 (10)

Los estados en rojo son estados transitorios que se producen mientras
se va propagando la señal a todos los biestables. En la
transición del 8 al 7 hay un transitorio que vale 15 y hace que
la puerta NAND actúe cuando no debe. Probad varias soluciones: 
1. Añadid una entrada adicional a la puerta NAND y conectar
la señal de reloj a ella. De este modo, la puerta actuará
solamente en el nivel alto del reloj, cuando los biestables ya
tienen el estado correcto.
2. Una alternativa al punto anterior es introducir un pequeño
retardo en la puerta NAND
3. La solución más fetén, aunque no más
económica pasa por distinguir las dos ocasiones en que
aparece 1111 ~2~ en la cuenta. Se puede
hacer con un biestable que almacene el valor anterior de
Q ~4~ y agregar dicho valor como una
entrada adicional de la puerta NAND. Un biestable D activo en
flanco de subida es perfecto para este trabajo.

## Ejercicio 3
Comprobad, mediante Verilog, el funcionamiento correcto de este contador
síncrono:

La {numref}`fig-verilog-08-contsinc` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_08/contsinc.png
---
name: fig-verilog-08-contsinc
alt: Contador ascendente/descendente
width: 85%
align: center
---
Contador ascendente/descendente
```

## Ejercicio 4
Se trata de analizar el siguiente contador de cuenta arbitraria y construir su
diagrama de transición de estados:

La {numref}`fig-verilog-08-analisis` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_08/analisis.png
---
name: fig-verilog-08-analisis
alt: Circuito para analizar
width: 85%
align: center
---
Circuito para analizar
```

Recordemos los pasos que hay que dar:

1. Primero hay que escribir las ecuaciones de las jotas y kas de los
biestables en función de las variables de salida
Q ~2~ Q ~1~ Q ~0~ .
2. Con ayuda de esas ecuaciones, construid una tabla con todos los
estados y los valores de las jotas y kas de los biestables para
cada estado
3. Completad la tabla con el estado nuevo al que va a parar el estado
de cada fila.
4. Dibujad el diagrama de transición de estados a partir de la
tabla.

Comprobad que habéis realizado el ejercicio correctamente introduciendo
el circuito en Verilog.

## Ejercicio 5
En el año 2718, la humanidad ha sido capaz de explorar numerosos
sistemas planetarios lejanos sin haber encontrado vida
inteligente

1

.
Los científicos deciden dejar dispositivos en los planetas visitados
que den pistas de la localización de la Tierra a otros viajeros
interestelares. Para que el visitante tenga constancia de que el objeto
que ve es producto de vida inteligente y no del azar, se decide que debe
llevar un contador que cuente según el inicio de la sucesión
de Fibonacci, en la que cada término resulta ser la suma de los
dos anteriores:

0, 1, 1, 2, 3, 5, 8, 13, y vuelta a empezar.

Nuestro cometido es diseñar tal contador. Después de mucho
recapacitar, se decide que se va a realizar el dispositivo como un 
contador de cuatro bits de cuenta arbitraria. Sin embargo, nos encontramos con
el problema de que hay un número que se repite (el 1). Se decide
solucionarlo usando para el primer 1 otro número no usado (el 9)
e intentar corregir esa salida con lógica combinacional añadida
al final. De este modo, la cuenta que se debe generar es:

0, 9, 1, 2, 3, 5, 8, 13, y vuelta a empezar.

Veamos los pasos que hay que dar, recordando el ejemplo visto en teoría:

1. Debemos construir el diagrama de transición de estados,
haciendo que los estados no usados decaigan a cualquiera de los
otros. De una elección acertada de estos decaimientos puede
depender lo simple o complicado que resulte el circuito final y,
dada la gran cantidad de planetas con posibilidad de vida, unos
céntimos de ahorro puede suponer un gran pellizco al final.
Este es el diagrama del ejemplo que veíamos en teoría:
2. Con ayuda de la tabla de transiciones del biestable JK, se debe escribir la tabla de transiciones. En el ejemplo de la
teoría, era:
3. Toca ahora escribir las jotas y las kas de los biestables en
función de las variables binarias que determinan el estado.
Estas variables son, en este ejercicio, las salidas de los
biestables: Q ~3~ Q ~2~ Q ~1~ Q ~0~ .
Nos podemos auxiliar de mapas de Karnaugh. Como muestra, parte del
ejemplo visto en teoría:
4. Una vez deducidas las ecuaciones de excitación de las jotas y
las kas de cada biestable, se puede construir el circuito. En el ejemplo
de teoría, este es el circuito resultante:
5. Probad con Verilog el circuito que habéis obtenido. En caso
de que no realice la cuenta: 0, 9, 1, 2, 3, 5, 8, 13, 0, ...,
revisad los cálculos.
6. Diseñad el circuito combinacional que cambie el 9 por un 1,
dejando el resto de valores que importan como está. 
Si no sois capaces
de diseñarlo sobre la marcha, construid la tabla de verdad y
aplicad de nuevo los mapas de Karnaugh.
7. Probad el diseño final y, de funcionar, disfrutad de vuestra
obra: un flamante señalador de vida inteligente para 
extraterrestres ^2^ ,
marca ACME ^®^ .

Nota:

podéis mandar vuestros diseños, junto
con el código Verilog al correo del profesor. Aquel diseño
que funcione, esté realizado con el menor número de puertas
y, en caso de empate, llegue antes, será publicado, bajo pseudónimo,
en esta página web. Podéis usar biestables JK activos por
flanco sin líneas de PRESET y CLEAR y puertas AND, OR, NOT, XOR, NAND,
NOR y XNOR. Cada biestable cuenta como 6 puertas, se realice como se realice.
Si se usan puertas AND, OR, XOR, NAND, NOR o XNOR de más de dos
entradas, cada entrada adicional cuenta como media puerta más.

Segunda nota

: ¿Cómo quedaría de sencillo este
circuito si lo realizásemos en Verilog con un modelo de comportamiento?
¿En qué circunstancia se usaría tal aproximación al
problema?

Soluciones y comentarios

.

## Fuente original

Contenido adaptado a TeachBook a partir de la pagina de referencia: <http://avellano.usal.es/~compi/sesion8.htm>.
