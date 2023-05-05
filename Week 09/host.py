import socket
import ipaddress

# Get my IP address
my_ip_address = socket.gethostbyname(socket.gethostname())
print("My IP address: ", my_ip_address)

# Get the host name
host_name = socket.gethostname()
print("The host name:", host_name)

# Used in validating the IP address V4
ipaddress.IPv4Address(my_ip_address)

# Get the subnet prefix (first 3 octets) as a list
print(my_ip_address.split(".")[:3])

# Use the join() function to convert the list to a string
separator = "."
print(".".join(my_ip_address.split(".")[:3]))

# Use the prefix to generate a range of ips in a list
subnet_prefix = ".".join(my_ip_address.split(".")[:3])
ips_list = [subnet_prefix + "." + str(num) for num in range(11, 256, 2)]
print(ips_list)
