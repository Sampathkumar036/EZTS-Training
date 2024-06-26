p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]

p_w={}
for i in range(len(p)):
  p_w[i]=p[i]/w[i]
print(p_w)

l=list(p_w.items())
print(l)
n=len(l)

B=lambda x:l[x][1]
print(B(2))
sorted_list=sorted(l,key=lambda x:x[1],reverse=True)
print("sorting using lambda function",sorted_list)


# for i in range(n-1):
#   max=i
#   for j in range(i+1,n):
#     if l[j][1]>l[max][1]:
#       max=j

#   l[i],l[max]=l[max],l[i]    
# print(l)
# sorted_pw={}
# for i in l:
#   sorted_pw[l[0]]=l[1]
# print(sorted_pw)  