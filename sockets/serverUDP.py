from socket import *

serverPort = 12000  # Porta do servidor
serverSocket = socket(AF_INET, SOCK_DGRAM)  # Cria um objeto de socket UDP
serverSocket.bind(('localhost', serverPort))  # Associa o socket com a porta e ao endereço localhost, ou seja, o próprio computador
print('O servidor está pronto para receber')

while True:
    try:
        sentence, addr = serverSocket.recvfrom(1024)
        print('Conexão recebida de:', addr)
        print('Mensagem recebida do cliente', addr, ':', sentence.decode())

        capitalizedSentence = sentence.upper()
        serverSocket.sendto(capitalizedSentence, addr)
    except ConnectionResetError:
        print('Erro de conexão resetada detectado. Continuando...')
        continue

# recvfrom e sendto são usados para receber e enviar mensagens em sockets UDP
# UDP não tem conexão, então não há necessidade de aceitar conexões (retira-se o accept) nem de criar um novo socket para cada conexão (retira-se o connectionSocket)