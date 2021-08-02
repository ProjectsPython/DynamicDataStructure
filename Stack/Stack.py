class Stack:
    class _Node:
        def __init__(self, _value):
            self._value = _value
            self._next_node = None

    def __init__(self):
        self._head = None
        self._queue = None
        self._size = 0
