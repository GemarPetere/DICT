def stringInput(input:str):
	i = ''
	count = 0

	#loop for calculation in reverse word and count the characters
	for x in input:
		i = x + i
		count+=1
		
	return i, count

input = input('Enter word: ').upper()

result = stringInput(input) 
print("%s (%s characters)"%(result[0],result[1]))

