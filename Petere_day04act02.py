collect = []
countAlpha = 0
countDigit = 0

sentence = input('Enter Sentence: ')

for x in sentence:
	if x != ' ':
		collect.append(x)
		i = collect.index(x)
		if collect[i].isalpha() == True:
			countAlpha+=1
		elif collect[i].isdigit() == True:
			countDigit+=1

print('The sentence contained {} letters and {} numbers.'.format(countAlpha,countDigit))