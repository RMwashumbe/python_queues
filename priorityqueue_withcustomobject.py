import queue

class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        return self.priority < other.priority


pq = queue.PriorityQueue()

pq.put(Task(3, 'Low priority task'))
pq.put(Task(1, 'High priority task'))
pq.put(Task(2, 'Medium priority task'))

while not pq.empty():
    task = pq.get()
    print("Priority:", task.priority, "| Description:", task.description)
