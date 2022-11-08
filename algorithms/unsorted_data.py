import random


def random_list(max_value=20, item_amount=5):
    return random.sample(range(1, max_value), item_amount)
