from socket import *
from constCS import *

testes = [
    "ASTERISCO:Olá mundo",
    "MAIUSCULO:estou gritando no servidor"
]

for msg in testes:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    
    print(f"Enviando requisição: {msg}")
    s.send(str.encode(msg)) 
    
    data = s.recv(1024) 
    print(f"Resposta do servidor: {bytes.decode(data)}")
    
    s.close()
    print("-" * 30)
