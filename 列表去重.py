A = ['a','b','a','c']

A.sort()
print(A)

a=0
b=[]
c=len(A)
print(c)
while a<c:
    if A[a]!=A[a+1]:
        b=b.append(A[a])
        print(b)
    a=a+1   
print(b)
