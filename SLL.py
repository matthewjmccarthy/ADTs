class SLinkedList:
    ''' Singly Linked List implimentation'''
    def __init__(self):
        self._first = None  # SLL node
        self._last = None   # SLL node
        self._size = 0      # Integer

    def __str__(self):
        pass
    
    def add_first(self, element):
        ''' Adds an element ot the front of the list\n
            O(1) complexity'''
        node = SLLNode(element, self._first)
        self._first = node
        if self._size == 0:
            self._last = node
        self._size += 1

    def get_first(self):
        ''' Returns the element at the front of the list\n
            O(1) complexity'''
        if self._size == 0:
            return None
        return self._first.getElement()

    def remove_first(self):
        ''' Removes the element from the front of the list\n
            O(1) complexity'''
        if self._size == 0:
            return None
        item = self._first.getElement()
        self._first = self._first.getNext()
        self._size -= 1
        return item


    def add_last(self, element):
        ''' Adds an element to the end of the list\n
            O(1) complexity'''
        node = SLLNode(element, None)
        if self._first == None:
            self._first = node
        else:
            self._last.setNext(node)
        self._last = node
        self._size += 1

    def get_last(self):
        ''' Returns the element at the end of the list\n
            O(1) complexity'''
        if self._size == 0:
            return None
        return self._last.getElement()


    def length(self):
        ''' Returns the number of elements in the list\n
            O(1) complexity'''
        return self._size

class SLLNode:
    '''Individual node of a Singly Linked Link'''
    def __init__(self, element, next):
        self._element = element # any object
        self._next = next       # SLL node

    def getElement(self):
        '''Returns the element associated with this node'''
        return self._element

    def setElement(self, element):
        '''Changes the element associated with this node'''
        self._element = element

    def getNext(self):
        '''Returns the node this node points to'''
        return self._next
    
    def setNext(self, node):
        '''Changes the node this node points to'''
        self._next = node