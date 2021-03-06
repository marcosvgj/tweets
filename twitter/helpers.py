import operator
import itertools
from datetime import datetime
from functools import reduce


class Singleton(type):
    """
    Singleton metaclass template
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def flat_map(function, items):
    return itertools.chain(*map(function, items))


def fill_na_dict(items):
    return {k: v for k, v in items.items() if v}