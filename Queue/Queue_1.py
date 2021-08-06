class Queue:
    class _Node:
        def __init__(self,_value):
            self._value = _value
            self._next_node = None

    def __init__(self):
        self._head = None
        self._queue = None
        self._size = 0
    
    def __str__(self):
        _array = []
        _present_node = self._head
        while _present_node != None:
            _array.append(_present_node._value)
            _present_node = _present_node._next_node
        return str(_array) + " Size: " + str(self._size)
    
    def enqueue(self, _value):
        _new_node = self._Node(_value)
        if self._head == None and self._queue == None:
            self._head = _new_node
            self._queue = _new_node
        else:
            self._queue._next_node = _new_node
            self._queue = _new_node
        self._size += 1
    
    def dequeue (self):
        if self._size == 0:
            self._head = None
            self._queue = None
        else:
            _removed_node = self._head
            self._head = _removed_node._next_node
            _removed_node._next_node = None
            self._size -= 1
            return _removed_node._value


print('First in, first out (FIFO)')
obj_node = Queue()
obj_node.enqueue(1)
obj_node.enqueue(2)
obj_node.enqueue(3)
obj_node.enqueue(4)
print(obj_node)
obj_node.dequeue()
print(obj_node)


        
