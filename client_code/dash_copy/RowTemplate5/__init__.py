from ._anvil_designer import RowTemplate5Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate5(RowTemplate5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_date.text = self.item['Date']
    self.label_icsa_yield.text = self.item['ICSA Yield']
    self.label_total_icsa.text = self.item['Total ICSA']

    # Any code you write here will run when the form opens.
