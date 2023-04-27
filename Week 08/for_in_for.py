players_1 = ["John", "David", "Max"]
players_2 = ["Sara", "Rita", "Sofia"]

for player in players_1:
    for a_player in players_2:
        print(player, "VS", a_player)

ips = ["192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4"]
ports = ["80", "443", "21"]
for ip in ips:
    for port in ports:
        # scan(ip, port)
        print(ip + ":" + port)

