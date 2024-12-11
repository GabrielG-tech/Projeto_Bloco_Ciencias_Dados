import socket
import ssl

# cria o servidor TLS
def iniciar_servidor():
    contexto = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    contexto.load_cert_chain(certfile="servidor_cert.pem", keyfile="servidor_key.pem")

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('localhost', 12345))
    servidor_socket.listen(1)
    print("Servidor aguardando conexão...")
    
    # aceita a conexão e aplica TLS
    conexao, endereco = servidor_socket.accept()
    conexao_tls = contexto.wrap_socket(conexao, server_side=True)

    print(f"Conexão segura estabelecida com {endereco}")

    # recebe a mensagem criptografada do cliente
    mensagem_cliente = conexao_tls.recv(1024).decode()
    print(f"Mensagem recebida do cliente: {mensagem_cliente}")

    # responde com uma confirmação
    conexao_tls.sendall(b"Mensagem recebida com sucesso!")

    conexao_tls.close()
iniciar_servidor()
