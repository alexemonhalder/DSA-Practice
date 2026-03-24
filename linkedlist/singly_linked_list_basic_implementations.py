#creating node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a linked list with nodes containing: 5 → 10 → 15 → 20.
head = Node(5)
first = Node(10)
second = Node(15)
third = Node(20)

head.next = first
first.next = second
second.next = third


# Traverse it and print all values.
current = head

while current:
    print(current.data)
    current = current.next


# Insert a node with value 2 at the beginning.
new_node = Node(2)
new_node.next = head
head = new_node

print("After inserting 2 at the beginning:")
current = head
while current:
    print(current.data)
    current = current.next


# Insert a node with value 25 at the end.
new_node = Node(25)

current = head
while current.next:
    current = current.next

current.next = new_node

print("After Inserting 25 at the End:")
current = head
while current:
    print(current.data)
    current = current.next



# Delete the first node.
head = head.next

print("After deleting the first node:")
current = head
while current:
    print(current.data)
    current = current.next



# Delete a node with value 15.
current = head

if current.data == 15:
    head = head.next

else:
    while current.next:
        if current.next.data == 15:
            current.next = current.next.next    #skipping the node
            break
        current = current.next

print("After deleting 15:")
current = head
while current:
    print(current.data)
    current = current.next



# Insert a node with value 12 after 10.
new_node = Node(12)

current = head
while current:
    if current.data == 10:
        new_node.next = current.next
        current.next = new_node
        break
    current = current.next

print("After inserting 12 after 10:")
current = head
while current:
    print(current.data)
    current = current.next

        

# Count the number of nodes in your list.
count = 0
current = head

while current:
    count += 1
    current = current.next

print("Number of nodes in the list:", count)



# Search for a value (e.g., 20) and return True/False.
target = 20
current = head
found = False

while current:
    if current.data == target:
        found = True
    
    current = current.next

print("20 is in the list:", found)