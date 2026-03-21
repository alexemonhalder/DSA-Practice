#Enqueue function for circular queue
def enqueue(item):
    global rear, front, queue

    #check if the queue is full or not
    if(rear+1)%size == front:
        print("Queue is full, cannot add", item)
        return 
    
    if front == -1:    #check if the queue is empty or not
        front = 0
        
    rear = (rear+1) % size
    queue[rear]=item
    print(f"Enqueued: {item}")



#Dequeue function for circular queue
def dequeue():
    global rear, front, queue

    if front == -1:       #check if queue is empty
        print("Queue is empty, cannot remove.")
        return None
    
    #remove the element at the front
    item = queue[front]
    queue[front] = None

    #if it was the last element
    if front == rear:
        front = rear = -1

    else:
        front = (front+1)%size     #move the front pointer forward
        print(f"Dequeued: {item}")
        return item
    



# Create a circular queue of size 5 (use a list).
size = 5
queue = [None]*size
front = rear = -1


# Write code to enqueue 10 into the circular queue.
enqueue(10)

# Enqueue 20 and 30 into the circular queue.
enqueue(20)
enqueue(30)
# Print the circular queue.
print(queue)

# Dequeue one element from the circular queue.
dequeue()

# Enqueue 40 and 50 into the circular queue.
enqueue(40)
enqueue(50)

# Try to enqueue another element and handle the queue full case.
enqueue(60)
enqueue(70)

# Print the circular queue after all operations.
print(queue)

# Dequeue all elements one by one until the queue is empty.
while front != -1:
    dequeue()


print("Final queue:", queue)