def asarray(value):
    import torch 
    import torch_directml

    return torch.as_tensor(
        value,
        dtype=torch.float64,
        device=torch_directml.device(),
    )

def asnumpy(value):
    return value.detach().cpu().numpy()
