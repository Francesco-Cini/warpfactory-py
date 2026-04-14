from solver.utils.strcmpi import strcmpi

def change_tensor_index(input_tensor, index, metric_tensor):

    if metric_tensor is None:
        if not strcmpi(input_tensor['type'], "metric"):
            raise Exception("metric_tensor is needed as third input when changing index of non-metric tensors.")
        
    else:
        if strcmpi(metric_tensor['index'], "mixedupdown") or strcmpi(metric_tensor['index'], "mixeddownup"):
            raise Exception("Metric tensor cannot be used in mixed index.")
        
    if not (strcmpi(index_type, "mixedupdown") or strcmpi(index_type, "mixeddownup") or strcmpi(index_type, "covariant") or strcmpi(index_type, "contravariant")):
        raise Exception("Transformation selected is not allowed, use either: covariant, contravariant, mixedupdown, mixeddownup")
    
    output_tensor = input_tensor

    if strcmpi(input_tensor['type'], "metric"):
        if (strcmpi(input_tensor['index'], "covariant") and strcmpi(index_type, "contravariant")) and ()

    output_tensor["index"] = index_type

    return output_tensor