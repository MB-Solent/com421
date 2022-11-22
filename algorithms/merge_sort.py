import math


def merge(list_a, list_b):

    counter_a = 0
    counter_b = 0

    sorted_list = []

    while counter_a < len(list_a) and counter_b < len(list_b):

        if list_a[counter_a] < list_b[counter_b]:
            sorted_list.append(list_a[counter_a])
            counter_a += 1
        elif list_b[counter_b] < list_a[counter_a]:
            sorted_list.append(list_b[counter_b])
            counter_b += 1

    leftover_counter = 0
    leftover_list = None

    # list A is done first, put remaining items of B
    if counter_a >= len(list_a):
        leftover_counter = counter_b
        leftover_list = list_b

    # list B is done first, put remaining items of B
    elif counter_b >= len(list_b):
        leftover_counter = counter_a
        leftover_list = list_a

    if leftover_list is not None:
        for i in range(leftover_counter, len(leftover_list)):
            sorted_list.append(leftover_list[i])

    return sorted_list


def mergesort(target_list):
    if len(target_list) == 1:
        return list
    else:
        midpoint = math.floor(len(target_list)/2)

        list_a = [list[i] for i in range(midpoint)]
        list_b = [list[i] for i in range(midpoint, len(target_list))]

        list_a = mergesort(list_a)
        list_b = mergesort(list_b)

        output_list = merge(list_a, list_b)

        return output_list


test = [4, 7, 2, 5, 6, 8, 1]

a = [2,5,8]
b = [1,3,4]

print(mergesort(test))