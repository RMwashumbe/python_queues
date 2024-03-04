class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.max_size:
            print("Queue is full. Overwriting oldest element.")
            self.front = (self.front + 1) % self.max_size
        else:
            self.size += 1
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty.")
            return None
        self.size -= 1
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size
        return item


cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
