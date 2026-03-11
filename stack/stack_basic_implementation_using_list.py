#1. Implement a stack using a list with push and pop operations.
stack1 = []

stack1.append(10)
stack1.append(20)
stack1.append(30)
stack1.append(40)
stack1.append(50)

print(stack1)

stack1.pop()
stack1.pop()

print(stack1)



#2. Check if a stack is empty.
stack2 = []
print("Stack2 is empty: ", len(stack2)==0)

stack2.append("Alex")
print("Stack2 is empty: ", len(stack2)==0)




#3. Peek at the top element of the stack without removing it.
print("Last element of stack2 is: ", stack2[-1])



#4. Count the number of elements in the stack.
stack3 = []

stack3.append("Orange")
stack3.append("Apple")
stack3.append("Banana")
stack3.append("Berry")

print("Total elements in stack3:", len(stack3))



#5. Reverse a string using a stack.
txt = "Alex Emon Halder"
reversed_txt = ""

stack = []

for ch in txt:
    stack.append(ch)

while stack:
    reversed_txt += stack.pop()

print("Original Text: ", txt)
print("Reversed Text: ", reversed_txt)