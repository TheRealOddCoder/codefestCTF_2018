# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 13:31:25 2018

@author: OddCoder
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('34.216.132.109',9093))

sending = ""

buffer = sock.recv(1024)
string = buffer.decode('utf8')

print(string)

string = string.replace("'","")
string = string.split(' ')

count = 0
l1=""
l2=""
t1= ""
t2 = ""
#print(string)
for i in range(1,15):
    if(len(string[i]) == 1):
        if(count == 0):
            l1 = string[i]
            t1 = string[i+1]
            count+=1
        else:
            l2 = string[i]
            t2 = string[i+1]

#print(l1)
#print(l2)

mul1 = l1*int(t1)
sending+=str(mul1)

mul2 = l2*int(t2)
sending+=str(mul2)

total = ord(l1) + ord(l2)
sending+=str(total)

sending+=str('\x0a')
print(sending)


sock.send(str.encode(sending))
flag = str(sock.recv(2048))
print(flag)
