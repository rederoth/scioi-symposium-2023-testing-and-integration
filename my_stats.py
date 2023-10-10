import pytest

def my_median(my_list):
    my_list.sort()
    # assert len(my_list) > 0, "empty data passed to my_median"
    if len(my_list) == 0:
        # pass
        raise ValueError("empty data passed to my_median")
    elif len(my_list) % 2 == 0:
        return (my_list[int(len(my_list) / 2)] + my_list[int(len(my_list) / 2) - 1]) / 2
    else:
        return my_list[int(len(my_list) / 2)]
    

def my_mean(my_list):
    raise NotImplementedError


def my_variance(my_list):
    raise NotImplementedError
