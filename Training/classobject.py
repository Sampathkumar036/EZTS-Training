# class Student :
#   def __init__(self,nm,ag,gn):
#     self.name = nm 
#     self.age = ag
#     self.gender = gn
# st1 = Student("sampath",22,'M') 
# print(st1.name,st1.age,st1.gender)   


class STUDENT :
  def __init__(self,nm,ag,gn):
    self.name = nm 
    self.age = ag
    self.gender = gn
a=input("enter your name:")
b=input("enter your age:")
c=input("enter your gender:") 

st3 = STUDENT(a,b,c) 
print(st3.name,st3.age,st3.gender)   