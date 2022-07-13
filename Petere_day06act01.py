 
output = {}
answer = 'C'

while answer != 'E':
	print("Select what you need to do: ")
	print(" A => Add data \n D => Delete data \n E => End process")
	user_select = input().upper()

	match user_select:
		case 'A':
			name = input('Enter Name: ')
			grade = input('Enter Grade: ')

			output[name]= int(grade)
			print("%s \n"%(output))
		case 'D':
			name = input('Enter Name: ')
			output.pop(name)
			if bool(output) == True:
				print("%s \n"%(output))
			else:
				print('Record Empty! \n')
		case _:
			if user_select == 'E':
				answer = 'E'
			else:
				print('Please select valid value ! \n')
				answer = 'A'
print('Thank you!')