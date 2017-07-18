import SolidTCP
#import livematrix
import time
import threading



# call tcp server through a thread.  This will free the main thread
# then loop to read from the server

server_thread = threading.Thread(target=SolidTCP.StartTheServer)
server_thread.start()
while True:
    thisreceive = SolidTCP.qp.get()
    stampsplit = thisreceive.split(";")
    stamptime = stampsplit[1]
    #if stampsplit[0] == "clear":
        #livematrix.clear()
    #else:
    #    colonsplit = stampsplit[0].split(b':')
    #    livematrix.livereading(colonsplit[0],colonsplit[1])    
    print(stampsplit[0])
