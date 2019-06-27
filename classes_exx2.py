#!/usr/bin/env python

class NetDevice(object):
    def __init__(self,ip_addr,username,password):
        self.ip_addr = ip_addr
        self.username = username
        self.password =  password
        
        self.serial_number = ""
        self.vendor = ""
        self.model =""
        self.os_version = ""
        self.uptime = ""

    def print_ip(self):
        print("Device Ip address is : {}".format(self.ip_addr))

    def print_userCredentials(self):
        print("user name : {}".format(self.username))
        print("password : {}".format(self.password))

    def set_vendor(self, vendor):
        self.vendor = vendor
        print("Setting vendor : {}".format(self.vendor))

if __name__ == "__main__":

    print()
    #validation code
    obj1 = NetDevice(ip_addr="1.1.1.1",username="Siva",password="Siva")
    obj1.print_ip()
    obj1.set_vendor("Microsoft")
    print()

