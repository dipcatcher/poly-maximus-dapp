from ._anvil_designer import suggestion_boxTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class suggestion_box(suggestion_boxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

  
  def button_mint_poly_click(self, **event_args):
    try:
      rd = {}
      rd['Liquidation ID'] = self.text_box_liquidation_id.text
      rd['HSI Address'] = self.text_box_hsi_address.text
      rd['Maximum HDRN Bid Amount'] = self.text_box_bid_amount.text
      rd['Notes'] = self.text_area_notes.text
      
      message = "Suggestion Box Entry\n{}".format(str(rd))
      signature = get_open_form().signer.signMessage(message)
      
      data = {}
      data['user'] = get_open_form().address
      if get_open_form().verify_signature( message , signature ) == data['user']:
        data['raw_message'] = message
        data['signature'] = signature
        data['hsi_address'] = rd['HSI Address']
        data['liquidation_id'] = rd['Liquidation ID']
        data['max_hdrn_bid'] = rd['Maximum HDRN Bid Amount']
        data['poly_balance']=int(get_open_form().poly_contract_read.balanceOf(data['user']).toString())
        data['hdrn_balance'] = int(get_open_form().hedron_contract_read.balanceOf(data['user']).toString())
        data['water_balance']=int(get_open_form().get_contract("WATER", True).balanceOf(data['user']).toString())
        anvil.server.call('save_suggestion', **data)
        Notification('Thank you, your suggestion has been submitted.', style='Success').show()
        get_open_form().menu_click(sender=get_open_form().link_suggestion_box)
    except:
      alert("Make sure you are on a browser that supports MetaMask and make sure you are connected to the dapp.", title="Unable to Send Suggestion")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert('The Liquidation ID is a number given to each liquidation auction. It will be a number between 30 and 7000 and is used to collect data about HSI liquidations. Leave blank if this HSI liquidation auction has not started yet.', title='Liquidation ID')

  

      
    
