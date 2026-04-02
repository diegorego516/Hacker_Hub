import socket

def servidor():
    HOST = "127.0.0.1"
    PORT = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
    print("Servidor aguardando conexão...")

    conn, addr = s.accept()
    print("conectado por", addr)

    while True:
        data = conn.recv(1024).decode("utf-8")
        if not data or data.lower() == "sair":
            break
        print("Mensagem recebida")
        conn.send(f"Echo: {data}".encode("utf-8"))

    conn.close()
    s.close()

def cliente():
    HOST = "127.0.0.1"
    PORT = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    while True:
        msg = input("Digite uma mensagem ('sair' para encerrar): ")
        s.send(msg.encode("utf-8"))
        if msg.lower() == "sair":
            break
        resposta = s.recv(1024).decode("utf-8")
        print("Servidor respondeu: ", resposta)

    s.close()

if __name__ == "__main__":
    escolha = input("Digite 's' para servidor ou 'c' para cliente: ")
    if escolha == "s":
        servidor()
    else:
        cliente()

import socketserver

def tcp_ip():
    HOST = "127.0.0.1"
    PORT = 5000

    s = socket.socket(socketserver.TCPServer, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
    print("Servidor conectado com sucesso...")

    conn, addr = s.accept()
    print("conectado por", addr)

    while True:
        data = conn.recv(1024).decode("utf-8")
        if not data or data.lower() == "sair":
            break
        print("Conexão aceita, conectando o usuário...")
        def connect():
            conn.connect(f"Echo: {connect}".encode("utf-8"))
    
        conn.close()
        s.close()

if __name__ == "__main__":
    escolha = input("Digite 't' para tcp-ip, 's' para servidor e 'c' para cliente")
    if escolha == "s":
        tcp_ip()
    try:
        servidor()
    except Exception as e:
        cliente()
