from scapy.all import sniff, IP, Raw # pip install scapy

# callback para processar os pacotes
def processar_pacote(pacote):
    if pacote.haslayer(IP):  # verifica se o pacote possui a camada IP
        ip_origem = pacote[IP].src
        ip_destino = pacote[IP].dst
        if pacote.haslayer(Raw):  # verifica se o pacote contém dados
            carga_util = pacote[Raw].load
            print(f"Origem: {ip_origem}, Destino: {ip_destino}, Carga útil: {carga_util}")

# inicia a captura de pacotes na porta 12345
sniff(filter="tcp port 12345", prn=processar_pacote, store=0)
