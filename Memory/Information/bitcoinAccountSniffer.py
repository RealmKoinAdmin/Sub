import pickle # Imports Pickle
import bitcoin # Imports Bitcoin Module (For Sha256 (Newbie Move Via Skrypt *Hashlib Is Built In))
from blocklink import * # Imports A Standard Blocklink (Modified Blockchain Module(block return from Object To Json))

# Try To Open A Pickle 'Accounts' File Creates A New One Upon Failure.
try:
 Accounts = pickle.load(open('bitcoin-accounts.vnm','rb'))
except Exception as e: # Sets Up New File
 Accounts = dict()
 Accounts['Counter'] = 0 # Sets How Many Accounts Are Collected
 Accounts['List'] = list() # Creates A List Of Accounts
 pickle.dump(Accounts,open('bitcoin-accounts.vnm','wb'))

# Try To Open A Pickle 'Transactions' File Creates A New One Upon Failure.
try:
 Transactions = pickle.load(open('btc-transaction-hashes.vnm','rb'))
except Exception as e:
 Transactions = dict()
 pickle.dump(Transactions,open('btc-transaction-hashes.vnm','wb'))

# Try To Open A Standard Program Memory File. Creates A New One Upon Failure.
try:
 AccountSnifferDB = pickle.load(open('ASDB.vnm','rb'))
except Exception as e: # Sets Up A New File
 AccountSnifferDB = dict()
 AccountSnifferDB['Count'] = 1 # Sets Count For Hash To Start On (1)
 AccountSnifferDB['Total Accounts'] = 0 # Sets How Many Accounts Total
 AccountSnifferDB['Total Bitcoin Circulated'] = 0.0 # Sets How Much Bitcoin Has Been Circulated (Broken Needs To Be Fixed Due To Reset -5 Upon Error)
 pickle.dump(AccountSnifferDB,open('ASDB.vnm','wb'))

# Internal Function To Extract Hash File.
def _checkfile():
 CHECKFILE = 'btc-block-hashes.vnm'
 try:
  CF = pickle.load(open(CHECKFILE,'rb'))
  return CF
 except Exception as e:
  print('Error Returning CheckFile Please Inform Skrypt With Error: [{}]'.format(e))
  exit()

# Internal Function To Extract Accounts File.
def _accountsFile():
 try:
  Accounts = pickle.load(open('bitcoin-accounts.vnm','rb'))
  return Accounts
 except Exception as e:
  print('Failure To Load Bitcoin Accounts File Please Inform Skrypt Of Error: [{}]'.format(e))
  exit()

# Internal Function To Extract Transactions File.
def _transactionsFile():
 try:
  Transactions = pickle.load(open('btc-transaction-hashes.vnm','rb'))
  return Transactions
 except Exception as e:
  print('Failure To Load Bitcoin Transaction Hash File Please Inform Skrypt Of Error: [{}]'.format(e))
  exit()
BLOCKHASHES = _checkfile() # Pulls One Instance Of The Hash File.
ON = True # Flips Us On For Later 'Off' Usage? (Not Yet Implimented.)
while ON:
 try:
  AccountSnifferDB = pickle.load(open('ASDB.vnm','rb')) # Opens Program Memory Data File
  Accounts = _accountsFile() # Opens Accounts File
  Transactions = _transactionsFile() # Opens Transactions File
  if str(AccountSnifferDB['Count']) not in Transactions: # Check
   Transactions[str(AccountSnifferDB['Count'])] = list()
  if str(AccountSnifferDB['Count']) in BLOCKHASHES:
   block = blockexplorer.get_block(BLOCKHASHES[str(AccountSnifferDB['Count'])])
   if block['n_tx'] == 0:
    print('No Transactions For Block: [{}]'.format(str(AccountSnifferDB['Count'])))
   elif block['n_tx'] > 0:
    for i in block['tx']:
     if i['hash'] not in Transactions[str(AccountSnifferDB['Count'])]:
      Transactions[str(AccountSnifferDB['Count'])].append(i['hash'])
      print('Added Transaction Hash: [{}] For Block [{}]'.format(i['hash'],str(AccountSnifferDB['Count'])))
     if 'in' in i:
      if i['in'][0]['addr'] not in Accounts:
       print('Adding Account [{}]'.format(i['in'][0]['addr']))
       Accounts['Counter'] += 1
       Accounts['List'].append(i['in'][0]['addr'])
       Accounts[i['in'][0]['addr']] = dict()
       AccountSnifferDB['Total Accounts'] += 1
       AccountSnifferDB['Total Bitcoin Circulated'] += i['in'][0]['value']//1e8
      elif i['in'][0]['addr'] in Accounts:
       print('Account [{}] Already Known'.format(i['in'][0]['addr']))
       AccountSnifferDB['Total Bitcoin Circulated'] += i['in'][0]['value']//1e8
     if 'out' in i:
      if i['out'][0]['addr'] not in Accounts:
       print('Adding Account [{}]'.format(i['out'][0]['addr']))
       Accounts['Counter'] += 1
       Accounts['List'].append(i['out'][0]['addr'])
       Accounts[i['out'][0]['addr']] = dict()
       AccountSnifferDB['Total Accounts'] += 1
       AccountSnifferDB['Total Bitcoin Circulated'] += i['out'][0]['value']//1e8
      elif i['out'][0]['addr'] in Accounts:
       print('Account [{}] Already Known'.format(i['out'][0]['addr']))
       AccountSnifferDB['Total Bitcoin Circulated'] += i['out'][0]['value']//1e8
  elif str(AccountSnifferDB['Count']) not in BLOCKHASHES:
   print('We\'ve Utilized All To Date Block Hashes.')
   exit()
  AccountSnifferDB['Count'] += 1
  pickle.dump(AccountSnifferDB,open('ASDB.vnm','wb'))
  pickle.dump(Accounts,open('bitcoin-accounts.vnm','wb'))
  pickle.dump(Transactions,open('btc-transaction-hashes.vnm','wb'))
 except Exception as e:
  print('Error With Main Routine: [{}]'.format(e))
  print('Resetting AccountSnifferDB')
  AccountSnifferDB['Count'] -= 5
  pickle.dump(AccountSnifferDB,open('ASDB.vnm','wb'))
 finally:
  print('Block [{}] Cleared'.format(AccountSnifferDB['Count']-1))
  print('Total Accounts [{}]'.format(AccountSnifferDB['Total Accounts']))
  print('Total Bitcoin Circulated: [{}]'.format(AccountSnifferDB['Total Bitcoin Circulated']))
