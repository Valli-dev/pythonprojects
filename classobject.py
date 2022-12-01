class Car:


    def __init__(self, name, color):
        self.model = name
        self.color = color

    def display(self):
        print('car name:', self.model, 'car color:', self.color)


#mycar1 = Car()
#mycar1.name = "Honda"
#mycar1.color = "black"
#mycar2 = Car()
mycar3 = Car("BMW", 'white')
mycar3.model = "chevy"
#del mycar3.model

#mycar2.name = "Toyota"
#mycar2.color = "grey"

#mycar1.display()
#mycar2.display()
mycar3.display()


class MyClass:
  def __init__(self, height):
    self.height = 20


myHeight = MyClass(100)
#del myHeight.height
myHeight.height=450
print(myHeight.height)

class Person:

  def __init__(self,fname,lname):

    self.firstname= fname
    self.lastname=lname

  def printname(self):

    print(self.firstname,self.lastname)


class Student(Person):

  def __init__(self, fname, lname, age, gender):

    super().__init__(fname,lname)
    self.age= age
    self.gender= gender

  def student_profile(self):
      print("Student first name:",self.firstname)
      print("Student last name:",self.lastname)
      print("Age:", self.age)
      print("Gender:", self.gender)

student1 = Student('Daniel','Robertson',30,'male')
student1.student_profile()

student1.printname()
