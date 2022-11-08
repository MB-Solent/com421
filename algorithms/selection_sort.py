import unsorted_data
import sys


def selection_sort(list_reference):
    for i in range(len(list_reference) - 1):
        small_number = sys.maxsize
        small_number_index = 0
        for j in range(i, len(list_reference)):
            if list_reference[j] < small_number:
                small_number = list_reference[j]
                small_number_index = j
        list_reference[small_number_index] = list_reference[i]
        list_reference[i] = small_number


def run():
    numbers = unsorted_data.random_list()
    print(numbers)
    selection_sort(numbers)
    print(numbers)


if __name__ == "__main__":
    run()
