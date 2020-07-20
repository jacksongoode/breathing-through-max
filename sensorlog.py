import socket
import argparse
from pythonosc import udp_client

try:
    # Create argument parser
    parser = argparse.ArgumentParser()

    # Positional mandatory arguments
    parser.add_argument("ip", help="Your local ip address", type=str)
    parser.add_argument("in_port", help="Incoming port (from app)", type=int)
    parser.add_argument("out_port", help="Outgoing port (to Max)", type=int)

    # Parse arguments
    args = parser.parse_args()

    # Specify port and ip
    in_port = args.in_port
    out_port = args.out_port
    local_ip = args.ip

    # Recieving from UDP
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((local_ip, in_port))

    # Set up an outgoing OSC server
    client = udp_client.SimpleUDPClient(local_ip, out_port)
    start_msg = True

    print("Recieving on port: ["+str(in_port)+"]\nSending on port: ["+str(out_port)+"]")
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        while start_msg == True & len(data) > 0:
            print("Now streaming data...")
            start_msg = False
        data = str(data)
        data_osc = data.split(",") # split csv format
        data_osc[6] = data_osc[6][:-3]

        # add osc prefixes
        client.send_message("/x", float(data_osc[4]))
        client.send_message("/y", float(data_osc[5]))
        client.send_message("/z", float(data_osc[6]))

# Send out errors within Max console
except Exception as e:
    print("Error: "+str(e))