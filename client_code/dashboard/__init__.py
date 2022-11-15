from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class dashboard(dashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.daily_data = app_tables.latest_day.get(name='latest')

    # Any code you write here will run when the form opens.
