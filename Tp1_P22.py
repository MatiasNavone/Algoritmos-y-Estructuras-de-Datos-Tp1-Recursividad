# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo;

# c. Utilizar un vector para representar la mochila.

def usar_la_fuerza(mochila, i=0, cosas_sacadas=0):
  
    if i >= len(mochila):
        return False, cosas_sacadas
    
  
    if mochila[i] == 'sable de luz':
        return True, cosas_sacadas + 1
    

    encontrado, cosas_necesarias = usar_la_fuerza(mochila, i + 1, cosas_sacadas + 1)
    
    
    return encontrado, cosas_necesarias


mochila = ['comida', 'botiquin', 'sable de luz', 'mapa', 'agua']
encontrado, cosas_necesarias = usar_la_fuerza(mochila)
if encontrado:
    print("Se encontro un sable de luz en la mochila despues de sacar {} objetos.".format(cosas_necesarias))
else:
    print("No se encontro un sable de luz en la mochila.")
