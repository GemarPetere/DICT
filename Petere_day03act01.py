print('Sample input: \n')
name = input('Enter Name: ').title()
math = float(input('Enter Math Grade: '))
science = float(input('Enter Science Grade: '))
english = float(input('Enter English Grade: '))
print('\n')
print('Sample output: \n')
print('Name: %s'%(name))
print('Math: {}'.format(math))
print('Science: {}'.format(science))
print('English: {}'.format(english))

#calculation for average
average = (math + science + english) / 3
print('Average: {}'.format(round(average, 2)))

if average >= 75:
	print('Congratulations for passing the semester! %s'%(name))
else:
	print('Sorry Balik comply kanalang! %s'%(name))
