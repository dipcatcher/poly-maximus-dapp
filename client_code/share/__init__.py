from ._anvil_designer import shareTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import party
class share(shareTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    party.confetti(anvil.js.get_dom_node(self))
    t = "I just minted POLY 🅿️ \nJoin the Poly Maximus HDRN pool to bid on the best HSI HEX stakes together 👇\nhttps://poly.maximus.cash"
    text = anvil.http.url_encode(t)
    url = "https://twitter.com/intent/tweet?text={}".format(text)
    self.link_1.url = url

    # Any code you write here will run when the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event("x-close-alert", value=42)

  

    

