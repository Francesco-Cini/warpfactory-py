import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from warp_factory_py.metrics.alcubierre.metric_get_alcubierre import metric_get_alcubierre
from warp_factory_py.visualiser.utils.surf_q import surf_q

grid_size = np.array([5, 20, 20, 20])
world_centre = (grid_size + 1) / 2
velocity = 0.5
R = 5
sigma = 0.5

metric = metric_get_alcubierre(grid_size, world_centre, velocity, R, sigma)

# Plotting

fig, axs = plt.subplots(4, 4, subplot_kw={"projection": "3d"})
fig.suptitle(metric["name"])

for i in range(4):
    for j in range(4):
        ax = axs[i,j]
        surf_q(
            metric["tensor"][i][j][2, :, :, int(np.round(world_centre[3])) - 1],
            ax=ax,
            edgecolor="none",
        )
        ax.set_title(f"{i+1},{j+1}")

plt.show()

