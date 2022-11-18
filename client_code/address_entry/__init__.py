from ._anvil_designer import address_entryTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class address_entry(address_entryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.dashboard_form = properties['dashboard_form']

    # Any code you write here will run when the form opens.



  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""

    self.input = self.text_box_1.text

    



  def button_1_click(self, **event_args):
    a = self.dashboard_form.search(self.text_box_1.text)
    if a[0] == False:
      self.text_box_1.role = 'outlined-error'
    else:
      self.text_box_1.role = 'outlined'
    self.label_1.text = a[1]
    
