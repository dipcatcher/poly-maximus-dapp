import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.http_endpoint('/poly_logo.png')
def get_logo():
  return app_tables.logo.get(name='POLY')['logo']
