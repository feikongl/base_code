# -*- coding: utf-8 -*-
import operator
from functools import reduce


def log_do_func_succ(log_func):
    """
    a decorator to log which function execute successfully.
    :param log_func: log function
    :return:
    """
    def decorator(func):
        def wrapper(*args, **kw):
            params = list()
            if args:
                params.append(args)
            if kw:
                params.append(kw)
            tuple_param = tuple(reduce(operator.add, params))
            log_func(f"call {func.__name__}{tuple_param} successfully.")
            return func(*args, **kw)
        return wrapper
    return decorator

