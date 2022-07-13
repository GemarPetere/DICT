answer ='Y'
while answer == 'Y':
	try:
		operation = input('a. add \nb. subtract \nc. multiply \nd. divide \n Operation: ')

		num1 = float(input('first number: '))
		num2 = float(input('second number: '))

		match operation:
			case 'a':
				print(num1+num2)
			case 'b':
				print(num1-num2)
			case 'c':
				print(num1*num2)
			case 'd':
				print(num1/num2)
				
	except Exception as a:
		print(a)
	except ArithmeticError as ar:
		print('Values are not accepted %s'%(ar))

	answer = input('Do you want to continue ? Press Y if yes N and it will terminate: ')