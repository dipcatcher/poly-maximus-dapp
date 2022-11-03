from ._anvil_designer import mint_polyTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..text_entry_amount import text_entry_amount
from ..text_entry_budget import text_entry_budget
import time
import anvil.js
class mint_poly(mint_polyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh_tbs()
  def refresh_tbs(self):
    self.text_entry_amount = text_entry_amount(mint_poly_form = self)
    self.text_entry_budget = text_entry_budget(mint_poly_form = self)
    self.column_panel_text_entry.clear()
    self.column_panel_budget_entry.clear()
    self.column_panel_text_entry.add_component(self.text_entry_amount)
    self.column_panel_budget_entry.add_component(self.text_entry_budget)
    
    
    
  def check_entry(self):
    self.entry = [self.text_entry_amount.evm_input, self.text_entry_budget.percent]
    self.valid_entry =[b>0 for b in self.entry]
    if self.valid_entry:
      self.button_mint_poly.text = "Mint {:,f} POLY".format(self.text_entry_amount.input)
    self.valid_allowance=False
    if get_open_form().address is not None:
      self.valid_allowance = self.allowance >= self.text_entry_amount.evm_input
      self.column_panel_allowance.visible = not self.valid_allowance
      self.label_allowance_prompt.text = "Poly Maximus needs your approval to interact with {:,} of your HDRN.".format(self.text_entry_amount.input)
      
      self.button_mint_poly.enabled=all([self.valid_entry, self.valid_allowance])
    
    # Any code you write here will run when the form opens.
  def refresh_page(self):
    
    self.poly_contract = get_open_form().poly_contract_read
    self.hedron_contract = get_open_form().hedron_contract_read
    self.days_remaining = self.poly_contract.MINTING_PHASE_END().toNumber() - self.poly_contract.getCurrentDay().toNumber()
    self.hedron_balance = int(self.hedron_contract.balanceOf(get_open_form().address).toString())/(10**9)
    self.label_hedron_balance.text = "{:,f}".format(self.hedron_balance)
    self.poly_balance =int(self.poly_contract.balanceOf(get_open_form().address).toString())/(10**9)
    self.label_poly_balance.text = "{:,f}".format(self.poly_balance)
    self.allowance = int(self.hedron_contract.allowance(get_open_form().address, get_open_form().POLY_CONTRACT_ADDRESS).toString())
    if self.allowance >0:
      self.label_approved_hdrn.text = "✅ {:,} HDRN Approved".format(self.allowance/10**9)
      self.label_approved_hdrn.visible = True
    else:
      self.label_approved_hdrn.visible = False
    data = self.get_budget_data()
    self.label_poly_supply.text = "{:,}B".format(data['POLY Minted']/(10**9))
    #self.label_budget.text = "Current Budget: {}%".format(data['Bidding Budget Percent'])
  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    if get_open_form().address is not None:
      self.refresh_page()
    else:
      self.get_budget_data()

  def button_approve_click(self, **event_args):
    """This method is called when the button is clicked"""
    current = self.allowance
    anvil.js.await_promise(get_open_form().hedron_contract_write.approve(get_open_form().POLY_CONTRACT_ADDRESS, self.text_entry_amount.evm_input))
    while current ==int(self.hedron_contract.allowance(get_open_form().address, get_open_form().POLY_CONTRACT_ADDRESS).toString()):
      time.sleep(1)
      self.button_approve.text = 'Approving {} HDRN'.format(self.text_entry_amount.input)
      self.button_approve.enabled = False
    self.button_approve.text = "Approve"
    self.button_approve.enabled = True
    self.column_panel_allowance.visible=False
    self.button_mint_poly.enabled=True
    self.refresh_page()

  def button_mint_poly_click(self, **event_args):
    """This method is called when the button is clicked"""
    if get_open_form().address is None:
      alert('You must sign in with MetaMask to Mint Poly', title="No Wallet Connection Found")
      return None
    current = self.poly_balance
    #alert(["Minting: ", self.text_entry_amount.evm_input, self.text_entry_amount.input])
    if self.text_entry_amount.evm_input == 0 :
      alert('You must enter an amount greater than zero', title="No Wallet Connection Found")
      return None
    anvil.js.await_promise(get_open_form().poly_contract_write.mintPoly(self.text_entry_amount.evm_input, self.text_entry_budget.percent))
    self.button_mint_poly.enabled=False
    while current == int(self.poly_contract.balanceOf(get_open_form().address).toString())/(10**9):
      time.sleep(1)
      
    self.button_mint_poly.enabled=True
    self.button_mint_poly.text = "Mint POLY"

    self.refresh_tbs()
    self.refresh_page()


  
  def get_budget_data(self):
    try:
      data = {}
      data['Bidding Budget Percent']=int(get_open_form().poly_contract_read.bidding_budget_percent().toString())
      data['POLY Minted'] = int(get_open_form().poly_contract_read.totalSupply().toString())/(10**9)
    except Exception as e:
      pass
      #print(e)
      #data = anvil.server.call('get_data')
    return data

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert("The HSI Bid Budget is the percent of the Poly Maximus Treasury HDRN that is allocated towards bidding on HSIs. This number is calculated based on the POLY minted weighted average vote of all minters. The remaining HDRN will simply be staked via the Icosa contract.", title="HSI Bid Budget")

  def link_add_token_click(self, **event_args):
    """This method is called when the link is clicked"""
    if event_args['sender'].icon == 'fa:check':
      pass
    else:
      try:
        tokenSymbol = 'POLY'
        tokenDecimals = 9
        tokenImage = app_tables.logo.get(name='POLY')['logo'].url

        from anvil.js.window import ethereum
        a = ethereum.request({
        'method': 'wallet_watchAsset',
        'params': {
          'type': 'ERC20', 
          'options': {
            'address': get_open_form().POLY_CONTRACT_ADDRESS, 
            'symbol': tokenSymbol, 
            'decimals': tokenDecimals, 
            'image': tokenImage, 
          },
        },
      })
        anvil.js.await_promise(a)
        
        event_args['sender'].icon = 'fa:check'
        event_args['sender'].text='POLY Token Added'
      except Exception as e:
        print(e)

