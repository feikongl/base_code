# -*- coding: utf-8 -*-


def log_do_func_succ(func, log_func):
    def wrapper(*args, **kw):
        # log_func('call %s():' % func.__name__)
        log_func(f"call {func.__name__}({args}, {kw}) successfully.")
        return func(*args, **kw)
    return wrapper
