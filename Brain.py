# Brain.py
# Multi use server object python3
# Author: Skrypt

# test dict() setup
import pickle
import time
from Memory.Information.VBActions import BrainActionsBuild
from Memory.Information.VBDefinitions import BrainDefinitionsBuild
from Memory.Information.VBCommunications import BrainCommunicationsBuild
from Memory.Users.VBUsers import USER
from hashlib import sha256
global BIND_PORT
global ActionBuild
global DefinitionBuild
global CommunicationBuild
global UsersBuild
BIND_PORT = 45426
ActionBuild = False
DefinitionsBuild = False
CommunicationsBuild = False
UsersBuild = False

def _say(message,who):
 try:
  if who.lower() == 'vivian':
   sym = '|[Vivian]|>>: '
   print(sym+message)
  elif who.lower() == 'server':
   sym = '|[Server]|>>: '
   print(sym+message)
  else:
   print('|[Unknown]|>>: '+message)
 except Exception as E:
  print('|[Server Error]|>>: [Unknown \'Say\'] Function Error: [{}]'.format(E))
  print('Message: [{}]  Who: [{}]'.format(message,who))

def _setupUser(i):
 dirc = './Memory/Users/'
 try:
  if not os.path.exists(dirc+i):
   
   os.makedirs(dirc+i)
  else:
   _say('Directory Already Created For User [{}]'.format(i))
 except Exception as E:
  _say('Something Has Gone Wrong With Setting Up The User Directory','Vivian')
  _say('Error: [{}]'.format(E),'Server')
  exit()
############ INFORMATION PATHS ###########
def _setupActions():
 global BrainActions
 try:
  BrainActions = BrainActionsBuild()
  _say('Brain Actions Established','Vivian')
  return True
 except Exception as E2:
  _say('Something Has Gone Seriously Wrong With Brain Actions Build Please Contact Skrypt With Error Below','Vivian')
  _say('[{}]'.format(E2),'Server')
  _say('Forced To Initiate Exit Protocol.','Vivian')
  exit()
def _setupUsers():
 global USERS
 try:
  USERS = USER()
  _say('Brain Users Established','Vivian')
  return True
 except Exception as E2:
  _say('Something Has Gone Seriously Wrong With Brain Users Build Please Contact Skrypt With Error Below','Vivian')
  _say('[{}]'.format(E2),'Server')
  _say('Forced To Initiate Exit Protocol.','Vivian')
  exit()

def _createUser(i):
 global USERS
 USERS.List.append(i)
 USERS.Map[i] = dict()
 USERS.Map[i]['Client'] = True
 USERS.Map[i]['Client Type'] = BrainDefinitions[Hashcode]['Type']
 USERS.Map[i]['Client Version'] = BrainDefinition[Hashcode]['Version']
  
def _setupDefinitions():
 global BrainDefinitions
 _BRAINDEFINITIONPATH = './Memory/Information/Definitions.vnm'
 try:
  BrainDefinitions = pickle.load(open(_BRAINDEFINITIONPATH,'rb'))
  _say('Brain Definitions Established','Vivian')
  return True
 except Exception as E:
  try:
   _say('Brains Definitions Memory Cell Needed.','Vivian')
   BrainDefinitions = BrainDefinitionsBuild()
   pickle.dump(BrainDefinitions,open(_BRAINDEFINITIONPATH,'wb'))
   return True
  except Exception as E2:
   _say('Something Has Gone Seriously Wrong With Brain Definitions Build Please Contact Skrypt With Error Below','Vivian')
   _say('[{}]'.format(E2),'Server')
   _say('Forced To Initiate Exit Protocol.','Vivian')
   exit()

def _setupCommunications():
 global BrainCommunications
 _BRAINCOMMUNICATIONPATH = './Memory/Information/Communications.vnm'
 try:
  BrainCommunications = pickle.load(open(_BRAINCOMMUNICATIONPATH,'rb'))
  _say('Brain Communications Established','Vivian')
  return True
 except Exception as E:
  try:
   _say('Brains Communications Memory Cell Needed.','Vivian')
   BrainCommunications = BrainCommunicationsBuild()
   pickle.dump(BrainCommunications,open(_BRAINCOMMUNICATIONPATH,'wb'))
   return True
  except Exception as E2:
   _say('Something Has Gone Seriously Wrong With Brain Communication Build Please Contact Skrypt With Error Below','Vivian')
   _say('[{}]'.format(E2),'Server')
   _say('Forced To Initiate Exit Protocol.','Vivian')
   exit()

print('''
Usage:
`
  Server = Central()                           `
''')

class Central():

 def __init__(self):
    print('''
#################################################################################
#                                                                               #
#                                                                               #
#____   ____.__      .__                                                        #
#\   \ /   /|__|__  _|__|____    ____                                           #
# \   Y   / |  \  \/ /  \__  \  /    \                                          #
#  \     /  |  |\   /|  |/ __ \|   |  \                                         #
#   \___/   |__| \_/ |__(____  /___|  /                                         #
#                            \/     \/                                          #
#                                       v0.3.2                                  #
# C.P.S:                                                                        #
# Public Central Processing Server                                              #
# Unlicenced, Public Domain                                                     # 
#                                                                               #         
#USE AT OWN RISK!                                                               #
#################################################################################
|[Vivian]| >>: Welcome To Vivians Central Server Monitoring System.''')
    self.start_server()
    
 def check_client_auth(self, ip, hashcode):
  global USERS
  if hashcode in BrainDefinitions.ClientHashList: # List Of Usable Client Hashes Within BrainDefinitions Object.
   Req = BrainDefinitions.Map[Hashcode]  # Pulls Function From Mapping
   Act = Req._Action(digest[len(payload[0]):]) # Initiates A Function From Brain
   return Act # Returns Functions Output.
  else:
   return '|[Vivian]|>>: Unknown Input At This Time'

 def check_client_input(self, ip, digest):
    payload = digest.split(' ')
    if payload[0].lower() in BrainActions.List: # List Of Usable Actions Within BrainActions Object.
      Req = BrainActions.Map[payload[0].lower()]  # Pulls Function From Mapping
      Act = Req._Action(digest[len(payload[0]):]) # Initiates A Function From Brain
      return Act # Returns Functions Output.
    else:
     return '|[Vivian]|>>: Unknown Input At This Time'

 def grab_time(self):
  timed = time.localtime()
  return str(timed[1])+'/'+str(timed[2])+'/'+str(timed[0])+' '+str(timed[3])+':'+str(timed[4])+':'+str(timed[5])
  

 def trigger_action_log(self, user,sub,act):
  timer = self.grab_time()   
  path = './Memory/Users/'+str(user)+'_action.log'
  try:
   action = pickle.load(open(path,'rb'))
   action['Time List'].append(str(timer))
   action[str(timer)] = dict()
   if sub not in action['Sub Port List']:
    action['Sub Port List'].append(sub)
   action[str(timer)]['Actions'] = list()
   action[str(timer)]['Actions'].append(act)
  except Exception as No_User_Log:
   try:
    action = dict()
    action['Time List'] = list()
    action['Time List'].append(str(timer))
    action[str(timer)] = dict()
    action['Sub Port List'] = list()
    if sub not in action['Sub Port List']:
     action['Sub Port List'].append(sub)
    action[str(timer)]['Actions'] = list()
    action[str(timer)]['Actions'].append(act)
    pickle.dump(action,open(path,'wb'))
   except Exception as Action_Log_Error:
    _say('Error With Internal Action Log Creation. Please Inform Skrypt Of Error Below','Vivian')
    _say('Server Error: [{}]'.format(Action_Log_Error),'Server')
    _say('Initiating Exit Protocol','Vivian')
    exit()

 def internal_client_thread(self, conn, ip, port, MAX_BUFFER_SIZE = 4096):

    # the input is in bytes, so decode it
    input_from_client_bytes = conn.recv(MAX_BUFFER_SIZE)

    # MAX_BUFFER_SIZE input max
    import sys
    siz = sys.getsizeof(input_from_client_bytes)
    if siz >= MAX_BUFFER_SIZE:
     _say('The Length Of Input [{}] Is Too Long. Exceeds By [{}] Bytes.'.format(siz,int(siz)-int(MAX_BUFFER_SIZE)),'Server')
    # decode input and strip the end of line
    input_from_client = input_from_client_bytes.decode("utf8").rstrip()
    HashCheck = _HashCheck(input_from_client)
    if not HashCheck:
     res = '0xc43ck' # Sends Code For Verification Function Via Client.
     vysl = res.encode("utf8") # encode the result string
     conn.sendall(vysl)  # send it to client
    else:
     res = self.check_client_auth(ip, input_from_client)
     if res:
      _createUser(ip,input_from_client)
      _say('Client Activated','Vivian')
      conn, addr = soc.accept()
      ip, port = str(addr[0]), str(addr[1])
      _say('Accepting Connection From [IP:{}/Port:{}]'.format(ip,port),'Server')
      try:
       Thread(target=self.client_thread, args=(conn, ip, port)).start()
       _say('Vivian Unit Activated For [IP:{}/Port:{}]'.format(ip,port),'Vivian')
       res = 'Client Linked'
       vysl = res.encode("utf8")
       conn.sendall(vysl)
      except Exception as e:
       _say('Terible Error! [{}]'.format(e),'Server')
       import traceback
       _say('Return Trace Back Now.','Vivian')
       traceback.print_exc()
     else:
      _say('Unknown Client From IP [{}].'.format(ip),'Server') 
    
 def client_thread(self, conn, ip, port, MAX_BUFFER_SIZE = 4096):

    # the input is in bytes, so decode it
    input_from_client_bytes = conn.recv(MAX_BUFFER_SIZE)

    # MAX_BUFFER_SIZE input max
    import sys
    siz = sys.getsizeof(input_from_client_bytes)
    if siz >= MAX_BUFFER_SIZE:
     _say('The Length Of Input [{}] Is Too Long. Exceeds By [{}] Bytes.'.format(siz,int(siz)-int(MAX_BUFFER_SIZE)),'Server')
    # decode input and strip the end of line
    input_from_client = input_from_client_bytes.decode("utf8").rstrip()
    res = self.check_client_input(ip, input_from_client)
    _say('Input Received [{}] From Client [IP:{}/PORT:{}]'.format(res,ip,port),'Vivian')
    _say('Sending Digest [{}] To Server.'.format(input_from_client),'Vivian')
    vysl = res.encode("utf8") # encode the result string
    self.trigger_action_log(ip,port,input_from_client)
    conn.sendall(vysl)  # send it to client
    #conn.close()  # close connection? Need Update Feature.
    #print('|[Vivian]| >>: Connection ' + ip + ':' + port + " ended")
    
 def start_server(self):
    global ActionBuild

    import socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    _say('Socket created.','Server')

    try:
        soc.bind(("127.0.0.1", BIND_PORT))
        _say('Socket bind complete','Server')
    except socket.error as msg:
        import sys
        _say('Bind failed. Error: [{}]'.format(str(sys.exc_info())),'Server')
        sys.exit()

    #Start listening on socket
    soc.listen(10)
    _say('Socket now listening','Server')
    _say('Vivian Unit Awaiting Connection','Vivian')

    # for handling task in separate jobs we need threading
    from threading import Thread

    # this will make an infinite loop needed for 
    # not reseting server for every client
    while True:
     while not ActionBuild:
      ActionBuild = _setupActions()
     while not UsersBuild:
      UsersBuild = _setupUsers()
     if ip in USERS.List and USERS.Map[ip]['Client'] == True:
      conn, addr = soc.accept()
      ip, port = str(addr[0]), str(addr[1])
      _say('Accepting Connection From [IP:{}/Port:{}]'.format(ip,port),'Server')
      try:
       Thread(target=self.client_thread, args=(conn, ip, port)).start()
       _say('Vivian Unit Activated For [IP:{}/Port:{}]'.format(ip,port),'Vivian')
      except Exception as e:
       _say('Terible Error! [{}]'.format(e),'Server')
       import traceback
       _say('Return Trace Back Now.','Vivian')
       traceback.print_exc()
     else:
      _say('[{}] Needs To Be A Verified Client.'.format(ip),'Vivian')
      conn, addr = soc.accept()
      ip, port = str(addr[0]), str(addr[1])
      _say('Accepting Connection From [IP:{}/Port:{}]'.format(ip,port),'Server')
      try:
       Thread(target=self.internal_client_thread, args=(conn, ip, port)).start()
       _say('Vivian Unit Activated For [IP:{}/Port:{}]'.format(ip,port),'Vivian')
      except Exception as e:
       _say('Terible Error! [{}]'.format(e),'Server')
       import traceback
       _say('Return Trace Back Now.','Vivian')
       traceback.print_exc()
      _setupUser(ip)
    soc.close() #Quik Close?
