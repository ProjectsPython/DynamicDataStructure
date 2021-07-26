class DoublyLinkedList:
    class _Node:
        def __init__(self,_value):
            self._value =  _value
            self._previous_node = None
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
        return str(_array)+" Size: "+ str(self._size)
    def prepend(self,_value):
        _new_node = self._Node(_value)
        if self._head == None and self._queue == None:
            self._head = _new_node
            self._queue = _new_node
        else:
            self._head._previous_node = _new_node
            _new_node._next_node = self._head
            self._head = _new_node
        self._size += 1
    def append(self,_value):
        _new_node = self._Node(_value)
        if self._head == None and self._queue == None:
            self._head = _new_node
            self._queue = _new_node
        else:
            self._queue._next_node = _new_node
            _new_node._previous_node = self._queue
            self._queue = _new_node
        self._size += 1



obj_node = DoublyLinkedList()
obj_node.append(1)
obj_node.append(2)
obj_node.append(3)
obj_node.append(4)
print(obj_node)