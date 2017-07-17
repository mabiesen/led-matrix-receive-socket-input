import socket
import threading
import livematrix
    

def parse_and_send(mystring):
    colonsplit = mystring.split(':')
    print(colonsplit[1])
    livematrix.livereading(colonsplit[0],colonsplit[1])
    
    

def start_server():
	bind_ip = "192.168.254.27"
	bind_port = 8080

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((bind_ip, bind_port))
	server.listen(5)

	print("[*] Listening on %s:%d" % (bind_ip, bind_port))

	#send back strings to client
	#server_manage_client_input determines what to do with a request.
	#def reply_to_client(client_socket, request):
	#	success = "success"
	#	client_socket.send(success)
	#	client_socket.close()


	#this function called as new thread
	#receives information, then works on a reply
	def handle_client(client_socket):

	    #print out what the client sends
		request = client_socket.recv(1024)
		print("[*] Received %s" % request)
		request.strip(' \t\n\r')
		parse_and_send(request)



#Constantly scans for connections to clients.
#spins off a new thread when contact is made with client
	while True:
	    client, addr = server.accept()

	    print ("[*] Accepted connection from %s:%d" % (addr[0], addr[1]))

	    #spin up our client thread to handle incoming data
	    #the thread is declared in the first line and started in the second line
	    client_handler = threading.Thread(target=handle_client, args=(client,))
	    client_handler.start()


server_thread = threading.Thread(target=start_server)
server_thread.start()
