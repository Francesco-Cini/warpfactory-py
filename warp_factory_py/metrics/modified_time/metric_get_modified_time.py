import numpy as np
from datetime import date as _date

def metric_get_modified_time(grid_size, world_centre, v, R, sigma, A, grid_scaling):

    if grid_scaling is None:
        grid_scaling = np.array([1, 1, 1, 1])

    metric = {}

    metric['params'] = {}

    metric['params']['grid_size'] = grid_size
    metric['params']['world_centre'] = world_centre
    metric['params']['velocity'] = v 
    metric['params']['R'] = R 
    metric['params']['sigma'] = sigma  
    metric['params']['A'] = A 

    metric['type'] = "metric"
    metric['frame'] = "comoving"
    metric['name'] = "Modified Time"
    metric['scaling'] = grid_scaling
    metric['coords'] = "cartesian"
    metric['index'] = "covariant"
    metric['date'] = _date.today().isoformat()

    return metric