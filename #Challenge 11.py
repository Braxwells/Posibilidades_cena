#Challenge 11
import random as rdm

print(f'11. Máximo número de empleados a invitar a una reunión \n'+
'Una empresa está organizando una reunión y tiene una lista de n empleados que \n'+
'esperan ser invitados. Han dispuesto una gran mesa circular, con capacidad para \n'+
'cualquier número de empleados. Los empleados están numerados del 0 al n - 1. Cada \n'+
'empleado tiene una persona favorita y sólo asistirá a la reunión si puede sentarse junto \n'+
'a su persona favorita en la mesa. La persona favorita de un empleado no es él mismo. \n'+
'Dada una matriz de enteros con índice 0, donde favorite[i] denota la persona favorita \n'+
'del i-ésimo empleado, devuelva el número máximo de empleados que pueden ser \n'+
'invitados a la reunión. \n'+
'Restricciones: \n'+
'- n == favorito.length \n'+
'- 2 <= n <= 105 \n'+
'- 0 <= favorito[i] <= n - 1 \n'+
'- favorito[i] != i')

#Generamos un número aleatorio de comensales
comensales = rdm.randint(2, 105)
print(f'El número de comensales es de {comensales}')

#Una vez tenemos el número de comensales creamos los favoritos de cada uno
favoritos = rdm.sample(range(comensales), comensales)

print(f'Sabiendo que empezamos a contar en 0 el número de comensales, obtendremos que las combinaciones para sentarlos será: ')


#Una vez ya tenemos la lista de favoritos, empezamos a generar las posibilidades de mesa y creamos una variable que nos indica el número de comensales máximo a invitar 'mejor_mesa'
def coloca(mesa,pendientes, mejor_mesa = 0):
    print(mesa)
    ultimo = mesa[-1]
    amigo = favoritos[ultimo]
    if len(mesa) > 1 and mesa[-2] == amigo:
        for n in list(pendientes):
            pendientes.remove(n)
            mesa.append(n)

            coloca(mesa, pendientes)

            pendientes.add(n)
            mesa.pop()
    elif mesa[0] == amigo:
        pass #TODO
    elif amigo in mesa:
        pass #TODO
    else: # amigo in pendientes
        pendientes.remove(amigo)
        mesa.append(amigo)

        coloca(mesa, pendientes)

        pendientes.add(amigo)
        mesa.pop()


        
#Hacemos un for para repetir con todas las posibilidades la función de 'coloca' 
for i in range(len(favoritos)):
    pendientes = set(range(len(favoritos)))
    pendientes.remove(i)
    coloca([i], pendientes)
    