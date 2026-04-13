import numpy as np
N=int(input())
arr=np.zeros([N,N])
while 1:    
    a=input().split()
    b=[int(d) for d in a]
    if b==[0,0,0]:
        break   
    arr[b[0]-1,b[1]-1]=b[2]
whole=np.zeros([2**(2*N-2),2*(N-1)+1],dtype=bool)
for i in range(2**(2*N-2)-1,-1,-1):
    j=bin(i)
    tem=j[2:]
    tem2=[int(x) for x  in tem]
    if sum(tem2)!=N-1:
        whole[i,2*(N-1)]=1
    k=0
    for p in tem2:
        k=k+1
        if p==1:
            whole[i,k-1]=1
max=0
for i in range(0,2**(2*N-2)-1):
    if whole[i,2*(N-1)]==1:
        continue
    x,y=0,0
    number=0
    number+=arr[x,y]
    for j in range(0,2*(N-1)):
        if whole[i,j]==0:
            x+=1
        else:
            y+=1
        number+=arr[x,y]
    if number>max:
        max=number
for i in range(0,2**(2*N-2)-1):
    if whole[i,2*(N-1)]==1:
        continue
    x,y=0,0
    number=0
    number+=arr[x,y]
    for j in range(0,2*(N-1)):
        if whole[i,j]==0:
            x+=1
        else:
            y+=1
        number+=arr[x,y]
    if number==max:
        arr[0,0]=0
        x,y=0,0
        for k in range(0,2*(N-1)):
            if whole[i,k]==0:
                x+=1
            else:
                y+=1
            arr[x,y]=0
max2=0
for i in range(0,2**(2*N-2)-1):
    if whole[i,2*(N-1)]==1:
        continue
    x,y=0,0
    number=0
    number+=arr[x,y]
    for j in range(0,2*(N-1)):
        if whole[i,j]==0:
            x+=1
        else:
            y+=1
        number+=arr[x,y]
    if number>max2:
        max2=number
print(f"{int(max+max2)}")
