# def print_num(n):
#   if n<10:
#     print(n)
#     print_num(n+1)
# print_num(0)    

#Fibanocci Series
# def fib(n):
#   if n == 1:
#     return 0
#   if n==2:
#     return 1
#   return fib(n-1)+fib(n-2)

# if __name__=="__main__":
#   n=int(input())
#   print(fib(n))


#factorial
def fact(n):
  if n==0:
    return 1
  return n*fact(n-1)

if __name__=="__main__":
  n=int(input())
  print(fact(n))