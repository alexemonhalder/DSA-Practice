#priority_queue_basic_implementation_easy.py


import heapq

# Create an empty priority queue and insert 5 numbers.
pq = []

heapq.heappush(pq, 20)
heapq.heappush(pq, 5)
heapq.heappush(pq, -10)
heapq.heappush(pq, 15)
heapq.heappush(pq, 30)


# print the smallest element without removing it.
print("Smallest element:", pq[0])


# remove the smallest one.
smallest = heapq.heappop(pq)
print("Removed:", smallest)


# print all values in ascending order using heappop().
print("Values in ascending order:", pq)