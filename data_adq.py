from scapy.all import sniff, IP
import numpy  as np
import time



packet_sizes = []
packet_times = []
WINDOW_SIZE = 20
def procesar_paquete (pkt):
    global packet_sizes, packet_times
    

    if pkt.haslayer(IP):
        size = len(pkt)
        timestamp = pkt.time

        packet_sizes.append(size)
        packet_times.append(timestamp)


        if len(packet_sizes) >= WINDOW_SIZE:

            mean_size = np.mean(packet_sizes)
            std_size = np.std(packet_sizes)

            iats = np.diff(packet_times)
            mean_iat = np.mean(iats)
            std_iat = np.std(iats)
            features = [mean_size, std_size, mean_iat, std_iat]
            print(f"Features extraídas: Size_Avg={mean_size:.1f}, IAT_Avg={mean_iat:.4f}s")

            packet_sizes = []
            packet_times = []       


sniff(iface="wlan0", filter="tcp", prn=procesar_paquete, store=0)