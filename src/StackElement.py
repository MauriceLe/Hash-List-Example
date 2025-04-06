class StackElement:
    """ Element of a StackList """
    content = None
    next = None
    list = None

    def __init__(self, content, list):
        """ Initialize a StackElement with its content and the according list

         Set list to None if not known yet
         :param content: Student
         :param list: List the element is located in.
         """
        self.content = content
        self.list = list

    def getList(self):
        """ Returning the elements list
        :return: Elements list
        """
        return self.list

    def setList(self, list):
        """ Overwrite the elements list
        :param list: New list
        """
        self.list = list

    def getTail(self):
        """ Return the last object of the element chain
        :return: Last object of the chain.
        """
        if self.next is None:
            return self
        return next.getTail()

    def getContent(self):
        """ Return the objects content
        :return: Content of the element
        """
        return self.content

    def getNextElem(self):
        """ Return the elements following element
        :return: Following element
        """
        return self.next

    def setNextElem(self, element):
        """ Overwrite the following element

         If the following element is None or the following
         element of the following object is None, it simply
         gets overwritten.
         Else the following element of the following element
         will be the following element of the new
         following element before overwrite.
         :param element: New following object.
         """
        if self.next is None or self.next.getNextElem() is None:
            self.next = element
        else:
            element.setNextElem(self.next.getNextElem())
            self.next = element

    def removeNextElem(self):
        """ Remove the following element

         If there are following elements to the
         following element, they will be pulled
         to the following element instead.
         """
        if self.next is None:
            return
        if self.next.getNextElem is None:
            self.next = None
        else:
            self.next = self.next.getNextElem

    def getPrevElem(self):
        """ Get the previous element

         For more detail look StackList
         :return: Previous object in the chain.
         """
        return self.list.getPrev(self, self.list.getHead())

    def setPrevElem(self, newValue):
        """ Overwrite the previous element

         For more detail look StackList
         :param newValue: New previous object
         """
        self.list.setPrev(self, self.list.getHead(), newValue)

    def removePrevElem(self):
        """ Remove the previous element

         For more detail look StackList
         """
        self.list.removePrev(self, self.list.getHead())

    def toString(self):
        """ Turning the StackElement into a readable String object
        :return: String object summary of the element
        """
        o = "\n(" + self.content.toString() + ") ->"
        if self.next is None:
            o += "\nTAIL"
        else:
            o += self.next.toString()
        return o
