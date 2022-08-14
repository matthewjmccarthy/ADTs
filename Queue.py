import sys
from SLL import SLinkedList

class Queue:
    '''Queue implementation using a Singly Linked List'''
    def __init__(self):
        self._list = SLinkedList()

    def __str__(self):
        pass

    def enqueue(self, element):
        '''
            O(1) complexity'''
        self._list.add_last(element)

    def dequeue(self):
        '''
            O(1) complexity'''
        return self._list.remove_first()

    def first(self):
        '''
            O(1) complexity'''
        return self._list.get_first()

    def length(self):
        '''
            O(1) complexity'''
        return self._list.length()

class _Queue:
    def __init__(self):
        self._list = [None] * 10
        self._head = 0
        self._tail = 0
        self._size = 0

    def __str__(self):
        str = "Queue:"
        for i in self._list[:-1]:
            if i != None:
                str += f" {i},"
        if self._list[-1] != None:
            str += f" {self._list[-1]}"
        return str

    def enqueue(self, item):
        #O(1) on average
        if self._size == 0:
            self._list[0] = item
            self._size = 1
            self._tail = 1
        else:
            self._list[self._tail] = item
            self._size += 1
            if self._size == len(self._list):
                self.grow()
            elif self._tail == len(self._list) - 1:
                self._tail = 0
            else:
                self._tail += 1

    def dequeue(self):
        #O(1) on average
        if self._size == 0:
            return None
        item = self._list[self._head]
        self._list[self._head] = None
        if self._size == 1:
            self._head = 0
            self._tail = 0
            self._size = 0
        elif self._head == len(self._list) - 1:
            self._head = 0
            self._size -= 1
        else:
            self._head += 1
            self._size -= 1
        return item

    def length(self):
        #O(1)
        return self._size
        
    def first(self):
        #O(1)
        if self.length() == 0:
            return None
        return self._list[self._head]

    def grow(self):
        old = self._list
        self._list = [None] * (2 * self._size)
        old_head = self._head
        pos = 0
        if self._head < self._tail:
            while old_head <= self._tail:
                self._list[pos] = old[old_head]
                old[old_head] = None
                pos += 1
                old_head += 1
        else:
            while old_head < len(old):
                self._list[pos] = old[old_head]
                old[old_head] = None
                pos += 1
                old_head += 1
            old_head = 0
            while old_head <= self._tail:
                self._list[pos] = old[old_head]
                old[old_head] = None
                pos += 1
                old_head += 1
        self._head = 0
        self._tail = self._size

    
    def get_size(self):
        return sys.getsizeof(self._list)

    def _old_dequeue(self):
        #O(n) due to list.pop(0)
        if len(self._list) != 0:
            return self._list.pop(0)
        return None

    def _old_length(self):
        #O(1)
        return len(self._list)

if __name__ == "__main__":
    queue = Queue()
    print(f"List size = {queue.get_size()} bytes")
    for i in range(10):
        queue.enqueue(i)
        print(queue)

    for _ in range(4):
        queue.dequeue()
        print(queue)

    print(f"List size = {queue.get_size()} bytes")
    print(f"List length = {queue.length()}")
    print(queue.first())

    queue2 = Queue()
    print(queue2.dequeue())