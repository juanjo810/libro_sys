# Sesion 2. Operaciones con bits

Esta pagina respeta la secuencia de la sesion original: cada apartado aparece en el mismo orden y los ejercicios se mantienen como secciones propias dentro del recorrido.

```{admonition} Objetivos de aprendizaje
:class: tip

- Usar mascaras para activar, desactivar, voltear y consultar bits.
- Aplicar operadores de reduccion.
- Combinar senales mediante concatenacion y replicacion.
```

## Operaciones con bits
A veces, es interesante realizar operaciones sobre un conjunto
determinado de bits dejando el resto inalterado. En las
secciones que vienen a continuación aprenderemos
a activar, desactivar, voltear, comprobar el valor,
reducir, concatenar y replicar los bits de registros en Verilog.
Estas nuevas
instrucciones de manejo de bits se añaden a las
ya vistas de desplazamiento lógico y aritmético.

## Complemento a uno
Para cambiar todos los bits de un registro de 0 a 1 ó
de 1 a 0, lo que se denomina

complemento a uno

,
se usa en Verilog el operador

~

, también
conocido como NOT a nivel de bits (no confuncir con el NOT
lógico, cuyo símbolo es el signo de cierre de
admiración "

!

"):

| NOT |
| --- |
| ~ 1011101010101011 |
| 0100010101010100 |

## Activar un conjunto de bits
Para activar un conjunto de bits de un registro dejando el resto
inalterado se construye una máscara binaria con un
1 en cada posición que queremos activar y un cero el las
posiciones que queremos dejar tal cual. Con dicha máscara,
se realiza una operación OR con el registro.
El operador OR a nivel de bits de Verilog es

|

.
No se debe confundir con el operador lógico OR
(

||

).

Por ejemplo, si queremos activar los bits primero, tercero
y séptimo de un registro empezando a contar por la
izquierda, la máscara debe ser `'b1000101` :

| BIT SET |
| --- |
| 1011101010101011 |
| | 0000000001000101 |
| 101110101 1 101 1 1 1 |

## Desactivar un conjunto de bits
La máscara se contruye de modo inverso al caso anterior.
Se debe poner un 0 en cada lugar que queramos desactivar un
bit y un 1 en el resto. La operación pertinente
en este caso es AND que, en Verilog, se representa por

&

. No debe confundirse con la operación
lógica AND que se escribe

&&

:

Desactivemos los bits primero, tercero
y séptimo de un registro empezando a contar por la
izquierda, la máscara debe ser `~'b1000101` que, para 16 bits es lo que
aparece en la figura:

| BIT RESET |
| --- |
| 1011101010101011 |
| & 1111111110111010 |
| 101110101 0 101 0 1 0 |

## Voltear un conjunto de bits
En este caso se trata de cambiar un conjunto de bits de un
registro por su valor opuesto, dejando el resto igual.
La máscara se construye igual que en el caso de la
activación. La operación que se debe realizar
es XOR, que en Verilog se representa por

^

.

Se voltean ahora los bits primero, tercero
y séptimo de un registro empezando a contar por la
izquierda, la máscara debe ser `'b1000101` :

| BIT COMPLEMENT |
| --- |
| 1011101010101011 |
| ^ 0000000001000101 |
| 101110101 1 101 1 1 0 |

## Comprobar el valor de un bit
A veces nos interesa saber si un determinado bit de un registro
es 1 ó 0. Para ello, nos ayudamos de una máscara
y la operación AND. Por ejemplo, si queremos saber si el
bit sexto empezando a contar por la derecha de un registro

r

está a 1, haríamos algo como:

```text
if ((r & 'b100000) != 0)
     begin
       // Hacemos lo que hay que hacer cuando el bit estA activado
     end
   else
     begin
       // Hacemos lo que hay que hacer cuando el bit estA desactivado
     end
```

## Ejercicio 1

Declarad un registro de dieciséis bits sin signo y dadle un valor inicial cualquiera.

Activar el quinto bit, desactivar el noveno, décimo y undécimo, y voltead el decimosexto empezando por la derecha. Imprimid por pantalla el contenido del registro antes y después de las operaciones.

## Ejercicio 2 (más difícil)

Haced un pequeño programa que cuente cuántos bits están activos en un registro `r` de dieciséis bits sin signo.

Para ello, construid la máscara con valor `'h8000`. Efectuad mediante un `while` dieciséis vueltas comprobando bit a bit el registro con ayuda de la máscara, que se desplazará un bit a la derecha en cada iteración.

```{note}
La sintaxis de la orden `while` en Verilog es idéntica a la de C, salvo que el cuerpo del bucle puede estar rodeado por las sentencias `begin` y `end`, en lugar de por llaves.
```

## Operaciones de reduccion de bits
En Verilog es posible, con una unica instruccion
calcular el resultado de aplicar una operación lógica
a todos los bits de un registro. Así, si tenemos un registro

r

de cuatro bits, cuyo valor es

'b1100

,
la reducción AND se expresa como

&r

y consiste
en aplicar la operación AND a todos los bits del registro
de derecha a izquierda, o sea,

&r

es lo mismo que

0 & 0 & 1 & 1

en el ejemplo.

Se pueden aplicar reducción con todas las operaciones
principales:

| Operación Símbolo Operación Símbolo | Símbolo Operación Símbolo | Símbolo Operación Símbolo |  | Operación Símbolo | Símbolo | Símbolo |
| --- | --- | --- | --- | --- | --- | --- |
| and & nand ~& | & nand ~& | & |  | nand ~& | ~& | ~& |
| or | nor ~| | | nor ~| | | |  | nor ~| | ~| | ~| |
| xor ^ xnor ~^ o ^~ | ^ xnor ~^ o ^~ | ^ |  | xnor ~^ o ^~ | ~^ o ^~ | ~^ o ^~ |

## Ejercicio 3

El bit de *paridad par* de un registro se define como:

- `0`, si el número de bits `1` en el registro es par.
- `1`, si el número de bits `1` en el registro es impar.

El bit de *paridad impar* de un registro se define como:

- `0`, si el número de bits `1` en el registro es impar.
- `1`, si el número de bits `1` en el registro es par.

Estos bits se usan para detectar errores de transmisión. Prográmese un código Verilog que, dado un registro de ocho bits:

1. Ponga el bit más significativo del registro a cero.
2. Imprima el registro en binario.
3. Calcule el bit de paridad par del registro, mediante una orden `while`, similarmente a cómo se hizo en el ejercicio anterior para contar los bits de un registro que son `1`.
4. Almacene dicho bit en el bit más significativo del registro.
5. Imprima el registro modificado en binario.

Hágase lo mismo, pero sin bucle y usando instrucciones de reducción.

Decidir, sin ayuda de Verilog, si al recibirse `8'b10101010` con el bit de paridad impar almacenado en el bit más significativo, dicho valor es un error de transmisión o no.

¿Cómo haríamos esa comprobación con una única instrucción de Verilog?

## Operaciones de concatenacion y replicacion
Podemos concatenar varios registros de tamaño conocido para
formar otro de tamaño mayor con el operador concatenación
de Verilog (

{ }

). Los registros o constantes que se
quieren concatenar se separan por comas.

El operador de replicación permite concatenar varias
copias seguidas de un mismo registro. Se expresa anteponiendo
el numero de veces que se quiere replicar el registro
a las llaves, como se ve en el siguiente ejemplo general:

```text
reg A;
  reg [1:0] B, C;
  A=1'b1; B=2'b00; C=2'b10;

  // { 4{A}, 2{C}, B, 3{3'b011} } da como resultado
  // 19'b1111101000011011011.
  //
  // ExplicaciOn: 1111 (4xA) 1010 (2xC) 00 (B) 011011011 (3x3'b011)
```

## Fuente original

Contenido adaptado a TeachBook a partir de la pagina de referencia: <http://avellano.usal.es/~compi/sesion2.htm>.
