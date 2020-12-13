# Documentación de uso del TP final 

La aplicación web permitirá visualizar información analizada a partir de un código PDB. Este análisis incluye:
- Datos sobre las secuencias homólogas a la secuencia query:
  - Estructuras primarias
  - Estructuras secundarias
  - Visualización de la estructura terciaria de la secuencia query

# ¿Cómo usar la aplicación? 

## Consultar por un código PDB
Como primer paso, es necesario ingresar el código PDB que se desea analizar. Es posible que el usuario tenga que elegir entre varias secuencias que corresponden a ese código 

## Análisis de una secuencia 
Una vez seleccionada una sequencia query, el sistema buscará todas las secuencias que sean homólogas a la misma y realizará un análisis de datos. Como resultado obtendremos, para cada secuencia, la estructura primaria y la estructura secundaria. Tambin podemos visualizar la estructura terciaria (3D) de la secuencia query.
Podremos especificar el E-value y el coverage. Hoy en día las búsquedas se realizan utilizando la matriz BLOSUM62 con gap open 11 y gap extend 1 como valor default.

## Botonera
Podremos acceder a las distintas visualizaciones desde la botonera principal. 
 - Ver alineamiento de secuencias 
 - Ver estructuras secundarias 
 - Ver estructura terciaria

# Para el desarrollador o la desarrolladora

## Backend

Por el lado del backend es necesario contar con python 3.6 o superior instalado.
Además contar los siguientes programas instalados: 
  - [Pymol](https://pymol.org/2/support.html?#installation)
  - [Blast](https://biopython.readthedocs.io/en/latest/chapter_blast.html)
  - [Clustal](http://www.clustal.org/omega/#Download)
  - [Dssp](https://ssbio.readthedocs.io/en/latest/instructions/dssp.html#installation-instructions-ubuntu)

Se debe descargar de la página de [ncbi](https://ftp.ncbi.nlm.nih.gov/blast/db) alguna DB de PDB para consultar localmente. Recomendamos: https://ftp.ncbi.nlm.nih.gov/blast/db/pdbaa.tar.gz

Finalmente para instalar las dependencias de python correr:

> pip install -r requeriments.txt

Levantar la aplicación. Al utilizar Flask por defecto la levanta en el puerto 5000

> python app.py

## Frontend

Para levantar el frontend es necesario tener instalado [Node.](https://nodejs.org/en/) 

Instalar las dependencias

> npm install

Levantar la aplicación por default en el puerto 3000

> npm start


# Autores
 - Alvarenga, Marcos
 - Amat, Belen 
 - Avalos, Lucas
 - Britez, Fabrizio
