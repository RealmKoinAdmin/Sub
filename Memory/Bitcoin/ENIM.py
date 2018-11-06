"""
ENIM.py
(English Number Input Multi)

Skrypt
Copyright (C) 2018 Skryptek
 

"""
from bitcoin import sha256 as _SHA # Pulls SHA Algorithm From Skrypt's Custom Bitcoin Module
from bitcoin import privtopub as _PUB # Pulls PUBLIC KEY Algorithm From Skrypt's Custom Bitcoin Module
from bitcoin import pubtoaddr as _NAME # Pulls ADDRESS Algorithm From Skrypt's Custom Bitcoin Module
from bitcoin import privkey_to_address as _V5 # Pulls ADDRESS/MAGICBYTE=5 Algorithm From Skrypt's Custom Bitcoin Module
import pickle # Imports Pickle (Binary Databasing Utility)

# Quick Helper Function To Make Certain A Memory File Exists.
def checkMemory(where):
 try:
  Req = pickle.load(open(where,'rb')) # Utilizes Pickle To Clone Memory File To (Req)
 except Exception as E: # Excepts ANY Exception.
  print('New Memory File Needed') # Alerts User We Need To Create A New File.
  Memory = 1 # Sets A Numerical Variable.
  pickle.dump(Memory,open(where,'wb')) # Dumps Variable Within File Named From (where) Argument.
  print('Memory File Created') # Alerts The User The File Is Created.

# Quick Helper Function To Return A Full Memory File. 
def PullMemory(where):
 try:
  Req = pickle.load(open(where,'rb'))
  return Req
 except Exception as E:
  print('Error With Memory Pull')
  print('Error: [{}]'.format(E))
  exit()

# External Hash V5 Function To Return A Mock Key Incase Off Eliptical Curve

def _hashV5(seed):
 try:
  Req = _V5(seed)
  return Req
 except Exception as e:
  print('Unusable Data For V5')
  seed = '0'*63+'1' # Creates Fallback Seed.
  Req = _V5(seed)
  return Req

# External Public Key Conversion V5 Function To Return A Mock Key Incase Off Eliptical Curve

def _public(seed):
 try:
  Req = _PUB(seed)
  return Req
 except Exception as e:
  print('Unusable Data For Public Key')
  seed = '0'*63+'1' # Creates Fallback Seed.
  Req = _PUB(seed)
  return Req

# External Address Conversion V5 Function To Return A Mock Key Incase Off Eliptical Curve

def _address(pub):
 try:
  Req = _NAME(pub)
  return Req
 except Exception as e:
  print('Unusable Data For Address')
  seed = '0'*63+'1' # Creates Fallback Seed.
  PreReq = _PUB(seed) # Creates Fallback Public Key
  Req = _NAME(PreReq)
  return Req

# Quick Helper Function To Update Our Numerical Memory File.
def _updateMemory(where):
 try:
  Memory = pickle.load(open(where,'rb'))
  Memory += 1
  pickle.dump(Memory,open(where,'wb'))
 except Exception as E:
  print('Failure With Memory Update Please Investigate')
  print('Error: [{}]'.format(E))
  exit()
  
def _createKey(seed):
 padding = ['0','1','2','3','4','5','6','7','8','9',
            'a','b','c','d','e','f']
 Cache = []
 if len(seed) < 64:
  for item in padding:
   padded = seed+(item*(64-len(seed)))
   if len(padded) == 64:
    Cache.append(padded)
   else:
    print('KeyGen Broken Please Investigate')
    exit()
  return Cache
  
# Actual ENIM (English Number Input Multi) Object.
class ENIM_Start():
# Initialization Function.
 def __init__(self):
  self.MemoryPath = 'Memory/Information/Bitcoin/ENIM.vnm' # Sets Memory File Path
  checkMemory(self.MemoryPath) # Checks To Make Sure Path Exists. Creates A New One Upon Failure.
  self.StartingNumber = 1 # Starting Number For Data Multiplication.
  self.EndingNumber = 65 # Ending Number (Exceeds Reach ++1) For Data Multiplication
  self.Memory = PullMemory(self.MemoryPath) # Pulls Memory File To Memory Container.
  self.Number = self.Memory # Sets Numerical Starting Point Via Memory File
  self.cycle() # Starts Object Cycle.
# Internal Function To Update Information Cache
 def _updateInformationCache(self,address,privateKey,Number,Multi):
  #print('Updating Information Cache With Address: [{}] Number: [{}] Multi [{}]'.format(address,Number,Multi))
  if address not in self.AddressCache:
   self.AddressCache.append(address)
  if address not in self.AddressInformationCache:
   self.AddressInformationCache[address] = dict()
   self.AddressInformationCache[address]['Name'] = address
   self.AddressInformationCache[address]['Private'] = privateKey
   self.AddressInformationCache[address]['Number'] = Number
   self.AddressInformationCache[address]['Multi'] = Multi
# Internal Function To Update V5 Information Cache
 def _updateInformationCacheV5(self,address,privateKey,Number,Multi):
  #print('Updating Information Cache V5 With Address: [{}] Number: [{}] Multi [{}]'.format(address,Number,Multi))
  if address not in self.AddressCacheV5:
   self.AddressCacheV5.append(address)
  if address not in self.AddressInformationCache:
   self.AddressInformationCache[address] = dict()
   self.AddressInformationCache[address]['Name'] = address
   self.AddressInformationCache[address]['Private'] = privateKey
   self.AddressInformationCache[address]['Number'] = Number
   self.AddressInformationCache[address]['Multi'] = Multi

# @ DEV: Needs To Be Switched To External Conversions For Off Eliptical Curve Conversion
# @ DEV: _createKey Cycle Needs To Be Finished.
# Internal Cycle Function.
 def cycle(self):
  self.AddressCache = list()
  self.AddressCacheV5 = list()
  self.AddressInformationCache = dict()
  while self.StartingNumber < self.EndingNumber:
   print('Collecting Seed Banks Now')
   _SEEDBANK_ = _createKey(str(self.Number)*self.StartingNumber)
   _HEXSEEDBANK_ = _createKey(hex(self.Number)[2:]*self.StartingNumber)
   if str(self.Number)*self.StartingNumber != (str(self.Number)*self.StartingNumber)[::-1]:
    _REVERSESEEDBANK_ = _createKey(str(self.Number)[::-1]*self.StartingNumber)
   if hex(self.Number)[2:]*self.StartingNumber != (hex(self.Number)[2:]*self.StartingNumber)[::-1]:
    _REVERSEHEXSEEDBANK_ = _createKey((hex(self.Number)[2:]*self.StartingNumber)[::-1])
   if _SEEDBANK_ != []: # _createKey cycle (BROKEN/NOT FINISHED)
    for p in _SEEDBANK_:
     self._SEEDBANK_HASHED = p
     self._SEEDBANK_HASHED_a = p[::-1]
     self._SEEDBANK_HASH = _SHA(p)
     self._SEEDBANK_HASH_a = _SHA(p[::-1])
     self._SEEDBANK_PUB = _PUB(_SEEDBANK_HASH)
     self._SEEDBANK_PUB_a = _PUB(_SEEDBANK_HASH_a)
     self._SEEDBANK_PUB_b = _PUB(_SEEDBANK_HASHED)
     self._SEEDBANK_PUB_c = _PUB(_SEEDBANK_HASHED_a)
     self._SEEDBANK_ADDRESS = _NAME(_SEEDBANK_PUB)
     self._SEEDBANK_ADDRESS_a = _NAME(_SEEDBANK_PUB_a)
     self._SEEDBANK_ADDRESS_b = _NAME(_SEEDBANK_PUB_b)
     self._SEEDBANK_ADDRESS_c = _NAME(_SEEDBANK_PUB_c)
     self._SEEDBANK_ADDRESSV5 = _V5(_SEEDBANK_HASH)
     self._SEEDBANK_ADDRESSV5_a = _V5(_SEEDBANK_HASH_a)
     self._SEEDBANK_ADDRESSV5_b = _V5(_SEEDBANK_HASHED)
     self._SEEDBANK_ADDRESSV5_c = _V5(_SEEDBANK_HASHED_a)
     
     self._updateInformationCache(self._SEEDBANK_ADDRESS,self._SEEDBANK_HASH,self.Number,self.StartingNumber)
     self._updateInformationCache(self._SEEDBANK_ADDRESS_a,self._SEEDBANK_HASH_a,self.Number,self.StartingNumber)
     
   self.Hash_0 = _SHA(str(self.Number)*self.StartingNumber)
   self.Hash_1 = _SHA(hex(self.Number)*self.StartingNumber)
   self.Hash_2 = _SHA(hex(self.Number)[2:]*self.StartingNumber)

   self.Hash_0_a = _SHA(str(self.Number)[::-1]*self.StartingNumber)
   self.Hash_1_a = _SHA(hex(self.Number)[::-1]*self.StartingNumber)
   self.Hash_2_a = _SHA(hex(self.Number)[2:][::-1]*self.StartingNumber)

   self.Hash_0_b = _SHA(str(self.Number)*self.StartingNumber)[::-1]
   self.Hash_1_b = _SHA(hex(self.Number)*self.StartingNumber)[::-1]
   self.Hash_2_b = _SHA(hex(self.Number)[2:]*self.StartingNumber)[::-1]

   self.Hash_0_c = _SHA(str(self.Number)[::-1]*self.StartingNumber)[::-1]
   self.Hash_1_c = _SHA(hex(self.Number)[::-1]*self.StartingNumber)[::-1]
   self.Hash_2_c = _SHA(hex(self.Number)[2:][::-1]*self.StartingNumber)[::-1]
   
   self.Pub_0 = _PUB(self.Hash_0)
   self.Pub_1 = _PUB(self.Hash_1)
   self.Pub_2 = _PUB(self.Hash_2)
   
   self.Pub_0_a = _PUB(self.Hash_0_a)
   self.Pub_1_a = _PUB(self.Hash_1_a)
   self.Pub_2_a = _PUB(self.Hash_2_a)

   self.Pub_0_b = _PUB(self.Hash_0_b)
   self.Pub_1_b = _PUB(self.Hash_1_b)
   self.Pub_2_b = _PUB(self.Hash_2_b)

   self.Pub_0_c = _PUB(self.Hash_0_c)
   self.Pub_1_c = _PUB(self.Hash_1_c)
   self.Pub_2_c = _PUB(self.Hash_2_c)
   
   self.Address_0 = _NAME(self.Pub_0)
   self.Address_1 = _NAME(self.Pub_1)
   self.Address_2 = _NAME(self.Pub_2)
   self.AddressV5_0 = _V5(self.Hash_0, magicbyte=5)
   self.AddressV5_1 = _V5(self.Hash_1, magicbyte=5)
   self.AddressV5_2 = _V5(self.Hash_2, magicbyte=5)

   self.Address_0_a = _NAME(self.Pub_0_a)
   self.Address_1_a = _NAME(self.Pub_1_a)
   self.Address_2_a = _NAME(self.Pub_2_a)
   self.AddressV5_0_a = _V5(self.Hash_0_a, magicbyte=5)
   self.AddressV5_1_a = _V5(self.Hash_1_a, magicbyte=5)
   self.AddressV5_2_a = _V5(self.Hash_2_a, magicbyte=5)

   self.Address_0_b = _NAME(self.Pub_0_b)
   self.Address_1_b = _NAME(self.Pub_1_b)
   self.Address_2_b = _NAME(self.Pub_2_b)
   self.AddressV5_0_b = _V5(self.Hash_0_b, magicbyte=5)
   self.AddressV5_1_b = _V5(self.Hash_1_b, magicbyte=5)
   self.AddressV5_2_b = _V5(self.Hash_2_b, magicbyte=5)

   self.Address_0_c = _NAME(self.Pub_0_c)
   self.Address_1_c = _NAME(self.Pub_1_c)
   self.Address_2_c = _NAME(self.Pub_2_c)
   self.AddressV5_0_c = _V5(self.Hash_0_c, magicbyte=5)
   self.AddressV5_1_c = _V5(self.Hash_1_c, magicbyte=5)
   self.AddressV5_2_c = _V5(self.Hash_2_c, magicbyte=5)
   
   self._updateInformationCache(self.Address_0,self.Hash_0,self.Number,self.StartingNumber)
   self._updateInformationCache(self.Address_1,self.Hash_1,self.Number,self.StartingNumber)
   self._updateInformationCache(self.Address_2,self.Hash_2,self.Number,self.StartingNumber)
   self._updateInformationCacheV5(self.AddressV5_0,self.Hash_0,self.Number,self.StartingNumber)
   self._updateInformationCacheV5(self.AddressV5_1,self.Hash_1,self.Number,self.StartingNumber)
   self._updateInformationCacheV5(self.AddressV5_2,self.Hash_2,self.Number,self.StartingNumber)

   self._updateInformationCache(self.Address_0_a,self.Hash_0_a,self.Number,self.StartingNumber)
   self._updateInformationCache(self.Address_1_a,self.Hash_1_a,self.Number,self.StartingNumber)
   self._updateInformationCache(self.Address_2_a,self.Hash_2_a,self.Number,self.StartingNumber)
   self._updateInformationCacheV5(self.AddressV5_0_a,self.Hash_0_a,self.Number,self.StartingNumber)
   self._updateInformationCacheV5(self.AddressV5_1_a,self.Hash_1_a,self.Number,self.StartingNumber)
   self._updateInformationCacheV5(self.AddressV5_2_a,self.Hash_2_a,self.Number,self.StartingNumber)

   self._updateInformationCache(self.Address_0_b,self.Hash_0_b,self.Number,self.StartingNumber)
   self._updateInformationCache(self.Address_1_b,self.Hash_1_b,self.Number,self.StartingNumber)
   self._updateInformationCache(self.Address_2_b,self.Hash_2_b,self.Number,self.StartingNumber)
   self._updateInformationCacheV5(self.AddressV5_0_b,self.Hash_0_b,self.Number,self.StartingNumber)
   self._updateInformationCacheV5(self.AddressV5_1_b,self.Hash_1_b,self.Number,self.StartingNumber)
   self._updateInformationCacheV5(self.AddressV5_2_b,self.Hash_2_b,self.Number,self.StartingNumber)

   self._updateInformationCache(self.Address_0_c,self.Hash_0_c,self.Number,self.StartingNumber)
   self._updateInformationCache(self.Address_1_c,self.Hash_1_c,self.Number,self.StartingNumber)
   self._updateInformationCache(self.Address_2_c,self.Hash_2_c,self.Number,self.StartingNumber)
   self._updateInformationCacheV5(self.AddressV5_0_c,self.Hash_0_c,self.Number,self.StartingNumber)
   self._updateInformationCacheV5(self.AddressV5_1_c,self.Hash_1_c,self.Number,self.StartingNumber)
   self._updateInformationCacheV5(self.AddressV5_2_c,self.Hash_2_c,self.Number,self.StartingNumber)
   
   if len(str(self.Number)*self.StartingNumber) == 64:
    try:
     self.KeyedNumber = str(self.Number)*self.StartingNumber
     self.KeyedNumber_a = str(self.Number)[::-1]*self.StartingNumber
     self.KeyedNumber_b = (str(self.Number)*self.StartingNumber)[::-1]
     self.PubNumber = _PUB(self.KeyedNumber)
     self.PubNumber_a = _PUB(self.KeyedNumber_a)
     self.PubNumber_b = _PUB(self.KeyedNumber_b)
     self.AddrNumber = _NAME(self.PubNumber)
     self.AddrNumber_a = _NAME(self.PubNumber_a)
     self.AddrNumber_b = _NAME(self.PubNumber_b)
     self.AddrNumberV5 = _V5(self.KeyedNumber, magicbyte=5)
     self.AddrNumberV5_a = _V5(self.KeyedNumber_a, magicbyte=5)
     self.AddrNumberV5_b = _V5(self.KeyedNumber_b, magicbyte=5)
     self._updateInformationCache(self.AddrNumber,self.KeyedNumber,self.Number,self.StartingNumber)
     self._updateInformationCacheV5(self.AddrNumberV5,self.KeyedNumber,self.Number,self.StartingNumber)
     self._updateInformationCache(self.AddrNumber_a,self.KeyedNumber_a,self.Number,self.StartingNumber)
     self._updateInformationCacheV5(self.AddrNumberV5_a,self.KeyedNumber_a,self.Number,self.StartingNumber)
     self._updateInformationCache(self.AddrNumber_b,self.KeyedNumber_b,self.Number,self.StartingNumber)
     self._updateInformationCacheV5(self.AddrNumberV5_b,self.KeyedNumber_b,self.Number,self.StartingNumber)
    except Exception as Number_E:
     pass
   if len((hex(self.Number)[2:]*self.StartingNumber)) == 64:
    try:
     self.KeyedHex = hex(self.Number)[2:]*self.StartingNumber
     self.KeyedHex_a = hex(self.Number)[2:][::-1]*self.StartingNumber
     self.KeyedHex_b = (hex(self.Number)[2:]*self.StartingNumber)[::-1]
     self.HexPub = _PUB(self.KeyedHex)
     self.HexPub_a = _PUB(self.KeyedHex_a)
     self.HexPub_b = _PUB(self.KeyedHex_b)
     self.HexAddress = _NAME(self.HexPub)
     self.HexAddress_a = _NAME(self.HexPub_a)
     self.HexAddress_b = _NAME(self.HexPub_b)
     self.HexAddressV5 = _V5(self.KeyedHex, magicbyte=5)
     self.HexAddressV5_a = _V5(self.KeyedHex_a, magicbyte=5)
     self.HexAddressV5_b = _V5(self.KeyedHex_b, magicbyte=5)
     self._updateInformationCache(self.HexAddress,self.KeyedHex,self.Number,self.StartingNumber)
     self._updateInformationCacheV5(self.HexAddressV5,self.KeyedHex,self.Number,self.StartingNumber)
     self._updateInformationCache(self.HexAddress_a,self.KeyedHex_a,self.Number,self.StartingNumber)
     self._updateInformationCacheV5(self.HexAddressV5_a,self.KeyedHex_a,self.Number,self.StartingNumber)
     self._updateInformationCache(self.HexAddress_b,self.KeyedHex_b,self.Number,self.StartingNumber)
     self._updateInformationCacheV5(self.HexAddressV5_b,self.KeyedHex_b,self.Number,self.StartingNumber)
    except Exception as Hex_E:
     pass
   self.StartingNumber += 1
  _updateMemory(self.MemoryPath)
  print('Number Update Finished With Package: [{}]'.format(self.Number))

