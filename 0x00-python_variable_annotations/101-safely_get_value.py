#!/usr/bin/env python3
'''Duck typing - first element of a sequence'''
from typing import Any, Union, Mapping, Optional


def safely_get_value(dct: Mapping, key: Any, default: Union[Optional[Any], None] = None) -> Union[Any, Optional[Any]]:
    '''Given the parameters and the return values, add
    type annotations to the function'''
    if key in dct:
        return dct[key]
    else:
        return default



annotations = safely_get_value.__annotations__

print("Here's what the mappings should look like")
for k, v in annotations.items():
    print( ("{}: {}".format(k, v)))