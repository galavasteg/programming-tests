# 1. Write a decorator not allowing the function to be called more than
#  a certain number of times (parameter).


def raise_exception_if_called_too_many_times(function, call_count_threshold: int):
    """
    Decorator that count function calls and raise UnboundLocalError exception
    on more than *call_count_threshold* call.

    :param function: any callable function.
    :param call_count_threshold: allowed maximum number of function calls.
    :return: decorated function

    >>> threshold = 1
    >>> do_not_call_twice = raise_exception_if_called_too_many_times(
    ...     lambda: 1, threshold)
    >>> do_not_call_twice()
    1
    >>> do_not_call_twice()
    Traceback (most recent call last):
      File ..., ..., in decorated
        raise UnboundLocalError(msg)
    UnboundLocalError: Maximum number of function calls exceeded: 1

    """
    def decorated(*args, **kwargs):
        if decorated._call_count == call_count_threshold:
            msg = 'Maximum number of function calls exceeded: {c}'.format(
                    c=call_count_threshold)
            raise UnboundLocalError(msg)

        decorated._call_count = decorated._call_count + 1
        return function(*args, **kwargs)

    decorated._call_count = 0
    return decorated


# 2 INPUT: sorted array. Write func(x) -> iterable of unique

import itertools
from typing import Iterable


def get_unique_iterable(sorted_iterable: Iterable) -> Iterable:
    """
    >>> tuple(get_unique_iterable([1, 'a', 'a', 'a', 'f', 'h', 'k', 'k']))
    (1, 'a', 'f', 'h', 'k')
    """
    unique_iterator = (key for key, g in itertools.groupby(sorted_iterable, lambda v: v))
    return unique_iterator
