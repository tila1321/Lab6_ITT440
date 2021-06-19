import socket
import sys
import math
import time
import errno
from multiprocessing import Process

def process_start(soc_sock):
    while True:
      soc_sock.send(str.encode('\n----||Welcome to online Calculator||----\n Operation: [1-Sqrt || 2-Exp || 3-Log || 4-Pi]\n\nPlease enter your choice:'))
      while True:
        data = soc_sock.recv(2048)
        data = data.decode('utf-8')
        print(data)
        if not data:
             break
        elif data == '1':
             soc_sock.send(str.encode('\nEnter a number:'))
             number = soc_sock.recv(2048)
             number = int(number)
             number = str(math.sqrt(number))
             print(number)
             soc_sock.send(str.encode('\nThe answer is:'+ number + '\n\nPress ENTER to continue'))
        elif data == '2':
             soc_sock.send(str.encode('\nEnter a number:'))
             number = soc_sock.recv(2048)
             number = int(number)
             number = str(math.exp(number))
             print(number)
             soc_sock.send(str.encode('\nThe answer is:'+ number + '\n\nPress ENTER to continue'))
        elif data == '3':
             soc_sock.send(str.encode('\nEnter a number:'))
             number = soc_sock.recv(2048)
             number = int(number)
             number = str(math.log(number))
             print(number)
             soc_sock.send(str.encode('\nThe answer is:'+ number + '\n\nPress ENTER to continue.'))
        elif data == '4':
             soc_sock.send(str.encode('\nEnter a number:'))
             number = soc_sock.recv(2048)
             number = int(number)
             number = str(math.pi)
             print(number)
             soc_sock.send(str.encode('\nThe answer is:'+ number + '\n\nPress ENTER to continue.'))
        else:
             soc_sock.send(str.encode('Error. Operation that you choose is not available.\nPress ENTER to continue.')) 
        break


    soc_sock.close()



if __name__ == '__main__':
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(("",5567))
    print("Server is listening............")
    soc.listen(3)
    try:
        while True:
            try:
                soc_sock, soc_addr = soc.accept()
                pr = Process(target=process_start, args=(soc_sock,))
                pr.start()

            except socket.error:

                print('A socket error occured')

    except Exception as e:
                print('An exception occurred!')
                print(e)
                sys.exit(1)
    finally:
     	   soc.close()
