import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables

try:
  dotenv_path = Path(
      os.path.dirname(os.path.abspath(__file__)) + '/../.env'
  )
  with open(dotenv_path, 'r'): load_dotenv(dotenv_path)
  use_dotenv = True
except:
  use_dotenv = False
  
def env(var, type = 'string'):
  if use_dotenv: 
    value = os.getenv(var) 
  else: 
    value = os.environ[var]
  
  if value is None:
    if type == 'int': 
      return 0
    else: 
      return ''
    
  if type == 'int': 
    return int(value)
  else: 
    return str(value)

def models_path(filename, mode = 'src'):
  if mode != 'notebook':
    return os.path.dirname(os.path.abspath(__file__)) + '/../models/' + filename
  else:
    return '../models/' + filename
  
def data_path(filename, mode = 'src'):
  if mode != 'notebook':
    return os.path.dirname(os.path.abspath(__file__)) + '/../data/' + filename
  else:
    return '../data/' + filename
  
def response(data = {}, success = True):
  return {
    'success': success,
    'data': data
  }