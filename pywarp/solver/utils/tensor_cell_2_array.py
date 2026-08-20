from array_api_compat import array_namespace


def tensor_cell_2_array(tensor):

    components = tensor["tensor"]
    flat_components = tuple(
        components[i][j]
        for i in range(4)
        for j in range(4)
    )
    xp = array_namespace(*flat_components)

    rows = tuple(
        xp.stack(tuple(components[i]), axis=-1)
        for i in range(4)
    )
    return xp.stack(rows, axis=-2)
