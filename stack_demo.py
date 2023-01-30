from collections import deque

class Stack:
  def __init__(self):
    self.container = deque()

  def push(self, value):
    self.container.append(value)

  def pop(self):
    return self.container.pop()

  def peek(self):
    return self.container[-1]

  def is_empty(self):
    return len(self.container) == 0

  def size(self):
    return len(self.container)

  def reverse_string(self, str):
    reversed_str = ""
    for ch in str:
      self.container.append(ch)
    for i in range(len(str)):
      reversed_str += self.container.pop()

    return reversed_str


s = Stack()
s.push(5)
#print(s.peek())
#s.pop()
print(s.reverse_string("We will conquer COVI-19"))

