class CircularDoublyLinkedList:
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

    def prepend(self, _value):
        _new_node = self._Node(_value)
        if self._head == None and self._queue == None:
            self._head = _new_node
            self._queue = _new_node
        else:
            self._head._previous_node = _new_node
            _new_node._next_node = self._head
            self._queue._next_node = _new_node
            _new_node._previous_node = self._queue
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
            _new_node._next_node = self._head
            self._head._previous_node = _new_node
            self._queue = _new_node
        self._size += 1
    def shift(self):
        if self._size == 0:
            self._head = None
            self._queue = None
        else:
            _removed_node = self._head
            self._head = _removed_node._next_node
            self._head._previous_node = self._queue
            self._queue._next_node = self._head
            _removed_node._next_node = None
            _removed_node._previous_node = None
            self._size -= 1
            return _removed_node._value
    def pop(self):
        if self._size == 0:
            self._head = None
            self._queue = None
        else:
            _removed_node = self._queue
            self._queue = _removed_node._previous_node
            self._queue._next_node = self._head
            self._head._previous_node = self._queue
            _removed_node._next_node = None
            _removed_node._previous_node = None
            self._size -= 1
            return _removed_node._value

    def get(self, _index):
        if _index == self._size - 1:
            return self._queue
        elif _index == 0:
            return self._head
        elif _index > 0 and _index < self._size - 1:
            _auxiliary_index = int(self._size/2)
            if _index <= _auxiliary_index:
                _present_node = self._head
                _accountant = 0
                while _accountant != _index:
                    _present_node = _present_node._next_node
                    _accountant += 1
                return _present_node
            else:
                _present_node = self._queue
                _accountant = self._size - 1
                while _accountant != _index:
                    _present_node = _present_node._previous_node
                    _accountant -= 1
                return _present_node
        else:
            return None
        
    def update(self,_index, _value):
        _target_node = self.get(_index)
        if _target_node != None:
            _target_node._value =  _value
        else:
            return None

    def insert(self,_index, _value):
        if _index == self._size - 1:
            return self.append(_value)
        elif _index >= 0 and _index < self._size - 1:
            _new_node = self._Node(_value)
            _previous_nodes = self.get(_index)
            _next_nodes = _previous_nodes._next_node
            _previous_nodes._next_node = _new_node
            _new_node._previous_node = _previous_nodes
            _new_node._next_node = _next_nodes
            _next_nodes._previous_node = _new_node
            self._size += 1
        else:
            return None


obj_node = CircularDoublyLinkedList()
obj_node.append(1)
obj_node.append(2)
obj_node.append(3)
obj_node.append(4)
print(obj_node)
obj_node.insert(0,1.5)
obj_node.insert(3,3.5)
print(obj_node)
