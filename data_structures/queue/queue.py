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
        if type(val) == list:
            self.container.extendleft(val)
        else:
            self.container.appendleft(val)
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

s.push(10)
s.push([30, 20, 10])

print(s.display())
print(s.is_empty())