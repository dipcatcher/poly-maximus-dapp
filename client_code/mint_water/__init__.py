from ._anvil_designer import mint_waterTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..text_entry_amount import text_entry_amount
from ..text_entry_budget import text_entry_budget
from ..text_entry_amount_eth import text_entry_amount_eth
from .. import contract_details
import time
import anvil.js
class mint_water(mint_waterTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh_tbs()
  def refresh_tbs(self):
    self.text_entry_amount = text_entry_amount_eth(mint_poly_form = self)
    
    self.column_panel_text_entry.clear()

    self.column_panel_text_entry.add_component(self.text_entry_amount)



  def check_entry(self):
    if get_open_form().address is None:
      Notification('You must connect to your MetaMask wallet to mint WATER.', style='warning', title='Wallet Not Connected').show()
      return False
    self.entry = [self.text_entry_amount.evm_input]
    self.valid_entry =[b>0 for b in self.entry]
    if self.valid_entry:
      self.button_mint_water.text = "Mint {:,f} WATER".format(self.text_entry_amount.input*self.global_data['Minting Rate'])

    if get_open_form().address is not None:
    
      self.button_mint_water.enabled=all([self.valid_entry])

    # Any code you write here will run when the form opens.
  def refresh_page(self):
    self.global_data = self.get_global_data()
    self.label_days_remaining.text = "Poly Water is the Poly Maximus Executor gas fee donation pool. Donate ETH to the Poly Water contract and automatically mint {} WATER tokens per ETH.".format(self.global_data['Minting Rate'])
    self.label_eth_balance.text = "{}".format(self.global_data['User Balance ETH'])
    self.label_water_balance.text = "{}".format(self.global_data['User Balance WATER'])
    self.label_water_supply.text = "{}".format(self.global_data['Total Supply'])
    #self.label_budget.text = "Current Budget: {}%".format(data['Bidding Budget Percent'])
  
  def get_global_data(self):
    self.water_contract_read = get_open_form().get_contract("WATER", True)
    
    data = {}
    data['Minting Rate'] = self.water_contract_read.current_mint_rate().toNumber()
    data['Total Supply'] = int(self.water_contract_read.totalSupply().toString())/(10**18)
    data['User Balance WATER'] = int(self.water_contract_read.balanceOf(get_open_form().address).toString())/(10**18)
    data['User Balance ETH']= float(get_open_form().provider.getBalance(get_open_form().address).toString())/(10**18)
    print(data)
    return data
  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    if get_open_form().address is not None:
      self.refresh_page()
    

  
  def button_mint_water_click(self, **event_args):
    """This method is called when the button is clicked"""
    if get_open_form().address is None:
      alert('You must sign in with MetaMask to Mint WATER', title="No Wallet Connection Found")
      return None
      
    #current = self.poly_balance
    #alert(["Minting: ", self.text_entry_amount.evm_input, self.text_entry_amount.input])
    if self.text_entry_amount.evm_input == 0 :
      alert('You must enter an amount greater than zero', title="Unable to Process")
      return None
      '''signer.sendTransaction({
    to: "ricmoo.firefly.eth",
    value: ethers.utils.parseEther("1.0")
});'''
    tx = {
    'to': contract_details.get_contract_details("WATER")[0],
    'value': self.text_entry_amount.evm_input}
    anvil.js.await_promise(get_open_form().signer.sendTransaction(tx))
    self.button_mint_water.enabled=False
    current = self.global_data['User Balance WATER']
    while current == int(self.water_contract_read.balanceOf(get_open_form().address).toString())/(10**18):
      time.sleep(1)

    self.button_mint_water.enabled=True
    self.button_mint_water.text = "Mint WATER"

    self.refresh_tbs()
    self.refresh_page()


  def link_add_token_click(self, **event_args):
    """This method is called when the link is clicked"""
    if event_args['sender'].icon == 'fa:check':
      pass
    else:
      try:
        tokenSymbol = 'WATER'
        tokenDecimals = 18
        tokenImage = app_tables.logo.get(name='WATER')['logo'].url

        from anvil.js.window import ethereum
        a = ethereum.request({
        'method': 'wallet_watchAsset',
        'params': {
          'type': 'ERC20',
          'options': {
            'address': contract_details.get_contract_details("WATER")[0],
            'symbol': tokenSymbol,
            'decimals': tokenDecimals,
            'image': tokenImage,
          },
        },
      })
        anvil.js.await_promise(a)

        event_args['sender'].icon = 'fa:check'
        event_args['sender'].text='WATER Token Added'
      except Exception as e:
        print(e)
