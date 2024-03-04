from queue import Queue

# Create a Queue object
q = Queue()

# Add elements to the queue
q.put(1)
q.put(2)
q.put(3)

# Get and remove elements from the queue
while not q.empty():
    print(q.get())
