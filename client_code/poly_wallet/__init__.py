from ._anvil_designer import poly_walletTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..text_entry_amount import text_entry_amount
from ..text_entry_budget import text_entry_budget
from ..share import share
import time
import anvil.http
import anvil.js
class poly_wallet(poly_walletTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)




    # Any code you write here will run when the form opens.
  def refresh_page(self):
    if get_open_form().provider is not None:
      self.poly_contract = get_open_form().poly_contract_read
      self.hedron_contract = get_open_form().hedron_contract_read
      self.days_remaining = self.poly_contract.LAST_POSSIBLE_MINTING_DAY().toNumber() - self.poly_contract.getCurrentDay().toNumber()
      self.hedron_balance = int(self.hedron_contract.balanceOf(get_open_form().address).toString())/(10**9)
      self.label_hedron_balance.text = "{:,f}".format(self.hedron_balance)
      self.raw_poly_balance = int(self.poly_contract.balanceOf(get_open_form().address).toString())
      self.poly_balance =self.raw_poly_balance/(10**9)
  
      self.label_poly_balance.text = "{:,f}".format(self.poly_balance)
      self.allowance = int(self.hedron_contract.allowance(get_open_form().address, get_open_form().POLY_CONTRACT_ADDRESS).toString())
      if self.allowance >0:
        self.label_approved_hdrn.text = "✅ {:,} HDRN Approved".format(int(self.allowance/10**9))
        self.label_approved_hdrn.visible = True
      else:
        self.label_approved_hdrn.visible = False
      data = self.get_budget_data()
      self.label_poly_supply.text = "{:,}B".format(data['POLY Minted']/(10**9))
    #self.label_budget.text = "Current Budget: {}%".format(data['Bidding Budget Percent'])
    else:
      url = ""
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
    current = self.raw_poly_balance
    #alert(["Minting: ", self.text_entry_amount.evm_input, self.text_entry_amount.input])
    if self.text_entry_amount.evm_input == 0 :
      alert('You must enter an amount greater than zero', title="No Wallet Connection Found")
      return None
    try:
      anvil.js.await_promise(get_open_form().poly_contract_write.mintPoly(self.text_entry_amount.evm_input, self.text_entry_budget.percent))
    except Exception as e:
      if 'finalizeMinting' in str(e):
        Notification('The contract is transitioning into the next part of the minting phase. Try again in a few minutes once finalizeMinting() function has been called on the contract and minting resumes.', style='warning',title='Try again').show()
      elif 'must still be ongoing' in str(e):
        Notification('The Mint Phase is over.', style='warning',title='Minting is Over').show()
      else:
        alert("MetaMask error: {}".format(str(e)), title='Transaction not Processed')
    self.button_mint_poly.enabled=False
    while current == int(self.poly_contract.balanceOf(get_open_form().address).toString()):
      time.sleep(1)

    self.button_mint_poly.enabled=True
    self.button_mint_poly.text = "Mint POLY"

    self.refresh_tbs()
    self.refresh_page()
    alert(share(),buttons=[], title='Congratulations 🎉')




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
