#!/usr/bin/env python

def my_func(x,y,z=20):
    return x+y+z

print()
return_val = my_func(10,20,30)
print("calling with three positional arg: {}".format(return_val))

return_val = my_func(x=10, y=20)
print("Calling with two named args : {}".format(return_val))

return_val = my_func(10, z=13, y=20)
print("calling two named args and one positional : {}".format(return_val))

return_val = my_func(x="x", y="y", z="z")
print("Calling with three strings : {}".format(return_val))

return_val = my_func(x=["x"],y=["y"], z=["z"])
print("calling with three list : {}".format(return_val))
print()


