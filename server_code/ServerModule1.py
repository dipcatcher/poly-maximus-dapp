import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

import web3
from web3 import Web3
rpc = "https://mainnet.infura.io/v3/4bc6de7e41714f5587595b1e2ce5fd31"
import anvil.http


def getw3():
  return Web3(Web3.HTTPProvider(rpc))
from . import contract_details
@anvil.server.callable
def get_data():
  POLY_ABI = [{"inputs":[{"internalType":"uint256","name":"mint_duration","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"liquidationId","type":"uint256"},{"internalType":"uint256","name":"liquidationBid","type":"uint256"}],"name":"bid","outputs":[],"stateMutability":"nonpayable","type":"function"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"liquidationId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"liquidationBid","type":"uint256"}],"name":"Bid","type":"event"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"hsiIndex","type":"uint256"},{"internalType":"address","name":"hsiAddress","type":"address"}],"name":"endHSIStake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"stakeIndex","type":"uint256"},{"internalType":"uint40","name":"stakeIdParam","type":"uint40"}],"name":"endNativeStake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"finalizeMinting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"incrementTestDay","outputs":[],"stateMutability":"nonpayable","type":"function"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Mint","type":"event"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"bid_budget_percent","type":"uint256"}],"name":"mintPoly","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"hsi_id","type":"uint256"}],"name":"processHSI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"hsi_address","type":"address"},{"indexed":False,"internalType":"uint256","name":"hsi_id","type":"uint256"}],"name":"ProcessHSI","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"hex_redeemed","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"hedron_redeemed","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"icosa_redeemed","type":"uint256"}],"name":"Redeem","type":"event"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"redeemPoly","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"restake_leftover","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"stake_leftover_hdrn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bidding_budget_percent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"BIDDING_BUDGET_TRACKER","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"supply","type":"uint256"}],"name":"calculate_redemption_rate","outputs":[{"internalType":"uint256","name":"redemption_rate","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DID_STAKE_LEFTOVER","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentDay","outputs":[{"internalType":"uint256","name":"hex_day","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"liquidation_index","type":"uint256"}],"name":"getLiquidation","outputs":[{"components":[{"internalType":"uint16","name":"mintedDays","type":"uint16"},{"internalType":"uint8","name":"launchBonus","type":"uint8"},{"internalType":"uint16","name":"loanStart","type":"uint16"},{"internalType":"uint16","name":"loanedDays","type":"uint16"},{"internalType":"uint32","name":"interestRate","type":"uint32"},{"internalType":"uint8","name":"paymentsMade","type":"uint8"},{"internalType":"bool","name":"isLoaned","type":"bool"},{"internalType":"uint256","name":"liquidationStart","type":"uint256"},{"internalType":"address","name":"hsiAddress","type":"address"},{"internalType":"uint96","name":"bidAmount","type":"uint96"},{"internalType":"address","name":"liquidator","type":"address"},{"internalType":"uint88","name":"endOffset","type":"uint88"},{"internalType":"bool","name":"isActive","type":"bool"}],"internalType":"struct PolyMaximus.LiquidationData","name":"liquidation_data","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"HDRN_STAKING_BUDGET","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"HEDRON_REDEMPTION_RATE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"HEX_REDEMPTION_RATE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"HEXStakes","outputs":[{"internalType":"uint40","name":"stakeId","type":"uint40"},{"internalType":"uint72","name":"stakedHearts","type":"uint72"},{"internalType":"uint72","name":"stakeShares","type":"uint72"},{"internalType":"uint16","name":"lockedDay","type":"uint16"},{"internalType":"uint16","name":"stakedDays","type":"uint16"},{"internalType":"uint16","name":"unlockedDay","type":"uint16"},{"internalType":"bool","name":"isAutoStake","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ICOSA_CONTRACT_ADDRESS","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ICOSA_REDEMPTION_RATE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"IS_REDEMPTION_ACTIVE","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"LAST_ACTIVE_HSI","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"LAST_STAKE_START_DAY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"LATEST_STAKE_END_DAY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINTING_PHASE_END","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINTING_PHASE_START","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"STAKING_BUDGET_TRACKER","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TEST_CURRENT_DAY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"THANK_YOU_TEAM","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TOTAL_BIDDING_BUDGET","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]
  POLY_CONTRACT_ADDRESS = "0x3215F61116126793Ba002B95E4E15A58Ee16aD58"
  w3 = getw3()
  poly_contract = w3.eth.contract(address=POLY_CONTRACT_ADDRESS, abi=POLY_ABI)
  data = {}
  data['Bidding Budget Percent']=poly_contract.functions.bidding_budget_percent().call()
  data['POLY Minted'] = poly_contract.functions.totalSupply().call()
  return data


def get_wallet(address):
  POLY_CONTRACT_ADDRESS,POLY_ABI = contract_details.get_contract_details('POLY')
  HDRN_CONTRACT_ADDRESS,HDRN_ABI = contract_details.get_contract_details('HDRN')
  w3 = getw3()
  poly_contract = w3.eth.contract(address=POLY_CONTRACT_ADDRESS, abi=POLY_ABI)
  hdrn_contract = w3.eth.contract(address=HDRN_CONTRACT_ADDRESS, abi=HDRN_ABI)
  icsa_contract = w3.eth.contract(address=ICSA_CONTRACT_ADDRESS, abi=ICSA_ABI)
  data = {}
  data['POLY Supply'] = poly_contract.functions.totalSupply().call()
  data['HDRN Balance'] = hdrn_contract.functions.balanceOf(address).call()
  data['POLY Balance'] = poly_contract.functions.balanceOf(address).call()
  
  stakeStart, capitalAdded, stakePoints, isActive , payoutPreCapitalAddIcsa, payoutPreCapitalAddHdrn, stakeAmount, minStakeLength = icsa_contract.functions.hdrnStakes(address).call()
  data['POLY Backing'] = hdrn_contract.functions.balanceOf(POLY_CONTRACT_ADDRESS).call() + stakeAmount
  data['HDRN Stake Points'] = stakePoints
  #today = icsa_contract.functions.currentDay().call()
  
  #data['ICSA Earned To Date'] = payoutPreCapitalAddIcsa + sum([stakePoints*icsa_contract.functions.hdrnPoolPayout(d).call() for d in range(capitalAdded:today) ])

@anvil.server.callable
def test():
  from_block = 16177473
  POLY_CONTRACT_ADDRESS,POLY_ABI = contract_details.get_contract_details('POLY')
  HDRN_CONTRACT_ADDRESS,HDRN_ABI = contract_details.get_contract_details('HDRN')
  ICSA_CONTRACT_ADDRESS,ICSA_ABI = contract_details.get_contract_details('ICSA')
  w3 = getw3()
  poly_contract = w3.eth.contract(address=POLY_CONTRACT_ADDRESS, abi=POLY_ABI)
  hdrn_contract = w3.eth.contract(address=HDRN_CONTRACT_ADDRESS, abi=HDRN_ABI)
  icsa_contract = w3.eth.contract(address=ICSA_CONTRACT_ADDRESS, abi=ICSA_ABI)
  today = icsa_contract.functions.currentDay().call()
  stakeStart, capitalAdded, stakePoints, isActive , payoutPreCapitalAddIcsa, payoutPreCapitalAddHdrn, stakeAmount, minStakeLength = icsa_contract.functions.hdrnStakes(POLY_CONTRACT_ADDRESS).call(None,from_block)
  print(stakePoints)
  return stakePoints
@anvil.server.callable
def resave(start, end):
  for n in range(start, end+1):
    save_treasury_value(day=n)

@anvil.server.callable
@anvil.server.background_task
def save_treasury_value(day = None):
  POLY_CONTRACT_ADDRESS,POLY_ABI = contract_details.get_contract_details('POLY')
  HDRN_CONTRACT_ADDRESS,HDRN_ABI = contract_details.get_contract_details('HDRN')
  ICSA_CONTRACT_ADDRESS,ICSA_ABI = contract_details.get_contract_details('ICSA')
  w3 = getw3()
  poly_contract = w3.eth.contract(address=POLY_CONTRACT_ADDRESS, abi=POLY_ABI)
  hdrn_contract = w3.eth.contract(address=HDRN_CONTRACT_ADDRESS, abi=HDRN_ABI)
  icsa_contract = w3.eth.contract(address=ICSA_CONTRACT_ADDRESS, abi=ICSA_ABI)
  today = icsa_contract.functions.currentDay().call()
  last_full_day = today if day is None else day
  
  data = {}
  stakeStart, capitalAdded, stakePoints, isActive , payoutPreCapitalAddIcsa, payoutPreCapitalAddHdrn, stakeAmount, minStakeLength = icsa_contract.functions.hdrnStakes(POLY_CONTRACT_ADDRESS).call()
  if last_full_day<292:
    stakePoints = 555545247999966
    
  data['Liquid HDRN'] = hdrn_contract.functions.balanceOf(POLY_CONTRACT_ADDRESS).call() / (10**9)
  data['Staked HDRN'] = stakeAmount / (10**9)
  data['Total HDRN'] = data['Liquid HDRN'] + data['Staked HDRN']
  data['Stake Points'] = stakePoints
  proportion  = stakePoints#(stakePoints/icsa_contract.functions.hdrnPoolPoints(last_full_day).call())/(10**9)
  data['ICSA Yield'] = payoutPreCapitalAddIcsa/(10**9) + (icsa_contract.functions.hdrnPoolPayout(last_full_day).call()-icsa_contract.functions.hdrnPoolPayout(capitalAdded).call())*proportion/(10**27)
  
  psraw=poly_contract.functions.totalSupply().call()
  data['POLY Supply']  = psraw / (10**9)
  data['HDRN per POLY'] = data['Total HDRN'] / data['POLY Supply']
  data['Day'] = last_full_day
  daily_data = app_tables.daily_data.add_row(**data)
  app_tables.latest_day.get(name='latest').update(daily_data=daily_data)
  return data
@anvil.server.callable
def balanceOf(token, user_address):
  user_address = Web3.toChecksumAddress(user_address)
  w3 = getw3()
  address, abi = contract_details.get_contract_details(token)
  contract = w3.eth.contract(address = address,abi=abi)
  return contract.functions.balanceOf(user_address).call() / (10**9)
  

