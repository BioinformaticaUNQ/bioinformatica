# bio-informatica-2020-2c
Repo para la materia de Introducción a la Bioinformática de la UNQ

## Trabajo práctico 2. 

### - ¿Por qué una célula querría destruir sus propias proteínas?

Primero, que es la ubiquitina y que hace? La ubiquitina es una pequeña proteína que se encuentra en todo el organismo y está formada por 76 aminoácidos. Cuando varias moléculas de ubiquitina en una conformación determinada se unen a la proteína que tiene que ser eliminada, el proteasoma -gran complejo multiproteico responsable de la degradación-, la identifica como “desechable” e inicia una cadena de reacciones que terminan con la destrucción de la misma.

Ahora, ¡por qué querría un célula destruir proteínas? En primer lugar el exceso de proteínas y organelas puede tener un fuerte impacto en la capacidad proliferativa de las células y esto está asociado comunmente al desarrollo de una amplia variedad de patologías, entre ellos cancer o distintas enfermedades neurodegenerativas.

https://www.conicet.gov.ar/ubiquitina-la-importancia-de-las-pequenas-cosas/ Leyendo esto.

............................

### - ¿Qué información nos provee esta página?

Nos provee información sobre las formas 3D de proteínas, los ácidos nucleicos que la conforman y conjuntos complejos que ayuda a estudiantes e investigadores a comprender todos los aspectos de la biomedicina y la agricultura, desde la sintesis de proteínas hasta la salud y enfermedad. 

............................
### - ¿Cómo se determinó la estructura de esta proteína?
Se obtuvo a partir de la Cristalografía de rayos X (X-ray crystallography)
............................
### - A la izquierda vemos una representación de la estructura de ubiquitina. ¿Qué significan las cintas, las flechas y las regiones angostas?
Las cintas, flechas y las regiones angostas representan cómo se va plegando la proteina. Es decir, representan las posibles alfa hélices, las hojas beta plegadas y los loops.
............................
### - ¿Representa esa imagen a la realidad del sistema biológico?
No. Es una representación que se acerca mucho a la real pero tenemos que tener en cuenta que los átomos están en constante movimiento. Con este esquema se busca solo representan cómo está formada la estructura de la protenia pero no los movimientos e interacciones de la misma. 
............................
### - La estructura 1UBQ fue “refinada a una resolución de 1.8 Angstroms”. Éste es el error asociado al experimento: mientras mayor es la resolución, menor es la certeza al determinar la posición de cada átomo. ¿Cuál es la utilidad y los condicionamientos de usar un modelo científico que sabemos inexacto?
Nos permite tener una idea aproximada de cómo es la estructura de la proteina. Decimos que es aproximada porque una proteina en la vida real no estará completamente quieta como la del esquema. Aún así, el modelo nos sirve para poder predecir comportamientos y caractersticas basandonos en él. Pero siempre hay que tener en cuenta un posible margen de error. 
............................
### - ¿Qué diferencias y similitudes notamos respecto de la representación inicial?
Podemos notar que se mantienen las alfa hélices, las hojas beta plegadas y los loops. Sin embargo ahora, cada aminoacido está representado con un color distinto. En la primera (la verde) podiamos ver en detalle la posición de cada átomo pero ahora no.
............................

### - ¿Qué información esperaría encontrar como resultado un experimento destinado a determinar la estructura terciaria de una molécula biológica?
Esperaríamos encontrar cómo son los enlaces formados por las cadenas laterales de los esqueletos proteícos de la estructura secundaria. Es decir, dónde se posiciona cada atómo de la estructura en el espacio según cómo esté plegada la proteína. 
............................

### - En el menú de la derecha hay opciones de distintos tipos de representación y formas de colorear la estructura tridimensional. ¿Para qué podría ser útil visualizar lo mismo de distintas maneras?

Para poder estudiar y observar caractersticas diferentes. Cada vista ofrece más detalle sobre una caracteristica en particular y, seguramente, menos sobre otra.
............................

### - Podemos explorar el contenido del archivo que acabamos de descargar si lo observamos con un editor de texto. Haciendo clic con el botón derecho del mouse sobre el archivo descargado, usemos la opción Abrir con y seleccionemos el Bloc de Notas u otro editor de texto. ¿En qué consiste un archivo PDB?

Los archivos PDB son archivos de texto que describen la estructura de las proteinas guardadas en el Banco de Datos de Proteinas en sus distintios niveles. Provee información sobre cantidades de átomos, los aminoacidos que conforman, cómo estos se relacionan entre si y los enlaces que forman.
............................
### - Desplacémonos por el archivo hasta encontrar las líneas que comienzan con la palabra ATOM. ¿Qué tipo de información brinda esta sección?
Cada una de las filas que comienza con la palabra ATOM corresponde a cada uno de los átomos que conforman la proteína. De cada uno de ellos sabemos el nombre, la ocurrencia y en qué aminoacido se encuentra entre otra información.
............................
### - ¿Podríamos extraer de este archivo información sobre la estructura primaria de la proteína en cuestión? ¿Cómo se presenta dicha información y qué significa la representación? Desde el punto de vista computacional:¿de qué tipo de dato se trata esta información?
Si. La columna resName indica a qué aminoacido pertenece cada átomo. Por ende podemos saber el orden de los aminoacidos y así, la estructura primaria de la proteina. Desde el punto de vista computacional, esta información podria tratarse de un String si usamos la notación de un solo caracter para cada aminoacido o de una lista de Strings si usamos la notación de 3 caracteres para cada uno.
............................
### - ¿Considera que el formato PDB es útil para presentar los resultados del experimento?
Es muy útil porque este tipo de archivos se puede usar como input para algun programa que tome un PDB y con él arme un dibujo tridimensional de la proteína, como los que se ven en la página analizada anteriormente. Ademas con esos datos podemos sacar estadísticas y asi predecir parte del comportamiento de la proteína. 
............................
### - Observamos que la información respeta cierta estructura interna. ¿Cuáles son los beneficios y las limitaciones de imponer una estructura para comunicar los resultados de un experimento?
Respetar siempre la misma interfaz nos da como beneficio que a la hora de armar un programa que tome como input un archivo PDB, ya sabremos que forma tendrá y en qué orden están las cosas. Si esto no fuese de esta manera, tendríamos que adaptar nuestros programas a las distintas posibles estructuras de archivo.
............................
### - Hemos visto que las proteínas tienen estructura tridimensional y hemos podido observar algunas características de las mismas. ¿Será igual con los ácidos nucléicos?
g
### Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. Contanos sobre los procedimientos que puso a punto Rosalind. Por supuesto, es difícil entender en qué consiste la estructura de una molécula simplemente mirando el contenido de un archivo PDB. Ya sabemos que existen formas de representar la información tridimensional en la computadora. Existen una multiplicidad de aplicaciones gratuitas que nos permita visualizar la estructura de una proteína. Te proponemos algunas aplicaciones para teléfonos celulares disponibles en las tiendas de nuestro teléfono (NDKmol - molecular viewer o RSCB PDB mobile) de sencilla instalación.

