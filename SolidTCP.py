import socket
import threading, queue
import time

############## TCP Class Portion ################################
#thread for all interactions
class client(threading.Thread):
    def __init__(self, conn):
        super(client, self).__init__()
        self.conn = conn
    def run(self):
        stamp = 0
        while True:
            #Timestamp for accuracy and error handling
            stamp = stamp + 1
            data = self.conn.recv(1024)
            cleandata = data.rstrip()
            cleandata = data.decode()

            qp.put(str(cleandata) + ";" + str(stamp))
            if len(data) < 3:
                self.refresh()
                break

    def send_msg(self,msg):
        self.conn.send(msg)

    def refresh(self):
        q.put(1)
        self.conn.shutdown(socket.SHUT_RDWR)
        self.conn.close()


#set variables, create socket
class clientConnSetup():
    def __init__(self):
        self.host = '192.168.254.41'
        self.currport = 8080
        self.port1 = 8080
        self.port2 = 9999


    def createSocket(self):
        s = None
        while s == None:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind((self.host, self.currport))
                s.listen(5)
                print('[+] Listening for connections on port: {0}'.format(self.currport))
                conn, address = s.accept()
                return conn
            except socket.error as e:
                if self.currport == self.port1:
                    self.currport =self.port2
                else:
                    self.currport = self.port1
                print('Failed to create socket')
                print(e)
                s = None
                time.sleep(1)

###########################################################
################### Main Portion #############################

# Global Variables
switch = 0
q = queue.Queue()
qp = queue.Queue()
q.put(switch)

#this is weird. Logic, when you go to use this with other programs...:
#We don't want to disrupt the thread, or cause it to cross the main thread
#We don't want to integrate our code into the class out of principle
#We could implement an inheritance, but thats still bad principle: the TCP class i not an led, or person, etc!
def StartTheServer():
    
    while True:
        ccS = clientConnSetup()
        myconn = ccS.createSocket()
        c = client(myconn)
        c.start()
        while q.get() == 0:
            time.sleep(1)
        q.put(0)
        c.join()
        time.sleep(3)
    
