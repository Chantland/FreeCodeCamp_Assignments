import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    in_matrix = np.reshape(list, (3,3))
    calculations = {
          'mean': [np.mean(in_matrix, axis = 0), np.mean(in_matrix, axis = 1), np.mean(in_matrix)],
          'variance': [np.var(in_matrix, axis = 0), np.var(in_matrix, axis = 1), np.var(in_matrix)],
          'standard deviation': [np.std(in_matrix, axis = 0), np.std(in_matrix, axis = 1), np.std(in_matrix)],
          'max': [np.max(in_matrix, axis = 0), np.max(in_matrix, axis = 1), np.max(in_matrix)],
          'min': [np.min(in_matrix, axis = 0), np.min(in_matrix, axis = 1), np.min(in_matrix)],
          'sum': [np.sum(in_matrix, axis = 0), np.sum(in_matrix, axis = 1), np.sum(in_matrix)]
    }
    for key, value in calculations.items():
        calculations[key][0] = calculations[key][0].tolist()
        calculations[key][1] = calculations[key][1].tolist()


    # calculations = in_matrix # temporary dummy output
    return calculations


