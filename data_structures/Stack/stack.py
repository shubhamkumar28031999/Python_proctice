from collections import deque
# stack = deque()
# stack.append(10)
# stack.append(20)
# stack.extend([200,400])
# print(stack.pop())
# print(stack)

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,val):
        if type(val)==list:
            self.container.extend(val)
        else:
            self.container.append(val)
    def peek(self):
        return self.container[-1]
    def pop(self):
        return self.container.pop()
    def size(self):
        return  len(self.container)
    def is_empty(self):
        if len(self.container) == 0:
            return True
        else:
            return False
    def display(self):
        stack=[]
        for val in self.container:
            stack.append(val)
        return stack
s = Stack()

s.push([10,20])
print(s.display())

