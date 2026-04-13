import numpy as np
N=int(input())
arr=np.zeros([N,N])
while 1:    
    a=input().split()
    b=[int(d) for d in a]
    if b==[0,0,0]:
        print("over")
        break   
    arr[b[0]-1,b[1]-1]=b[2]
whole=np.ones([2**(2*N-2),2*(N-1)],dtype=bool)
for i in range(0,2**(N-1)):
    j=bin(i)
    tem=j[2:]
    tem2=[int(x) for x  in tem]
    print(tem2)
    print("\n")
    if sum(tem2)!=N-1:
        continue
    k=0
    for p in tem2:
        k=k+1
        if p==0:
            whole[i,k]=0
print(whole)