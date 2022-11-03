from ._anvil_designer import text_entry_amount_ethTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class text_entry_amount_eth(text_entry_amount_ethTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.input = 0
    self.evm_input = 0
    self.mint_poly_form = properties['mint_poly_form']
    self.ticker = 'ETH'
    self.label_1.text = self.ticker


    # Any code you write here will run when the form opens.



  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""

    self.input = self.text_box_1.text

    if self.input in [None, "", 0]:
      self.input = 0
      self.evm_input = 0
      self.text_box_1.role = 'outlined-error'
      Notification("{} amount must be greater than 0".format(self.ticker), title="Invalid {} Amount".format(self.ticker), style="danger").show()

    else:
      if self.input <0:
        self.input = 0
        self.text_box_1.text = 0
        self.text_box_1.role = 'outlined-error'
        Notification("{} amount must be greater than 0".format(self.ticker), title="Invalid {} Amount".format(self.ticker), style="danger").show()
      else:
        self.text_box_1.role = 'outlined'
      self.evm_input = int(self.text_box_1.text*(10**18))
    self.mint_poly_form.check_entry()



  