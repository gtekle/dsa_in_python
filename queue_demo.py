from collections import deque

class Queue:
  def __init__(self):
    self.buffer = deque()

  def enqueue(self, val):
    self.buffer.appendleft(val)

  def dequeue(self):
    return self.buffer.pop()

  def is_empty(self):
    return len(self.buffer) == 0

  def size(self):
    return len(self.buffer)


q = Queue()
q.enqueue(4)
q.enqueue(6)
q.enqueue(3)

print(q.buffer)
print(q.dequeue())
