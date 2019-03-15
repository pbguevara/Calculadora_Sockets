import socket
import sys

PORT = 8087
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5
n = 0

def sumar(num1, num2):
    suma = num1+num2
    return suma

def restar(num1, num2):
    resta = num1-num2
    return resta

def multiplicar(num1, num2):
    multiplicacion = num1*num2
    return multiplicacion

def dividir(num1, num2):

    if num2 == 0:
        return "No es posible dividir por 0."
    else:
        division = num1/num2
        return division



def mi_logica(clientsocket):
    while True:
        operacion = clientsocket.recv(2048).decode("utf-8")
        print("El cliente ha escogido la siguiente operacion: ", operacion)
        operacion_lista = operacion.split(' ')
        if operacion_lista[0] == "exit":
            clientsocket.close()
            break

        num1 = float(operacion_lista[1])
        num2 = float(operacion_lista[2])


        if operacion_lista[0] == "1":
            resultado = sumar(num1, num2)

        elif operacion_lista[0] == "2":
            resultado = restar(num1, num2)

        elif operacion_lista[0] == "3":
            resultado = multiplicar(num1, num2)

        elif operacion_lista[0] == "4":
            resultado = dividir(num1, num2)

        else:
            resultado = "Lo siento, la opción no es válida"
            continue

        resultado = str(resultado)
        send_bytes = str.encode(resultado)
        clientsocket.send(send_bytes)

    condicion = False
    return condicion

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = IP

try:
    serversocket.bind((hostname, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    condicion = True
    while condicion:
        print("Esperando conexiones en %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        mi_logica(clientsocket)
    serversocket.close()

except socket.error:
    print("Problemas usando el puerto %i. ¿Tiene permiso?" % PORT)