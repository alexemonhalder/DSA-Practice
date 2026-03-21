from collections import deque

# Write a program to create an empty queue using deque.
q = deque()

# Write code to enqueue one element into the queue.
q.append(10)

# Write code to enqueue multiple elements into the queue.
q.extend([20, 30, 40, 50])
print("After adding multiple elements: ",q)

# Write code to dequeue one element from the queue.
q.popleft()
print("After popping one element from left: ", q)

# Write code to print the front element of the queue.
print("The front element is: ", q[0])

# Write code to check if the queue is empty.
if not q:
    print("Empty")

# Write code to print all elements of the queue.
print("All the elements: ", q)

# Write code to find the size of the queue.
print("Length of the queue is: ", len(q))

# Write code to enqueue an element and then immediately dequeue it.
q.append(100)
print("After enqueue: ", q)

q.popleft()
print("After dequeue: ", q)

# Write a program to insert 3 elements and remove them one by one.
q.append(101)
q.append(102)
q.append(103)

print("Queue after enqueue: ", q)

while q:
    dequeued_element = q.popleft()
    print("Dequeued element:", dequeued_element)
    print("After dequeue operation: ", q)