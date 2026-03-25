#creating class for Nodes
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Creating nodes
head = Node(10)
second = Node(20)
third = Node(30)

#connecting nodes
head.next = second
second.next = third

#printing the linkedlist
current = head
while current:
    print(current.data)
    current = current.next

#reversing the linkedlist
prev = None
current = head

while current:
    next_node = current.next     #save the next
    current.next = prev          #reverse
    prev = current               #move previous
    current = next_node          #move current


#printing reversed linkedlist
print("Reversed:")
current = prev
while current:
    print(current.data)
    current = current.next
