import numpy as np

def calculate(list):
  # check if the list given has 9 elements, if not, raise ValueError
  try:
    before = np.array(list)
    arr = before.reshape(3, 3)
  except ValueError:
    raise ValueError("List must contain nine numbers.")
  # create calculations dict
  calculations = dict()
  # add key, value pairs to calculations dict
  calculations['mean'] = [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr)]
  calculations['variance'] = [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr)]
  calculations['standard deviation'] = [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr)]
  calculations['max'] = [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr)]
  calculations['min'] = [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr)]
  calculations['sum'] = [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr)]
  # return calculations dict
  return calculations
