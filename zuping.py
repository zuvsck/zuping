import socket
import struct
import time
import sys
import os
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

def checksum(source_string):
    """Calculate the checksum of the packet."""
    sum = 0
    count_to = (len(source_string) // 2) * 2
    count = 0

    while count < count_to:
        this_val = source_string[count + 1] * 256 + source_string[count]
        sum = sum + this_val
        sum = sum & 0xFFFFFFFF
        count = count + 2

    if count_to < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xFFFFFFFF

    sum = (sum >> 16) + (sum & 0xFFFF)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xFFFF
    answer = answer >> 8 | (answer << 8 & 0xFF00)
    return answer

def create_packet(id):
    """Create a new ICMP packet."""
    header = struct.pack("bbHHh", 8, 0, 0, id, 1)
    data = struct.pack("d", time.time())
    my_checksum = checksum(header + data)
    header = struct.pack("bbHHh", 8, 0, socket.htons(my_checksum), id, 1)
    return header + data

def ping(host):
    """Perform a ping to the specified host."""
    try:
        dest = socket.gethostbyname(host)

        icmp = socket.getprotobyname("icmp")
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp) as sock:
            sock.settimeout(1)
            packet_id = int((id(0) * time.time()) % 65535)
            packet = create_packet(packet_id)

            start_time = time.time()
            sock.sendto(packet, (dest, 1))
            try:
                recv_packet, addr = sock.recvfrom(1024)
                end_time = time.time()
                icmp_header = recv_packet[20:28]
                type, code, checksum, p_id, sequence = struct.unpack("bbHHh", icmp_header)
                if p_id == packet_id:
                    elapsed_time = int((end_time - start_time) * 1000)
                    print(Fore.GREEN + f"Reply from " + Fore.RED + f"{addr[0]}" + Fore.WHITE + f" (" + Fore.YELLOW + f"{host}" + Fore.WHITE + f") " + Fore.GREEN + f"time=" + Fore.RED + f"{elapsed_time}" + Fore.GREEN + f"ms" + Style.RESET_ALL)
                    return True
            except socket.timeout:
                print(Fore.RED + f"Reply from {host}: Request timed out." + Style.RESET_ALL)
                return False
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
        return False

def check_permissions():
    if os.name != 'nt' and os.geteuid() != 0:
        print(Fore.RED + "Error: This script must be run as root on Linux." + Style.RESET_ALL)
        sys.exit(1)

def main():
    check_permissions()
    if len(sys.argv) != 2:
        print("Usage: zuping <address or IP>")
        sys.exit(1)

    host = sys.argv[1]
    print(f"Starting ping verification for " + Fore.RED + f"{host}" + Style.RESET_ALL)
    try:
        while True:
            ping(host)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n" + Fore.RED + "Stopping ping verification." + Fore.WHITE)
