import numpy as np
from itertools import permutations
n=input()
list1=[x for x in n]
c=int(np.log2(10**(len(list1))))+1
list3=[2**x for x in range(0,c)]
for order in permutations(list1):
    if order[0]=='0':
        continue
    list2=''.join(order)
    m=int(list2)
    if m in list3:
        print("True")
        break
   