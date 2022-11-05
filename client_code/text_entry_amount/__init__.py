from ._anvil_designer import text_entry_amountTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class text_entry_amount(text_entry_amountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.input = 0
    self.evm_input = 0
    self.mint_poly_form = properties['mint_poly_form']
    

    # Any code you write here will run when the form opens.

  

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    
    self.input = self.text_box_1.text
    
    if self.input in [None, "", 0]:
      self.input = 0
      self.evm_input = 0
      self.text_box_1.role = 'outlined-error'
      Notification("HDRN amount must be greater than 0", title="Invalid HDRN Amount", style="danger").show()
      
    else:
      if self.input <0:
        self.input = 0
        self.text_box_1.text = 0
        self.text_box_1.role = 'outlined-error'
        Notification("HDRN amount must be greater than 0", title="Invalid HDRN Amount", style="danger").show()
      else:
        self.text_box_1.role = 'outlined'
      self.evm_input = int(self.text_box_1.text*(10**9))
    self.mint_poly_form.check_entry()
    
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if get_open_form().address is not None:
      #self.text_box_1.text = "{float(get_open_form().hedron_contract_read.balanceOf(get_open_form().address).toString())/(10**9)
      raw_balance = int(get_open_form().hedron_contract_read.balanceOf(get_open_form().address).toString())
      
      
      display = "{:.9f}".format(raw_balance/(10**9))
      
      self.text_box_1.text = display
      
      self.text_box_1_change(sender=self.text_box_1)
      if int(float(self.text_box_1.text*10**9)) >raw_balance:
        self.evm_input = raw_balance
    else:
      alert("Connect to MetaMask to mint POLY.")
      
      



