
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.count() == 0:
            return None
        
        return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack):
            print(item)



my_stack = Stack()

my_stack.push('A')
my_stack.push('B')
my_stack.push('C')

print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
my_stack.print()

class Queue:

    def __init__(self):
        self.queue = []

    def equeue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.count()==0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)

    def print(self):
        for item in (self.queue):
            print(item)


my_queue = Queue()
my_queue.equeue('D')
my_queue.equeue('E')
my_queue.equeue('F')
print(my_queue.count())
my_queue.print()
my_queue.dequeue()
print(my_queue.count())
my_queue.print()
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.count())
my_queue.print()
