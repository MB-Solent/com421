import math


def hoare_partition(data, start, end):
    i = start
    j = end
    pivot = math.ceil((start + end) / 2)

    pivot_value = data[pivot]

    while True:

        while data[i] < pivot_value:
            i += 1

        while data[j] > pivot_value:
            j -= 1

        if i < j:

            temp = data[i]
            data[i] = data[j]
            data[j] = temp

        else:
            return i


def quicksort(data, start=0, end=None):
    end = len(data) - 1 if (end is None) else end

    if start >= end:
        return

    pivot = hoare_partition(data, start, end)
    quicksort(data, start, pivot - 1)
    quicksort(data, pivot + 1, end)


test = [4, 7, 2, 5, 6, 8, 1]

print(test)

quicksort(test)

print(test)
