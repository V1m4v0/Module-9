def apply_all_func(int_list, *function):
    reuslts = {}
    for func in function:
        reuslts[func.__name__] = func(int_list)
    return reuslts

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))