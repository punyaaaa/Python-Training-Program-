import heapq
elements=[20,40,30,1,3,2,5,36]
max_heap=[]
for i in elements:
    heapq.heappush(max_heap, -i)
res=[-i for i in max_heap]
print(res)
