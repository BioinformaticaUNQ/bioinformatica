## Trabajo práctico 4
## ¿En qué se parecen una gallina y una mosca?

### - Trabajaremos con las secuencias del citocromo c de nueve organismos, listados en la tabla de abajo. Además de su denominación taxonómica, deberíamos conocer su nombre común: intentemos completar la tabla.

| Secuencia      | Nombre Taxonimico       | Nombre Comun            |
|----------------|-------------------------|-------------------------|
| NP_061820.1    | Homo sapiens            | Humano                  |  
| NP_001072946.1 | Gallus gallus           | Gallo                   |   
| NP_001065289.1 | Pan troglodytes         | Chimpance               |  
| NP_001157486.1 | Equus caballus          | Caballo                 |
| NP_001183974.1 | Canis lupus familiaris  | Perro                   |
| AEP27192.1     | Gorilla gorilla         | Gorila occidental       |
| XP_024245566.1 | Oncorhynchus tshawytscha| Salmón chinook          |
| NP_001086101.1 | Xenopus laevis          | Rana de garras africana |
| NP_477164.1    | Drosophila melanogaster | Mosca de fruta          |

### - ¿Cuán sencillo será alinear dos o más secuencias a mano? ¿Cuánto influirán el número de secuencias a alinear, su longitud, y la similitud entre ellas?
A mano es facil alineas dos secuencias, pero cuando se agregan mas se vuelve mas complejo. Además la alineación a mano puede traer errores involuntarios. Es preferible el uso de una herramienta programada y probada para estos análisis.

### - ¿Son parecidos los citocromos c de humano y gallo?
Es su mayoria son parecidos. Usando Clustal Omega podemos ver las diferencias.

Humano  NP_061820.1  
Gallo   NP_001072946.1   

NP_061820.1         MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIW	60  
NP_001072946.1      MGDIEKGKKIFVQKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAEGFSYTDANKNKGITW	60  
                    ***:*******: ******************************* *:*** ******* *  

NP_061820.1         GEDTLMEYLENPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE	105  
NP_001072946.1      GEDTLMEYLENPKKYIPGTKMIFAGIKKKSERVDLIAYLKDATSK	105  
                    ***********************.*****.**.*******.**.:  

Los asteriscos ( * ), indican las coincidencias entre las dos secuencias. Teien un 89% de concidencias. 12 sobre 105.

### - ¿Qué teorías subyacen a este análisis?
La teoria que subyace al análisis es la Teoria de Evolución.

### - ¿Cómo nos ayuda la evolución a explicar sus similitudes y diferencias?
La teoria plantea que todos los organismos tenemos un ancestro en común. Las similitudes entre las secuencias  provienen de dicho ancestro.

### - Podemos elegir verlo en colores (Show Color). ¿Qué indican los colores?
Los colores indican las propiedades físico-químicas de un sub-segmento. Cuando coinciden los colores es porque ese sub-segmento de aminoácidos tienen similitudes, aunque no coincidan exactamente los mismos aminoácidos en ese segmento.

### - ¿Qué indican el guión (-), los dos puntos (:) y el asterisco ( * ) ?
El “-” significa un GAP, que es un corrimiento de la cadena que puede ser por una deleción o una adición. 
El “ * ” implica que el residuo analizado se conserva en la posición analizada. 
El “:” implica que el residuo analizado en esa posición tiene una conservación fuerte. El “.” es una conservación débil

### - A simple vista, ¿se conserva la secuencia del citocromo c en los organismos?
A simple vista y ayudado por la herramienta se puede ver una gran similitud entre las secuencias de los organismos.

### - ¿Creeríamos que todos los organismos se asemejan por igual al resto, o se pueden identificar grupos de mayor similitud? Si es así, ¿tienen sentido?


### - ¿Qué evidencias nos aportaría este análisis, a la luz de la evolución?

### - A juzgar por los organismos participantes, ¿cuáles creería que deberían estar más agrupados en el árbol filogenético?
A juzgar por los organismos, esperariamos que el humano e l gorila y el chimpance esten agrupados dentro del arbol.
Luego de la puesta en comun en clase, vimos que los oviparos fueron agrupados en una de las ramas del arbol mientras que el chimpance gorila y el humano fueron agrupados en otra de las ramas.

### - Observemos el árbol filogenético. ¿Concuerda con lo esperado? ¿De qué organismos son los citocromos c más parecidos? ¿Cómo se explica?
Si concuerda con lo esperado. Se explica por dos motivos. 
El primero es que hay mas similitudes en la secuencias de un salmon y una rana, mucho mas que entre un salmon y un perro. 
El segundo puede ser la falta de mas información para tomar decisiones mas certeras en cuanto al agrupamiento. Con la información que le brindamos a Clustal Omega,la aplicación realizó la asocianción entre organismo lo mas aproximada posible, aunque entre un gallo y un salmon no haya tanta similitud.
