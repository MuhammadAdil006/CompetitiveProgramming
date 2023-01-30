import heapq
li = [5, 7, 6, 9]
heapq.heapify(li)

print(li)
heapq.heappush(li, 4)
#heap is adjusted
heapq.heappop(li)
