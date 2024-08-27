my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_index = 0
my_len = len(my_list) - 1
while my_index < my_len or my_list[my_index] > 0:
    if my_list[my_index] > 0:
        print(my_list[my_index])
        my_index = my_index + 1
        if my_index <= my_len:
            continue
        else:
            break
    else:
        if my_list[my_index] == 0:
            my_index = my_index + 1
            if my_index <= my_len:
                continue
            else:
                break
        else:
            break
