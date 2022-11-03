from ._anvil_designer import text_entry_budgetTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class text_entry_budget(text_entry_budgetTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.percent = int(self.text_box_1.text)
    self.mint_poly_form = properties['mint_poly_form']
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    val = self.text_box_1.text
    
    if self.text_box_1.text in [None, "", 0]:
      self.text_box_1.role = 'outlined-error'
      Notification('You must submit a percent greater than or equal to 1%.', style='danger', title='Invalid Bid Budget Submission').show()
    elif all([val <1, val>0]):
      self.text_box_1.role = 'outlined-error'
      Notification('You must submit a percent greater than or equal to 1%.', style='danger',title='Invalid Bid Budget Submission').show()
    elif val<0:
      self.text_box_1.role = 'outlined-error'
      Notification('You must submit a percent greater than or equal to 1%.', style='danger',title='Invalid Bid Budget Submission').show()
      self.text_box_1.text = 0
      val = int(self.text_box_1.text)
      
    else:
      if float(val)>int(val):
        Notification("Only whole numbers are valid entries.", style="warning", title='Bid Budget').show()
      val = int(val)
      self.text_box_1.text=  val
      self.text_box_1.role = 'outlined'
      if val >100:
        self.text_box_1.text = 100
        val = int(self.text_box_1.text)
        Notification('Maximum Bid Budget Percent is 100%.' , title= "Maximum Bid Budget", style='warning'
                    ).show()
      #if val <0:
       # self.text_box_1.text = 0
       # self.text_box_1_change(sender=self.text_box_1)
    
    self.percent = val or 0
    self.mint_poly_form.check_entry()
   