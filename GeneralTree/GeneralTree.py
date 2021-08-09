class GeneralTree:
    class CLL:
        class Node:
            def __init__(self, _value, _parent):
                self._value = _value
                self._parent = _parent
                self._child = None
                self._next_node = None
        
        def __init__(self):
            self._head = None
            self._queue = None
            self._size = 0
        
        def append(self, _value, _parent):
            _new_node = self.Node(_value, _parent)
            if self._head == None and self._queue == None:
                self._head = _new_node
                self._queue = _new_node
                self._queue._next_node = self._head
            else:
                self._queue._next_node = _new_node
                _new_node._next_node = self._head
                self._queue = _new_node
            self._size += 1
            
    def __init__(self):
        self._root = None
        self._size = 0

                
