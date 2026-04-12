# ClientServerBasics (2.0)

Calculadora remota usando sockets TCP, baseada no exemplo da Fig. 2.3 do livro.

## Funcionalidades

O servidor oferece 4 operações: `add`, `subtract`, `multiply` e `divide`.

O cliente envia requisições no formato `<operacao> <a> <b>` e recebe o resultado. É possível fazer múltiplas chamadas sem reconectar.

## Como executar

1. Ajuste o IP/porta em `constCS.py`
2. Inicie o servidor: `python server.py`
3. Em outro terminal, inicie o cliente: `python client.py`

## Exemplo

```
>>> add 10 5
15.0
>>> multiply 3 7
21.0
>>> divide 10 0
Erro: divisao por zero
>>> sair
```
