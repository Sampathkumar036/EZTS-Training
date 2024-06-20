class node:
  def __init__(self,data):
    self.value=data
    self.right=None
    self.left=None

def Leaf_node(root):
  if not root:
    return
  if not root.left and not root.right:
    print(root.value,end=" ")
    return 
  Leaf_node(root.left)
  Leaf_node(root.right)   


if __name__=="__main__":
  root = node(1)
  root.left=node(2)
  root.right=node(3)
  root.left.left=node(4)
  root.left.right=node(5)
  root.right.left=node(6)
  root.right.right=node(7)
  root.left.right.left=node(9)
  root.left.right.right=node(10)
  root.right.right.right=node(11)
  root.left.right.left.left=node(12)
  root.left.right.left.right=node(13)

  print(Leaf_node(root))        