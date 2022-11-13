import random


def bubble_sort(list_reference):
    for i in range(len(list_reference) - 1):
        for j in range(len(list_reference) - 1 - i):
            if list_reference[j] > list_reference[j+1]:
                temp = list_reference[j]
                list_reference[j] = list_reference[j + 1]
                list_reference[j + 1] = temp


def run():
    numbers = random.sample(range(1, 20), 5)

    print(numbers)

    bubble_sort(numbers)

    print(numbers)


if __name__ == "__main__":
    run()




