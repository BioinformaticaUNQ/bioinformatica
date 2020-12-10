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

