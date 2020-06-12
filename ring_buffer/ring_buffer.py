class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = 0


    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)

        else:
            self.storage[self.oldest] = item
            self.oldest = (self.oldest +1) % self.capacity

    def get(self):
         return self.storage