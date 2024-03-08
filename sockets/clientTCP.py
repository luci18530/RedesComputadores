# Cliente TCP
from socket import *

serverName = 'localhost' # Endereço IP do servidor, o próprio computador
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) # Cria um objeto de socket TCP
clientSocket.connect((serverName, serverPort)) # Conecta ao servidor    

while True:
    sentence = input('Digite uma string em minúsculo (ou "EXIT" para sair): ')

    # Envia a string codificada para o servidor
    clientSocket.send(sentence.encode())

    # Se o comando for "EXIT", fecha a conexão
    if sentence.upper() == 'EXIT':
        print("Encerrando conexão com o servidor...")
        break

    # Recebe a resposta do servidor
    modifiedSentence = clientSocket.recv(1024)
    print('Do Servidor:', modifiedSentence.decode())

# Fecha o socket do cliente
clientSocket.close()