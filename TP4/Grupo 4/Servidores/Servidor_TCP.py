import socket

def servidor_tcp():
    # cria o socket TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 12345))  # vincula à porta 12345
    servidor.listen(1)  # aguarda conexões
    print("Aguardando conexão...")

    while True:
        cliente, endereco = servidor.accept()  # aceita a conexão
        print(f"Conexão recebida de {endereco}")
        mensagem = "Bem-vindo ao servidor TCP!"
        cliente.send(mensagem.encode())  # envia uma mensagem
        cliente.close()  # fecha a conexão
