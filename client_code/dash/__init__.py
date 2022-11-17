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
    self.form_show()
  
    

    # Any code you write here will run when the form opens.

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    self.data = app_tables.latest_day.get(name='latest')['daily_data']
    url = "http://polyapi.anvil.app/_/api/pool_prices/{}"
    icsa_pool = "0x3aaf77ba7da262e34dffb9b10fc6777bfda79ab7"
    hdrn_pool = "0xe859041c9c6d70177f83de991b9d757e13cea26e"
    print('urls')
    icsa_prices = anvil.http.request(url.format(icsa_pool), json=True)
    hdrn_prices = anvil.http.request(url.format(hdrn_pool), json=True)
    print(hdrn_prices)
    dd = {}
    hdrn_value = hdrn_prices['USDC per HDRN'] * self.data['Total HDRN'] 
    icsa_value = icsa_pool['USDC per ICSA'] * self.data['ICSA Yield']
    
    dd['Treasury Value'] = {"c":self.custom_1 , 'content':"${:,}".format(int(hdrn_value + icsa_value))}
    dd['Total HDRN'] = {"c":self.custom_2 , 'content':"{:,}".format(int(self.data['Total HDRN']))}
    dd['Total ICSA'] = {"c":self.custom_3 , 'content':"{:,.1f}".format(self.data['ICSA Yield'])}
    dd['POLY Supply'] = {"c":self.custom_4 , 'content':"{:,}".format(int(self.data['POLY Supply']))}
    dd['HDRN Value'] = {"c":self.custom_5 , 'content':"${:,}".format(int(hdrn_value))}
    dd['ICSA Value'] = {"c":self.custom_6 , 'content':"${:,}".format(int(icsa_value))}

    for k,v in dd.items():
      print(k,v)
      v['c'].title = k
      v['c'].content = v['content']
      
    

