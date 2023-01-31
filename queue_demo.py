from collections import deque

q = deque()

q.appendleft(5)
q.appendleft(8)
q.appendleft(27)

print(q)
print(q.pop())
