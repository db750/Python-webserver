# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)  # Listen for incoming connections, with a queue of 1

  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()     #Fill in end
    
    try: 
      message = connectionSocket.recv(1024).decode() #Fill in start -a client is sending you a message   #Fill in end 
      print("Received message:\n", message)  # Debug print
      
      filename = message.split()[1]
      if filename == '/':
        filename = '/helloworld.html' 
      
      print("Requested file:", filename)  # Debug print
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], 'r') #fill in start #fill in end)
      #fill in end
      
      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 

      headers = "HTTP/1.1 200 OK\r\n"  # This is the response header for a successful request        
      #Content-Type is an example on how to send a header as bytes. There are more!
      headers += "Content-Type: text/html; charset=UTF-8\r\n"
      headers += "server: PythonWebServer\r\n"  
      headers += "Connection: close\r\n"  
      outputdata = headers.encode()  

      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
 
      #Fill in end
               
      # Instead of reading line by line, read entire file content
      file_content = f.read()
      outputdata += file_content.encode()  # Fill in start - append the file contents to the outputdata variable # Fill in end  
      
      f.close()
        
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!

      # Fill in start
      connectionSocket.send(headers + outputdata)  # Send the headers and the file content together as bytes

      # Fill in end
        
      connectionSocket.close() #closing the connection socket  
    except Exception as e:
      print("Error:", e)  # Debug print for exceptions
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      headers = "HTTP/1.1 404 Not Found\r\n"
      headers += "Content-Type: text/html\r\n"
      headers += "myserver: PythonWebServer\r\n"
      headers += "Connection: close\r\n\r\n"  
      body = "<html><body><h1>404 Not Found</h1></body></html>"
      
      response = headers + body  # Send the 404 Not Found response with HTML body
      #Fill in end
      connectionSocket.send(response.encode())

      #Close client socket
      #Fill in start
      connectionSocket.close()  # Close the connection socket after sending the response
      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)