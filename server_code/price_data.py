import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http
import datetime
import Maximus_Portfolio_Tracker as api
@anvil.server.background_task
@anvil.server.callable
def get_prices():
  icsa_pool = "0x3aaf77ba7da262e34dffb9b10fc6777bfda79ab7"
  hdrn_pool = "0xe859041c9c6d70177f83de991b9d757e13cea26e"
  poly_hex_pool = "0x1c1cb0F537A7FCd0a1A99fb8A54Ae21B5d1F1Fd2"
  hex_usdc_pool  = "0x69d91b94f0aaf8e8a2586909fa77a5c2c89818d5"
  print('urls')
  icsa_prices = api.api.get_pool_prices(icsa_pool)
  hdrn_prices = api.api.get_pool_prices(hdrn_pool)
  poly_prices = api.api.get_pool_prices(poly_hex_pool)
  hex_prices = api.api.get_pool_prices(hex_usdc_pool)
  all_prices = {}
  for a in [icsa_prices, hdrn_prices, poly_prices, hex_prices]:
    for k,v in a.items():
      all_prices[k]=v
  print(all_prices)
  app_tables.recent_prices.get(name='prices').update(price_data=all_prices, timestamp=datetime.datetime.utcnow())
  