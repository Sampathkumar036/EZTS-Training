def math(a,b,op):
  match op:
    case '+':return a+b
    case '-':return a-b
    case '*':return a*b
    case '/':return a/b
    case '//':return a//b
    case '**':return a**b
    case _:return None
S=str(input())
op=["**","//","+","-","/","*"]
for i in op:
  ls = str.split(i)
  if len(ls) == 3:
    break
  print(math(float(ls[0]),float(ls[2],ls[0])))
