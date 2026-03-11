#1. Implement a stack using collections.deque with push and pop operations.

from collections import deque

stack = deque()
stack.append("Apple")
stack.append("Banana")
stack.append("Orange")
stack.append("Coconut")
stack.append("Strawberry")
stack.append("Grape")

print(stack)

stack.pop()
stack.pop()
stack.pop()

print("After 3 times pop operations:", stack)





#2. Check if the stack is empty.

stack2 = deque()

stack2.append(10)
stack2.append(20)
stack2.append(30)
stack2.append(40)
stack2.append(50)

print("The stack2 is empty: ", len(stack2)==0)




#3. Peek at the top element of the stack without removing it.

print("The top element of the stack2 is: ", stack2[-1])




#4. Count the number of elements in the stack.

print("The total number of elements in stack2 is:", len(stack2))




#5. Reverse a string using a stack implemented with deque.

txt = "Reversed String"
reversed_order = ""
stack3 = deque()

for ch in txt:
    stack3.append(ch)

while stack3:
    reversed_order += stack3.pop()


print("Before reversing: ", txt)
print("After reversing: ", reversed_order)