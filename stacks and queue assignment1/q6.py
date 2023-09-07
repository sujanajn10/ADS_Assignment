

def Transfer(S, T):

 for i in range(len(S)):

   T.append(S.pop())

 return T


S = ["a","b","c","d"]

print(S)

T=[]
T = Transfer(S, T)
print(T)