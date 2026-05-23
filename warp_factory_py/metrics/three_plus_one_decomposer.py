from warp_factory_py.analyser.change_tensor_index import change_tensor_index
from warp_factory_py.solver.utils.c3_inv import c3_inv

def three_plus_one_decomposer(metric):

    metric = change_tensor_index(metric, "covariant")

    beta_down = [metric['tensor'][0][1], metric['tensor'][0][2], metric['tensor'][0][3]]

    gamma_down = [metric['tensor'][1][1], metric['tensor'][1][2], metric['tensor'][1][3], 
                  metric['tensor'][2][1], metric['tensor'][2][2], metric['tensor'][2][3], 
                  metric['tensor'][3][1], metric['tensor'][3][2], metric['tensor'][3][3]
                  ]
    
    gamma_up = c3_inv(gamma_down)


    return alpha, beta_down, gamma_down, beta_up, gamma_up