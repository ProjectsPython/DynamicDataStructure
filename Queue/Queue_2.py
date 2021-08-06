class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items) + " Size: " + str(self.size())

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


print('First in, first out (FIFO)')
obj_node = Queue()
obj_node.enqueue(1)
obj_node.enqueue(2)
obj_node.enqueue(3)
print(obj_node)
print(obj_node.peek())
obj_node.dequeue()
print(obj_node)
