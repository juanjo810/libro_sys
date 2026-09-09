# Sesion 9. ALU

Esta pagina respeta la secuencia de la sesion original: cada apartado aparece en el mismo orden y los ejercicios se mantienen como secciones propias dentro del recorrido.

```{admonition} Objetivos de aprendizaje
:class: tip

- Usar `` `include `` para incorporar un modulo externo.
- Preparar pruebas para la ALU 74181.
- Guardar resultados intermedios en operaciones compuestas.
```

## Inclusion de ficheros fuente
Se puede, en un punto cualquiera, incluir otro fichero que
funcionará tal y como si lo hubiéramos tecleado en
dicho punto. La orden es

`include

. Así, si
queremos incluir el fichero

SumadorAuxiliar.v

,
tecleamos:

```text
`include "SumadorAuxiliar.v"
```

## Ejercicio 1
El fichero

74181.v

contiene el 
código Verilog
del ALU 74181 vista en teoría. Podéis encontrar el fichero
original en la página web del profesor

John P. Hayes

,
de la Universidad de Michigan
(

http://www.eecs.umich.edu/~jhayes/iscas.restore/74181.html

).
Escríbase un
fichero Verilog con un módulo que realice las siguientes
operaciones usando dicha ALU:

1. 7+4
2. 2+6+1
3. 0110 ~2~ AND
1010 ~2~
4. 0110 ~2~ XOR
1010 ~2~
5. 0110 ~2~ OR
NOT (1010 ~2~ XNOR
0111 ~2~ ) (2 operaciones)
6. 2*7
7. 3*5+1 (2 operaciones)

En el caso de operaciones múltiples, se deben usar registros
para almacenar los valores intermedios. Recordemos el esquema y
la tabla de operaciones de este circuito integrado:

La {numref}`fig-verilog-09-74181` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_09/74181.png
---
name: fig-verilog-09-74181
alt: Esquema del 74181
width: 85%
align: center
---
Esquema del 74181
```

La {numref}`fig-verilog-09-74181t` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_09/74181t.png
---
name: fig-verilog-09-74181t
alt: Tabla de operaciones del 74181
width: 85%
align: center
---
Tabla de operaciones del 74181
```

Si observáis la definición del módulo:

```verilog
module Circuit74181 (S, A, B, M, CNb, F, X, Y, CN4b, AEB);
```

os daréis cuenta de que las líneas de acarreo negadas
son

CNb

y

CN4b

, respectivamente. Las
líneas

X

e

Y

las podéis
dejar sin conectar.

## Fuente original

Contenido adaptado a TeachBook a partir de la pagina de referencia: <http://avellano.usal.es/~compi/sesion9.htm>.
