class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


#create a linked list:
head = Node(10)
second = Node(20)
third = Node (30)

head.next = second
second.next = third


#traverse the linked list:
current = head

print("Traversing the linked list: ")
while current:
    print(current.data)
    current = current.next



#insertion operation
#---------------------

#insertion at the beginning
new_node = Node(5)
new_node.next = head
head = new_node

print("After adding 5 at the beginning:")
current = head
while current:
    print(current.data)
    current = current.next



#insert at the end:
new_node = Node(40)
current = head

while current.next:
    current = current.next

current.next = new_node



print("After adding 40 at the end:")
current = head
while current:
    print(current.data)
    current = current.next



#insert after a value(20):
current = head

while current:
    current = current.next
    if current.data == 20:
        new_node = Node(25)
        new_node.next = current.next
        current.next = new_node
        break
    

print("After adding 25 after 20:")
current = head
while current:
    print(current.data)
    current = current.next


#Deletion Operation
#----------------------

#Delete the first node
head = head.next

print("After deleting the first node:")
current = head
while current:
    print(current.data)
    current = current.next


#Delete by value (20)
current = head

while current.next:
    if current.next.data == 20:
        current.next = current.next.next
        break
    current = current.next

print("After deleting 20:")
current = head
while current:
    print(current.data)
    current = current.next



#delete the last node
current = head

while current.next.next:
    current = current.next

current.next = None


print("After deleting the last node:")

current = head
while current:
    print(current.data)
    current = current.next

    