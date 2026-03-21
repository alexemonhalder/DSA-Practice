# Store (priority, task) pairs and print tasks based on priority.
import heapq

hq = []

heapq.heappush(hq, (1, "Learn Priority Queue"))
heapq.heappush(hq, (5, "Learn Python Function"))
heapq.heappush(hq, (2, "Do Data Communication Assignment"))
heapq.heappush(hq, (4, "Meet my friends"))
heapq.heappush(hq, (3, "Do Meditation"))

print("Elements in heap structure:", hq)


print("Elements based on priority:")
while hq:
    priority, value = heapq.heappop(hq)
    print(priority, value)



# Implement a max-priority queue using negative values and print elements in descending order.
numlist = []

heapq.heappush(numlist, -20)
heapq.heappush(numlist, -40)
heapq.heappush(numlist, -10)
heapq.heappush(numlist, -30)
heapq.heappush(numlist, -50)

print("Elements in descending order: ")
while numlist:
    print(-heapq.heappop(numlist))




#Given a list of numbers, find the 3 smallest elements using a priority queue.
nombors = [10, -6, 0, 3, 21, 35]
smallest_3 = []

heapq.heapify(nombors)

for i in range(3):
    smallest_3.append(heapq.heappop(nombors))


print("Three smallest numbers are:", smallest_3)