from scapy.all import ARP, Ether, srp
"""
ARP es la clase para crear paquetes ARP, Ether es la clase para crear tramas Ethernet 
y srp es la función para enviar y recibir paquetes a nivel de enlace (capa 2).
"""

def scan(ip):
    arp = ARP(pdst=ip) #Creación del Paquete ARP: pdst es el destino de la solicitud ARP
    ether = Ether(dst="ff:ff:ff:ff:ff:ff") #Se crea una trama Ethernet con la direcciónde difusión  todos los dispositivos en la red
    packet = ether/arp #Combina Trama Ethernet y Paquete ARP:

    result = srp(packet, timeout=5, verbose=0)[0] #srp envía el paquete a nivel de enlace y espera respuestas. 

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

# reemplace "192.168.56.0/24" con la dirección de su red
devices = scan("192.168.1.1/24")

for device in devices:
    print(device)