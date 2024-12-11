import socket
import ssl

# conecta ao servidor TLS
def conectar_ao_servidor():
    contexto = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile="servidor_cert.pem")
    
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('localhost', 12345))
    
    cliente_tls = contexto.wrap_socket(cliente_socket, server_hostname='localhost')

    # envia uma mensagem criptografada ao servidor
    mensagem = "Olá, servidor seguro!"
    cliente_tls.sendall(mensagem.encode())

    # recebe a resposta do servidor
    resposta = cliente_tls.recv(1024).decode()
    print(f"Resposta do servidor: {resposta}")

    cliente_tls.close()
conectar_ao_servidor()
