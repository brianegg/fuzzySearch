import sys
import json
import re

# Funcion para darle formato al argumento de entrada
# de una busqueda para que se pueda convertir en json
def format_string_search(arg):
	a  = arg[:1] + '"' + arg[1:]
	a1 = a[:8] + '"' + a[8:]
	a2 = a1[:10] + '"' + a1[10:]
	a3 = a2[:-1] + '"' + a2[-1:]
	return a3

# Funcion para darle formato al argumento de entrada
# de agregar para que se pueda convertir en json
def format_string(arg):
	a  = arg[:1] + '"' + arg[1:]
	a1 = a[:6] + '"' + a[6:]
	a2 = a1[:8] + '"' + a1[8:]
	a3 = a2[:-1] + '"' + a2[-1:]
	return a3

# Funcion que lee el archivo e imprime los nombres que
# que tenga escritos
def list():
	arr = []
	f = open(file,"r")
	if f.mode == 'r':
		f.seek(0)
		first_char = f.read(1)
		if not first_char:
			print(arr)
		else:
			f.seek(0)
			contents = f.read().split('\n')
			f.close()
			for x in range(len(contents)-1):
				nombre = {"name": contents[x]}
				arr.append(nombre)
			print(json.dumps(arr, indent=2))

# Funcion que escribe un nombre en el archivo
def add():
	if(len(sys.argv) > 2):
		arg = sys.argv[2]
		jsonString = format_string(arg)
		nombre = json.loads(jsonString)
		if nombre['name'] != '':
			f = open(file, 'a')
			f.write(nombre['name'] + "\n")
			f.close()
			print('Usuario agregado')
		else:
			print('Se necesita un nombre válido.')
	else:
		print('Se requiere de un objeto json para insertar el nombre.')
		print('Ejemplo: add {"name":"nombre"}')

# Lee el archivo, guarda los nombres en un arreglo, realiza la busqueda
# y regresa el nombre con mayor coincidencia o imprime 'Sin coincidencias'
# si no se encuentra coincidencia.
def search():
	if(len(sys.argv) > 2):
		arg = sys.argv[2]
		jsonString = format_string_search(arg)
		nombre = json.loads(jsonString)
		if nombre['search'] != '':
			f = open(file, 'r')
			names = f.read().split('\n')
			f.close()
			busqueda = fuzzy_search(nombre['search'],names)
			if(len(busqueda) == 0):
				print('Sin coincidencias')
			else:
				name = {"name" : busqueda[0]}
				print (name)
		else:
			print('Se necesita un nombre válido para realizar la búsqueda.')
	else:
		print('Se requiere de un objeto json para realizar la búsqueda.')
		print('Ejemplo: add {"search":"nombre"}')

# Naive Regex Matching
# https://blog.amjith.com/fuzzyfinder-in-10-lines-of-python
# El algoritmo utiliza expresiones regulares para realizar 
# la busqueda de aproximación
def fuzzy_search(nombre, nombres):
    coincidencias = []
    patron = '.*?'.join(nombre)   # Converts 'name' to 'n.*a.*m.*e'
    regex = re.compile(patron)  # Compiles a regex.
    for nombre in nombres:
        coincide = regex.search(nombre)   # Checks if the current item matches the regex.
        if coincide:
            coincidencias.append((len(coincide.group()),coincide.start(), nombre))
    return [x for _, _, x in sorted(coincidencias)]

file = 'fuzzy-search.txt'

if sys.argv[1] == 'add':
	add()
elif sys.argv[1] == 'list':
	list()
elif sys.argv[1] == 'fuzzy-search':
	search()
else:
	print('Acción no permitida.')
	print('Debe usar alguno de los siguientes comandos: ')
	print(' add {"name":"nombre"}')
	print(' list')
	print(' fuzzy-search {"search":"nombre"}')