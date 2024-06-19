# class A:
#   def fun1(self):
#     print("this is class A function 1")
#   def fun3(self):
#     print("this is class A function 3")

# class B(A):
#   def fun3(self):
#     print("this is class B function 3")

# obj=A(2,5)
# obj.fun2()






# class Std:
#     def __init__(self):
#         self.USN=None
#         self.Name=None
#         self.Marks=[]
#         self.Percentage=None
#         self.grade=None
#     def Std_input(self):
#         self.Name=input("Name: ")
#         self.USN=input("USN: ")
#         for i in range(0,5):
#             Marks=int(input(f"Marks for {i+1}: "))
#             self.Marks.append(Marks)
#     def calc_percentage(self):
#         sum=0
#         for i in self.Marks:
#             sum+=i
#         self.Percentage=(sum/500)*100
#     def calc_grade(self):
#         per=self.Percentage
#         if per>=90:
#             self.grade="A"
#         elif per>=80:
#             self.grade="B"
#         elif per>=70:
#             self.grade="C"
#         elif per>=60:
#             self.grade="D"
#         else:
#             self.grade="Invalid"
#     def print_details(self):
#         print("Name: ",self.Name)
#         print("USN: ",self.USN)
        
#         print("Marks: ")
#         for i in range(0,5):
#             print(self.Marks[i])
#         print("Percentage: ",self.Percentage)
#         print("Grade: ",self.grade)
# obj=Std()
# obj.Std_input()
# obj.calc_percentage()
# obj.calc_grade()
# obj.print_details()    


