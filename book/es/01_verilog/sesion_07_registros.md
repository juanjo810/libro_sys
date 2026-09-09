# Sesion 7. Registros

Esta pagina respeta la secuencia de la sesion original: cada apartado aparece en el mismo orden y los ejercicios se mantienen como secciones propias dentro del recorrido.

```{admonition} Objetivos de aprendizaje
:class: tip

- Construir registros SISO y SIPO.
- Generar ficheros de ondas.
- Depurar circuitos secuenciales con GTKWave.
```

## Ejercicio 1
Construid un biestable D con cualquiera de los métodos que
hemos visto hasta ahora o de los vistos en teoría.

La {numref}`fig-verilog-07-d` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_07/d.png
---
name: fig-verilog-07-d
alt: Biestable D
width: 85%
align: center
---
Biestable D
```

Soluciones y comentarios

## Ejercicio 2
Con el módulo construido en el ejercicio anterior, debéis
construir un registro SISO.

La {numref}`fig-verilog-07-siso` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_07/siso.png
---
name: fig-verilog-07-siso
alt: Registro SISO
width: 85%
align: center
---
Registro SISO
```

Limpiad mediante CLR el contenido de los biestables.
Aplicad una señal de reloj y unas entradas al azar y observad
que la salida es la esperada.

Soluciones y comentarios

## Depuracion de senales en Verilog
Es posible generar un cronograma de las señales de un diseño en
Verilog. Para ello, se han de usar las órdenes que veremos en este
apartado. La primera de ellas sirve para especificar cuál será
el fichero de salida. Debe incluirse al principio del programa:

```text
$dumpfile("
nombre_del_fichero.dmp
");
```

Hay que indicar, también, qué señales son la que queremos
seguir:

```text
$dumpvars(
profundidad
,
nombre_del_objeto
);
```

Esto también se hará al inicio de la simulación.
El nombre del objeto es el del módulo o variable que se quiere seguir.
En el caso de que sea un módulo, una profundidad mayor que 1 significa
cuántos niveles se desea profundizar en la jerarquía de objetos.
Si el registro SISO del ejercicio anterior se llama

pepe

y
queremos seguir todas sus señales y no la de los objetos que incluya,
la orden sería:

```text
$dumpvars(1,pepe);
```

Solamente falta arrancar o parar el volcado, a voluntad.
A continuación de escribir

$dumpvars

, comienza el
volcado.
Cada vez que queramos
pararlo, ponemos la orden

$dumpoff;

y cada vez que queramos
reanudarlo, ponemos

$dumpon

.

La salida que se vuelca en el fichero no es para consumo humano.
Debe analizarse con un programa gráfico. Uno de ellos disponible para
Linux se llama GTKwave. Observemos la salida que se produce para el ejemplo
anterior:

La {numref}`fig-verilog-07-gtkwave` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_07/gtkwave.png
---
name: fig-verilog-07-gtkwave
alt: Salida de GTKwave para el ejemplo anterior
width: 85%
align: center
---
Salida de GTKwave para el ejemplo anterior
```

Para lograr esta salida, invocamos el programa desde la línea
de órdenes mediante `gtkwave nombre_del_fichero_de_volcado` . Para que
funcione, debe estar instalado el programa en vuestro Linux.
Una vez dentro, podéis examinar las señales navegando
por la ventana superior izquierda. Para que las señales aparezcan
en el cronograma, arrastradlas desde la ventana inferior izquierda hasta
la ventana larga inmediatamente situada a su derecha.

## Ejercicio 3
Modificad ligeramente el código del ejercicio anterior para
obtener el siguiente registro SIPO:

La {numref}`fig-verilog-07-sipo` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_07/sipo.png
---
name: fig-verilog-07-sipo
alt: Registro SIPO
width: 85%
align: center
---
Registro SIPO
```

Probadlo. Usad para los cables O una única variable de
cuatro bits, en lugar de cuatro variables de 1 bit.

## Ejercicio 4
Construid y probad el siguiente registro de cuatro bits:

La {numref}`fig-verilog-07-pisiso` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_07/pisiso.png
---
name: fig-verilog-07-pisiso
alt: Registro PISISO
width: 85%
align: center
---
Registro PISISO
```

¿Sois capaces de diseñarlo de modo modular?
Cargad un valor por la entrada paralela e idla desplazando hacia
la salida serie.

## Ejercicio 5 (mas dificil)
Debido a restricciones de espacio se debe
diseñar un sistema sumador de cuatro bits a partir de
un único sumador completo de un bit. Se usarán,
además dos registros PISO como los del ejercicio anterior,
uno SIPO
y algún biestable adicional. El funcionamiento ha de ser
el siguiente:

1. En el primer flanco de reloj se cargan los dos sumandos
en los registros PISO
2. En los cuatro siguientes se van desplazando los sumandos
un bit. Esos bits se ofrecen al circuito sumador completo
de un bit, junto con el acarreo anterior (usad un biestable
para retener el acarreo anterior un pulso de reloj). La salida
del sumador va al registro SIPO
3. Al final, transcurrido un número adecuado de pulsos de
reloj, dispondremos de la suma efectuada en las salidas del registro
SIPO

No se os da un esquema del diseño, pues el ejercicio también
consiste en que lo hagáis. No obstante, aquí van algunas
pistas o un camino para hacerlo:

1. Cread los dos registros PISO. Usad dos variables `a` y `b` de tipo `reg` para alimentar los sumandos
a los registros PISO
2. Activad CLR y la carga paralela de los registros. Ejecutad y
comprobad que los valores cargados salen, al cabo del tiempo,
por las salidas serie de los registros PISO
3. Cread un sumador completo. En la entrada de los sumandos conectad
las salidas de los registros PISO anteriores. Dejad el acarreo de
entrada a 0. Ejecutad y observad que se suma bien, salvo los
acarreos
4. Mediante un biestable, almacenad el acarreo de salida del sumador
para en el siguiente ciclo realimentarlo en el acarreo de entrada
del sumador. Si lo hacéis bien, al ejecutar, notaréis
que ahora la suma se realiza correctamente
5. Finalmente, construid un registro SIPO, a cuya entrada serie
debéis conectar la salida del sumador. Si lo habéis hecho
bien, al ejecutar, la suma de los dos números introducidos
al principio debe aparecer en la salida paralela del registro
SIPO, tal y como se pedía

## Fuente original

Contenido adaptado a TeachBook a partir de la pagina de referencia: <http://avellano.usal.es/~compi/sesion7.htm>.
