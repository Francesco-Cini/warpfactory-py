import numpy as np

def tensor_cell_2_array(tensor):

    array_tensor = np.empty((1, 1, 1, 1, 4, 4), dtype=object)

    array_tensor[0, 0, 0, 0, :, :] = tensor['tensor']

    array_tensor = np.block(array_tensor.tolist())

    return array_tensor