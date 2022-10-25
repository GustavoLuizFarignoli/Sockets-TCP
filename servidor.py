#importar a biblioteca da API
from ast import While
import socket

#HOST : loopback
print("Iniciando O Servidor")
HOST = '127.0.0.1'
PORTA = int(input('Entre com a porta do servidor'))

#criação do nosso socket
#inicialização com o tipo de endereçamento e IP e PROTOCOLO
#IPV4 : AF_INET
#TCP : SOCK_STREAM
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#vincular host e porta : BIND
while True:
    try:
        sock.bind((HOST,PORTA))
        break
    except:
        print("Erro em executar o bind")
        continue

#ENTRAR NO MODO DE ESCUTA
sock.listen()
print(f"Aguardando conexões em {HOST}:{PORTA}")

while True:
    #RETORNAR UMA PORTA E UM ENDEREÇO
    conn, ender = sock.accept()
    print(f'Conectado na porta {ender[1]}')

    #RECEBIMENTO DOS DADOS DO CLIENTE
    #LOOP PARA RECEBIMENTO
    while True:
        dados = conn.recv(5) #tamanho do buffer
        if not dados:
            print(f"Fechando a conexão com {ender[0]}:{ender[1]}...")
            conn.close()
            break
        print(dados)
        #envia para o cliente a mensagem lida
        #"ecoa para o cliente"
        conn.sendall(dados)


