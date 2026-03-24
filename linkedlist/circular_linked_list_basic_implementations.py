#create a linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

head.next = second
second.next = third
third.next = fourth
fourth.next = head             #it makes it circular



# Print all elements of a circular linked list.
current = head
while True:
    print(current.data)
    current = current.next
    if current == head:
        break


# Count the number of nodes.
count = 0
current = head

while True:
    count += 1
    current = current.next

    if current == head:
        break

print("Total nodes:", count)



# Search for a value (e.g., 25) and print True/False.
target = 25
found = False
current = head

while True:
    if current.data == target:
        found = True
        break
    current = current.next

    if current == head:
        break

print("The value is in the list: ", found)




# Print only the first n nodes.
n = 3
head = current

print("First 3 nodes are:")
for i in range(3):
    print(current.data)
    current = current.next

    if current == head:
        break



# Find and print the last node.
current = head

while current.next != head:
    current = current.next

print("The last node is:", current.data)



# Insert a node with value 5 at the beginning.
new_node = Node(5)
current = head

while current.next != head:
    current = current.next

current.next = new_node
new_node.next = head
head = new_node


print("After adding 5 at the beginning:")
current = head
while True:
    print(current.data)
    current = current.next

    if current == head:
        break



# Insert a node with value 50 at the end.
new_node = Node(50)
current = head

while current.next != head:
    current = current.next

current.next = new_node
new_node.next = head

print("After adding 50 at the end:")

current = head
while True:
    print(current.data)
    current = current.next

    if current == head:
        break



# Insert a node with value 25 after value 20.
new_node = Node(25)
current = head

while True:
    if current.data == 20:
        new_node.next = current.next
        current.next = new_node
        break

    current = current.next
    if current == head:
        break

print("After adding 25 after 20:")
current = head
while True:
    print(current.data)
    current = current.next

    if current == head:
        break



# Insert a node with value 15 before value 20.
new_node = Node(15)
current = head

while True:
    if current.next.data == 20:
        new_node.next = current.next
        current.next = new_node
        break

    current = current.next
    if current == head:
        break

print("After adding 15 before 20:")
current = head
while True:
    print(current.data)
    current = current.next

    if current == head:
        break



# Delete the head node.
current = head
while current.next != head:
    current = current.next

current.next = head.next
head = head.next

print("After deleting the head node:")
current = head
while True:
    print(current.data)
    current = current.next

    if current == head:
        break


# Delete the last node.
current = head
while current.next.next != head:
    current = current.next

current.next = head.next
head = current.next

print("After deleting the last node:")
current = head
while True:
    print(current.data)
    current = current.next

    if current == head:
        break


# Delete a node with value 20.
target = 20
current = head

while current.next!= head:
    if current.next.data == target:
        current.next = current.next.next
        break

    current = current.next

print("After deleting the node with the value 20:")
current = head
while True:
    print(current.data)
    current = current.next

    if current == head:
        break