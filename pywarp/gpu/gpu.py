import numpy as np


def asarray(value, *, library=None):
    if library is None or library == "numpy":
        return np.asarray(value)

    if library == "cupy":
        from .utils.cupy import asarray
        return asarray(value)

    if library == "torch-directml":
        from .utils.directml import asarray
        return asarray(value)

    raise ValueError(
        f"Unsupported array library: {library!r}. "
        "Use None, 'numpy', 'cupy', or 'torch-directml'."
    )


def asnumpy(value):
    from array_api_compat import (
        is_cupy_array,
        is_torch_array,
    )

    if is_cupy_array(value):
        from .utils.cupy import asnumpy
        return asnumpy(value)

    if is_torch_array(value):
        from .utils.directml import asnumpy
        return asnumpy(value)

    return np.asarray(value)