from Memory.Bitcoin.ENIM import *
import pickle
ACT = pickle.load(open('Memory/Information/bitcoin-accounts.vnm','rb'))
try:
 LIST = pickle.load(open('Found/ENIM_Found_List.vnm','rb'))
except Exception as E:
 print('Need A New Found List File')
 LIST = list()
 pickle.dump(LIST,open('Found/ENIM_Found_List.vnm','wb'))

def update_LIST(addy):
 LIST = pickle.load(open('Found/ENIM_Found_List.vnm','rb'))
 if addy not in LIST:
  LIST.append(addy)
  pickle.dump(LIST,open('Found/ENIM_Found_List.vnm','wb'))
 else:
  print('Address: [{}] Already Known'.format(addy))

while True:
 a = ENIM_Start()
 LIST = pickle.load(open('Found/ENIM_Found_List.vnm','rb'))
 print('Processing Chunk [{}]'.format(a.Number))
 print('Checking Address Cache For Chips In Chunk [{}]'.format(a.Number))
 for obj in a.AddressCache:
  if obj in ACT['List'] and obj not in LIST:
   print('Found One! Account: [{}] Private-Key: [{}]'.format(obj,a.AddressInformationCache[obj]['Privte']))
   file = dict()
   file['Name'] = a.AddressInformationCache[obj]['Name']
   file['Private'] = a.AddressInformationCache[obj]['Private']
   file['Word'] = a.AddressInformationCache[obj]['Number']
   file['Algorithm'] = a.AddressInformationCache[obj]['Multi']
   update_LIST(a.Addy0)
   pickle.dump(file,open('Found/'+str(obj)+'.vnm','wb'))
   print('We Are Paused')
   paused = input('>>: ')
  elif obj in ACT['List'] and obj in LIST:
   try:
    file = pickle.load(open('Found/'+str(obj)+'.vnm','rb'))
    print('Address [{}] Already Known.'.format(obj))
   except Exception as e:
    print('Found One! Account: [{}] Private-Key: [{}]'.format(obj,a.AddressInformationCache[obj]['Privte']))
    file = dict()
    file['Name'] = a.AddressInformationCache[obj]['Name']
    file['Private'] = a.AddressInformationCache[obj]['Private']
    file['Word'] = a.AddressInformationCache[obj]['Number']
    file['Algorithm'] = a.AddressInformationCache[obj]['Multi']
    pickle.dump(file,open('Found/'+str(obj)+'.vnm','wb'))
    print('We Are Paused')
    paused = input('>>: ')

########## V5 Cache #####################
 print('Checking Address Cache V5 For Chips In Chunk [{}]'.format(a.Number))
 for obj in a.AddressCacheV5:
  if obj in ACT['List'] and obj not in LIST:
   print('Found One! Account: [{}] Private-Key: [{}]'.format(obj,a.AddressInformationCache[obj]['Privte']))
   file = dict()
   file['Name'] = a.AddressInformationCache[obj]['Name']
   file['Private'] = a.AddressInformationCache[obj]['Private']
   file['Word'] = a.AddressInformationCache[obj]['Number']
   file['Algorithm'] = a.AddressInformationCache[obj]['Multi']
   update_LIST(obj)
   pickle.dump(file,open('Found/'+str(obj)+'.vnm','wb'))
   print('We Are Paused')
   paused = input('>>: ')
  elif obj in ACT['List'] and obj in LIST:
   try:
    file = pickle.load(open('Found/'+str(obj)+'.vnm','rb'))
    print('Address [{}] Already Known.'.format(obj))
   except Exception as e:
    print('Found One! Account: [{}] Private-Key: [{}]'.format(obj,a.AddressInformationCache[obj]['Privte']))
    file = dict()
    file['Name'] = a.AddressInformationCache[obj]['Name']
    file['Private'] = a.AddressInformationCache[obj]['Private']
    file['Word'] = a.AddressInformationCache[obj]['Number']
    file['Algorithm'] = a.AddressInformationCache[obj]['Multi']
    pickle.dump(file,open('Found/'+str(obj)+'.vnm','wb'))
    print('We Are Paused')
    paused = input('>>: ')
 
