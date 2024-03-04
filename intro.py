from queue import Queue

# create a Queue object
q = Queue()

# Add elements to the queue
q.put(1)
q.put(2)
q.put(3)

# Get and remove elements from the queue
print(q.get())
print(q.get())
print(q.get())

# Check if the queue is empty
print(q.empty())
