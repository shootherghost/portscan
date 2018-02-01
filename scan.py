import socket
def scan():
    ip = input("Digite o endereço: ")

    portas = []
    count = 0

    while count < 5:
        portas.append(int(input("Digite a porta: ")))
        count += 1

    for porta in portas:
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexao.settimeout(0.3)
        codigo = conexao.connect_ex((ip, porta))

        if codigo == 0:
            print (str(porta) + "-> Porta aberta")

    print("Scan finalizado com sucesso")
    print("\nBy: ShootherGhost")
