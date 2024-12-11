import socket
import threading

# gerencia a comunicação com cada cliente
def gerenciar_cliente(cliente, endereco):
    print(f"Conexão recebida de {endereco}")
    while True:
        mensagem = cliente.recv(1024).decode()
        if mensagem == 'sair':
            break
        print(f"Mensagem de {endereco}: {mensagem}")
        for other_cliente in clientes_conectados:
            if other_cliente != cliente:
                other_cliente.send(f"{endereco}: {mensagem}".encode())
    cliente.close()

# servidor de chat TCP
def servidor_chat():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 12345))
    servidor.listen(5)
    print("Servidor de chat aguardando conexões...")

    while True:
        cliente, endereco = servidor.accept()
        clientes_conectados.append(cliente)
        threading.Thread(target=gerenciar_cliente, args=(cliente, endereco)).start()
clientes_conectados = []
