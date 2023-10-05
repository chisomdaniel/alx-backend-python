#!/usr/bin/env python3
'''Complex types - string and int/float to tuple'''
from typing import List, Union, Tuple
from collections.abc import Callable


def make_multiplier(multiplier: float)-> Callable[[float], float]:
    def new(num: float) -> float:
        return num * multiplier
    
    return new

make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))
