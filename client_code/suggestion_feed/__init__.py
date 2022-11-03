from ._anvil_designer import suggestion_feedTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class suggestion_feed(suggestion_feedTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    suggestions = anvil.server.call('get_suggestions')
    self.repeating_panel_1.items = suggestions

    # Any code you write here will run when the form opens.
