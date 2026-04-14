def take_finite_difference_1(A, k, delta, phi_phi_flag):

    if is_gpu_array(A):
        delta = gpu_array(delta)

        s = gpu_array(A.shape)
        B = np.zeros(s, 'gpu_array')
    
    else:
        s = A.shape
        B = np.zeros(s)

    return B