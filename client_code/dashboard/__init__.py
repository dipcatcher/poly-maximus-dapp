from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..address_entry import address_entry
def display_format(data, address = "Poly"):
  dd = {}
  if address =="Poly":
    dd['Entity'] = address
  else:
    dd['Entity'] = "{}...{}".format(address[0:4], address[-2:])
  for k,v in data.items():
    
    digits = len(str(int(v)))
    m = all([digits > 6, digits<=9])
    b = all([digits > 9, digits<=12])
    t = all([digits > 12])
    
    s = ""
    a =["M", "B", "T"]
    _ = [6,9,12]
    n = 0
    fv = v
    
    for l in [m,b,t]:
      if l:
        s = a[n]
        fv = v / (10**_[n])
        print(k, s)
      n+=1
   
    if any([m,b,t]): 
     
      dd[k] = "{:,.3f}{}".format(float(fv), s)
    else:
      dd[k] = "{:,.3f}".format(float(v))
  print(dd)
  return dd
class dashboard(dashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  def search(self, address):
    try:
      self.display_user_values(address)
      return (True, None)
    except Exception as e:
      return (False, str(e))
  def display_user_values(self, address):
    self.user_balance = anvil.server.call('balanceOf', "POLY", address)
    self.user_data = {}
    for k,v in self.daily_data.items():
      fv = v
      if k not in ['HDRN per POLY']:
        fv = float(v * self.user_balance / self.daily_data['POLY Supply'])
      self.user_data[k] = fv
    self.user_row = display_format(self.user_data, address)
    display = [display_format(self.daily_data), self.user_row]
    self.repeating_panel_1.items =display
    # Any code you write here will run when the form opens.

  def form_show(self, **event_args):
    self.daily_data = app_tables.latest_day.get(name='latest')['daily_data']
    self.ae = address_entry(dashboard_form = self)
    self.column_panel_2.add_component(self.ae)
    display = [display_format(self.daily_data)]
    self.repeating_panel_1.items =display
    
    self.address = get_open_form().address
    self.ae.text_box_1.text = self.address
    if self.address is None:
      pass
    else:
      self.display_user_values(self.address)

