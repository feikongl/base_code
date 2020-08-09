# -*- coding: utf-8 -*-


def log_do_func_succ(log_func):
    def decorator(func):
        def wrapper(*args, **kw):
            log_func(f"call {func.__name__}({args}, {kw}) successfully.")
            return func(*args, **kw)
        return wrapper
    return decorator

