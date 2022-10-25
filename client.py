#SCRIPT PARA CLIENTE
import socket
#FAZ ASSOCIAÇÃO AS INFOS DO SERVIDOR
print("Iniciando Cliente")
HOST = '127.0.0.1'
PORTA = int(input('Entre com a porta do servidor'))

#criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#cliente se conecta ao servidor
sock.connect((HOST,PORTA))

#enviar uma string de dados
sock.sendall(str.encode('BES - MELHOR CURSO DA PUC'))

#recebe do SERVIDOR
dados = sock.recv(2048)

#teste da mensagem
print("Mensagem ecoado do servidor ", dados.decode() )