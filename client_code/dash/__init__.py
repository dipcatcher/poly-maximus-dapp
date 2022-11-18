from ._anvil_designer import dashTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.http

from ..info_display import info_display
class dash(dashTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    
    self.init_components(**properties)
    
  
    

    # Any code you write here will run when the form opens.

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    self.data = app_tables.latest_day.get(name='latest')['daily_data']
    self.prices = app_tables.recent_prices.get(name='prices')['price_data']
    print(self.prices)
    dd = {}
    hdrn_value = float(self.prices['USDC per HDRN']) * self.data['Total HDRN'] 
    icsa_value = float(self.prices['USDC per ICSA']) * self.data['ICSA Yield']
    poly_price = float(self.prices['USDC per HDRN'])* float(self.prices['HDRN per POLY'])
    backing_value = (hdrn_value + icsa_value)/self.data['POLY Supply']
    
    dd['Treasury Value'] = {"c":self.custom_1 , 'content':"${:,}".format(int(hdrn_value + icsa_value))}
    dd['Total HDRN'] = {"c":self.custom_2 , 'content':"{:,}".format(int(self.data['Total HDRN']))}
    dd['Total ICSA'] = {"c":self.custom_3 , 'content':"{:,.1f}".format(self.data['ICSA Yield'])}
    dd['POLY Supply'] = {"c":self.custom_4 , 'content':"{:,}".format(int(self.data['POLY Supply']))}
    dd['HDRN Value'] = {"c":self.custom_5 , 'content':"${:,}".format(int(hdrn_value))}
    dd['ICSA Value'] = {"c":self.custom_6 , 'content':"${:,}".format(int(icsa_value))}
    dd['POLY Market Price'] = {"c":self.custom_7, 'content':"${:.8f}".format(poly_price)}
    dd['Backing Value'] = {"c":self.custom_8, 'content':"${:.8f}".format(backing_value)}
    if poly_price > backing_value:
      # 150 / 100
      p = (poly_price / backing_value) - 1
      d = "Premium"
    else:
      d = "Discount"
      p = (backing_value-poly_price)/backing_value
    dd['Valuation'] = {"c":self.custom_9, 'content':"{:.2f}% {}".format(100*p, d)
    }
    for k,v in dd.items():
      print(k,v)
      v['c'].title.text = k
      v['c'].content.text = v['content']
      
    

