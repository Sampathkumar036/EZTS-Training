#finding a prime number using less time complexity

m=int(input("enter the message:"))
flag=0
if m<1:
  flag=1
elif m==0:
  flag=0
else:
  for i in range(2,(m//2)+1):
    if m%i==0:
      flag=1
      break
if flag==0:
  print("valid")
else:
  print("invalid")       