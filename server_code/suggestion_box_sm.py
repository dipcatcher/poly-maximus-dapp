import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def save_suggestion(**data):
  app_tables.suggestion_box.add_row(**data)

@anvil.server.callable
def get_suggestions():
  return app_tables.suggestion_box.search()
  
  
