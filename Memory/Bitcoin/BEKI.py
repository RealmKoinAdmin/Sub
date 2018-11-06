"""
BEKI.py
(Bitcoin English Keyboard Input)

Skrypt
Copyright (C) 2018 Skryptek
 

"""
print(''' Welcome To BEKI Learning Utility Please Be Patient While I Import The Following Modules And Packages.''')
################ PATH DECLARATION ###########################################
CHECKPOINT_PATH = './Memory/Information/Bitcoin/BEKI.vnm'
######################## System / Bitcoin Modules Below ################

try:
 print('Attempting To Import [os] Module.')
 import os
except Exception as bad_os_mod:
 print('Error Importing [os] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_os_mod))
 exit()
try:
 print('Attempting To Import [time] Module.')
 import time
except Exception as bad_time_mod:
 print('Error Importing [time] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_time_mod))
 exit()
try:
 print('Attempting To Import [string] Module.')
 import string
except Exception as bad_string_mod:
 print('Error Importing [string] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_string_mod))
 exit()
try:
 print('Attempting To Import [pickle] Module.')
 import pickle
except Exception as bad_pickle_mod:
 print('Error Importing [pickle] Module. Instructing Program To Exit This Is A Requirement.')
 print('Error: [{}]'.format(str(bad_pickle_mod)))
 exit()
try:
 print('Importing Bitcoin.')
 import bitcoin
except Exception as bad_bitcoin_mod:
 print('Error Importing [bitcoin] Module. Instructing Program To Exit.')
 print('Error: [{}]'.format(str(bad_bitcoin_mod)))
 exit()
print('Imports Complete')
print('Attempting To Unpickle BEKI Memory Sets.')
############ CHECKPOINT MEMORY #######################
try:
 Last_Checkpoint = pickle.load(open(CHECKPOINT_PATH,'rb'))
 print('Collected Memory From [{}]'.format(CHECKPOINT_PATH))
except Exception as E:
 print('Need To Make New [{}] Database File Just A Moment.'.format(CHECKPOINT_PATH))
 Last_Checkpoint = 0
 pickle.dump(Last_Checkpoint, open(CHECKPOINT_PATH,'wb'))
 print('[{}] Created.'.format(CHECKPOINT_PATH))
 
################ Object Section #############################################


class BEKI_Start():
 def __init__(self):
  self.Data = {'Chars': {'Menu': {'Items': list(string.printable)[:]}},'Constant Pointer': 0,
               'Digits': list(), 'Length Capacity': 46}
  self.Data['Chars']['Menu']['Item Size'] = len(self.Data['Chars']['Menu']['Items'])
  self.Data['Chars']['Current'] = self.Data['Chars']['Menu']['Items']
  self.Data['Chars']['Base'] = len(self.Data['Chars']['Menu']['Items'])
  self.Data['Chars']['Size'] =  self.Data['Chars']['Menu']['Item Size']
  self.Solved = False
  try:
   self.Starting = pickle.load(open(CHECKPOINT_PATH,'rb'))
  except Exception as LE:
   print('Starting Point Load Error! Please Inform Skrypt Of Error Below!')
   print('Error: [{}]'.format(LE))
   exit()
  self.Data['Constant Pointer'] = self.Starting
  self.generate_keyboard_data()
 
 
 def numberToBase(self, cont_pointer, char_base):
  self.Data['Digits'] = list()
  while cont_pointer:
    self.Data['Digits'].append(int(cont_pointer % char_base))
    cont_pointer /= char_base
  return self.Data['Digits'][::-1]

 def hash_calculations(self,word_used, word_size):
  self.Word = word_used[-word_size:]
  self.Priv = bitcoin.sha256(str(self.Word))
  self.Pub = bitcoin.privtopub(self.Priv)
  self.Addy0 = bitcoin.pubtoaddr(self.Pub)
  self.Addy1 = bitcoin.privkey_to_address(self.Priv, magicbyte=5)
  self.Data['Constant Pointer'] += 1
  pickle.dump(self.Data['Constant Pointer'],open(CHECKPOINT_PATH,'wb'))

 def generate_keyboard_data(self):
  try:
   if not self.Solved:
      lst = self.numberToBase(self.Data['Constant Pointer'], self.Data['Chars']['Base'])
      word = ''
      for x in lst:
       word += str(self.Data['Chars']['Current'][x])
      if self.Data['Constant Pointer'] >= 0 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 1:
       self.hash_calculations(word, 1)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 1 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 2:
       self.hash_calculations(word, 2)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 2 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 3:
       self.hash_calculations(word, 3)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 3 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 4:
       self.hash_calculations(word, 4)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 4 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 5:
       self.hash_calculations(word, 5)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 5 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 6:
       self.hash_calculations(word, 6)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 6 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 7:
       self.hash_calculations(word, 7)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 7 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 8:
       self.hash_calculations(word, 8)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 8 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 9:
       self.hash_calculations(word, 9)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 9 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 10:
       self.hash_calculations(word, 10)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 10 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 11:
       self.hash_calculations(word, 11)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 11 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 12:
       self.hash_calculations(word, 12)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 12 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 13:
       self.hash_calculations(word, 13)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 13 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 14:
       self.hash_calculations(word, 14)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 14 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 15:
       self.hash_calculations(word, 15)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 15 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 16:
       self.hash_calculations(word, 16)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 16 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 17:
       self.hash_calculations(word, 17)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 17 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 18:
       self.hash_calculations(word, 18)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 18 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 19:
       self.hash_calculations(word, 19)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 19 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 20:
       self.hash_calculations(word, 20)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 20 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 21:
       self.hash_calculations(word, 21)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 21 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 22:
       self.hash_calculations(word, 22)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 22 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 23:
       self.hash_calculations(word, 23)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 23 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 24:
       self.hash_calculations(word, 24)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 24 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 25:
       self.hash_calculations(word, 25)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 25 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 26:
       self.hash_calculations(word, 26)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 26 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 27:
       self.hash_calculations(word, 27)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 27 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 28:
       self.hash_calculations(word, 28)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 28 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 29:
       self.hash_calculations(word, 29)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 29 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 30:
       self.hash_calculations(word, 30)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 30 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 31:
       self.hash_calculations(word, 31)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 31 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 32:
       self.hash_calculations(word, 32)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 32 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 33:
       self.hash_calculations(word, 33)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 33 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 34:
       self.hash_calculations(word, 34)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 34 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 35:
       self.hash_calculations(word, 35)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 35 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 36:
       self.hash_calculations(word, 36)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 36 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 37:
       self.hash_calculations(word, 37)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 37 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 38:
       self.hash_calculations(word, 38)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 38 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 39:
       self.hash_calculations(word, 39)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 39 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 40:
       self.hash_calculations(word, 40)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 40 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 41:
       self.hash_calculations(word, 41)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 41 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 42:
       self.hash_calculations(word, 42)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 42 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 43:
       self.hash_calculations(word, 43)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 43 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 44:
       self.hash_calculations(word, 44)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 44 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 45:
       self.hash_calculations(word, 45)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 45 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 46:
       self.hash_calculations(word, 46)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 46 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 47:
       self.hash_calculations(word, 47)
      elif self.Data['Constant Pointer'] > self.Data['Chars']['Size'] ** 47 and self.Data['Constant Pointer'] <= self.Data['Chars']['Size'] ** 48:
       self.hash_calculations(word, 48)
      else:
       print('Searched Up To [{}] Characters!.'.format(self.Data['Length Capacity']))
       exit()
  except Exception as KI:
   print('Error With Generating Keyboard Data.')
   print('Error [{}]'.format(KI))
   exit()

