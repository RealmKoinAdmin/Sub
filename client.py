# client.py

import socket
global Broken
Broken = False

class Client():
 def __init__(self):
  print('Vivian Client V1.0')
  self.connect_to_server()

 def connect_to_server(self):
  soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
  soc.connect(("127.0.0.1", 45426))
  clients_input = input("|[Vivian]| Action Required: \n")
  clients_input_split = clients_input.split(' ')
  soc.send(clients_input.encode("utf8")) # we must encode the string to bytes  
  result_bytes = soc.recv(4096) # the number means how the response can be in bytes  
  result_string = result_bytes.decode("utf8") # the return will be in bytes, so decode
  print("{}".format(result_string))
  digest = '%s' % ', '.join(clients_input_split[1:])
  self.keep_alive()
   

 def keep_alive(self):
    self.connect_to_server()


while not Broken:
 a = Client()
 
