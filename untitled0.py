# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 11:08:01 2018

@author: jetjo
"""

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()