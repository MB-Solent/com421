class Queue:
    def __init__(self, capacity=5):

        self.internal_array = [None] * capacity
        self.queue_start = 0
        self.queue_end = 0
        self.queue_size = 0

    def add(self, *args):

        for item in args:

            # check if queue has space
            if self.queue_size < len(self.internal_array):

                # if not full, add new item at end of queue

                self.internal_array[self.queue_end] = item
                print(f"Added {item} to position {self.queue_end}")

                # increase queue size variable

                self.queue_size += 1

                # update end of queue

                self.queue_end += 1

                # wrap around queue end position

                if self.queue_end >= len(self.internal_array):

                    self.queue_end = 0

                print(f"Queue end position changed to {self.queue_end}")

            else:

                print("Not enough space to add another item.")
                break

    def remove(self, amount=1):

        # check if already empty

        for _ in range(amount):

            if self.queue_size > 0:

                print(f"Removed {self.internal_array[self.queue_start]} from position the start position {self.queue_start}")

                self.internal_array[self.queue_start] = None

                self.queue_size -= 1

                self.queue_start += 1

                if self.queue_start >= len(self.internal_array):

                    self.queue_start = 0

                print(f"The start of the queue is now at position {self.queue_start}")

            else:
                print("The queue is empty.")
                break

    def __str__(self):
        return self.internal_array.__str__()


printer_queue = Queue(6)

print(printer_queue)

print(len(printer_queue.internal_array))
print(printer_queue.queue_size)

printer_queue.add("a")
printer_queue.add("b", "c")

print(printer_queue)

printer_queue.remove(2)

print(printer_queue)

printer_queue.add("d", "e", "f", "g", "h")
print(printer_queue)

printer_queue.add("i")

printer_queue.remove(2)

print(printer_queue)
printer_queue.add("i")
printer_queue.remove(1)


