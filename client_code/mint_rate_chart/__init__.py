from ._anvil_designer import mint_rate_chartTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class mint_rate_chart(mint_rate_chartTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    x = list(range(216))
    y = []
    '''months = ((hex_contract.currentDay() - launch_day) * ds)/(36 * ds); 
        return 369 * ds / ( 3**months * ds );'''
    for d in x:
      y.append(int(369 / (3**int(d/36)) ))

    g = go.Scatter(x=x, y=y)
    self.plot_1.config['displayModeBar'] = False
    self.plot_1.layout.title = "Current Mint Rate 41 WATER : 1 ETH"
    self.plot_1.layout.xaxis.title = "Day Since Launch"
    self.plot_1.layout.yaxis.title = "WATER per ETH"
    self.plot_1.layout.xaxis.color = "white"
    self.plot_1.layout.yaxis.color = "white"
    self.plot_1.layout.font.color = 'white'
    g.marker.color= "cyan"
    g.textfont.family = "Poppins"
  
    self.plot_1.layout.font.family = "Poppins"
    self.plot_1.layout.plot_bgcolor = 'rgba(0,0,0,0)'
    self.plot_1.layout.paper_bgcolor = 'rgba(0,0,0,0)'
    # Any code you write here will run when the form opens.
    self.plot_1.data = g