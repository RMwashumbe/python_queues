from queue import LifoQueue

# Create a LifoQueue object
stack = LifoQueue()

#Add elements to the stack
stack.put(1)
stack.put(2)
stack.put(3)

# Get and remove elements from the stack
while not stack.empty():
    print(stack.get())
    