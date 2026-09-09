# Sesion 4. Modulos

Esta pagina respeta la secuencia de la sesion original: cada apartado aparece en el mismo orden y los ejercicios se mantienen como secciones propias dentro del recorrido.

```{admonition} Objetivos de aprendizaje
:class: tip

- Definir modulos con `input`, `output` e `inout`.
- Construir circuitos jerarquicos.
- Verificar modulos con bancos de prueba.
```

## Modulos
El diseño modular es ampliamente usado en informática.
El diseño de hardware no es una excepción. Consiste
en dividir el problema en unidades más sencillas denominadas

módulos

. Los módulos deben presentar las
siguientes características:

1. Deben ser autocontenidos: desde dentro de un módulo
no se puede acceder al interior de otro
2. La comunicación con el exterior de un módulo
o con otros módulos se debe realizar mediante
interfaces bien definidas
3. Es conveniente que exista la posibilidad de anidar
módulos (construir módulos dentro de otros)

El diseño modular tiene numerosas ventajas:

1. Facilita el proceso de construcción de sistemas
complejos a partir de otros más simples
2. En caso de fallo, es mucho menos complicado localizar el fallo
y depurar la aplicación

En Verilog los módulos serán módulos
electrónicos y las interfaces con el exterior u otros
módulos serán

puertos

. Los puertos se 
dividen en tres tipos:

1. de entrada ( `input` ): la información
fluye hacia el
interior del módulo. Se indican con una flecha
apuntando hacia dentro del módulo
2. de salida ( `output` ): la información 
sale del 
módulo. La flecha que los representa apunta hacia
el exterior
3. de entrada/salida ( `inout` ): una
combinación de los
dos anteriores. La flecha tiene punta en ambos extremos

Las reglas de conexión en Verilog dependen del tipo
de puerto. Las posibilidades de conexión 
se muestran en la figura siguiente para los tres tipos de puertos
y los dos tipos de variables pertinentes ( `reg` y `wire` ):

La {numref}`fig-verilog-04-modulo` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_04/mOdulo.png
---
name: fig-verilog-04-modulo
alt: Reglas de puertos para módulos
width: 85%
align: center
---
Reglas de puertos para módulos
```

Podemos considerar a las puertas ya vistas como pequeños
módulos predefinidos del lenguaje.

## Modulo comparador
El primer módulo que vamos a definir y construir será
el módulo comparador de un bit visto en teoría:

La {numref}`fig-verilog-04-compar1` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_04/compar1.png
---
name: fig-verilog-04-compar1
alt: Comparador de un bit
width: 85%
align: center
---
Comparador de un bit
```

Como se puede observar, este módulo presenta dos entradas,
que denominaremos `a` y `b` , ambas de
un bit, y tres salidas, que llamaremos `mayor` , `igual` y `menor` , también todas
de un bit.

Cuando se define un módulo en Verilog, lo primero que
hay que hacer es declarar su interfaz:

```verilog
// MOdulo comparador de un bit
module Comp1(output wire mayor, output wire igual, output wire menor,
             input wire a, input wire b);

  // AquI vendrA el cOdigo del mOdulo

endmodule
```

En el cuerpo del módulo hay que efectuar la conexiones
entre las puertas. Para ello hay que nombrar cada una de ellas
y, si es necesario, algunos cables auxiliares. Por ejemplo:

La {numref}`fig-verilog-04-compar11` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_04/compar11.png
---
name: fig-verilog-04-compar11
alt: Comparador de un bit
width: 85%
align: center
---
Comparador de un bit
```

```verilog
// MOdulo comparador de un bit
module Comp1(output wire mayor, output wire igual, output wire menor,
             input wire a, input wire b);

  wire wArriba, wAbajo;

  not nArriba(wArriba,a);
  not nAbajo(wAbajo,b);
  and aArriba(mayor,a,wAbajo);
  and aAbajo(menor,b,wArriba);
  nor n(igual,mayor,menor);

endmodule
```

Para poder comprobar si el resultado es correcto, definimos un
módulo auxiliar en el mismo fichero:

```verilog
module TestComp1;

  reg a,b;
  wire M,m,igual;
  
  Comp1 c(M,igual,m,a,b);

  // Bloque de comportamiento
  initial
    begin
      $monitor($time," a=%b, b=%b, mayor=%b, igual=%b, menor=%b",
                     a,b,M,igual,m);
      a=0; b=0;
      #5 a=0; b=1;
      #5 a=1; b=0;
      #5 a=1; b=1;
    end

endmodule
```

La línea fundamental es la que dice: `Comp1 c(M,igual,m,a,b)` . En la parte anterior *definíamos* la interfaz y el comportamiento
del módulo. En esta línea construimos *una instancia* del módulo cuyo nombre
es `c` . Una definición se puede
instanciar tantas veces como sea necesario. La salida
del programa es la siguiente:

```text
0 a=0, b=0, mayor=0, igual=1, menor=0
                   5 a=0, b=1, mayor=0, igual=0, menor=1
                  10 a=1, b=0, mayor=1, igual=0, menor=0
                  15 a=1, b=1, mayor=0, igual=1, menor=0
```

## Jerarquia de modulos. Nombrado
Al instanciar unos módulos dentro de otros, se forma
una

jerarquía de módulos

. En el ejemplo
del comparador de un bit de arriba, esta
jerarquía de módulos se refleja en este gráfico:

module TestComp1;
reg a,b;
wire M,m,igual;
Comp1 c(M,igual,m,a,b);
// Bloque de comportamiento
initial
begin
$monitor($time," a=%b, b=%b, mayor=%b, igual=%b, menor=%b",
a,b,M,igual,m);
a=0; b=0;
#5 a=0; b=1;
#5 a=1; b=0;
#5 a=1; b=1;
end
endmodule // MOdulo comparador de un bit
module Comp1(output wire mayor, output wire igual, output wire menor,
input wire a, input wire b);
wire wArriba, wAbajo;
not nArriba(wArriba,a);
not nAbajo(wAbajo,b);
and aArriba(mayor,a,wAbajo);
and aAbajo(menor,b,wArriba);
nor n(igual,mayor,menor);
endmodule

El módulo raíz no tiene nombre y es instanciado por
Verilog automáticamente. Para hacer referencia a un objeto
directamente perteneciente al módulo raíz desde sí
mismo, simplemente se pone el nombre del objeto como ya hemos visto.
¿Pero qué hacer si queremos acceder desde el
módulo raíz a la puerta `aAbajo` del
módulo `c` ? La respuesta es que se usa un
punto (.) para descender por la jerarquía de objetos.
Por consiguiente, para acceder a dicha puerta, se pondría `c.aAbajo` . El esquema se generaliza cuando hay más
niveles.

## Ejercicio 1
Instánciense dos veces el módulo anterior para
construir un comparador de dos bits, según el esquema
de la figura:

La {numref}`fig-verilog-04-comp2` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_04/comp2.png
---
name: fig-verilog-04-comp2
alt: Comparador de dos bits
width: 85%
align: center
---
Comparador de dos bits
```

Construir un módulo para comprobar todas las posibles
entradas (16). Úsense como entradas dos
variables de dos bits en lugar de cuatro variables de un bit,
esto es, todas las posibles combinaciones en las que `a` está en {0,1,2,3} y `b` también en {0,1,2,3}

## Puertos desconectados
Al instanciar un módulo, hemos visto que las conexiones
de sus puertos se realizan nombrando, en orden, las variables
entre paréntesis. Si queremos, por el motivo que sea,
dejar algún puerto desconectado, no hay más que no
poner nada en el lugar que ocupa. Por ejemplo, si queremos usar
un comparador de tipo

Comp1

definido más arriba
solamente para comparación de igualdad, la línea
de instanciación podría ser:

```text
Comp1 c7(,igual,,a,b);
```

En el ejemplo suponemos definidas tres variables

igual

,

a

y

b

que es donde queremos realizar
las conexiones.

## Ejercicio 2
Prográmese en un mismo fichero Verilog tres módulos:
uno para realizar un codificador 4x2 normal como el que se muestra
a la izquierda de la figura, otro codificador
4x2 con prioridad como el que aparece a la derecha y un 
módulo de comprobación para
probar cuáles son sus salidas para cada una de las 16 posibles
entradas. Comparad los resultados obtenidos.

La {numref}`fig-verilog-04-priocod` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_04/priocod.png
---
name: fig-verilog-04-priocod
alt: Codificadores
width: 85%
align: center
---
Codificadores
```

## Puertas con mas de dos entradas
Es posible usar puertas lógicas de más de dos
entradas en Verilog. Por ejemplo, una puerta AND de cuatro
entradas:

La {numref}`fig-verilog-04-and4` reproduce la figura original usada en este punto de la sesion.

```{figure} ../../_static/verilog/sesion_04/and4.png
---
name: fig-verilog-04-and4
alt: Puerta AND de cuatro entradas
width: 85%
align: center
---
Puerta AND de cuatro entradas
```

La puerta de la izquierda es idealmente equivalente al
conjunto de puertas de la derecha. En Verilog para instanciar
puertas de más de dos entradas simplemente se añaden
argumentos en la línea de instanciación:

```text
and a4(salida, entrada1, entrada2, entrada3, entrada4);
```

## Ejercicio 3
Uno de los problemas que presentan los diseños del
último ejercicio es que no hay manera de diferenciar
observando las líneas de salida el estado en que
ninguna de las líneas de entrada del decodificador
está activa.

Añádase un línea de salida adicional,
V, que se active cuando la salida sea válida, es decir,
permanezca desactivada cuando no haya ninguna línea
del codificador activa.

## Ejercicio 4
Tomando solamente el caso del decodificador sin prioridad,
modífiquese el caso anterior para que la línea V
se mantenga activa si y solo si hay exactamente una línea
activa en la entrada.

## Fuente original

Contenido adaptado a TeachBook a partir de la pagina de referencia: <http://avellano.usal.es/~compi/sesion4.htm>.
