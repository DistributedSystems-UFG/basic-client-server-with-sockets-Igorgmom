from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

print("Calculadora remota — operacoes: add, subtract, multiply, divide")
print("Formato: <operacao> <a> <b>   (ex: add 10 5)")
print("Digite 'sair' para encerrar\n")

while True:
    msg = input(">>> ")
    if msg.strip().lower() == "sair":
        break
    s.send(msg.encode())
    data = s.recv(1024)
    print(data.decode())

s.close()
