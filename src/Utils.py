import os

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