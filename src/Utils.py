import os

# Load environment variables (Replit's workaround)
try:
  from pathlib import Path
  from dotenv import load_dotenv
  dotenv_path = Path(os.path.dirname(os.path.abspath(__file__)) + '/../.env')
  with open(dotenv_path, 'r'): load_dotenv(dotenv_path)
  use_dotenv = True
except: use_dotenv = False
  
# Get the environment variable value
def env(var, type = 'string'):
  if use_dotenv: value = os.getenv(var) # local .env
  else: value = os.environ[var] # replit env (secret)
  
  if value is None:
    if type == 'int': return 0
    else: return ''
    
  if type == 'int': return int(value)
  else: return str(value)

# Get a file placed in models directory
def models_path(filename, mode = 'src'):
  if mode != 'notebook':
    return os.path.dirname(os.path.abspath(__file__)) + '/../models/' + filename
  else:
    return '../models/' + filename

# Get a file placed in data directory
def data_path(filename, mode = 'src'):
  if mode != 'notebook':
    return os.path.dirname(os.path.abspath(__file__)) + '/../data/' + filename
  else:
    return '../data/' + filename

# Get a serialized response (used to padronize api responses)
def response(data = {}, success = True):
  return {
    'success': success,
    'data': data
  }