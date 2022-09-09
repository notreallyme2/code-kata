from functools import update_wrapper
from re import search
import typing
from typing import Any

def chop(search_value: Any, search_list: list) -> int:
    # check that there are elements in the list
    if len(search_list) == 0:
        return -1

    lower_bound = 0; upper_bound = len(search_list) - 1

    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) // 2
        value_at_midpoint = search_list[midpoint]
        # print (lower_bound, upper_bound, search_index)
        if value_at_midpoint == search_value:
            return midpoint
        elif value_at_midpoint > search_value:
            upper_bound = midpoint - 1
        elif value_at_midpoint < search_value:
            lower_bound = midpoint + 1

    return -1
