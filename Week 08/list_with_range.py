for number in range(0, 11, 2):  # Start=0 | End | Steps=1
    # print(number)
    pass

# 0.0.0.0
# 255.255.255.255
# 10.10.10.10

# 192.168.0.1
# 192.168.0.2
# 192.168.0.3
# 192.168.0.4
""" Generate a list of all valid ip addresses that are formed of the
    subnet prefix + subsequent numbers, skipping the first 10 and the even numbers.
    For example  ['192.168.0.11', '192.168.0.13', '192.168.0.15...']
"""
subnet_prefix = input("Enter a subnet prefix (example 198.168.0): ")
# list = [APPENDING ZONE    LOOPING ZONE]
ips_list = [subnet_prefix + "." + str(num) for num in range(11, 256, 2)]
print(ips_list)