from DLL import *

class List(DLinkedList):
    def __init__(self):
        self._head = DLLNode(None, None, None)
        self._tail = DLLNode(None, self._head, None)
        self._head.setNext(self._tail)
        self._size = 0
        self._current = None

    def get(self, pos):
        if (self._size != 0 and pos < self.length()):
            node = self._get(pos)
            return node.getElement()

    def add(self, pos, element):
        if (self._size != 0 and pos < self.length() and element != None):
            front_node = self._get(pos)
            end_node = front_node.getNext()
            node = DLLNode(element, None, None)

            node.setNext(end_node)
            node.setPrev(front_node)
            front_node.setNext(node)
            end_node.setPrev(node)

            self._size += 1

    def replace(self, pos, element):
        if (self._size != 0 and pos < self.length() and element != None):
            node = self._get(pos)
            node.setElement(element)

    def remove(self, pos):
        if (self._size != 0 and pos < self.length()):
            node = self._get(pos)
            prev_node = node.getPrev()
            next_node = node.getNext()

            prev_node.setNext(next_node)
            next_node.setPrev(prev_node)

            if self._current == node:
                if self._current.getNext() == self._tail:
                    self._current = prev_node
                else:
                    self._current = next_node

    def clear(self):
        node = self.get_first()

        self._head.setNext(self._tail)
        self._tail.setPrev(self._head)
        self._size = 0

        while node.getElement() != None:
                old_node = node
                node = node.getNext()
                del old_node

    def replace_current(self, element):
        self._current.setElement(element)

    def move_to_front(self):
        self._current = self.get_first()

    def move_to_end(self):
        self._current = self.get_last()
    
    def has_next(self):
        if self._current.getNext() != self._tail:
            return True
        return False

    def find(self, element):
        count = 0
        node = self.get_first()
        while node.getElement() != None:
            if node.getElement() == element:
                return count
            node = node.getNext()
            count += 1
        return -1

    # Private Methods

    def _get(self, pos):
        #O(n) complexity
        counter = 0
        node = self.get_first()
        while counter < pos:
            counter += 1
            node = node.getNext()
        return node


if __name__ == "__main__":
    ADT_list = List()

    for i in range(10):
        ADT_list.add_last(i*i)

    print(ADT_list)
    print(ADT_list.get(5))

    ADT_list.move_to_end()
    ADT_list.remove(9)
    print(ADT_list, ADT_list.get(5))

    print(ADT_list.find(49), ADT_list.find(66))

    ADT_list.clear()
    print(ADT_list)