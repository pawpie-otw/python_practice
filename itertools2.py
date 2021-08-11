def get_factors(x):

    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list


print(sum(get_factors(6)))
