import math


def binary_search(data, target):

    range_start = 0
    range_end = len(data) - 1

    while True:

        divider = math.floor((range_start + range_end) / 2)  # get midpoint between indices, round down
        # print(f"Start:{range_start}:{data[range_start]},Divider:{divider}:{data[divider]},End:{range_end}:{data[range_end]}")

        if divider == range_start and divider == range_end:
            if data[divider] != target:
                print("Target not in array.")
                break

        if target < data[divider]:
            range_end = divider - 1

        elif target > data[divider]:
            range_start = divider + 1

        else:
            print("Target found.")
            break

    # print("Target not found in data set.")


def run():
    # squares = [i*i for i in range(20)]

    squares = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

    print(squares)

    while True:

        target = None

        while target is None:
            try:
                target = int(input("Please input the number you want to search for: "))
            except ValueError:
                print("That is not a number")

        print(f"Target is {target}")

        binary_search(squares, target)


if __name__ == "__main__":
    run()
