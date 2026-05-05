import numpy as np
from datetime import date as _date

from warp_factory_py.metrics.set_minkowski_three_plus_one import set_minkowski_three_plus_one

def metric_get_lentz(grid_size, world_centre, v, scale, grid_scale):

    if scale is None:
        scale = np.max(grid_size[1:4] / 7)

    if grid_scale is None:
        grid_scale = np.array([1, 1, 1, 1])

    metric = {}

    metric['params'] = {}

    metric['params']['grid_size'] = grid_size
    metric['params']['world_centre'] = world_centre
    metric['params']['velocity'] = v 

    metric['type'] = "metric"
    metric['name'] = "Lentz"
    metric['scaling'] = grid_scale 
    metric['coords'] = "cartesian"
    metric['index'] = "covariant"
    metric['date'] = _date.today().isoformat()

    alpha, beta, gamma = set_minkowski_three_plus_one(grid_size)

    for i in range(grid_size[1]):
        for j in range(grid_size[2]):
            for k in range(grid_size[3]):

                x = i * grid_scale[1] - world_centre[1]
                y = j * grid_scale[2] - world_centre[2]
                
                for t in range(grid_size[0]):

                    xs = (t * grid_scale[0])

    return metric 