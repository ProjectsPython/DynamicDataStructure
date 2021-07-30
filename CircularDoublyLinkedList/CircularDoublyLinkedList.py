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
        



