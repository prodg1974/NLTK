import socket
import os

        
fn="security_now_"

listOfShowIDs=[1,2]

for str in str(listOfShowIDs):
    print('top of loop with ' + str)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('www.grc.com', 80))
    mysock.send('GET https://www.grc.com/sn/sn-' + str +'.txt HTTP/1.0\n\n')
    
    myfile= fn + str + ".txt"
    with open(myfile,'w'):
        while True:
            data = mysock.recv(512)
            if ( len(data) < 1 ) :
                break
            print(data)
    close(myfile)
    data = ''
    mysock.close()
    print('Done with ' + str)
#mysock.close()
 
