from socket import *

serverPort = 12000 # Porta do servidor
serverSocket = socket(AF_INET, SOCK_STREAM)  # Cria um objeto de socket TCP
serverSocket.bind(('localhost', serverPort)) # Associa o socket com a porta e ao endereço localhost, ou seja, o próprio computador
serverSocket.listen(1) # Ouve na porta, permitindo apenas uma conexão pendente
print('O servidor está pronto para receber')

while True:
    # Aceita a conexão entrante, retornando novo socket e o endereço do cliente
    connectionSocket, addr = serverSocket.accept()
    # Exibe o endereço do cliente conectado
    print('Conexão recebida de:', addr)

    while True: # para receber e enviar mensagens
        # Recebe mensagem do cliente, com buffer de 1024 bytes, e decodifica para uma string
        sentence = connectionSocket.recv(1024).decode()

        # Se a mensagem for vazia, encerra a conexão
        if not sentence:  
            print('Conexão fechada com:', addr)
            break

        print('Mensagem recebida do cliente', addr, ':', sentence)

        # Se a mensagem for "EXIT", fecha a conexão
        if sentence.upper() == 'EXIT':
            print('Encerrando conexão com:', addr)
            break

        capitalizedSentence = sentence.upper() # Converte a string para maiúsculas
        connectionSocket.send(capitalizedSentence.encode()) # Envia a string codificada para o cliente

    connectionSocket.close()
