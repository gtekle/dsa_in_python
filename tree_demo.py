class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None

  def add_child(self, child):
    child.parent = self
    self.children.append(child)

def build_product_tree():
  root = TreeNode("Electronics")

  laptop = TreeNode("Laptop")
  laptop.add_child(TreeNode("Mac"))
  laptop.add_child(TreeNode("Surface"))
  laptop.add_child(TreeNode("Thinkpad"))

  cellphone = TreeNode("Cellphone")
  cellphone.add_child(TreeNode("iPhone"))
  cellphone.add_child(TreeNode("Google Pixel"))
  cellphone.add_child(TreeNode("Samsung"))

  return root


if __name__ == '__main__':
  root = build_product_tree()
  print(root)
