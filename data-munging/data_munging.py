import pandas as pd
import typing
from typing import Any


def munge(data_url: str) -> int:
    # check that there are elements in the list
    if len(data_url) == 0:
        return -1
    data = pd.read_csv(data_url)
    # print (data)
    return datadata =