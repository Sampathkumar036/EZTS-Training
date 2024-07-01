class Node:
  def __init__(self,data):
    self.value=data
    self.next=None

head=tail=Node(10)

tail.next=Node(16)
tail=tail.next

tail.next=Node(62)
tail=tail.next

tail.next=Node(100)
tail=tail.next

tail.next=Node(20)
tail=tail.next

tail.next=Node(86)
tail=tail.next

tail.next=Node(72)
tail=tail.next

tail.next=Node(7)
tail=tail.next

tail.next=Node(76)
tail=tail.next

tail.next=Node(99)
tail=tail.next
print(tail)
print(head)
print(head.next.next.next)

def print_link_list(head,data):
  if head==None:
    print("list is empty")
    return
# print(data)