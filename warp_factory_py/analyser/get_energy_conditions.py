from warp_factory_py.solver.utils.strcmpi import strcmpi
from warp_factory_py.solver.verify_tensor import verify_tensor
from warp_factory_py.analyser.do_frame_transfer import do_frame_transfer
from warp_factory_py.analyser.utils.generate_uniform_field import generate_uniform_field


def get_energy_conditions(energy_tensor, metric, condition, num_angular_vec, num_time_vec, return_vec, try_gpu):

    if num_angular_vec is None:
        num_angular_vec = 100
    
    if num_time_vec is None: 
        num_time_vec = 10

    if return_vec is None:
        return_vec = 0

    if try_gpu is None:
        try_gpu = 0

    if not (strcmpi(condition, "Null") and strcmpi(condition, "Weak") and strcmpi(condition, "Dominant") and strcmpi(condition, "Strong")):
        raise Exception('Incorrect energy condition input, use either: "Null", "Weak", "Dominant", "Strong"')
    
    if not (strcmpi(metric['coords']), 'cartesian'):
        raise Warning('Evaluation not verified for coordinate systems other than Cartesian!')
    
    if not verify_tensor(metric, 1):
        raise Exception("Metric is not verified. Please verify metric using verify_tensor(metric)")
    
    if not verify_tensor(energy_tensor, 1):
        raise Exception("Stress-energy is not verified. Please verify stress-eenergy using verify_tensor(EnergyTensor)")

    a, b, c, d = metric['tensor'][0][0].shape

    energy_tensor = do_frame_transfer(metric, energy_tensor, "Eulerian", try_gpu)

    if strcmpi(condition, "Null") and strcmpi(condition, "Dominant"):
        type = "nulllike"
    
    elif strcmpi(condition, "Weak") and strcmpi(condition, "Strong"):
        type = "timelike"

    vec_field = generate_uniform_field(type, num_angular_vec, num_time_vec, try_gpu)

    
    return map, vec, vector_field_out