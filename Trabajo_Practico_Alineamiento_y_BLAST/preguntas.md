👉 PARA PENSAR: 
¿Qué tipo de información se puede extraer de la comparación de secuencias? ¿Cómo esperás que se vea en una comparación? 🤔
Se pueden observar los cambios evolutivos, diferencias o coincidencias de secuencias homólogas con el tiempo. En una comparacion deberia buscarse que % de coincidencias
hay entre ambas cadenas antes de sacar alguna conclusión. 

👉 PARA PENSAR: 
¿Por qué crees que es mejor evaluar las relaciones evolutivas lejanas comparando proteínas? 🤔
Es mas conveniente evaluar las relaciones evolutivas lejanas comparando proteinas ya que las proteinas retienen mas información para analizar que los ácidos nucleicos 
y resulta más conveniente ya que es mas probable que las relaciones lejanas presenten mayores variaciones, mientras que en las cercanas no es tan necesario analizar.


RETO I: Intentemos, entonces alinear estas dos palabras, para comprender mejor el problema. Alineá en la tabla interactiva las palabras "BANANA" y "MANZANA".  
¡Tomá nota de tus observaciones y de las conclusiones que se desprendan de estas observaciones!
☑️ PREGUNTAS DISPARADORAS: ¿Existe una única forma de alinearlas? ¿Es alguno de los posibles alineamientos mejor que otro? Si así fuera ¿Por qué?

Solucion:
1) alinear por orden:
B - A - N - A - N - A
M - A - N - Z - A - N - A

observacion: La solo parece coincidir solamente con 2 letras. no parecen ser similares. tomemos en cuenta que no tienen el mismo largo las 2 cadenas, asumiento
que la ultima A no coincide con "vacio"

2) alinear por "conveniencia"
B - A - N - _ - A - N - A
M - A - N - Z - A - N - A

observacion: Si intento emparejar la cadena mas corta y le agrego un espacio en un punto especifico, la cadena parece concordar bastante y ahi si pareciera
que tienen algo en común. Podria aplicarse esta tecnica para cadenas de distintos tamaños?


👇 RETO II: En la siguiente tabla probá distintos alineamientos para las palabras "ANA" y "ANANA". Verás que en el margen superior izquierdo aparece un valor 
de identidad calculado para cada alineamitno que intentes.
Tomá nota de los valores de identidad observados y de las conclusiones que se desprendan de estas observaciones.

☑️ PREGUNTAS DISPARADORAS: ¿Son todos los valores iguales? ¿Qué consideraciones deberían tenerse en cuenta a la hora de realizar el cálculo? ¿Se te ocurre,
distintas formas de calcularlo? ¿Serán todas ellas igualmente válidas en Biología?

El numero mostrado representa el porcentaje de coincidencia entre ambas cadenas, tomando como referencia a la cadena mas larga.
El porcentaje maximo de coincidencia es de 60%, es decir, 0.6/1.0 mostrado en la tabla.
Como segunda observacion hay mas de una forma en que de el porcentaje máximo de coincidencia. Poner coincidir ANA con las
primeras 3 de ANANA o con las ultimas 3 dan las mismas coincidencias. 


👇 RETO III: En la siguiente tabla probá distintos alineamientos para las palabras "ANA" y "ANANA". Verás que en el margen superior izquierdo aparece un 
valor de identidad calculado para cada alineamitno que intentes y un botón para cambiar la penalidad que se le otorga a dicho para el cálculo de identidad.

Probá varias combinaciones, tomá nota de los valores de identidad observados y de las conclusiones que se desprendan de estas observaciones.

☑️ PREGUNTAS DISPARADORAS: ¿Cómo se relacionan los valores de identidad obtenidos con las penalizaciones que se imponen al gap?
¿Qué implicancias crees que tiene una mayor penalización de gaps? ¿Se te ocurre alguna otra forma de penalización que no haya sido
tenido en cuenta en este ejemplo?

Observando los distintos valores de coincidencia para ANA y ANANA, y la "penalidad" aplicada podemos intuir que es necesaria, ya que agregar demasiados "gasp"
a una cadena implicaria estar tratando de forzar coincidencias, aun si se llegara a un 100% sin penalidades. La idea es llegar a un mayor porcentaje
con la menor cantidad de gasp aplicados.


👉 PARA PENSAR:
Entonces, pensando en un alineamiento de ácidos nucleicos ¿Cuáles te parece que son las implicancias de abrir un gap en el alineamiento?
¿Qué implicaría la inserción o deleción de una región de más de un residuo?

Abrir un gap en el alineamiento significaria realizar una modificacion en la cadena original(o cortarla/romper lazos), asi como insertar o borrar algun residuo 
de la region implicaria tener que cambiar la composicion de la cadena original a analizar.


👇 RETO IV: Probá en la tabla interactiva distintos alineamientos para las secuencias nucleotídicas. Podrás ver las traducciones para cada secuencia.
Probá varias combinaciones, tomá nota de las observaciones y de las conclusiones que se desprendan de estas.
 
👉 PARA PENSAR: ¿Dá lo mismo si el gap que introducís cae en la primera, segunda o tercer posición del codón? ¿Cómo ponderarías las observaciones de este ejercicio para evaluar el parecido entre dos secuencias?

No, no da lo mismo donde introduzco el gap. Un gap puesto al azar puede hacer coincidir toda la cadena o hacer que toda la cadena pierda coincidencia alguna. Deben
acomodarse de manera "inteligente" a raiz de encontrar la mayor coincidencia posbible.

TIPOS DE ALINEAMIENTOS:

👉 PARA PENSAR: ¿En qué casos serán de utilidad uno u otro tipo de alineamientos? ¿Qué limitaciones tendrá cada uno?

- Global: alineamiento de la secuencia completa.
  -útil para secuencias muy similares en tamaño y composición.
  -No sirve para cadenas de distinto tamaño o regiones no conservadas
  
- Local: Cuando interesa alinear regiones similares entre secuencias. 
  -útil cuando las secuencias a comparar son diferentes en tamaño o poseen regiones no conservadas.
  -Ineficaz para secuencias de igual tamaño y con regiones conservadas.
  
  
 👇 RETO V: Estuvimos viendo que el alineamiento de secuencias no es trivial y requiere contemplar los múltiples caminos posibles, teniendo en cuenta 
 al mismo tiempo la información biológica que restringe ese universo de posibilidades. Es momento de llevar entonces estos conceptos a lo concreto! 
 
Te proponemos pensar los pasos a seguir en un alineamiento de dos secuencias cortas, teniendo en cuenta una matriz genérica de scoring (puntuación) que 
contemple las complejidades que estuvimos viendo, es decir que penalice de distinto modo una inserción o deleción, que una discordancia (mismatch) o una 
coincidencia (match). Escribilos o esquematizalos en un diagrama de flujo.

teniendo 2 secuencias cortas:
1)Analizar si las 2 secuencias coinciden en tamaño. De ser iguales no se requerira el uso de deleciones o gaps y se procederá a n alineamiento global.
2)De ser distintas, probar los casos donde pondrian un gap donde no hay coincidencias, o deleciones en la cadena mas larga. La posible prediccion de 
  la delecion debe otorgar el posible mayor resultado del % de coincidencia.
3) Se elegirá al mas efectivo en base al % de comparar los 2 mejores resultados para esta tarea.


👉 PARA PENSAR: ¿En qué consiste la programación dinámica? ¿Por qué crees que es útil en este caso?
La programación dinámica es útil en este caso para evitar analizar casos innecesarios y así no tengamos un trabajo extra. De hecho, la Prog. Dinámica se utiliza 
para otorgar una solucion eficiente a grandes problemas centrandose en los posibles mejores resultados a un determinado problema. 

👇 RETO VI: Utilizando la herramienta interactiva  desarrolladas por el Grupo de Bioinformática de Freiburg probá distintos Gap penalties para el ejemplo propuesto y observá lo que ocurre.
 
Interpretando la recursión, explicá con tus palabras de dónde salen los valores de la matriz  que se construye. ¡Esquematiza tus conclusiones!
 
1) el cuadro inicial arriba a la izquierda siempre empieza en 0
2) Se completa la primer fila y culumna con la regla y valores de gap en cada cuadro
3) Se completa la diagonal que corresponde con las comparaciones entre ambas cadenas con las reglas y valores de gap, match y mismatch.
4) se completan el resto de los cuadros, segun la siguiente regla:
   -se observan los cuadros de la izquierda, arriba y arriba a la izquierda, de los 3 se elige al mayor y se suma con el valor correspondiente al cuadro actual

👉 PARA PENSAR: Ingresá al servidor del NCBI y mirá los distintos programas derivados del BLAST que se ofrecen ¿Para qué sirve cada uno? ¿En qué casos usarías cada uno?

Solucion:
Global Align:
Compara dos secuencias en todo su lapso (Needleman-Wunsch)
 
CD Search:
Encuentre dominios conservados en su secuencia
 
IgBLAST
Búsqueda de inmunoglobulinas y secuencias de receptores de células T
 
VecScreen
Secuencias de búsqueda de contaminación por vectores
 
CDART
Encuentre secuencias con una arquitectura de dominio conservado similar
 
Multiple Alignment:
Alinear secuencias usando restricciones de dominio y proteína
 
MOLE-BLAST
Establecer taxonomía para secuencias no cultivadas o ambientales

Cada uno sirve para las distintas necesidades del analisis de proteinas segun las descripciones.

Vamos a explorar esta herramienta!
👇 RETO VII: calculá el E-value y % identidad utilizando el programa Blast de la siguiente secuencia input usando 5000 hits, un e-value de 100 y tomando aquellos hits con un mínimo de 70% cobertura. Observe y discuta el comportamiento de : E-value vs. % id, Score vs % id,  Score vs E-value

VVGGLGGYMLGSAMSRPIIHFGSDYEDRYYRENMHRYPNQVYYRPMDEYSNQNNFVHDCVNITIKQHTVTTTTKGENFTETDVKMMERVVEQMCITQYERESQAYYQRGSSMVLFSSPPVILLISFLIFLIVG


  
 


