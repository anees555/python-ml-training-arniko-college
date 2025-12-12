class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def pop(self):
        
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    

    ### Object 
my_stack = Stack()
my_stack.push(34)
my_stack.push(56)
my_stack.push(78)
my_stack.push(23)

print(f"My stack: {my_stack.stack}")
print(f"Popped element: {my_stack.pop()}")
print(f"Stack after pop: {my_stack.stack}")
print(f"top element: {my_stack.peek()}")
print(f"Size of stack: {my_stack.size()}")