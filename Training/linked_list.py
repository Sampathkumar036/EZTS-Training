class Node:
  def __init__(self,data):
    self.value=data
    self.next=None

head=tail=Node(10)

tail.next=Node(20)
tail=tail.next

tail.next=Node(30)
tail=tail.next

tail.next=Node(40)
tail=tail.next
print(tail)
print(head)
print(head.next.next.next)


def print_link_list(head):
  if head==None:
    print("list is empty")
    return
  curr=head
  while curr!=None:
    print(curr.value)
    curr=curr.next
print_link_list(head)    
temp=Node(50)
def insert(temp):
  curr=temp
  head.next=temp
  temp=head
  print(curr.value)
insert(temp)