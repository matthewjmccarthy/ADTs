import sys
from SLL import SLinkedList

class Stack:
    '''Stack implementing an SLL'''
    def __init__(self):
        self._list = SLinkedList()

    def __str__(self):
        str = "Stack:"
        return str

    def push(self, element):
        #O(1)
        self._list.add_first(element)

    def pop(self):
        #O(1)
        return self._list.remove_first()

    def top(self):
        #O(1)
        return self._list.get_first()

    def length(self):
        #O(1)
        return self._list.length()

    def get_size(self):
        return sys.getsizeof(self._list)

class _old_Stack:
    def __init__(self):
        self._list = []

    def __str__(self):
        str = "Stack:"
        for i in self._list[:-1]:
            str += f" {i},"
        str += f" {self._list[-1]}"
        return str

    def push(self, element):
        #O(1) on average
        self._list.append(element)

    def pop(self):
        #O(1) on average
        if len(self._list) == 0:
            return None
        return self._list.pop()

    def top(self):
        #O(1)
        if len(self._list) == 0:
            return None
        return self._list[-1]

    def length(self):
        #O(1)
        return len(self._list)

    def get_size(self):
        return sys.getsizeof(self._list)

    def postfix(self):
        return

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack)
    print(f"Top element = {stack.top()}")
    print(f"Length = {stack.length()}")
    stack.pop()
    print(stack.pop())
    for i in range(10):
        stack.push(i)
    print(stack)
    print(f"List size = {stack.get_size()} bytes")