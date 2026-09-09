# Sesion 5. Encaminadores y sumadores

Esta pagina respeta la secuencia de la sesion original: cada apartado aparece en el mismo orden y los ejercicios se mantienen como secciones propias dentro del recorrido.

```{admonition} Objetivos de aprendizaje
:class: tip

- Usar buffers triestado y tipos de red.
- Construir multiplexores y sumadores.
- Razonar sobre retardos de propagacion.
```

## Buferes triestado
En teoría hemos visto los siguientes búferes
con línea adicional de control para poder poner la salida
en alta impedancia:

La {numref}`fig-verilog-05-bufif1` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_05/bufif1.png
---
name: fig-verilog-05-bufif1
alt: Búfer activo en alta
width: 85%
align: center
---
Búfer activo en alta
```

La {numref}`fig-verilog-05-bufif0` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_05/bufif0.png
---
name: fig-verilog-05-bufif0
alt: Búfer activo en baja
width: 85%
align: center
---
Búfer activo en baja
```

Las instrucciones en Verilog que permiten instanciar el búfer
de la izquierda y el de la derecha son:

```text
bufif1 bIzquierda(Y,A,G);
  bufif0 bDerecha(Y,A,G);
```

También existen las equivalentes puertas NOT con control
de triestado por alto y por bajo que son, respectivamente,

notif1

y

notif0

.

## Contingencia de senales
Puede ocurrir que sobre un cable se viertan varias señales
a la vez. Para que Verilog haga un tratamiento correcto de estos
casos, en aquellas situaciones en que puedan coincidir varias
señales, se tiene que definir la variable no como

wire

, sino como

tri

.

En el caso de contingencia en una variable de tipo

tri

,
se resuelve del modo siguiente:

- Siempre tienen prioridad las señales 1, 0 ó `x` frente a las de alta impedancia ( `z` )
- Descontando las señales de alta impedancia,
si todas las señales coinciden el resultado es 
ese. En caso contrario, el resultado es `x` .

Algunos diseños lógicos exigen cables con
funciones especiales. En caso de contingencia, actúan del
siguiente modo:

- `tri0` : igual que `tri` , pero si todos
son `z` , el valor es 0
(resistencia *pull-down* )
- `tri1` : ídem valor 1 (resistencia *pull-up* )
- `wand` o `triand` : basta un 0 para que
el resultado sea 0
- `wor` o `trior` : basta un 1 para que
el resultado sea 1

## Asignacion de senales a cables
Para efectuar una conexión permanente de un registro a un
cable, se debe usar una asignación. Esto hace que el valor
del registro se vuelque continuamente al cable. La instrucción
en verilog es

assign

:

```text
wire w; reg r;

  assign w=r;
```

## Ejercicio 1
Vamos a aplicar lo aprendido en puntos anteriores con el 
siguiente ejemplo de un transmisor/receptor de bus de un bit,
visto en teoría:

La {numref}`fig-verilog-05-trans` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_05/trans.png
---
name: fig-verilog-05-trans
alt: Transceiver de un bit
width: 85%
align: center
---
Transceiver de un bit
```

Programemos el módulo:

```verilog
module Transceiver(inout tri a, inout tri b, input wire g, input wire dir);

  wire ng,ndir,sa1,sa2;

  not (ng,g);        // No hacemos referencia despuEs => no damos nombres
  not (ndir,dir);
  and (sa1,ng,dir);
  and (sa2,ng,ndir);
  bufif1 (b,a,sa1);
  bufif1 (a,b,sa2);
endmodule
```

Se ha cambiado la señal G para que sea activa a nivel alto.
Los nombres usados han sido:

La {numref}`fig-verilog-05-transnombres` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_05/transNombres.png
---
name: fig-verilog-05-transnombres
alt: Nombres Transceiver
width: 85%
align: center
---
Nombres Transceiver
```

Construimos ahora el módulo de comprobación:

La {numref}`fig-verilog-05-transtest` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_05/transTest.png
---
name: fig-verilog-05-transtest
alt: Test Transceiver
width: 85%
align: center
---
Test Transceiver
```

```verilog
module TestTransceiver;

  tri a,b;
  reg g,dir;
  reg ra,rb;
  Transceiver t(a,b,g,dir);
  assign a=ra; assign b=rb;

  // Bloque de comportamiento
  initial
    begin
      $monitor($time," g=%b, dir=%b, a=%b, b=%b, ra=%b, rb=%b",
                     g,dir,a,b,ra,rb);
         ra=0; rb=1; g=1; dir=0;
      #5 ra='bz; rb='bz; g=1; dir=0;
      #5 rb=1; g=0; dir=0;
      #5 ra='bz; rb='bz; g=1; dir=1;
      #5 ra=0; g=0; dir=1;
      #5 ra=0; rb=1; g=0; dir=1;
    end

endmodule
```

Observad el uso de las variables

tri

y la orden

assign

. Antes de ejecutar la simulación,
tratad de adivinar cuáles son los valores que aparecerán
en la pantalla. ¿Qué cambios habría que hacer
para que la línea G del módulo sea activa por nivel bajo
tal y como aparecía en el diseño original?

## Ejercicio 2
Constrúyase un módulo multiplexor 4x1 con línea
de control de salida OE, de modo que si dicha línea está
inactiva, la salida Y esté en alta impedancia. En caso
contrario, funciona como multiplexor normal. Con dos de estos
multiplexores constrúyase otro módulo multiplexor
8x1 según el esquema de la figura. Pruébese con
ayuda de un módulo auxiliar.

La {numref}`fig-verilog-05-mux8x1` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_05/mux8x1.png
---
name: fig-verilog-05-mux8x1
alt: Multiplexor 8x1
width: 85%
align: center
---
Multiplexor 8x1
```

*Pista* : si no sois capaces de construir el multiplexor 4x1,
podéis fijaros en [esta solución](http://avellano.usal.es/~compi/mux4x1a.png) .
Hay alternativas similares a la solución de la figura que usan un 
decodificador o búferes triestado, por ejemplo.

## Ejercicio 3
Siguiendo el procedimiento descrito en teoría, y con ayuda
del módulo multiplexor 8x1 construido en el ejercicio anterior,
genérese la función de cuatro variables lógicas:

La {numref}`fig-verilog-05-h4` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_05/h4.png
---
name: fig-verilog-05-h4
alt: Función h(a,b,c,d)
width: 85%
align: center
---
Función h(a,b,c,d)
```

Recordemos los pasos que hay que dar:

1. Elegir una variable para cada entrada de selección.
Se dará cuenta de la variable no elegida mediante
las entradas D del multiplexor
2. Sacar factor común de la variable no elegida en cada
posibilidad de las otras
3. Operar hasta conseguir que aparezcan todos los
minitérminos de las variables elegidas
4. Conseguimos, simplificando, que a cada línea del
multiplexor hay que aplicar 0, 1, la variable no elegida
o la variable no elegida negada
5. Construir un módulo que imprima la tabla de verdad
del diseño realizado
6. Compararla con la tabla de verdad de la función h: a b c d h 0 0 0 0 1 0 0 0 1 0 0 0 1 0 1 0 0 1 1 0 0 1 0 0 0 0 1 0 1 1 0 1 1 0 0 0 1 1 1 0 1 0 0 0 1 1 0 0 1 1 1 0 1 0 0 1 0 1 1 0 1 1 0 0 1 1 1 0 1 1 1 1 1 0 1 1 1 1 1 1

## Ejercicio 4
Constrúyase un módulo semisumador y compruébese
su funcionamiento correcto.

La {numref}`fig-verilog-05-semisuma` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_05/semisuma.png
---
name: fig-verilog-05-semisuma
alt: Semisumador
width: 85%
align: center
---
Semisumador
```

## Ejercicio 5
Basándose en el módulo construido en el ejercicio
anterior, ahora hay que programar un sumador completo y verificar
su funcionamiento.

La {numref}`fig-verilog-05-sumador1` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_05/sumador1.png
---
name: fig-verilog-05-sumador1
alt: Sumador completo de 1 bit
width: 85%
align: center
---
Sumador completo de 1 bit
```

## Parar la simulacion
Existen dos órdenes en Verilog para parar anticipadamente
la simulación:

$stop

y

$finish

.
La diferencia está en que la primera para la simulación
pero pasa al modo de depuración, donde se puede comprobar
el valor de los registros y las señales y la segunda para
la simulación definitivamente.

## Ejercicio 6
Tomando como base el sumador completo de un bit del ejercicio
anterior, hágase un módulo sumador de cuatro bits
con propagación de acarreo.

La {numref}`fig-verilog-05-propaga4` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_05/propaga4.png
---
name: fig-verilog-05-propaga4
alt: Sumador de 4 bits con propagación de acarreo
width: 85%
align: center
---
Sumador de 4 bits con propagación de acarreo
```

Para verificar su funcionamiento correcto, es necesario comprobar
512 combinaciones posibles. En lugar de generar una tabla, realizad
la comprobación mediante Verilog: generad todas las
combinaciones posibles y, en cada combinación, mediante `if` s comprobad que las salidas son correctas. Si no
son correctas, imprimid el valor de los registros y señales
y parad la simulación.

## Retardo en las puertas
Cuando las entradas de una puerta cambian de estado, hasta ahora
hemos supuesto que la salida se adapta a la nueva situación
instantáneamente. Esto está lejos de ser verdad.
Hay un retardo de propagación.

Verilog permite modelar estos retardos de un modo muy fino:
se pueden establecer valores independientes para el paso de 0
a 1, de 1 a 0 y de cualquiera a alta impedancia. En una primera
aproximación, aquí consideraremos el mismo valor
para todas las transiciones.

Para especificar que una puerta tiene un retardo, a
continuación del nombre del tipo de puerta, se añade
el símbolo ' `#` ' y las unidades de
tiempo del retardo entre paréntesis. Por ejemplo:

```text
and #(7) a1(salida, entrada1, entrada2); // AND con retardo 7
```

## Ejercicio 7
Añádase un retardo de dos unidades de tiempo a las
puertas del sumador de cuatro bits con propagación de acarreo
del ejercicio anterior. Observando el esquema, dedúzcase
cuál es el retardo de seguridad (cuándo se puede
garantizar
que la salida contiene el valor correcto y no una transición)
de este diseño. Compruébense en la práctica
algunos valores de entrada y los retardos que se producen.

## Ejercicio 8
Evalúese de un modo somero las ventajas en cuanto a rapidez
y precio del sumador de cuatro bits con propagación de
acarreo de los ejercicios anteriores frente al sumador con
anticipación de acarreo visto en teoría y que se
reproduce en la figura de abajo. ¿En
qué circunstancias las diferencias serán más
marcadas?

La {numref}`fig-verilog-05-anticipa` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_05/anticipa.png
---
name: fig-verilog-05-anticipa
alt: Sumador de 4 bits con anticipación de acarreo
width: 85%
align: center
---
Sumador de 4 bits con anticipación de acarreo
```

## Fuente original

Contenido adaptado a TeachBook a partir de la pagina de referencia: <http://avellano.usal.es/~compi/sesion5.htm>.
