# problem solved using slicing

S='ABABABCANFKABABCNKABABCACNDA'
P='ABABCA'
index=[]
for i in range(len(S)-len(P)):
  if S[i:i+len(P)]==P:
    index.append(i)
print(index)    