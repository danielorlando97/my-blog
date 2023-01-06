# Las metaclases de Python, un mensaje subliminal

Si conoces el lenguaje Python es muy probable que en alguna ocasión hallas escuchado
las frases "En Python todo son clases" o "En Python todo es un objeto de primera clase".
Luego de dichas frases se suele enumerar las entidades del lenguaje donde estos hechos se hacen
más evidentes, los número, los textos o las clases, e inclusos algunos artículos
rompen los estándares incluyendo en la lista a las funciones. Pero una de las ideas más interesantes
dentro del lenguaje se encuentra definida dentro de estas expresiones.

En Python todas las entidades son objetos de primera clase, los números, los textos, las clases,
las funciones e incluso las definiciones de las clases. Cada una de clases de Python definidas por
los programadores son instancias de su respectiva metaclase. Al igual que toda clase hereda de la clase
base `object` toda metaclase hereda de la metaclase base `type`.

## 🤔 ¿Qué es una metaclase?

    definición

El lenguaje ofrece los mecanismos necesarios para implementar metaclases personalizadas y para indicar
que la definición de una clase determinada debe ser una instancia de la metaclase previamente definida.

## 😱 Hay vida antes de la función \_\_init\_\_

Aunque la implementación de metaclases no es lo más cotidiano a la hora de escribir código en Python.
El conocimiento de esta característica del lenguaje trae consigo el descubrimiento de otro de los más
importantes secretos del lenguaje. Si has crecido como programador bajo la tutela de el patrón orientado
a objeto, con lenguajes como C# o Java, es probable que creas que la función `\_\_init\_\_` es el constructor
de las clases de Python y que los procesos anteriores a esta función es responsabilidad del interprete del
lenguaje. Pero la verdad es que Python es mucho más claro y flexible en lo que respecta a inicialización de
instancias.

El procesos de inicialización de las instancias de las clases de definimos cuando escribimos código en Python
comienza con la función \_\_call\_\_ de su metaclase respectiva. Esta función se encarga de detectar y trasmitir
cual es la clase específica a la que se le creará una nueva instancia. Esto inicialmente puede resultar contradictorio
por el hecho de que cuando intentamos crear una nueva instancia de una clase usamos explícitamente el nombre de la
misma. Pero este espacio de duda es lo que hace a este diseño tan maravilloso y flexible.

La función \_\_call\_\_ termina su implementación realizando un llamado a la función \_\_new\_\_ de la clase
seleccionada para la creación de la nueva instancia. Dicha función es la encargada de crear la base inicial
de la instancia o lo que comúnmente conocemos com **self**. Finalmente, la función \_\_new\_\_ realiza una
llamada a la función \_\_init\_\_ pasando como parámetro la nueva instancia creada, **self**, para inicializar
las distintas propiedades que el desarrollador allá definido.

De todas formas, no me creas a mi. Revisa este ejemplo sencillo y velo por ti mismo 😉

## 🧐 Todo muy interesante pero, ¿para que sirve esto?

El mayor potencial de las metaclases se encuentra en el espacio que deja la función \_\_call\_\_ de las mismas
para decidir cual es la clase a la que se le creará una nueva instancia. Patrones de diseño de software clásicos
como las Factorias de Clases o las Clases Singleton pueden provechar este espacio para realizar un análisis, ya sea
los parámetros iniciales o de el estado del programa, y seleccionar la clase correcta.

Las metaclases son una de las más potentes herramientas del lenguaje en cuanto a lo que metaprogramación se refiere.
El conocimiento y explotación de esta cualidad del lenguaje permite modificar la semántica de la inicialización de
instancias sin modificar su sintaxis, logrando el código resultante sea mucho más expresivo, abstraiéndonos los patrones
y la lógica subyacente.

Pero bueno, una de las mejores características de una persona inteligente es la incredulidad,
y a falta de pruebas buenos son ejemplos 😁

### Patrón Singleton

        definicion y ejemplo

### Factoría de clases

        definicion y ejemplo

## Conclusión
