#!usr/bin/env python

try:
   #PY2
   ip_add = raw_input("Enter IP address")
except NameError:
   #PY3
   ip_add = input("Enter IP address")

my_ip_list = ip_add.split(".");
my_ip_list[-1] = 0

ip_binary = []
ip_binary.append(bin(int(my_ip_list[0])))
ip_binary.append(bin(int(my_ip_list[1])))
ip_binary.append(bin(int(my_ip_list[2])))
ip_binary.append(bin(int(my_ip_list[3])))

print()
print("{:<12} {:<12} {:<12} {:<12}".format("octet1", "octet2", "octet3", "octet4")) 
print("{:<12} {:<12} {:<12} {:<12}".format(*my_ip_list))
print("{:<12} {:<12} {:<12} {:<12}".format(*ip_binary))
print()


