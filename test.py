from sx_code import funny

funny.funny("aaaa")


from sx_code.log import log_do_func_succ


@log_do_func_succ(print)
def add(x, y):
    print(x + y)

    add(1,2)


if __name__ == '__main__':
    add(1, 2)
