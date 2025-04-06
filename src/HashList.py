from src.StackElement import StackElement
from src.StackList import StackList
from src.Student import Student


class HashList:
    """ Class for a Hash based student list"""

    list = None

    def __init__(self, size):
        """ Initialize the list with a fixed size
        :param size: Size of the list
        """
        self.list = [None] * size

    def hash(self, element):
        """ Creating the bucket size of a String object

        Created by sum up all ASCII values of each letter
        :param element: String object to convert.
        :return: HashValue of an String object.
        """
        hashVal = 0
        for c in element:
            hashVal += ord(c)
        return hashVal % len(self.list)

    def add(self, student):
        """ Add a student to the hash list

        Simply replace the Index if previous value
        is None.
        If previous value is a student, create a
        StackList on this index with the previous student
        as the starting head and adding the new Student
        to the Stack after.
        Else we expect an already existing Stack on the index
        and simply push the Student to the list.
        :param student: Student to add to the list.
        """
        hashVal = self.hash(student.getLastName())
        if self.list[hashVal] is None:
            self.list[hashVal] = student
        elif isinstance(self.list[hashVal], Student):
            temp = self.list[hashVal]
            self.list[hashVal] = StackList(StackElement(temp, None))
            self.list[hashVal].push(StackElement(student, self.list[hashVal]))
        else:
            self.list[hashVal].push(StackElement(student, self.list[hashVal]))

    def delete(self, lastName):
        """ Deleting a student with a given last name

        If there is a student with the searched last name, and
        the matching index is a student, it will be simply
        replaced with None. Else, we expect a Stack, so we
        can use its pop function.
        :param lastName: Last name to search.
        """
        hashVal = self.hash(lastName)
        if self.list[hashVal] is None:
            print("Student does not exist.")
        elif isinstance(self.list[hashVal], Student):
            self.list[hashVal] = None
        else:
            self.list[hashVal].pop()

    def modify(self, oldLastName, newLastName):
        """ Change the last name of a student

        If the last name exists, and the matching
        index is a student, this student will be
        temp saved and their name will be modified.
        The old last name index will be deleted and
        the new one will be added again.
        Same will happen to the Stack object with
        pop instead of delete method.
        :param oldLastName: Old last name to search and delete.
        :param newLastName: New last name to overwrite and add.
        """
        hashVal = self.hash(oldLastName)
        if self.list[hashVal] is None:
            print("Student does not exist.")
        elif isinstance(self.list[hashVal], Student):
            temp = self.list[hashVal]
            temp.setLastName(newLastName)
            self.delete(oldLastName)
            self.add(temp)
        else:
            temp = self.list[hashVal].pop()
            temp.getContent().setLastName(newLastName)
            self.add(temp)

    def toString(self):
        """ Turning the HashList into a readable String object.
         :return: Readable String object
        """
        o = "HASHTABLE"
        for i in range(len(self.list)):
            o += "\n" + str(i + 1) + ": "
            if self.list[i] is None:
                o += "None"
            else:
                o += self.list[i].toString()
        return o
