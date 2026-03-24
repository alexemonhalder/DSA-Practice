# Create a DLL: 10 ↔ 20 ↔ 30.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = Node(10)
first = Node(20)
second = Node(30)

head.next = first
first.prev = head
first.next = second
second.prev = first

current = head
while current:
    print("New DDL:", current.data)
    current = current.next
        


# Traverse forward and backward.
print("Forward traverse:")
current = head
while current:
    print(current.data)
    current = current.next

print("Backward traverse:")
current = second
while current:
    print(current.data)
    current = current.prev



# Insert a node with value 5 at the beginning.
new_node = Node(5)
current = head

new_node.next = head
head.prev = new_node
head = new_node

print("After adding 5 at the beginning:")
current = head
while current:
    print(current.data)
    current = current.next



# Insert a node with value 40 at the end.
new_node = Node(40)

current = head
while current.next:
    current = current.next

current.next = new_node
new_node.prev = current


print("After adding 40 at the end:")
current = head
while current:
    print(current.data)
    current = current.next



# Delete the first node.
head = head.next
head.prev = None


print("After deleting first node:")
current = head
while current:
    print(current.data)
    current = current.next



# Delete the last node.
current = head
while current.next:
    current = current.next

current.prev.next = None

print("After deleting last node:")
current = head
while current:
    print(current.data)
    current = current.next



# Insert a node with value 25 after node with 20.
current = head
while current:
    if current.data == 20:
        new_node = Node(25)
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node       #Current’s next node is now the new node.
        break
    current = current.next


print("After adding 25 after 20:")
current = head
while current:
    print(current.data)
    current = current.next



# Delete a node with value 20.
current = head
while current:
    if current.data == 20:
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
            break
    current = current.next


print("After deleting 20:")
current = head
while current:
    print(current.data)
    current = current.next



# Count the number of nodes in DLL.
count = 0
current = head

while current:
    count += 1
    current = current.next

print("Current DLL length: ", count)




# Search for a value in the DLL.
found = False
target = 30

current = head
while current:
    if current.data == target:
        found = True
    current = current.next

print("Target is in the DLL: ", found)