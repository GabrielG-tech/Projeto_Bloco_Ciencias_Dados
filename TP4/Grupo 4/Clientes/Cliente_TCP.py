import socket

def cliente_tcp():
    # cria o socket TCP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 12345))  # conecta ao servidor na porta 12345
    mensagem = cliente.recv(1024).decode()  # recebe a mensagem de boas-vindas
    print("Mensagem do servidor:", mensagem)
    cliente.close()  # fecha a conexão
