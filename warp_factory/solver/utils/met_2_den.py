import numpy as np

import c4_inv
import ricci_t
import ricci_s
import ein_t
import ein_e

def met_2_den(gl, delta):
    
    if delta is None:
        delta = np.array([1, 1, 1, 1])
    
    gu = c4_inv(gl)

    R_munu = ricci_t(gu, gl, delta)

    R = ricci_s(R_munu, gu)

    E = ein_t(R_munu, R, g1)

    energy_density = ein_e(E, gu)

    return energy_density