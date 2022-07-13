class Employee:
	def __init__(self, name, email, mobilenumber):
		self.name = name
		self.email = email
		self.mobilenumber = mobilenumber

	def personalInformation(self):
		name = self.name
		email = self.email
		mobilenumber = self.email

		return name, email, mobilenumber 


emp1 = Employee('gemar', 'gemar.petereb@gmail.com', '09353260432')
emp2 = Employee('emay', 'emay.petereb@gmail.com', '09353260433')


print(emp1.personalInformation())
print(emp2.personalInformation())
