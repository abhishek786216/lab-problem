# mat=[]
# for i in range(4):
#     l1=[]
#     for j in range(3):
#         a=int(input("Enter value : "))
#         l1.append(a)
#     mat.append(l1)
# print(mat)
# l=[]
# l3=[]

# for i in range(4):
#     if(i==0):
#         l.append(mat[i])
#     else:
#         l3.append(mat[i])
# l4=[]
# for i in range(3):
#    l4.append(l[0][i]) 
# d=dict(zip(l4,l3))
# print(d)
# import required modules 
import inspect 
import collections 

# use signature() 
print(inspect.signature(collections.Counter)) 
