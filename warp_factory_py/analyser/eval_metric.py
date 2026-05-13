from warp_factory_py.solver.get_energy_tensor import get_energy_tensor
from warp_factory_py.analyser.do_frame_transfer import do_frame_transfer

def eval_metric(metric, keep_positive, num_angular_vec, num_time_vec):

    if keep_positive is None:
        keep_positive = 1

    if num_angular_vec is None:
        num_angular_vec = 100

    if num_time_vec is None:
        num_time_vec = 10

    output = {}

    output['metric'] = metric

    output['energy_tensor'] = get_energy_tensor(metric)
    output['energy_tensor_eulerian'] = do_frame_transfer(metric, output['energy_tensor'], "Eulerian")

    return output