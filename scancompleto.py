import socket
import ipaddress
import sys
def scan2():
    ipinfo = input("Digite um IP: ")

    ports = range(1, 65535)

    try:
        ips = ipaddress.ip_network(ipinfo, strict=False)
    except:
        print("IP invalido")
        sys.exit()

    for ip in ips:
        print("Escaneando IP", ip)
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            code = s.connect_ex((str(ip), port))
            s.close()
            if code == 0:
                print("Porta", port, "aberta")