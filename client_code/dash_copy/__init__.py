from ._anvil_designer import dash_copyTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.http
import datetime
from ..info_display import info_display
class dash_copy(dash_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.

    self.init_components(**properties)
    
    



    # Any code you write here will run when the form opens.
  def show_daily_data(self):
    all_days= app_tables.daily_data.search()
    n = 0
    display = []
    for day in all_days:
      date = datetime.date(2022, 11,14) + datetime.timedelta(days=day['Day']-261)
      
      d = {'Date': date.strftime('%m/%d')}
      d['ICSA Yield'] = "{:,.2f}".format(day['ICSA Yield'] if n==0 else day['ICSA Yield'] - latest)
      latest = day['ICSA Yield']
      n+=1
      d['Total ICSA'] = "{:,.2f}".format(day['ICSA Yield'])
      display.append(d)
    self.repeating_panel_1.items=display
    
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
    dd['Total HDRN'] = {"c":self.custom_2 , 'content':"{:,.2f} B".format(self.data['Total HDRN']/(10**9))}
    dd['Total ICSA'] = {"c":self.custom_3 , 'content':"{:,.1f}".format(self.data['ICSA Yield'])}
    dd['POLY Supply'] = {"c":self.custom_4 , 'content':"{:,.2f} B".format(self.data['POLY Supply']/(10**9))}
    dd['HDRN Value'] = {"c":self.custom_5 , 'content':"${:,}".format(int(hdrn_value))}
    dd['ICSA Value'] = {"c":self.custom_6 , 'content':"${:,}".format(int(icsa_value))}
    dd['POLY Price'] = {"c":self.custom_7, 'content':"${:.8f}".format(poly_price)}
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

    self.show_daily_data()
