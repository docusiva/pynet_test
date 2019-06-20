#1/usr/bin/env phython

name1 ="Karthik"
name2 = "Muthuvel"

try:
   #PY2
   name3 = raw_input("Enter 3rd Name: ")
except NameError:
   #PY3
   name3 = input("Enter fourth Name:")

print()
print("{:>30}".format(name1))
print("{:>30}".format(name2))
print("{:>30}".format(name3))
print()
