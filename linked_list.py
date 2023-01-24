class Node:
 def __init__(self, data=None, next=None):
  self.data = data
  self.next = next


class LinkedList:
  def __init__(self):
   self.head = None

  def insert_at_begining(self, data):
   self.head = Node(data, self.head)

  def print_ll(self):
   itr = self.head
   while itr:
     print(f"{itr.data} -->")
     itr = itr.next


ll = LinkedList()
ll.insert_at_begining(34)
ll.insert_at_begining(21)
ll.print_ll()

