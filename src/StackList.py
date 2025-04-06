class StackList:
    """ List of StackElements """
    head = None
    tail = None

    def __init__(self, head):
        """ Initialize a new StackList with its head
        :param head: Lists head to begin
        """
        if head.getList() is None:
            head.setList(self)
        self.head = head
        self.tail = head.getTail()

    def getHead(self):
        """ Returning the lists head
        :return Lists head
        """
        return self.head

    def getPrev(self, next, i):
        """ Get the previous element of a given StackElement

        Recursive function checks, if the following element
        of the iterator is equal to the given StackElement.
        If so, it'll be returned.
        :param next: Following element which will be searched.
        :param i: Iterator, use lists head to begin
        :return Previous object of the given StackElement
        """
        if i.getNextElem() is None:
            return None
        if i.getNextElem() is next:
            return i
        return self.getPrev(next, i.getNextElem())

    def setPrev(self, next, i, newPrev):
        """ Overwrite the previous element of a given StackElement

        Recursive function checks, if the following element
        of the iterator is equal to the given StackElement.
        If so, it'll be overwritten.
        If the previous element was the head, it'll be
        overwritten to.
        :param next: Following element which will be searched.
        :param i: Iterator, use lists head to begin
        :param newPrev: Value to overwrite the previous object
        """
        if i.getNextElem() is None:
            return
        if i.getNextElem() is next:
            newPrev.setNextElem(next)
            i = newPrev
            if i.getPrevElem() is None:
                self.head = i
        else:
            self.setPrev(next, i.getNextElem(), newPrev)

    def removePrev(self, next, i):
        """ Remove the previous element of a given StackElement

        Recursive function checks, if the following element
        of the iterator is equal to the given StackElement.
        If so, it'll be removed.
        :param next: Following element which will be searched.
        :param i: Iterator, use lists head to begin
        """
        if i.getNextElem() is None:
            return
        if i.getNextElem() is next:
            i.getPrevElem().setNextElem(next)
        else:
            self.removePrev(next, i.getNextElem())

    def toString(self):
        """ Turn the StackList into a readable String object
        :return: String object of the entire list.
        """
        o = "HEAD ->"
        o += self.head.toString()
        return o

    def push(self, element):
        """ Add an element on top of the list.
        :param element: Element to add
        """
        element.setNextElem(self.head)
        self.head = element

    def top(self):
        """ Get the latest added element.
        :return: Lists head
        """
        return self.head

    def pop(self):
        """ Take the most top element
        Replace the head with the following
        element of the old head.
        :return: Old head
        """
        oldHead = self.head
        self.head = self.head.getNextElem()
        return oldHead