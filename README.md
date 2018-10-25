# fuzzySearch
Programa en python que permite escribir nombres a un archivo txt, listar los nombres y realizar una busqueda aproximada.
# Comandos
## Para agregar un nombre al archivo
#### ./fuzzy-search.py add {"name":"Nombre"}
## Para realizar la búsqueda aproximada sobre los nombres en el archivo
#### ./fuzzy-search.py fuzzy-search {"name":"Nombre"}
## Para listar los nombres del archivo
#### ./fuzzy-search.py list
# Naive Regex Matching
## Consultando la siguiente página:
[Naive Regex Matching](https://blog.amjith.com/fuzzyfinder-in-10-lines-of-python "Naive Regex Matching")
#### El algoritmo crea una expresión regular usando el parámetro que se inserta para la búsqueda
#### e itera por cada nombre en el archivo y revisa si coincide con la expresión regular.
#### El algoritmo ordena las coincidencias primero por la coincidencia mas compacta y luego por la posición de la conincidencia.

#### Se utilizó este algoritmo porque nos permite obtener nombres largos utilizando cadenas de caracteres cortas.
#### Otros algoritmos como distancia levenshtein no permite esta funcionalidad y son mas costosos en cuanto a procesamiento.

