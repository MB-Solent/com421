import unsorted_data


def insertion_sort(list_reference):
    for i in range(1, len(list_reference)):
        divider_value = list_reference[i]
        j = i - 1
        while list_reference[j] > divider_value and j >= 0:
            list_reference[j+1] = list_reference[j]
            j -= 1
        list_reference[j+1] = divider_value


def run():
    numbers = unsorted_data.random_list(100, 50)
    print(numbers)
    insertion_sort(numbers)
    print(numbers)


if __name__ == "__main__":
    run()

