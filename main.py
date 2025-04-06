from src.HashList import HashList
from src.Student import Student
from datetime import datetime

file = "Data.txt"
list = HashList(53)
running = True


def readFile():
    """ Read the file

    Also save the content of the file into the
    HashList and removing the latest added object and measure
    the duration of this operation.
    """
    lastStudent = None
    with open(file) as f:
        for l in f:
            (firstName, lastName, id) = l.replace("\n", "").split(",")
            student = Student(firstName, lastName, id)
            lastStudent = student
            list.add(student)
    start = datetime.now().microsecond * 1000
    list.delete(lastStudent.getLastName())
    end = datetime.now().microsecond * 1000
    t = end - start
    print("Deleting latest added element took " + str(t) + "ms.")


def printMenu():
    """ Print the main menu """
    o = "\n\n[1 = Add student]\n[2 = Remove student]\n[3 = Modify student]\n[4 = Show students]\n[5 = End]\n"
    print(o)


def userInput():
    """ Get a user input for the options

    If the users input cant be converted into a
    Integer object, the user will get an error
    message and is returning to the menu.
    """
    try:
        i = int(input("Select an option: "))
        options(i)
    except ValueError:
        print("Invalid input.")


def options(i):
    """ Match the users input to a function
    :param i: Users selection.
    """
    if i == 1:
        add()
    elif i == 2:
        delete()
    elif i == 3:
        modify()
    elif i == 4:
        show()
    elif i == 5:
        global running
        running = False
    else:
        print("Invalid input.")


def add():
    """ Add a new Student

    If the ID cant be casted into a Integer
    object, the user will get an error message
    and will return to the menu.
    """
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    try:
        id = int(input("ID: "))
        list.add(Student(firstName, lastName, id))
    except ValueError:
        print("Invalid input for ID.")


def delete():
    """ Delete an object by its last name """
    list.delete(input("Last Name: "))


def modify():
    """ Modify an object by its last name with a new last name """
    list.modify(input("Old last name: "), input("New last name: "))


def show():
    """ Prints the list """
    print(list.toString())


startTime = datetime.now().microsecond * 1000
readFile()
endTime = datetime.now().microsecond * 1000

total = endTime - startTime

print("Reading file took " + str(total) + "ms.\n\n\n")

while (running):
    printMenu()
    userInput()
