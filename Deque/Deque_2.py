class Deque:

    def __init__(self):
        self.items = []
    
    def __str__(self):
        return str(self.items) + " Size: " + str(self.size())

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


obj_node = Deque()
obj_node.add_front(1)
obj_node.add_front(2)
obj_node.add_front(3)
obj_node.add_front(4)
print(obj_node)
obj_node.add_rear(0)
print(obj_node)
obj_node.remove_rear()
print(obj_node)
obj_node.remove_front()
print(obj_node)
