class DLinkedList:
    def __init__(self):
        self._head = DLLNode(None, None, None)          # DLL node
        self._tail = DLLNode(None, self._head, None)    # DLL node
        self._current = self._head                      # DLL node
        self._size = 0                                  # Integer

        self._head.setNext(self._tail)

    def __str__(self):
        if self._size == 0:
            return "Empty list."
        outstr = "List: ["
        node = self.get_first()
        while node.getElement() != None:
            if node == self._current:
                outstr += ">"

            if node.getNext().getElement() == None:
                outstr += str(node.getElement())
            else:
                outstr += str(node.getElement()) + ", "
            node = node.getNext()
        outstr += "]"

        return outstr

    
    def add_first(self, element):
        if element != None:
            node = DLLNode(element, None, None)
            if self._size == 0:
                self._add_empty(node)

            else:
                front_node = self.get_first()
                front_node.setPrev(node)
                self._head.setNext(node)
                node.setNext(front_node)
                node.setPrev(self._head)

                self._size += 1

    def get_first(self):
        if self._size != 0:
            return self._head.getNext()
        return self._head

    def remove_first(self):
        if self._size != 0:
            old_first = self.get_first()
            new_first = old_first.getNext()
            self._head.setNext(new_first)
            new_first.setPrev(self._head)

            self._size -= 1

            if self._current == old_first:
                self._current = new_first
        

    def add_last(self, element):
        if element != None:
            node = DLLNode(element, None, None)
            if self._size == 0:
                self._add_empty(node)

            else:
                end_node = self.get_last()
                end_node.setNext(node)
                self._tail.setPrev(node)
                node.setNext(self._tail)
                node.setPrev(end_node)

                self._size += 1

    def get_last(self):
        if self._size != 0:
            return self._tail.getPrev()
        return self._tail

    def remove_last(self):
        if self._size != 0:
            old_last = self.get_last()
            new_last = old_last.getPrev()
            self._tail.setPrev(new_last)
            new_last.setNext(self._tail)

            self._size -= 1

            if self._current == old_last:
                self._current = new_last


    def get_current(self):
        return self._current

    def current_next(self):
        if self._current.getNext() == self._tail:
            self._current = self.get_first()
        else:
            self._current = self._current.getNext()

    def current_prev(self):
        if self._current.getPrev() == self._head:
            self._current = self.get_last()
        else:
            self._current = self._current.getPrev()

    def add_after(self, element):
        if element != None:
            node = DLLNode(element, None, None)
            front_node = self.get_current()
            end_node = front_node.getNext()
            node.setNext(end_node)
            node.setPrev(front_node)
            front_node.setNext(node)
            end_node.setPrev(node)

            self._size += 1

    def remove_current(self):
        if self._size != 0:
            node = self._current
            prev_node = node.getPrev()
            next_node = node.getNext()
            
            prev_node.setNext(next_node)
            next_node.setPrev(prev_node)

            del node

            self.current_next()
            self._size -= 1

    def reset(self):
        if self._size == 0:
            self._current = self._head
        else:
            self._current = self.get_first()


    def length(self): 
        return self._size

    # Private Methods

    def _add_empty(self, node):
        self._head.setNext(node)
        self._tail.setPrev(node)
        node.setPrev(self._head)
        node.setNext(self._tail)
        self._current = node

        self._size += 1


class DLLNode:
    '''Individual node of a Doubly Linked Link'''
    def __init__(self, element, prev, next):
        self._element = element
        self._prev = prev
        self._next = next
    
    def __del__(self):
        self._prev, self._next = None, None

    def getElement(self):
        '''Returns the element associated with this node'''
        return self._element

    def setElement(self, element):
        '''Change the element associated with this node'''
        self._element = element

    def getNext(self):
        '''Returns the next node this node points to'''
        return self._next

    def setNext(self, node):
        '''Changes the next node this node points to'''
        self._next = node

    def getPrev(self):
        '''Returns the previous node this node points to'''
        return self._prev

    def setPrev(self, node):
        '''Changes the previous node this node points to'''
        self._prev = node

class _DLinkedList:
    ''' Doubly Linked List implimentation'''
    def __init__(self):
        self._head = DLLNode(None, None, None)          # DLL node
        self._tail = DLLNode(None, self._head, None)    # DLL node
        self._head._next = self._tail                   # DLL node
        self._size = 0                                  # Integer
        self._current = self._head                      # DLL node

    def __str__(self):
        str = "DLL: "
        node = self._head._next
        while node != self._tail:
            if self._current == node:
                str += "["
            str += f"{node._element}"
            if self._current == node:
                str += "]"
            str += " "
            node = node._next
        return str

    def add_element(self, element):
        ''' Adds an element ot the front of the list'''
        node = DLLNode(element, None, None)
        self._add_node_after(node, self._tail._prev)
        if self._size == 1:
            self._current = self._head._next

    def get_current(self):
        return self._current.getElement()

    def next_element(self):
        if self._size > 0:
            if self._current._next == self._tail:
                self._current = self._head
            self._current = self._current._next
        else:
            self._current = self._head

    def prev_element(self):
        if self._size > 0:
            if self._current == self._head:
                self._current = self._tail
            self._current = self._current._prev
        else:
            self._current = self._head

    def reset(self):
        if self._size > 0:
            self._current = self._head._next
        else:
            self._current = self._head

    def remove_current(self):
        if self._current == self._head:
            return None
        temp = self._current
        self._current = temp._next
        if temp._next == self._tail:
            if self._size > 1:
                self._current = self._head._next
            else:
                self._current = self._head
        return self._remove_node(temp)

    def length(self):
        return self._size

    # Private Methods

    def _add_node_after(self, node, nodebefore):
        node._prev = nodebefore
        node._next = nodebefore._next
        nodebefore._next._prev = node
        nodebefore._next = node
        self._size = self._size + 1

    def _remove_node(self, node):
        self._extract_node(node)
        item = node._element
        node._element = None
        return item

    def _extract_node(self, node):
        if self._current == node:
            self._current = node._prev
        node._prev._next = node._next
        node._next._prec = node._prev
        node._next = None
        node._prev = None
        self._size = self._size - 1

    def _print_node(self, node):
        print(f"Element: {node._element}. Previous: {node._prev._element}. Next: {node._next._element}.")

if __name__ == "__main__":
    dllist = DLinkedList()
    print(dllist)

    # Test add_first(element) method
    for i in range(10):
        dllist.add_first(i)
        print(dllist)

    # Test remove_first() method
    for _ in range(10):
        dllist.remove_first()
        print(dllist)

    # Test add_last(element) method
    for i in range(10):
        dllist.add_last(i)
        print(dllist)

    # Test remove_last() method
    for _ in range(10):
        dllist.remove_last()
        print(dllist)


    # Test get_current(), current_next() and current_prev() methods
    test_var = False
    if test_var == True:
        for i in range(10):
            dllist.add_last(i)
            print(dllist)
        
        for i in range(15):
            dllist.current_next()
            print(dllist.get_current().getElement())

        for i in range(15):
            dllist.current_prev()
            print(dllist, dllist.get_current().getElement())

    dllist.add_first(1)
    dllist.add_first(2)
    dllist.add_last(3)
    dllist.add_first(4)
    dllist.current_next()
    print(dllist)
    print(dllist.get_current().getElement())
    dllist.remove_last()
    print(dllist)
    dllist.remove_last()
    print(dllist)
    dllist.remove_first()
    print(dllist)
    dllist.add_last(3)
    dllist.add_last(4)
    print(dllist)
    dllist.remove_first()
    print(dllist)
    dllist.remove_first()
    print(dllist)