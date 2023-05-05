import socket
import datetime

timestamp = datetime.datetime.now().strftime(f"%d-%b-%Y (%H:%M:%S.%f)")
ip = "10.56.17.7"
port = 445
socket.setdefaulttimeout(0.1)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((ip, port))  # if result is 0 port is OPEN

# Since we know the result now, we can print a message
if result == 0:
    status_message = f"{ip}:{port:<5d} Open | Time: {timestamp}"
    print(status_message)
else:
    status_message = f"{ip}:{port:<5d} Closed/Filtered or host is offline | Time: {timestamp}"
    print(status_message)

# TODO Generate a range of IP addresses (using suffix by a user + an octet between 0 and 255)
# TODO Retrieve port number as a list from lines of a txt file ports.txt
# TODO Scan each IP with each port and print the message (open or closed)
# TODO Write only the message of Open or Closed to a file ip_port_log.txt
