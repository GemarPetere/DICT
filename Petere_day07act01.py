import random

generated_name = []
g_name = 'Y'

firstname = ['Gemar', 'Klynsee','Justin', 'Neil', 'Macky', 'Reynaldo', 'John', 'Loyd', 'Janver', 'Aira']
middlename = ['Sarita', 'Parilla', 'Cagasan', 'Petere', 'Padpad', 'Helario', 'Mutia', 'Pastolero', 'Autida', 'Guardario']
lastname = ['Parilla', 'Cagasan', 'Sarita', 'Helario', 'Padpad', 'Petere', 'Mutia', 'Autida', 'Pastolero', 'Guardario']



while g_name == 'Y' :
	g_name = input('Do you want to generate a name? Press Y if yes N if no.: ').upper()

	match g_name:
		case 'Y':
			fname = random.choice(firstname)
			mname = random.choice(middlename)
			lname = random.choice(lastname)

			generated_name.append(fname+' '+mname+' '+lname)

			print('Congratulations! your new name is %s \n'%(generated_name[-1]))

		case 'N':
			print('Thank you!')
			for x in generated_name:
				print(x)