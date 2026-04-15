import numpy as np

from warp_factory_py.metrics.my_custom_metric import my_custom_metric
from warp_factory_py.metrics.utils.shape_function_alcubierre import (
    shape_function_alcubierre,
)


def main():
    grid_size = np.array([1, 10, 10, 10])
    world_centre = (grid_size + 1) / 2
    grid_scaling = np.array([1, 1, 1, 1])

    v = 0.9
    r = 1
    R = 5
    sigma = 0.5

    alpha_function = 1.0
    beta_function = np.array(
        [-v * shape_function_alcubierre(r, R, sigma), 0.0, 0.0]
    )
    gamma_function = np.identity(3)

    metric = my_custom_metric(
        grid_size,
        world_centre,
        grid_scaling,
        alpha_function,
        beta_function,
        gamma_function,
    )

    print("Metric constructed successfully.")
    print(f"Metric name: {metric['name']}")
    print(f"Grid size: {metric['params']['grid_size']}")
    print(f"Tensor component shape: {metric['tensor'][0][0].shape}")
    print(f"g_tt sample: {metric['tensor'][0][0][0, 0, 0, 0]}")
    print(f"g_tx sample: {metric['tensor'][0][1][0, 0, 0, 0]}")

    try:
        from warp_factory_py.analyser.get_energy_conditions import get_energy_conditions
        from warp_factory_py.solver.get_energy_tensor import get_energy_tensor

        energy_tensor = get_energy_tensor(metric, try_gpu=None, diff_order=None)

        null_energy_condition = get_energy_conditions(
            energy_tensor,
            metric,
            "Null",
            num_angular_vec=None,
            num_time_vec=None,
            return_vec=None,
            try_gpu=None,
        )
        weak_energy_condition = get_energy_conditions(
            energy_tensor,
            metric,
            "Weak",
            num_angular_vec=None,
            num_time_vec=None,
            return_vec=None,
            try_gpu=None,
        )
        strong_energy_condition = get_energy_conditions(
            energy_tensor,
            metric,
            "Strong",
            num_angular_vec=None,
            num_time_vec=None,
            return_vec=None,
            try_gpu=None,
        )
        dominant_energy_condition = get_energy_conditions(
            energy_tensor,
            metric,
            "Dominant",
            num_angular_vec=None,
            num_time_vec=None,
            return_vec=None,
            try_gpu=None,
        )

        print(null_energy_condition)
        print(weak_energy_condition)
        print(strong_energy_condition)
        print(dominant_energy_condition)
    except Exception as exc:
        print(f"Skipping energy-tensor analysis: {exc}")


if __name__ == "__main__":
    main()
