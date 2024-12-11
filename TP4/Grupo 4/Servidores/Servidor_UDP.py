import socket

def servidor_udp():
    # cria o socket UDP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind(('localhost', 12345))  # vincula à porta 12345
    print("Servidor UDP aguardando mensagens...")

    while True:
        mensagem, endereco = servidor.recvfrom(1024)  # recebe uma mensagem
        print(f"Mensagem recebida de {endereco}: {mensagem.decode()}")
        servidor.sendto("Mensagem recebida".encode(), endereco)  # envia uma confirmação
