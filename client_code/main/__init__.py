from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..mint_poly import mint_poly
import anvil.js
from .. import contract_details
from ..suggestion_box import suggestion_box
from ..mint_water import mint_water
anvil.js.report_all_exceptions(False, reraise=False)
try:
  from anvil.js.window import ethers, ethereum
  is_ethereum=True
except:
  
  is_ethereum=False

#from ..dashboard import dashboard
from ..dash_copy import dash_copy
    

class main(mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.is_ethereum = is_ethereum
    self.address=None
    if 'water' in anvil.server.get_app_origin():
      start = self.link_water
    else:
      start = self.link_mint
    if 'embed' in get_url_hash():
      '''self.clear()
      from ..dash_embed import dash_embed
      self.add_component(dash_embed())'''
      self.do_embed = True
      
    else:
      self.do_embed=False
      self.menu_click(sender=start)
    
      
  
    

    # Any code you write here will run when the form opens.

  def menu_click(self, **event_args):
    l = event_args['sender']
    self.current = l
    
    if "poly" in l.text.lower():
      self.content_panel.clear()
      mp = dash_copy()#poly_wallet()#mint_poly(main = self)
      self.content_panel.add_component(mp)
    if "water" in l.text.lower():
      self.content_panel.clear()
      mw = mint_water(main = self)
      self.content_panel.add_component(mw)
    if 'suggestion' in l.text.lower():
      #alert("This will be for passing ideas and suggestions to the Executor.")
      sb = suggestion_box()
      self.content_panel.clear()
      self.content_panel.add_component(sb)
    
  def get_contract(self, ticker, is_read):
    address, abi = contract_details.get_contract_details(ticker)
    return ethers.Contract(address, abi, self.provider if is_read else self.signer)
  def button_connect_wallet_click(self, **event_args):
    """This method is called when the button is clicked"""
    try:
      self.metamask.establish_connection()
      self.address= self.metamask.address
      self.provider= self.metamask.provider
      
      self.chain_id = self.provider.getNetwork().chainId
      self.signer=self.metamask.signer
      self.POLY_CONTRACT_ADDRESS, self.POLY_ABI = contract_details.get_contract_details('POLY')
      self.poly_contract_read = ethers.Contract(self.POLY_CONTRACT_ADDRESS,self.POLY_ABI,self.provider)
      self.poly_contract_write = ethers.Contract(self.POLY_CONTRACT_ADDRESS,self.POLY_ABI,self.signer)
      
      self.HEDRON_ABI = [{"inputs":[{"internalType":"address","name":"hexAddress","type":"address"},{"internalType":"uint256","name":"hexLaunch","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"spender","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"data","type":"uint256"},{"indexed":True,"internalType":"address","name":"claimant","type":"address"},{"indexed":True,"internalType":"uint40","name":"stakeId","type":"uint40"}],"name":"Claim","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"data","type":"uint256"},{"indexed":True,"internalType":"address","name":"borrower","type":"address"},{"indexed":True,"internalType":"uint40","name":"stakeId","type":"uint40"}],"name":"LoanEnd","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"data","type":"uint256"},{"indexed":True,"internalType":"address","name":"bidder","type":"address"},{"indexed":True,"internalType":"uint40","name":"stakeId","type":"uint40"},{"indexed":True,"internalType":"uint40","name":"liquidationId","type":"uint40"}],"name":"LoanLiquidateBid","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"data","type":"uint256"},{"indexed":True,"internalType":"address","name":"liquidator","type":"address"},{"indexed":True,"internalType":"uint40","name":"stakeId","type":"uint40"},{"indexed":True,"internalType":"uint40","name":"liquidationId","type":"uint40"}],"name":"LoanLiquidateExit","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"data","type":"uint256"},{"indexed":True,"internalType":"address","name":"borrower","type":"address"},{"indexed":True,"internalType":"uint40","name":"stakeId","type":"uint40"},{"indexed":True,"internalType":"uint40","name":"liquidationId","type":"uint40"}],"name":"LoanLiquidateStart","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"data","type":"uint256"},{"indexed":True,"internalType":"address","name":"borrower","type":"address"},{"indexed":True,"internalType":"uint40","name":"stakeId","type":"uint40"}],"name":"LoanPayment","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"data","type":"uint256"},{"indexed":True,"internalType":"address","name":"borrower","type":"address"},{"indexed":True,"internalType":"uint40","name":"stakeId","type":"uint40"}],"name":"LoanStart","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"data","type":"uint256"},{"indexed":True,"internalType":"address","name":"minter","type":"address"},{"indexed":True,"internalType":"uint40","name":"stakeId","type":"uint40"}],"name":"Mint","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"borrower","type":"address"},{"internalType":"uint256","name":"hsiIndex","type":"uint256"},{"internalType":"address","name":"hsiAddress","type":"address"}],"name":"calcLoanPayment","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"borrower","type":"address"},{"internalType":"uint256","name":"hsiIndex","type":"uint256"},{"internalType":"address","name":"hsiAddress","type":"address"}],"name":"calcLoanPayoff","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"hsiIndex","type":"uint256"},{"internalType":"address","name":"hsiAddress","type":"address"},{"internalType":"address","name":"hsiStarterAddress","type":"address"}],"name":"claimInstanced","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"stakeIndex","type":"uint256"},{"internalType":"uint40","name":"stakeId","type":"uint40"}],"name":"claimNative","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"currentDay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"dailyDataList","outputs":[{"internalType":"uint72","name":"dayMintedTotal","type":"uint72"},{"internalType":"uint72","name":"dayLoanedTotal","type":"uint72"},{"internalType":"uint72","name":"dayBurntTotal","type":"uint72"},{"internalType":"uint32","name":"dayInterestRate","type":"uint32"},{"internalType":"uint8","name":"dayMintMultiplier","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"hsim","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"liquidationList","outputs":[{"internalType":"uint256","name":"liquidationStart","type":"uint256"},{"internalType":"address","name":"hsiAddress","type":"address"},{"internalType":"uint96","name":"bidAmount","type":"uint96"},{"internalType":"address","name":"liquidator","type":"address"},{"internalType":"uint88","name":"endOffset","type":"uint88"},{"internalType":"bool","name":"isActive","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"hsiIndex","type":"uint256"},{"internalType":"address","name":"hsiAddress","type":"address"}],"name":"loanInstanced","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"hsiIndex","type":"uint256"},{"internalType":"address","name":"hsiAddress","type":"address"}],"name":"loanLiquidate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"liquidationId","type":"uint256"},{"internalType":"uint256","name":"liquidationBid","type":"uint256"}],"name":"loanLiquidateBid","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"hsiIndex","type":"uint256"},{"internalType":"uint256","name":"liquidationId","type":"uint256"}],"name":"loanLiquidateExit","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"hsiIndex","type":"uint256"},{"internalType":"address","name":"hsiAddress","type":"address"}],"name":"loanPayment","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"hsiIndex","type":"uint256"},{"internalType":"address","name":"hsiAddress","type":"address"}],"name":"loanPayoff","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"loanedSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"hsiIndex","type":"uint256"},{"internalType":"address","name":"hsiAddress","type":"address"}],"name":"mintInstanced","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"stakeIndex","type":"uint256"},{"internalType":"uint40","name":"stakeId","type":"uint40"}],"name":"mintNative","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"proofOfBenevolence","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"shareList","outputs":[{"components":[{"internalType":"uint40","name":"stakeId","type":"uint40"},{"internalType":"uint72","name":"stakeShares","type":"uint72"},{"internalType":"uint16","name":"lockedDay","type":"uint16"},{"internalType":"uint16","name":"stakedDays","type":"uint16"}],"internalType":"struct HEXStakeMinimal","name":"stake","type":"tuple"},{"internalType":"uint16","name":"mintedDays","type":"uint16"},{"internalType":"uint8","name":"launchBonus","type":"uint8"},{"internalType":"uint16","name":"loanStart","type":"uint16"},{"internalType":"uint16","name":"loanedDays","type":"uint16"},{"internalType":"uint32","name":"interestRate","type":"uint32"},{"internalType":"uint8","name":"paymentsMade","type":"uint8"},{"internalType":"bool","name":"isLoaned","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]
      self.HEDRON_CONTRACT_ADDRESS = "0x3819f64f282bf135d62168C1e513280dAF905e06"
      self.hedron_contract_read = ethers.Contract(self.HEDRON_CONTRACT_ADDRESS,self.HEDRON_ABI,self.provider)
      self.hedron_contract_write = ethers.Contract(self.HEDRON_CONTRACT_ADDRESS,self.HEDRON_ABI,self.signer)
      
      
      self.menu_click(sender=self.current)
      self.button_connect_wallet.remove_from_parent()
      a = self.address[:4]
      b = self.address[-4:]
      self.button_connect_wallet.text = "{}...{}".format(a,b)
      self.column_panel_corner.add_component(self.button_connect_wallet)
      self.button_connect_wallet.background = "#1B1D26"
      self.column_panel_connect.clear()
    except Exception as e:
      
      if "object Object" in str(e):
        text = "Make sure you are on the correct network and that you succesfully connected your account with this website in the MetaMask prompt."
      else:
        text = "Unable to connect. Make sure you are on an ethereum enabled web-browser connected to MetaMask. Error Message: {}".format(e)
      raise e
      alert(text)
  

     
  def verify_signature(self, message, signature):
    return ethers.utils.verifyMessage( message , signature )

  def getCurrentDay(self):
    return self.poly_contract_read.getCurrentDay().toNumber()

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if self.do_embed:
      open_form('dash_embed')


  
