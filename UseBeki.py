from Memory.Bitcoin.BEKI import *
import pickle
ACT = pickle.load(open('Memory/Information/bitcoin-accounts.vnm','rb'))
try:
 LIST = pickle.load(open('Found/Found_List.vnm','rb'))
except Exception as E:
 print('Need A New Found List File')
 LIST = list()
 pickle.dump(LIST,open('Found/Found_List.vnm','wb'))

def update_LIST(addy):
 LIST = pickle.load(open('Found/Found_List.vnm','rb'))
 if addy not in LIST:
  LIST.append(addy)
  pickle.dump(LIST,open('Found/Found_List.vnm','wb'))
 else:
  print('Address: [{}] Already Known'.format(addy))

while True:
 a = BEKI_Start()
 LIST = pickle.load(open('Found/Found_List.vnm','rb'))
 print('Address Pack: [{}/{}] Private-Key: [{}] Word Used: [{}].'.format(a.Addy0,a.Addy1,a.Priv,a.Word))
 if a.Addy0 in ACT['List'] and a.Addy0 not in LIST:
  print('Found One! Account: [{}] Private-Key: [{}]'.format(a.Addy0,a.Priv))
  file = dict()
  file['Name'] = a.Addy0
  file['Private'] = a.Priv
  file['Word'] = a.Word
  file['Algorithm'] = 'SHA256/DEFAULT MAGICBYTE'
  update_LIST(a.Addy0)
  pickle.dump(file,open('Found/'+str(a.Addy0)+'.vnm','wb'))
  print('We Are Paused')
  paused = input('>>: ')
 elif a.Addy0 in ACT['List'] and a.Addy0 in LIST:
  try:
   file = pickle.load(open('Found/'+str(a.Addy0)+'.vnm','rb'))
   print('Address [{}] Already Known.'.format(a.Addy0))
  except Exception as e:
   print('Found One WE THOUGHT WE KNEW! Account: [{}] Private-Key: [{}]'.format(a.Addy0,a.Priv))
   file = dict()
   file['Name'] = a.Addy0
   file['Private'] = a.Priv
   file['Word'] = a.Word
   file['Algorithm'] = 'SHA256/DEFAULT MAGICBYTE'
   update_LIST(a.Addy0)
   pickle.dump(file,open('Found/'+str(a.Addy0)+'.vnm','wb'))
   print('We Are Paused')
   paused = input('>>: ')
 if a.Addy1 in ACT['List'] and a.Addy1 not in LIST:
  print('Found One! Account: [{}] Private-Key: [{}]'.format(a.Addy1,a.Priv))
  file = dict()
  file['Name'] = a.Addy1
  file['Private'] = a.Priv
  file['Word'] = a.Word
  file['Algorithm'] = 'SHA256/MAGICBYTE=5'
  update_LIST(a.Addy1)
  pickle.dump(file,open('Found/'+str(a.Addy1)+'.vnm','wb'))
  print('We Are Paused')
  paused = input('>>: ')
 elif a.Addy1 in ACT['List'] and a.Addy1 in LIST:
  try:
   file = pickle.load(open('Found/'+str(a.Addy1)+'.vnm','rb'))
   print('Address [{}] Already Known.'.format(a.Addy1))
  except Exception as e:
   print('Found One WE THOUGHT WE KNEW! Account: [{}] Private-Key: [{}]'.format(a.Addy1,a.Priv))
   file = dict()
   file['Name'] = a.Addy1
   file['Private'] = a.Priv
   file['Word'] = a.Word
   file['Algorithm'] = 'SHA256/MAGICBYTE=5'
   update_LIST(a.Addy1)
   pickle.dump(file,open('Found/'+str(a.Addy1)+'.vnm','wb'))
   print('We Are Paused')
   paused = input('>>: ')
 
