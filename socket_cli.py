import socket
import sys

IP = "127.0.0.1"
PORT = 8087


menu = """Elija una opcion:
          exit. Salir
          1. Sumar
          2. Restar
          3. Multiplicar
          4. Dividir
          
          Ejemplo de cómo introducir los datos:
          
          <op> <num1> <num2> [op1] [op2] [op3] [34] 
          """

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

def mi_logica(s):
    print(menu)

    while True:

        operacion = input("Introduzca una opcion: ")
        print(operacion)
        send_bytes = str.encode(operacion)
        s.send(send_bytes)

        if operacion == "exit":
            s.close()
            sys.exit()
        else:
            resultado = s.recv(2048).decode("utf-8")
            print("El resultado es ", resultado)

try:
    s.connect((IP, PORT))
    mi_logica(s)
    s.close()
    sys.exit(0)
except OSError:
    print("Socket already used")
    s.close()
    sys.exit(1)


