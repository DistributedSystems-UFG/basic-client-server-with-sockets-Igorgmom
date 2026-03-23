from socket import *
from constCS import *
import time

s = socket(AF_INET, SOCK_STREAM) 
s.bind(('0.0.0.0', PORT)) 
s.listen(1) 

print("Servidor aguardando conexão...")
(conn, addr) = s.accept() 

while True: 
    data = conn.recv(1024) 
    if not data: break 
    
    mensagem = bytes.decode(data)
    
    if ":" in mensagem:
        comando, conteudo = mensagem.split(":", 1)        
        if comando == "MAIUSCULO":
            resultado = conteudo.upper()
        elif comando == "ASTERISCO":
            resultado = conteudo + "*"
        else:
            resultado = "Operação desconhecida"
    else:
        resultado = "Erro: Formato de mensagem inválido"

    conn.send(str.encode(resultado))

conn.close()
