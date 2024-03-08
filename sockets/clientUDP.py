from socket import *

serverName = 'localhost'  # Endereço IP do servidor, o próprio computador
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)  # Cria um objeto de socket UDP

while True:
    sentence = input('Digite uma string em minúsculo (ou "EXIT" para sair): ')

    # Envia a string codificada para o servidor
    clientSocket.sendto(sentence.encode(), (serverName, serverPort))

    # Se o comando for "EXIT", fecha o socket e sai
    if sentence.upper() == 'EXIT':
        print("Encerrando conexão com o servidor...")
        break

    # Recebe a resposta do servidor
    modifiedSentence, serverAddress = clientSocket.recvfrom(1024)
    print('Do Servidor:', modifiedSentence.decode())

# Fecha o socket do cliente
clientSocket.close()

# recvfrom e sendto são usados para receber e enviar mensagens em sockets UDP
# UDP não tem conexão, então não há necessidade de aceitar conexões (retira-se o accept) nem de criar um novo socket para cada conexão (retira-se o connectionSocket)