import socket 
import re 
 
LISTEN_ADDR = '127.0.0.1' 
PORT = 8080 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((LISTEN_ADDR, PORT)) 
s.listen(0) 
 
 
while True: 
    conn, addr = s.accept() 
	 
    while True: 

		 
            conn.sendall("HTTP/1.1 200 OK\n") 
            conn.sendall("Content-Type: text/html; charset=utf-8\n\n") 
            conn.sendall("<h1>Hello, World!</h1>") 
            conn.close() 