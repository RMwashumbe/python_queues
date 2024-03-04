from queue import PriorityQueue

# Create a PriorityQueue object
pq = PriorityQueue()

# Add elements to the priority queue with priorities
pq.put((3, 'Third Priority'))
pq.put((1, 'First Priority'))
pq.put((2, 'Second Priority'))

# Get and remove elements from the priority queue
while not pq.empty():
    print(pq.get()[1]) # Gettng the second element of the tuple,which is the actual data
