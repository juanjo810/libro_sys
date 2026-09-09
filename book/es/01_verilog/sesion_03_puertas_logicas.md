# Sesion 3. Puertas logicas

Esta pagina respeta la secuencia de la sesion original: cada apartado aparece en el mismo orden y los ejercicios se mantienen como secciones propias dentro del recorrido.

```{admonition} Objetivos de aprendizaje
:class: tip

- Instanciar puertas primitivas de Verilog.
- Comprobar tablas de verdad con `0`, `1`, `x` y `z`.
- Construir funciones combinacionales conectando puertas.
```

## Puerta AND
Recordemos de la parte de teoría el comportamiento
de una puerta AND:

La {numref}`fig-verilog-03-and` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_03/and.png
---
name: fig-verilog-03-and
alt: Puerta AND
width: 85%
align: center
---
Puerta AND
```

Vamos a comprobar, con Verilog, el funcionamiento de esta
puerta:

| /* ComprobaciOn de puerta AND: TestAnd.v */
module TestAnd;
reg a,b; // Entradas
wire salida;
and a1(salida,a,b);
// Bloque de comportamiento
initial
begin
$monitor($time," a=%b, b=%b, a.b=%b", a,b,salida);
a=0; b=0;
#5 a=0; b=1;
#5 a=1; b=0;
#5 a=1; b=1;
end
endmodule |  |
| --- | --- |

## Ejercicio 1
Completar la tabla de la puerta AND añadiendo
como posibles entradas

x

(indefinido)
y

z

(alta impedancia). Tiene que haber,
por consiguiente, dieciséis líneas en
la tabla.

## Otras puertas sencillas en Verilog
Recordemos algunas otras puertas vistas en teoría y cómo
se expresan en Verilog:

- Puerta OR, `or(salida,a,b)` :
- Puerta NOT, `not(salida,a)` :
- Puertas NAND, `nand(salida,a,b)` , 
y NOR, `nor(salida,a,b)` :
- Puertas XOR, `xor(salida,a,b)` , 
y XNOR, `xnor(salida,a,b)` :
- Puerta BUFFER, `buf(salida,a)` :

## Ejercicio 2
Haced en un papel una tabla de dieciséis líneas y
tantas columnas como puertas lógicas vistas. Rellenad
la tabla con los valores de las puertas lógicas
correspondientes a cada posible combinación de entradas
formadas con 0,1,

x

y

z

. Añadid
una a una las puertas al código del ejercicio anterior y
comprobad con Verilog si habéis acertado al rellenar
la tabla.

## Interconexion de puertas logicas
Vamos a construir la tabla de verdad de la función
lógica f

2

(a,b,c)=ab+c con la ayuda de
Verilog.

La {numref}`fig-verilog-03-f2` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_03/f2.png
---
name: fig-verilog-03-f2
alt: ab+c
width: 85%
align: center
---
ab+c
```

En lugar de escribir a mano los 8 casos de posibles combinaciones
de valores de a, b y c, construiremos un registro de tres
bits, le daremos valor inicial cero y lo iremos incrementando
hasta alcanzar el valor 7 (111

2

):

| // Tabla de verdad de f2(a,b,c)=ab+c
module f2;
reg [2:0] r; // Entradas: a=r[2], b=r[1], c=r[0]
wire salida, ab;
and a1(ab,r[2],r[1]);
or o1(salida,ab,r[0]);
// Bloque de comportamiento
initial
begin
$display(" a b c | f2");
$display(" ----------");
$monitor($time," %b %b %b | %b", r[2],r[1], r[0], salida);
r=0; // r=000 => a=0, b=0, c=0
while (r!='b111) #5 r=r+1;
end
endmodule | r r[2] r[1] r[0] 0 000 2 0 0 0 1 001 2 0 0 1 2 010 2 0 1 0 3 011 2 0 1 1 4 100 2 1 0 0 5 101 2 1 0 1 6 110 2 1 1 0 7 111 2 1 1 1 | r | r[2] | r[1] | r[0] | 0 | 000 2 | 0 | 0 | 0 | 1 | 001 2 | 0 | 0 | 1 | 2 | 010 2 | 0 | 1 | 0 | 3 | 011 2 | 0 | 1 | 1 | 4 | 100 2 | 1 | 0 | 0 | 5 | 101 2 | 1 | 0 | 1 | 6 | 110 2 | 1 | 1 | 0 | 7 | 111 2 | 1 | 1 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| r | r[2] | r[1] | r[0] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | 000 2 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | 001 2 | 0 | 0 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | 010 2 | 0 | 1 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | 011 2 | 0 | 1 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | 100 2 | 1 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | 101 2 | 1 | 0 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | 110 2 | 1 | 1 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | 111 2 | 1 | 1 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Se ha usado un cable auxiliar `ab` para conectar
la salida de la puerta AND `a1` con una entrada
de la puerta OR `o1` . El resultado de su ejecución
coincide con la tabla vista en teoría:

| a b c | f2 
----------
0 0 0 0 | 0
5 0 0 1 | 1
10 0 1 0 | 0
15 0 1 1 | 1
20 1 0 0 | 0
25 1 0 1 | 1
30 1 1 0 | 1
35 1 1 1 | 1 |  |
| --- | --- |

## Operadores relacionales
Además del ya visto

!=

, Verilog admite los
siguientes operadores relacionales:

<

(menor
que),

<=

(menor o igual que),

==

(igual que),

>=

(mayor o igual que) y

>

(mayor que). Cuando alguno de los operandos
contiene

x

o

z

, el resultado es

x

. En otro caso, el resultado dependerá
de si se cumple la condición (1) o no (0).

Si se desea una comparación de igualdad estricta
(considerando las `x` s y las `z` s)
se ha de usar `===` (estrictamente igual) y `!==` (estrictamente distinto)

## Operadores logicos
Para expresar una condición dentro de un programa
Verilog, a veces es necesario disponer de los operadores
lógicos Y, O y NO. En Verilog se expresan como

&&

(Y),

||

(O) y

!

(NO). Así, para expresar algo
como: "Si no ocurre que a es mayor que cero y
b distinto de cuatro...", lo haríamos con:

```text
if (!(a>0 && b!=4)) ...
```

Aplicando las leyes de De Morgan, ya sabemos que 
expresamos lo mismo con:

```text
if (a<=0 || b==4) ...
```

## Ejercicio 3
Constrúyase la tabla de verdad de la función
f

3

vista en teoría y cuyo diagrama con
puertas es el que se muestra a continuación:

La {numref}`fig-verilog-03-f3for` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_03/f3for.png
---
name: fig-verilog-03-f3for
alt: f3
width: 85%
align: center
---
f3
```

La {numref}`fig-verilog-03-f3` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_03/f3.png
---
name: fig-verilog-03-f3
alt: f3
width: 85%
align: center
---
f3
```

## Ejercicio 4
Comprobad, mediante un programa Verilog, que la función
f

3

es equivalente a esta otra elaborada
solamente con puertas NAND:

La {numref}`fig-verilog-03-f3nand` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_03/f3nand.png
---
name: fig-verilog-03-f3nand
alt: f3 con puertas NAND
width: 85%
align: center
---
f3 con puertas NAND
```

## Fuente original

Contenido adaptado a TeachBook a partir de la pagina de referencia: <http://avellano.usal.es/~compi/sesion3.htm>.
