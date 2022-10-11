class Queue:
    def __init__(self, capacity=5):
        self.internal_array = [None] * capacity

        self.queue_start = 0
        self.queue_end = 0
        self.size = 0

    def add(self, item):

        if self.size == len(self.internal_array):
            print("Queue is full, cannot add more.")

        else:
            self.internal_array[self.queue_end] = item

            self.size += 1

            self.queue_end += 1

            if self.queue_end >= len(self.internal_array):
                self.queue_end = 0

    def remove(self, amount):

        # index to start looping through the internal array from
        if self.size != 0:

            # Limit amount to remove to a max of the current size
            if amount > self.size:
                amount = self.size

            # Set the starting point to loop through the queue
            index = self.queue_start

            for count in range(amount):

                # remove the item from the queue and decrease size
                self.internal_array[index] = None
                self.size -= 1

                # go to next index, if out of the array size, go back to start.
                index += 1
                if index >= len(self.internal_array):
                    index = 0

        else:
            print("Can't remove from queue, it's currently empty.")

    def __str__(self):
        return self.internal_array.__str__()


printer_queue = Queue(6)

print(printer_queue)

print(printer_queue.size)

printer_queue.add("jpg")

print(printer_queue.size)

print(printer_queue)