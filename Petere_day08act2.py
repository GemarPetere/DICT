class Person:
	def __init__(self, iD, name, birthDate):
		self.iD = iD
		self.name = name
		self.birthDate = birthDate

	def getDetails(self):
		name = self.name
		i_d = self.iD
		dob = self.birthDate

		return name, i_d, dob


class Student(Person):
	def __init__(self, iD, name, birthDate, grades):
		super().__init__(iD, name, birthDate)
		self.grades = grades

	def getDetails(self):
		name = self.name
		i_d = self.iD
		dob = self.birthDate
		grade = self.grades

		return name, i_d, dob, grade


class Employee(Person):
	def __init__(self, iD, name, birthDate, sallary):
		super().__init__(iD, name, birthDate)
		self.sallary = sallary

	def getDetails(self):
		name = self.name
		i_d = self.iD 
		dob = self.birthDate
		sallary = self.sallary

		return name, i_d, dob, sallary

person = Person(1, 'Gemar', '10-10-97')

student1 = Student(1, 'Emay', '10-16-97', 97.5)
student2 = Student(2, 'Peheng', '10-20-97', 99.9)

employee = Employee(1, 'Pets', '11-11-11', 5000)

print("Person => {}".format(person.getDetails()))
print("Student1 => {}".format(student1.getDetails()))
print("Student2 => {}".format(student2.getDetails()))
print("Employee => {}".format(employee.getDetails()))