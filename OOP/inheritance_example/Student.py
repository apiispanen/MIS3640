from BabsonPerson import BabsonPerson
from Person import Person


class Student(BabsonPerson):
    pass

class Professor(BabsonPerson):
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def speak(self, utterance):
        return BabsonPerson.speak(self, " My lovely little peeps, " + utterance)

    def lecture(self, topic):
        return self.speak('It is obvious that' + topic*7)

class UG(Student):

    def __init__(self, name, classYear):
        BabsonPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return BabsonPerson.speak(self, " Dude, " + utterance)


class Grad(Student):
    def __init__(self, name, classYear=None):
        BabsonPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return BabsonPerson.speak(self, " My good man, " + utterance)



def isStudent(obj):
    return isinstance(obj, Student)


def main():
    s1 = UG('Christopher Kennedy', 2018)
    s2 = UG('Stephanie Herrera', 2018)
    s3 = UG('Gianca Devina', 2019)
    s4 = Grad('Matt Damon')
    p1 = Professor('Zhi Li', "IT")

    print(p1.lecture('Geography'))

    studentList = [s1, s2, s3, s4]

    print(s1)

    print(s1.getClass())

    # print(s1.speak('where is the quiz?'))

    # print(s2.speak('I have no clue!'))

    # print(s4.speak('I am not sure why I am here.'))
    for student in studentList:
        print(student.speak('Today is cold.'))

    # print(isStudent(s1))

    # p1 = Person('Taylor Swift')
    # print(isStudent(p1))

if __name__ == '__main__':
    main()
