import socket

def cliente_udp():
    # cria o socket UDP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cliente.sendto("Olá servidor UDP".encode(), ('localhost', 12345))  # envia uma mensagem ao servidor
    resposta, endereco = cliente.recvfrom(1024)  # recebe a resposta do servidor
    print("Resposta do servidor:", resposta.decode())
    cliente.close()  # fecha a conexão
