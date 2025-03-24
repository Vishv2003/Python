#Implement a Stack Using a List
#Creates a stack data structure using a list, supporting push, pop, and peek operations.
class Stack:
    def __init__(self):
        self.stack = [] 

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.display() 

print(stack.pop())  
stack.display() 

print(stack.peek()) 
stack.display() 

print(stack.size())  
stack.display()      
