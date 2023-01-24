class Node:
 def __init__(self, data=None, next=None):
  self.data = data
  self.next = next


class LinkedList:
  def __init__(self):
   self.head = None

  def insert_at_begining(self, data):
   self.head = Node(data, self.head)

  def insert_at_end(self, data):
   itr = self.head
   while itr.next:
     itr = itr.next
   itr.next = Node(data)

  def insert_at_index(self, data, index):
   count = 0
   itr = self.head
   while itr:
    if count == index - 1:
      new_node = Node(data, itr.next)
      itr.next = new_node
      break
    itr = itr.next
    count += 1

  def print_ll(self):
   itr = self.head
   while itr:
     print(f"{itr.data} -->")
     itr = itr.next


ll = LinkedList()
ll.insert_at_begining(34)
ll.insert_at_begining(21)
#ll.print_ll()
ll.insert_at_end(12)
ll.insert_at_end(50)
ll.insert_at_begining(10)
ll.insert_at_index(20, 2)
ll.insert_at_index(60, 4)
ll.print_ll()
