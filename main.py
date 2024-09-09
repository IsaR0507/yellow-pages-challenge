# Tu código aquí
from data import people

def menú():
    print("-----------------")
while True:
    print("Hola,")
    print("Presiona 1 para Ver el listado")
    print("Presiona 2 para Agregar usuarios")
    print("Presiona 3 para Modificar un usuario Existente")
    print("Presiona 4 para Eliminar un usuario")
    print("Presiona 5 para salir")
    print("----------------------")
    user_input= int(input())  
    
    if user_input == 1:
        print(f"Este es el listado de usuarios que hay: {people}")
        
    elif user_input == 2:
        print("Ingresa el nombre del usuario que quieres ingresar: ")
        nombre_usuario = input()
        print("Ahora ingresa el numero: ")
        numero_usuario = input()
        print (f"Estos son los datos correctos? {nombre_usuario}{numero_usuario}")
        respuesta = input()

        if respuesta = True
        people[nombre_usuario] = numero_usuario
        print(people)
        
        

    elif user_input == 3:
        