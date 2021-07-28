class CircularLinkedList:
    class _Node:
        def __init__(self,_value):
            self._value =  _value
            self._next_node = None

    def __init__(self):
        self._head = None
        self._queue = None
        self._size = 0

    def __str__(self):
        _array = []
        _pivot = True
        _present_node = self._head
        _accountant = self._size
        while _accountant != 0:
            if _pivot != False or _present_node != self._head:
                _array.append(_present_node._value)
                _present_node = _present_node._next_node
                _pivot = False
                _accountant -= 1
            else:
                 break
        return str(_array) + " Size: " + str(self._size)

    def prepend (self,_value):
        _new_node = self._Node(_value)
        if self._head == None and self._queue == None:
            self._head = _new_node
            self._queue = _new_node
        else:
            _new_node._next_node = self._head
            self._queue._next_node = _new_node
            self._head = _new_node
        self._size += 1

obj_node = CircularLinkedList()
obj_node.prepend(1)
obj_node.prepend(2)
obj_node.prepend(3)
obj_node.prepend(4)
print(obj_node)