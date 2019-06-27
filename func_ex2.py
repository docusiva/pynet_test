#!/usr/bin/env python

def my_func(x,y,z=20):
    return x+y+z


my_list = [22,17,19]
my_dict = {"x": 13, "y": 22, "z": 1}

print()
return_val = my_func(*my_list)
print("Calling with *args: {}".format(return_val))

return_val = my_func(**my_dict)
print("Calling with kwargs : {}".format(return_val))

