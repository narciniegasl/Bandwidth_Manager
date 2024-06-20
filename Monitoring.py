import psutil
import time

def get_network_usage():
    net_io = psutil.net_io_counters() #Obtiene la cantidad total de bytes enviados y recibidos
    bytes_sent, bytes_recv = net_io.bytes_sent, net_io.bytes_recv
    return bytes_sent, bytes_recv

def main():
    old_sent, old_recv = get_network_usage()
    while True:
        time.sleep(1)  # Sleep for 1 second
        new_sent, new_recv = get_network_usage()
        sent_per_sec = new_sent - old_sent
        recv_per_sec = new_recv - old_recv
        print(f"Upload: {sent_per_sec / 1024:.2f} KB/s, Download: {recv_per_sec / 1024:.2f} KB/s")
        old_sent, old_recv = new_sent, new_recv

if __name__ == "__main__":
    main()
