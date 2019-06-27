#!/usr/bin/env python

from __future__ import print_function

class NetDevice(object):
    def __init__(self,ip,usr,pwd):
        self.ip = ip
        self.usr = usr
        self.pwd = pwd
        
        self.serial_number = ""
        self.vendor = ""
        self.model = ""
        self.os_version = ""
        self.uptime = ""



