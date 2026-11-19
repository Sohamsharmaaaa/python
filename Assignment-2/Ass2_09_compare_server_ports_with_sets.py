"""Write a python program to create two sets of open ports if two servers and display the union,
intersection and difference of the sets."""

server1 = {21, 22, 80, 443, 3306, 8080}
server2 = {22, 25, 80, 443, 5432, 8443}
print("server 1 open ports : ", sorted(server1))
print("Server 2 open ports : ", sorted(server2))
print()

# union: ports open on at least one server
union_ports = server1 | server2
print("Union (open on either server) : ", sorted(union_ports))

# intersection: ports open on both servers
common_ports = server1 & server2
print("\nIntersection (open on both servers) : ", sorted(common_ports))

# Difference: ports open on one sers but not on other
only_server1 = server1 - server2
only_server2 = server2 - server1
print("\nDifference (server 1 - server 2) : ", sorted(only_server1))
print("\nDifference (server 2 - server 1) : ", sorted(only_server2))

# Symmetric difference: ports open exactly one of the servers
print("\nSymmetric difference: ", sorted(server1 ^ server2))
