input1 = input('Sample Input1:\n')

#split the number(year) and string(office)
getData = input1.split()
getYear = getData[0]
getOffice = getData[1]

match getOffice:
	case 'IT':
		if int(getYear) >= 10:
			print('Ouput:\n 10000')
		else:
			print('Ouput:\n 5000')
	case 'acct':
		if int(getYear) >= 10:
			print('Ouput:\n 12000')
		else:
			print('Ouput:\n 6000')
	case 'hr':
		if int(getYear) >= 10:
			print('Ouput: \n 15000')
		else:
			print('Ouput:\n 7500')
	case _:
		print('Please Input valid value.')