import random


def random_list(max_value, item_amount):
    return random.sample(range(1, max_value), item_amount)
