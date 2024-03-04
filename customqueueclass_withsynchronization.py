import threading


class CustomQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()

    def put(self, item):
        with self.lock:
            self.queue.append(item)

    def get(self):
        with self.lock:
            if self.queue:
                return self.queue.pop(0)
            else:
                return None


# Example usage:
cq = CustomQueue()


def producer():
    for i in range(5):
        cq.put(i)


def consumer():
    while True:
        item = cq.get()
        if item is not None:
            print("Consumed", item)
        else:
            break


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()
