class Student:
    """ Class for a student object"""

    firstName = None
    lastName = None
    id = None

    def __init__(self, firstName, lastName, id):
        """ Initialize a new student with its first and last name and its ID
        :param firstName: First name of the student
        :param lastName: Last name of the student
        :param id: ID of the student
        """
        self.firstName = firstName
        self.lastName = lastName
        self.id = id

    def getLastName(self):
        """ Returning the students last name.
        :return: Students last name
        """
        return self.lastName

    def setLastName(self, lastName):
        """" Overwrite the students last name
        :param lastName: New last name.
        """
        self.lastName = lastName

    def toString(self):
        """" Turning the student into a readable String object
        :return: Readable string object.
        """
        return self.firstName + "," + self.lastName + "," + str(self.id)