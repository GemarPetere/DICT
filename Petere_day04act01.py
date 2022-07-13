output = 0
answer = 'Y'


while answer == 'Y' or answer == 'y':
	numbers = input('Enter numbers: ')
	collect_num = numbers.split(' ')
	num1 = collect_num[0]
	num2 = collect_num[1]

	for x in collect_num:
		number = int(x)
		output+=number
	print("The sum of {} and {} is {}".format(num1,num2,output))
	print("Do you want to continue ? Press Y if yes N if no")
	answer = input()
print('Thank you!')