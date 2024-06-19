def count_vowel(s):
  dic={'A':0,'E':0,'I':0,'O':0,'U':0}
  for i in s:
    if i=='a' or i=='A':
      dic['A']+=1
    if i=='e' or i=='E':
      dic['E']+=1  
    if i=='i' or i=='I':
      dic['I']+=1
    if i=='o' or i=='O':
      dic['O']+=1
    if i=='u' or i=='U':
      dic['U']+=1

  x=max(dic.values())
  result=[]
  for i,j in dic.items():
    if j==x:
      result.append(i)

  return result
i_p=[
  ["Alex","I enjoy hiking in the mountains"],
  ["sam","A lovely sunny day at the beach"],
  ["sampath","I am working with laptop"],
  ["manu","He is sitting beside me"]
]
o_p={}
for i in i_p:
  o_p[i[0]]=count_vowel(i[1])
print(o_p)