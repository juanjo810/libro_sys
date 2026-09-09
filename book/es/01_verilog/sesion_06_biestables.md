# Sesion 6. Biestables

Esta pagina respeta la secuencia de la sesion original: cada apartado aparece en el mismo orden y los ejercicios se mantienen como secciones propias dentro del recorrido.

```{admonition} Objetivos de aprendizaje
:class: tip

- Construir biestables RS y JK.
- Distinguir asignaciones bloqueantes y no bloqueantes.
- Usar reloj, flancos, `always`, bucles y `case`.
```

## Ejercicio 1
Programar un biestable RS con ayuda de dos puertas NOR:

La {numref}`fig-verilog-06-rs` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_06/rs.png
---
name: fig-verilog-06-rs
alt: Biestable RS
width: 85%
align: center
---
Biestable RS
```

La {numref}`fig-verilog-06-rstabla` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_06/rstabla.png
---
name: fig-verilog-06-rstabla
alt: Tabla del biestable RS
width: 85%
align: center
---
Tabla del biestable RS
```

¿Cuál es la salida si se somete al biestable a esta
batería de entradas?

```text
$monitor($time," R=%b, S=%b, Q=%b, NQ=%b", R, S, Q, NQ);
      R=0; S=0;
      #5 R=0; S=1;
      #5 R=0; S=0;
      #5 R=1; S=0;
      #5 R=1; S=1;
      #5 R=0; S=0;
      #5 R=1; S=1;
      #5 S=0; R=0;
```

¿Por qué la salida es diferente en la última
línea y en la antepenúltima?

## Asignacion no bloqueante
Cuando aparecen varias asignaciones consecutivas en Verilog estas
asignaciones se realizan de modo consecutivo. Así, la
línea

```text
#5 R=0; S=0;
```

primero calcula el resultado de asignar 0 a R y sus consecuencias
y, posteriormente, asigna 0 a S.

Existe otro tipo de asignación en Verilog, la
asignación no bloqueante. Su símbolo es `<=` . Si se usa la asignación no bloqueante, #5 R<=0; S<=0; se asignan todos los valores y se calcula a la vez las consecuencias.
Probad si se producen cambios al sustituir alguna de las
asignaciones del ejercicio anterior por asignaciones no bloqueantes.
Incidid especialmente en los alrededores y en los propios estados
inválidos y neutros. ¿Cuál es el valor de `a` , `b` , `c` y `d` al final del siguiente ejemplo? #5 a=1; b=2; c=3; d=4;
#5 a=b; b=a;
#5 c<=d; d<=c;

## Ejercicio 2
Añadir al biestable del ejercicio anterior una entrada de
reloj activa a nivel alto:

La {numref}`fig-verilog-06-rsc` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_06/rsc.png
---
name: fig-verilog-06-rsc
alt: Biestable RS con reloj
width: 85%
align: center
---
Biestable RS con reloj
```

La {numref}`fig-verilog-06-rsctabla` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_06/rsctabla.png
---
name: fig-verilog-06-rsctabla
alt: Tabla del biestable RS con reloj
width: 85%
align: center
---
Tabla del biestable RS con reloj
```

[Soluciones y comentarios](http://avellano.usal.es/~compi/sol0703.htm)

## Senal de reloj. Bloque always
El bloque

always

da instrucciones a Verilog para
que el código que se especifica se ejecute una y otra vez
mientras dure la simulación. Podemos usar un bloque

always

para construir una señal de reloj:

```text
always #7 C=~C;
```

Suponemos que para generar la señal de reloj hemos definido
previamente un registro

C

. El bloque

always

anterior hace que dicho registro cambie a su valor complementario
cada 7 unidades de tiempo. Hemos conseguido, pues, un reloj de
periodo 14 unidades de tiempo.

`always` es un bloque, del mismo tipo que el que
ya hemos visto de `initial` . Si tiene que contener
más de una instrucción, deben ir rodeadas por `begin` y `end` , como de costumbre.

## Ejercicio 3
Añadir un bloque

always

a las pruebas del
ejercicio anterior para generar una señal de reloj de
periodo 14 unidades de tiempo. Obsérvese cómo
el biestable solamente reacciona a las señales R y S
cuando el reloj se encuentra en alto.

## Ejercicio 4
Modifíquese el diseño del ejercicio anterior
para construir un biestable RS activo en el flanco de subida
de reloj. Para ello, pásese la señal de reloj
por este circuito detector de flanco de subida antes de
pasársela al biestable del ejercicio anterior:

La {numref}`fig-verilog-06-det` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_06/det.png
---
name: fig-verilog-06-det
alt: Detector de flanco de subida
width: 85%
align: center
---
Detector de flanco de subida
```

El funcionamiento del circuito es muy sencillo. La puerta NOT
retarda una unidad de tiempo e invierte la señal. Esta
señal modificada y la original se pasan por una puerta
AND. El retardo y la inversión provocan la aparición
de unos pequeños pulsitos justo a continuación del
flanco de subida de la señal original.

Compruébese cómo el biestable es ahora activo en
los flancos de subida del reloj.

## Ejercicio 5
Prográmese en Verilog y compruébese este circuito
que realiza un biestable JK activo por nivel alto de reloj y
con líneas de PRESET y CLEAR:

La {numref}`fig-verilog-06-jk` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_06/jk.png
---
name: fig-verilog-06-jk
alt: Biestable JK con reloj, preset y clear
width: 85%
align: center
---
Biestable JK con reloj, preset y clear
```

La {numref}`fig-verilog-06-jktabla` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_06/jktabla.png
---
name: fig-verilog-06-jktabla
alt: Tabla del biestable JK con reloj, preset y clear
width: 85%
align: center
---
Tabla del biestable JK con reloj, preset y clear
```

Particularmente, estúdiese lo siguiente:

1. Poniendo la señal de reloj en cero continuo, véase
que las señales PRESET y CLEAR son asíncronas
2. Poniendo la señal de reloj en uno continuo, y
desactivando las señales de PRESET y CLEAR, comprobar
el funcionamiento de las entradas J y K. Es posible que
al probar a activar a la vez las señales J y K, el
funcionamiento no sea el esperado o que incluso se
bloquee la simulación. Si es el caso, púlsese
CTRL+C
3. Repetir la prueba de J=1 y K=1, pero asignando un retardo
de una unidad de tiempo a todas las puertas NAND.
4. Investigar qué sucede jugando con los retardos
independientes de cada puerta, hasta alcanzar valores
de comportamiento deseables

Como se deduce del último punto de la lista anterior, en
los circuitos secuenciales es fundamental tanto la existencia
de realimentación como los retardos.

## Bucles
En la sección de comportamiento de un módulo, Verilog
tiene instrucciones para realizar la misma operación
varias veces. Una de ellas ya la hemos visto (

while

),
aquí vienen algunas más:

- `while(` *condición* `)` *orden* : ejecuta la orden mientras la
condición sea verdadera
- `for(` *orden inicial* `;` *condición* `;` *orden recurrente* `)` *orden* : ejecuta la orden inicial una vez y, mientras la
condición sea verdadera, ejecuta la orden y la
orden recurrente
- `repeat(` *n* `)` *orden* : ejecuta la orden *n* veces
- `forever` *orden* : ejecuta la orden para siempre
( *bucle infinito* )

La orden que se repite (el *cuerpo del bucle* ) puede ser
una única instrucción o un bloque encerrado entre
las órdenes `begin` y `end` .

El siguiente ejemplo realiza una cuenta atrás de 10 a 0
mediante tres órdenes diferentes:

```text
integer i;
  $monitor("i=%d",i);

  // Con while
  i=10;
  while (i>0) #5 i=i-1;

  // Con for
  for (i=10; i>0; i=i-1) #5;

  // Con repeat
  i=10;
  repeat (10) #5 i=i-1;
```

## Las instrucciones case
Constituyen una forma muy cómoda de evitar sucesivos

if

s cuando se tiene que elegir una opción
de varias en función del valor de una variable o
expresión. Su forma general es:

case (

expresión

)

alternativa primera

:

instrucción primera

;

alternativa segunda

:

instrucción segunda

;

... demás alternativas con instrucciones ...

default:

instrucción por defecto (opcional)

;

endcase

Si se sustituye la palabra

case

(¡ojo! el

endcase

se deja igual) por

casex

o

casez

significa que las equis o zetas han de considerarse
como comodines: casan con cualquier otro valor.

## Bloque always condicionado
Se puede añadir al bloque

always

el nombre de una señal
de modo que el bloque se ejecute

siempre que

esa señal cambie:

```text
always @(
variable
)
     begin
        
...

     end
```

También se puede especificar más de una señal, separadas
por comas, con el significado de que se ejecute el bloque siempre que cambie
alguna de esas señales:

```text
always @(
variable
1
,
variable
2
, 
...
)
     begin
        
...

     end
```

Finalmente, añadiendo delante del nombre de la variable las palabras

posedge

o

negedge

, logramos que el bloque se ejecute
en el flanco de subida o de bajada, respectivamente.

## Modelos de comportamiento
Como se desprende del ejercicio anterior, tener en cuenta las
restricciones que impone el comportamiento real de los dispositivos
y puertas puede llegar a ser muy complicado.

Hay veces en que no nos interesa llegar hasta tanto nivel
de detalle, sino describir someramente lo que queremos y que sea
una herramienta automática de síntesis la que se
encargue de considerar el bajo nivel. Aparecen así los
modelos de comportamiento en Verilog. Veamos cómo construimos
un biestable JK activo en flanco ascendente de reloj con
línea de PRESET y CLEAR, ambas activas a nivel bajo y
prioritarias: module JKup(output reg Q, output wire NQ, input wire J, input wire K,
input wire C, input wire nPRESET, input wire nCLEAR);
not(NQ,Q);
initial
begin
Q=0;
end 
always @(posedge C)
if (nPRESET && nCLEAR) // PRESET y CLEAR tienen prioridad
case ({J,K})
2'b10: Q=1;
2'b01: Q=0;
2'b11: Q=~Q;
endcase
always @(nPRESET,nCLEAR)
case ({nPRESET,nCLEAR}) // Si estAn activas ambas, no hacer nada
2'b01: Q=1;
2'b10: Q=0;
endcase
endmodule Lo primero que necesitamos es algo que retenga el valor de Q, por
lo que transformamos el cable en un registro. Mediante una puerta
NOT obtenemos el valor de NQ como hacíamos antes.

En el bloque `initial` , asignamos al biestable el
valor 0

A continuación vienen dos bloques que se estarán
ejecutando siempre ( `always` ) que se cumpla una
condición. El el primero de ellos, en el flanco de subida
de `C` . El segundo, cada vez que varíen `nPRESET` o `nCLEAR` .

El resto del código es bastante autoexplicativo.
Mediante el operador de concatenación ( `{}` ),
construimos valores J,K o nPRESET,nCLEAR. Mediante la
instrucción de Verilog `case` , decimos lo que
ha de suceder en los casos en que ha de suceder algo.

## Ejercicio 6
Comprobad que el biestable JK recién definido funciona
correctamente. Tratad de añadir un detector de flanco
positivo al biestable JK del ejercicio anterior y de ajustar los
retardos del detector y de las puertas del biestable para que
el funcionamiento sea el esperado. Notad la diferencia en cuanto
a dificultad de ambos métodos.

## Fuente original

Contenido adaptado a TeachBook a partir de la pagina de referencia: <http://avellano.usal.es/~compi/sesion6.htm>.
