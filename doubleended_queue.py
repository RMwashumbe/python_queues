from collections import deque

d = deque()

d.append(1)
d.appendleft(2)
d.append(3)

while d:
    print("Pop from right:", d.pop())
    print("Pop from left:", d.popleft())
