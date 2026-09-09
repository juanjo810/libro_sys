# Sesion 1. Introduccion a Verilog

Esta pagina respeta la secuencia de la sesion original: cada apartado aparece en el mismo orden y los ejercicios se mantienen como secciones propias dentro del recorrido.

```{admonition} Objetivos de aprendizaje
:class: tip

- Entender Verilog como lenguaje de descripcion de hardware.
- Crear, compilar y ejecutar un primer fichero `.v`.
- Usar constantes, registros, cables y `$display` para comprobar resultados.
```

## Presentacion de Verilog
Verilog es una herramienta de diseño digital
asistido por ordenador (

Computer-Aided
Digital Design

). Con la llegada de la
tecnología VLSI (

Very Large Scale Integration

),
con más de 100,000 transistores en un chip,
estas herramientas se han convertido en un estándar
industrial y son imprescindibles.

En concreto, Verilog es un lenguaje de descripción
de hardware ( *HDL: Hardware Description Language* ),
creado en 1983 en la compañía Automated 
Integrated Design Systemas. Verilog está estandarizado
por el IEEE. Los HDLs permiten describir
un diseño al nivel de transferencia entre registros.
Los detalles de más bajo nivel (puertas lógicas
y su interconexión) pueden ser generadas por
herramientas automáticas de síntesis a partir
de su descripción en un HDL. Los HDLs también
se pueden usar para simular y depurar el resultado obtenido,
por lo que la elaboración de hardware sigue
un proceso en la actualidad que coincide en muchos aspectos 
con la elaboración de software.

La sintaxis de Verilog es muy similar a la sintaxis de C, por
lo que estas prácticas os servirán de apoyo y
complemento a las realizadas en las asignaturas de 
programación.

## Configuracion del entorno de trabajo
Las prácticas se realizarán en el Sistema
Operativo GNU/Linux. Para poder trabajar en vuestra casa,
es muy conveniente que os instaléis una distribución
de Linux.

[Icarus 
Verilog](http://www.icarus.com/eda/verilog/) y [GPL
Cver](http://sourceforge.net/projects/gplcver/) son dos implementaciones de Verilog libres que
están disponibles para Linux.

Si os instaláis una distribución de Linux
basada en Debian (la propia Debian, u otras más
sencillas como Kubuntu), debéis instalar los
paquetes `iverilog` y/o `gplcver` :

```text
sudo apt-get install iverilog
sudo apt-get install gplcver
```

En los ordenadores de clase, ya están instalados
estos dos paquetes.

Se necesita, tambíen, un editor de texto para
generar los programas. Cualquiera que genere texto
plano puede ser válido: `vi` , `kate` , `gedit` , etc.

## Primer programa en Verilog
Aunque el objetivo principal de verilog es el diseño de
hardware, es tradicional que el primer programa que se
prueba en un nuevo lenguaje de programación sea uno
que imprima en la pantalla las palabras

Hola mundo

.

Abrid, pues, el editor de textos para generar el siguiente
fichero al que nombraréis `hello.v` :

```verilog
/* Programa de ejemplo: hello.v */

module hello;

  initial
    // Imprimimos el mensaje y un salto de lInea
    $display("Hola, mundo\n");

endmodule
```

Una vez hayáis guardado el programa, debéis
abrir una ventana con la línea de órdenes.
Observad que habéis creado bien el programa tecleando `ls -l` . Os ha de aparecer una línea
similar a la siguiente:

```text
-rw-r--r-- 1 gyermo gyermo   151 2010-05-20 20:50 hello.v
```

Procedamos ahora a compilar y ejecutar el programa:

1. **Primero con iverilog** : Compilamos: iverilog hello.v -o hello Debe aparecer ahora un fichero ejecutable, cuyo nombre
será `hello` . Miradlo con `ls -l` : -rwxr-xr-x 1 gyermo gyermo 448 2010-05-20 20:50 hello
-rw-r--r-- 1 gyermo gyermo 151 2010-05-20 20:50 hello.v Finalmente, lo ejecutamos con `./hello` : Hola, mundo
2. **Ahora, con cver** : Con `cver` no es necesario compilar. Simplemente
hay que teclear `cver hello.v` . La salida es: GPLCVER_2.12a of 05/16/07 (Linux-elf).
Copyright (c) 1991-2007 Pragmatic C Software Corp.
All Rights reserved. Licensed under the GNU General Public License (GPL).
See the 'COPYING' file for details. NO WARRANTY provided.
Today is Thu May 20 21:39:01 2010.
Compiling source file "hello.v"
Highest level modules:
hello
Hola, mundo
0 simulation events and 0 declarative immediate assigns processed.
1 behavioral statements executed (1 procedural suspends).
Times (in sec.): Translate 0.0, load/optimize 0.1, simulation 0.1.
End of GPLCVER_2.12a at Thu May 20 21:39:01 2010 (elapsed 0.0 seconds). Esta salida también se escribe en un fichero denominado `verilog.log` . Lo podéis comprobar tecleando `cat verilog.log` .

De ahora en adelante, podéis usar cualquiera de los
dos, `iverilog` o `cver` , a no ser que
se especifique lo contrario en algún apartado.

## Comentarios
Los comentarios se marcan como en C.

```text
/* Este es un tipo de comentario */

/* Este tipo de comentario puede abarcar
   varias lIneas */

// Este tipo de comentario sOlo puede abarcar una lInea
```

## Cadenas de caracteres
Las cadenas de caracteres se encierran entre comillas dobles
("). Algunos caracteres se marcan de modo especial:

| \n | retorno del carro |
| --- | --- |
| \t | tabulador |
| %% | % |
| \\ | \ |
| \" | " |
| \ xxx | cualquier carácter, xxx en octal |

`"Hola, mundo\n"` es un ejemplo de una cadena
de caracteres que tiene 12 caracteres: 4 caracteres de la palabra *Hola* , una coma, un espacio, 5 caracteres de la palabra *mundo* y un carácter especial que hace que se produzca
un salto a la línea siguiente ( `\n` ).

## Constantes numericas
Si no se indica nada, una constante numérica es interpretada
por Verilog en decimal. También se pueden expresar
constantes numéricas en otras bases anteponiendo los
prefijos:

'b

(binario),

'o

(octal),

'd

(el propio decimal)

'h

(hexadecimal).

Si el numero es negativo, se antepone el signo menos.
Por ejemplo, `-'hD1C` .

Los numeros reales se pueden expresar en la notación
habitual, usando el punto como separador decimal o en notación
científica (por ejemplo, `7.237e10` ).
Solamente se admite
la base 10 en los numeros reales.

Con el objetivo de aumentar la legibilidad de los numeros
binarios, se permite el uso del carácter de subrayado
dentro de una constante numérica. Por ejemplo, `'b1_1011_1111_1000` es lo mismo que `'b1101111111000` .

## Tipos de dato de registros
En Verilog existen dos tipos de datos numéricos, uno
que representa un entero con signo (

integer

) y
otro un numero de coma flotante (

real

).

El entero será del tamaño de la palabra
que maneje nuestro ordenador, pero, como mínimo de
32 bits.

## Bloques de codigo
En C, algunas instrucciones como

for

,

if

o

while

admiten en su cuerpo
una unica instruccion o varias (un bloque
de instrucciones). En C, estos bloques se encierran entre
llaves (

{

y

}

). En Verilog, esta
misma función la realizan las palabras reservadas

begin

y

end

.

Así, la instruccion `initial` del ejemplo `hello.v` solo tienen una instruccion `$display` en su cuerpo. No necesita, por tanto,
ni `begin` ni `end` . Si llevara más
instrucciones sí que sería necesario, como en el ejemplo
del apartado siguiente.

## Funcion $display
Una función, al igual que ocurre en matemáticas, se
caracteriza en programación porque tiene varios argumentos
o parámetros y devuelve un valor. Las funciones en programación
se diferencian de las funciones matemáticas en que pueden no devolver nada
y pueden ejecutar instrucciones en su interior cuando se las llama.
Los parámetros de una función aparecen entre comillas
a continuación del nombre de la función y van separados
por comas.

La función

$display

puede llevar un numero
arbitrario de argumentos y no devuelve nada. Sirve para sacar información
por la pantalla. Si no lleva argumentos, imprime un salto de
línea. De llevarlos, el primero es una cadena de caracteres que,
como en el caso de

hello.v

, se imprimirá en la
pantalla.

La función

$display

puede también imprimir
en la pantalla el contenido de las variables que deseemos imprimir.
Para ello, se incluye un códigos de formato en el lugar que
queremos que aparezca el contenido de la variable. El código
de formato también sirve para indicar en qué base, por
ejemplo, queremos que salga el valor. Cuando se incluyen códigos
de formato, hay que añadir un parámetro por cada uno
de ellos indicando la variable cuyo contenido deseamos imprimir.
Por ejemplo:

```verilog
integer i;
real f;

initial
begin
  i=4;
  f=2.7172;
  $display("i vale %d y f vale %g",i,f);
end
```

La salida de este programa debería ser:

```text
i vale           4 y f vale 2.7172
```

`$display` ha sustituido el primer `%d` por
el contenido del la variable que aparece en el segundo argumento
(la `i` ) y `%f` por el contenido de la
variable que aparece como tercer argumento ( `j` ). Los códigos de formato de `$display` aparecen
a continuación. Son también admisibles con
mayúscula, con el mismo significado. 
| %d | Entero en decimal |
| --- | --- |
| %b | Entero en binario |
| %o | Entero en octal |
| %h | Entero en hexadecimal |
| %c | Carácter |
| %s | Cadena de caracteres |
| %f | Real en formato decimal |
| %e | Real en formato científico |
| %g | Real en el formato más corto 
de los dos anteriores |

## Estructura del programa
El programa anterior os puede haber quedado parecido a este:

La {numref}`fig-verilog-01-ej-1-9` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_01/ej_1_9.png
---
name: fig-verilog-01-ej-1-9
alt: Ejercicio 1.9
width: 85%
align: center
---
Ejercicio 1.9
```

Veamos someramente de qué partes está compuesto:

La {numref}`fig-verilog-01-ej-1-9-comentado` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_01/ej_1_9_comentado.png
---
name: fig-verilog-01-ej-1-9-comentado
alt: Ejercicio 1.9 comentado
width: 85%
align: center
---
Ejercicio 1.9 comentado
```

1. **Nombre e inicio del módulo** : un programa puede
tener, como ya veremos, varios módulos y al menos
debe tener uno. Le debemos dar un nombre a cada módulo.
El nombre elegido para el módulo de este programa
ha sido `ej_1_9`
2. **Área de definición de las variables** : 
las variables son elementos de nuestro programa capaces de almacenar
un valor. Todas tienen un nombre que las identifica ( `i` y `f` en las dos que aparecen en el ejemplo) y son de
una clase (tecnicamente *tienen un tipo* ). El tipo
de variable nos indica la clase de valores que puede contener
la variable. En el ejemplo, la primera variable puede contener
enteros ( `integer` ) y la segunda variable, numeros
de coma flotante ( `real` ). En el área marcada
se definirán las variables que vamos a usar en el módulo
3. **Bloque initial** : dentro de este bloque
situaremos las instrucciones del módulo (el programa).
Las instrucciones se irán ejecutando una tras otra.
Si el bloque contuviera una unica instruccion, como
en el primer ejemplo ( `hello.v` ), no sería necesario
incluir las palabras `begin` y `end` . En el
resto de casos se incluyen para que el ordenador sepa dónde
empieza y acaba el bloque
4. **Área de instrucciones** : las instrucciones
de un programa se pueden extender y partir en varias líneas.
Lo que marca el fin de una instruccion es el punto y coma
final, que es obligatorio. En el ejemplo damos valores a las
variables `i` y `j` y, posteriormente,
imprimimos el contenido de las variables con la función `$display` .
5. **Fin del módulo** : es obligatorio marcarlo
con `endmodule`

Notas:

- La orden `module` , las declaraciones de variables
y las órdenes de nuestro programa deben acabar
obligatoriamente en punto y coma ( `;` )
- La sintaxis de Verilog y sus conceptos son muy similares a los
del lenguaje de programación C que estudiaréis
en las asignaturas de Programación. Aunque ahora
os cueste digerir estos conceptos, los veréis en profundidad
y cobrarán sentido en dichas asignaturas

## Ejercicio 1

Responde a las siguientes preguntas provenientes de los ejemplos vistos en teoría, primero realizando el cálculo manualmente y, luego, comprobándolo con un programa en Verilog:

1. Expresa en decimal el número `0x1FEA`.
2. Ídem el número en binario `1000101`~2~.
3. Expresa en octal el número `1234`.
4. Pasa a hexadecimal el número en binario `1010011`~2~.

## Registros
Las variables de tipo representan unidades de almacenamiento.
Si no se especifica nada, los registros serán de un bit.
Si se desean de más de un bit, hay que declararlo
explícitamente. Estos registros de más de un
bit son, por defecto, sin signo. Si se quieren con signo,
se añade la palabra clave

signed

, como
se muestra en los siguientes ejemplos:

```text
reg reloj;           /* Registro de un bit */
reg [31:0] busA;     /* Registro de 32 bits, sin signo */
reg signed [63:0] m; /* Registro de 64 bits, con signo */
```

Al asignarle un valor a un registro, podemos hacerlo al
completo o a un subconjunto de sus bits. Si lo que se
asigna es una constante, se le puede anteponer su tamaño
en bits:

```text
reloj=1'b0;
busA='hAAAABBBB;
busA[7:4]=4'hC;
m=-1;
```

## Ejercicio 2

Declarad las variables y asignarles los valores del apartado anterior. Imprimidlas después en hexadecimal y tratad de adivinar el resultado que aparece por pantalla. A continuación, dad respuesta a las siguientes preguntas relacionadas con la teoría, primero manualmente y, luego, con Verilog:

1. Almacenad en un registro de 16 bits el número `2323` e imprimidlo en binario y hexadecimal.
2. Escribid en hexadecimal, binario y decimal el número mayor y más pequeño que se puede almacenar en un registro de 16 bits sin signo.
3. ¿Qué expresión tiene en binario el número `6789` cuando se expresa en complemento a dos en un registro de 16 bits?
4. Expresar el `-22` en un registro de ocho bits y pasarlo a uno de 16 bits extendiendo el signo.

## Operadores aritmeticos
Los operadores aritméticos coinciden con los de C:
suma (

+

), resta (

-

), 
multiplicación (

*

) y
división (

/

). También existe un
operador de exponenciación que no existe en C
(

**

).

La división de dos cantidades enteras nos da
la parte entera del cociente. Si se quiere saber cuál
es el resto de la división, se debe usar el
operador módulo ( `%` ).

## Ejercicio 3 (más difícil)

Declarad una variable de tipo registro de 16 bits. Asignadle un valor cualquiera. Escribid mediante cuatro instrucciones `$display` los cuatro dígitos hexadecimales que forman el registro, empezando por el menos significativo.

Por ejemplo, si asignáis a la variable `'hAB12`, debe salir por la pantalla `2`, `1`, `b` y `a`.

## Operaciones de desplazamiento de bits
Hemos visto en teoría que existen cuatro tipos de
desplazamiento de bits en un registro. Estos son los
cuatro tipos con el operador que se usa en Verilog para
usarlos:

- Desplazamiento lógico a la derecha 
( `>>` )
- Desplazamiento lógico a la izquierda
( `<<` )
- Desplazamiento aritmético a la derecha
( `>>>` )
- Desplazamiento aritmético a la izquierda
( `<<<` )

La diferencia entre desplazamiento lógico y aritmético
estriba en que el último respeta el bit de signo
en numeros expresados en complemento a dos en registros
con signo. Por ejemplo:

| LOGICAL 
SHIFT RIGHT (con signo o sin signo) |
| --- |
| 1011101010101011 |
| >> 7 |
| 0000000101110101 |
|  |
| ARITHMETIC
SHIFT RIGHT (con signo) |
| 1011101010101011 |
| >>> 7 |
| 1111111101110101 |

En el caso de que el registro sea sin signo, ambos tipos de
desplazamiento coinciden:

| ARITHMETIC
SHIFT RIGHT (sin signo) |
| --- |
| 1011101010101011 |
| >>> 7 |
| 0000000101110101 |

El primer operando es el numero que se quiere desplazar y
el segundo indica el numero de bits, como en este ejemplo
en que se desplaza 3 posiciones a la izquierda el contenido del
registro `a` y el resultado se escribe en `b` :

```text
b= (a<<3);
```

## Ejercicio 4 (más difícil)

Declarad dos números enteros con signo de 16 bits, `pos` y `neg`, y dadles un valor inicial positivo al primero y negativo al segundo.

Efectuad los cuatro tipos de desplazamientos sobre los números originales y anotad el resultado. Debéis imprimir los números en binario y decimal. Los desplazamientos serán todos de un bit. Se debe restaurar el valor de `pos` y `neg` después de cada desplazamiento.

## Redes y cables
Hay un tipo especial de variables en Verilog denominadas de
forma genérica como

nets

(redes) de las que
el tipo más frecuente es

wire

(cable).

Estas variables se usan como los cables en la realidad:
para conectar puertas o módulos entre sí.
Su tamaño es, por defecto, de un bit.

Necesitan que algún otro elemento les esté
proporcionando su valor, al contrario que los registros,
que son capaces de almacenarlo.

## Valores especiales
Cada bit de un cable o de un registro puede, además
de tomar valores fijos (0 ó 1), tomar uno de estos
dos valores:

1. *Indefinido* : se representa por `x` y significa que el valor puede ser cero o uno, no
se sabe
2. *Alta impedancia* : se representa por `z` y tiene el significado habitual en
electronica

Tanto `x` como `z` funcionan como
digitos normales. Por ejemplo, el valor `'b11xxzz00` indica que los primeros 
dos bits son 1, los dos siguientes no se sabe, los dos
siguientes están en alta impedancia y los
dos ultimos son 0.

Si al asignar un valor en un programa a un registro, el
valor especificado es de menos bits que el registro, se asigna
valor a esos bits con la siguiente regla: si el valor especificado 
tiene el bit 
más significativo a 1 ó 0, los bits más
significativos asignados son 0. Si dicho bit es `x` ,
son `x` . Y, si es `z` , son `z` .

## Ejercicio 5

Definid un registro de 16 bits que tenga sus cuatro bits más significativos ceros, los siguientes cuatro unos, los siguientes cuatro `x` y los últimos cuatro `z`.

Imprimid en binario el valor del registro. Realizad operaciones con él y observad el resultado.

## Fuente original

Contenido adaptado a TeachBook a partir de la pagina de referencia: <http://avellano.usal.es/~compi/sesion1.htm>.
