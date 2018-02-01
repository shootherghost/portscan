import scan
import portas
import sys
import ping
import contato
argumentos = sys.argv
print("""
 ____  ____  ____  _____  ____  ____  ____  _     
/  __\/  _ \/  __\/__ __\/ ___\/   _\/  _ \/ \  /|
|  \/|| / \||  \/|  / \  |    \|  /  | / \|| |\ ||
|  __/| \_/||    /  | |  \___ ||  \_ | |-||| | \||
\_/   \____/\_/\_\  \_/  \____/\____/\_/ \|\_/  \|
                                                  
By: ShootherGhost
""")

if len(argumentos) > 1:
    if argumentos[1] == "-s":
        print(scan.scan())
    if argumentos[1] == "-p":
        print(portas.portas())
    if argumentos[1] == "-P":
        print(ping.ping())
    if argumentos[1] == "-c":
        print(contato.contato())
    if argumentos[1] == "ajuda":
        print("-s para escanear portas", "\n-p para saber os significados das portas", "\n-P para da pings em um host", "\n-c para ver os meus contatos")