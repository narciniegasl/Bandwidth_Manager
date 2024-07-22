import psutil #Trafico de red
import time
import subprocess #Para ejecutar comandos en la terminal

# Define los límites de ancho de banda (en bytes por segundo)
LIMIT_UPLOAD = int(input("Ingrese el límite de subida en KB/s: ")) * 1024  # Convertir de KB/s a bytes/s
LIMIT_DOWNLOAD = int(input("Ingrese el límite de descarga en KB/s: ")) * 1024  # Convertir de KB/s a bytes/s

def get_network_usage():
    net_io = psutil.net_io_counters() #Obtiene la cantidad total de bytes enviados y recibidos
    bytes_sent, bytes_recv = net_io.bytes_sent, net_io.bytes_recv
    return bytes_sent, bytes_recv

def apply_bandwidth_limit(upload_rate, download_rate):
    # Esta función debe ser implementada específicamente para tu sistema operativo.
    get_qos_command = 'Get-NetQosPolicy | Format-Table Name, Owner, PriorityLevel'
    subprocess.run(["powershell", "-Command", get_qos_command], capture_output=True)
    # Para crear una nueva política de QoS para una aplicación específica:
    new_qos_command = 'New-NetQosPolicy -Name "MiAppLimitada" -AppPathNameMatchCondition "T2E.exe" -NetworkProfile All -ThrottleRateActionBitsPerSecond 1000000'
    subprocess.run(["powershell", "-Command", new_qos_command], capture_output=True)


def main():
    old_sent, old_recv = get_network_usage()
    while True:
        time.sleep(1)  # Sleep for 1 second
        new_sent, new_recv = get_network_usage()
        sent_per_sec = new_sent - old_sent
        recv_per_sec = new_recv - old_recv
        print(f"Upload: {sent_per_sec / 1024:.2f} KB/s, Download: {recv_per_sec / 1024:.2f} KB/s")
        
        if sent_per_sec > LIMIT_UPLOAD or recv_per_sec > LIMIT_DOWNLOAD:
            apply_bandwidth_limit(LIMIT_UPLOAD, LIMIT_DOWNLOAD)
        
        old_sent, old_recv = new_sent, new_recv

if __name__ == "__main__":
    main()
