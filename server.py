from socket import *
from constCS import *

def processar(msg):
    partes = msg.split()
    if len(partes) != 3:
        return "Erro: envie <operacao> <a> <b>"
    op, a, b = partes[0], float(partes[1]), float(partes[2])
    if op == "add":
        return str(a + b)
    elif op == "subtract":
        return str(a - b)
    elif op == "multiply":
        return str(a * b)
    elif op == "divide":
        return str(a / b) if b != 0 else "Erro: divisao por zero"
    else:
        return "Erro: operacao invalida"

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print("Servidor pronto")

while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        resultado = processar(data.decode())
        conn.send(resultado.encode())
    conn.close()
