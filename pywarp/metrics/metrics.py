import numpy as np

from dataclasses import dataclass, field
from datetime import date as Date
from datetime import datetime

@dataclass
class Metric: 

    name: str
    scaling: np.ndarray
    coords: str
    index: str
    date: Date | datetime | str

    tensor: np.ndarray | list[list[np.ndarray]]

    type: str = "metric"
    params: dict[str, object] = field(default_factory=dict)


