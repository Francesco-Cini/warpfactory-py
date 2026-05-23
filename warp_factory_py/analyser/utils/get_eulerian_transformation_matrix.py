import numpy as np

def get_eulerian_transformation_matrix(g, coords):

    if g.ndim == 2:

        assert np.allclose(g, g.T), "g is Not Symmetric"

        factor_0 = 
        factor_1 = 
        factor_2 = 
        factor_3 = 

        M[0, 0] = 
        M[1, 0] = 
        M[2, 0] = 
        M[3, 0] = 

        M[1, 1] = 
        M[2, 1] = 
        M[3, 1] = 

        M[2, 2] = 
        M[3, 2] = 

        M[3, 3] =

    elif g.ndim == 6:

        factor_0 = 
        factor_1 = 
        factor_2 = 
        factor_3 = 

        M[]

    else:
        raise Exception("Unrecognised matrix size")
    
    if np.sum(np.isinf(M), "all"):
        raise Exception("Eulerian Transformation is Infinite - Numerical Precision Insufficient")

    if not np.isreal(M):
        raise Exception("Eulerian Transformation is imaginary - Numerical Precision Insufficient")
 
    return M