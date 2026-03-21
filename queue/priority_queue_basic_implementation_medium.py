# Convert a list [7, 2, 9, 1, 5] into a heap and print it.
import heapq

nums = [7, 2, 9, 1, 5]
heapq.heapify(nums)

print(nums)



# Insert elements, remove 2 elements, then print the remaining queue.
heapq.heappush(nums, 10)
heapq.heappush(nums, 15)
heapq.heappush(nums, -5)
heapq.heappush(nums, -10)
heapq.heappush(nums, 0)

print("After inserting new elements:", nums)

heapq.heappop(nums)
heapq.heappop(nums)

print("After removing two elements:", nums)




# Insert duplicate values and observe the order when popping all elements.
heapq.heappush(nums, 0)
heapq.heappush(nums, 2)
heapq.heappush(nums, 5)
heapq.heappush(nums, 7)

print("After adding duplicate values:", nums)