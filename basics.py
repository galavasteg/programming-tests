import typing


def raise_exception_if_called_too_many_times(max_call_count: int) -> typing.Callable:
    """
    Create decorator that count function calls and raise RuntimeError exception
    on try to call it more than *max_call_count*.

    :param max_call_count: allowed maximum number of function calls.
    :return: decorator

    >>> max_call_count = 1
    >>> do_not_call_twice = raise_exception_if_called_too_many_times(
    ...     max_call_count)(lambda: 'foo')
    >>> do_not_call_twice()
    'foo'
    >>> do_not_call_twice()
    Traceback (most recent call last):
      File ..., ..., in decorated
        raise UnboundLocalError(msg)
    RuntimeError: Maximum number of function calls exceeded: 1

    """
    def decorator(function) -> typing.Callable:
        def wrapper(*args, **kwargs):
            if wrapper.call_count == max_call_count:
                msg = 'Maximum number of function calls exceeded: {c}'.format(
                        c=max_call_count)
                raise RuntimeError(msg)

            res = function(*args, **kwargs)
            wrapper.call_count = wrapper.call_count + 1

            return res

        wrapper.call_count = 0
        return wrapper

    return decorator


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
