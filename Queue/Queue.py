class Queue:
    class _Node:
        def __init__(self,_value):
            self._value = _value
            self._next_node = None

    def __init__(self):
        self._head = None
        self._queue = None
        self._size = 0
    
    def enqueue(self, _value):
        _new_node = self._Node(_value)
        if self._head == None and self._queue == None:
            self._head = _new_node
            self._queue = _new_node
        else:
            self._queue._next_node = _new_node
            self._queue = _new_node
        self._size += 1
    


        
