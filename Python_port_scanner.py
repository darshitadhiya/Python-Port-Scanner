import socket
import termcolor
import threading

def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1, ports + 1):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)  # Set a timeout for the socket connection
        sock.connect((ipaddress, port))
        service = socket.getservbyport(port)  # Get the service running on the port
        print("[+] Port {} Opened | Service: {}".format(port, service))
        sock.close()
    except (socket.timeout, socket.error):
        pass

def threaded_scan(ipaddress, ports):
    scan(ipaddress, ports)

targets = input("[*] Enter Targets To Scan (split them by ,): ")
ports_range = input("[*] Enter Port Range (e.g., 1-100): ")
port_start, port_end = map(int, ports_range.split('-'))

if ',' in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
    for ip_addr in targets.split(','):
        threading.Thread(target=threaded_scan, args=(ip_addr.strip(' '), port_end - port_start + 1)).start()
else:
    threading.Thread(target=threaded_scan, args=(targets, port_end - port_start + 1)).start()
