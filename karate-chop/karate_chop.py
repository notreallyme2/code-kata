from functools import update_wrapper
from re import search
import typing
from typing import Any

def chop(search_value: Any, search_list: list) -> int:
    # check that there are elements in the list
    if len(search_list) == 0:
        return -1

    lower_bound = 0; upper_bound = len(search_list)
    not_found = True

    while not_found == True:
        search_index = lower_bound + (upper_bound - lower_bound) // 2
        print (lower_bound, upper_bound, search_index)
        if search_list[search_index] == search_value:
            not_found = False
            return search_index
        if search_list[search_index] > search_value:
            upper_bound = search_index - 1
        if search_list[search_index] < search_value:
            lower_bound = search_index + 1
        if lower_bound == upper_bound: #or lower_bound > upper_bound:
            not_found = False
            return -1
