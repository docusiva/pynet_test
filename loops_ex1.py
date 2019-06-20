#!usr/bin/env python

#Extra list typecasting needed for PY3

my_list = list(range(1,50))

for i in my_list:
    if i >= 13:
         continue
    print(i) 
    if i == 39:
         break
