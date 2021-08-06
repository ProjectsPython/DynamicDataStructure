class Stack:

    def __init__(self):
        self.items = []
    
    def __str__(self):
        return str(self.items) + " Size: " + str(self.size())

    def push(self, item):
        self.items.append(item)

    def pop(self):
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


print('Last in, first out (LIFO)')
obj_node = Stack()
obj_node.push(1)
obj_node.push(2)
obj_node.push(3)
print(obj_node)
print(obj_node.peek())
obj_node.pop()
print(obj_node)
