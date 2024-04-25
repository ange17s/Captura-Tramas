from scapy.all import *

cantidad = int (input("Cuantos paquetes desea capturar"))

def captura(cantidad):
    global registros
    registros = sniff(count = cantidad)

captura(cantidad)
i = 0
for x in registros:
    print(i," - ", x.summary())
    i=i+1

num = int(input("Digite el numero del paquete que desee ver"))

print()
registros[num].show()
hexdump(registros[num])