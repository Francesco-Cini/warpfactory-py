from datetime import datetime 

from verify_tensor import verify_tensor
from solver.utils.strcmpi import strcmpi
from analyser.utils import change_tensor_index
from utils import met_2_den

def get_energy_tensor(metric, try_gpu, diff_order):

    if try_gpu is None:
        try_gpu = 0

    if diff_order is None:
        diff_order = 'fourth'
    
    if not verify_tensor(metric, 1): 
        raise Exception("Metric is not verified. Please verify metric using verify_tensor(metric).")
    
    if not strcmpi(metric['index'], "covariant"):
        metric = change_tensor_index(metric, "covariant")
        print()

    if try_gpu:
        metric_tensor_gpu =  [[None for _ in range(4)] for _ in range(4)]
    
        for i in range(4):
            for j in range(4):
                metric_tensor_gpu[i][j] = gpu_array(metric['tensor'][i][j])

        metric['scaling'] = gpu_array(metric['scaling'])
        if strcmpi(diff_order, 'fourth'):
            en_den_gpu = met_2_den(metric_tensor_gpu, metric['scaling'])
        
        elif strcmpi(diff_order, 'second'):
            en_den_gpu = met_2_den(metric_tensor_gpu, metric['scaling'])

        else:
            raise Exception("Order Flag Not Specified Correctly. Options: 'fourth' or 'second'")
        
        energy_tensor = [[None for _ in range(4)] for _ in range(4)]
        
        for i in range(4):
            for j in range(4):
                energy_tensor[i][j] = gather(en_den_gpu[i][j])
    
    else:
        if strcmpi(diff_order, 'fourth'):
            energy_tensor = met_2_den(metric['tensor'], metric['scaling'])

        elif strcmpi(diff_order, 'second'):
            energy_tensor = met_2_den_2(metric['tensor'], metric['scaling'])

        else:
            raise Exception("Order Flag Not Specified Correctly. Options: 'fourth' or 'second'")
        
    energy = {}
        
    energy['type'] = "Stress-Energy" 
    energy['tensor'] = energy_tensor
    energy['coords'] = metric['coords']
    energy['index'] = "contravariant"
    energy['order'] = diff_order
    energy['name'] = metric['name']
    energy['date'] = datetime.now()

    return energy 