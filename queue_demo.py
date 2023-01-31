from collections import deque
import time
import threading

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

def place_orders(orders):
   for order in orders:
      print("Placing order for: ", order)
      q.enqueue(order)
      print(q.buffer)
      time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while True:
       order = q.dequeue()
       print("Now serving: ",order)
       time.sleep(2)

orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

place_order_thread = threading.Thread(target=place_orders, args=(orders,))
serve_order_thread = threading.Thread(target=serve_order)

place_order_thread.start()
serve_order_thread.start()
