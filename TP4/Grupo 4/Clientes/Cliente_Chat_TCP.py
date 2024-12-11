import socket
import threading

def receber_mensagens(cliente):
    while True:
        mensagem = cliente.recv(1024).decode()
        print(mensagem)

def cliente_chat():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 12345))

    threading.Thread(target=receber_mensagens, args=(cliente,)).start()

    while True:
        mensagem = input("Digite a mensagem (ou 'sair' para sair): ")
        if mensagem == 'sair':
            cliente.send(mensagem.encode())
            break
        cliente.send(mensagem.encode())
    cliente.close()
