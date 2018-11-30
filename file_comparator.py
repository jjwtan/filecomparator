with open('fileA', encoding='utf8') as fileA:
	linesA = fileA.readlines()

with open('fileB', encoding='utf8') as fileB:
	linesB = fileB.readlines()

with open('output', 'w', encoding='utf8') as output:
	for word in linesA:
		word = word.strip() #strip new line
		lineAppearance = []
		for i, line in enumerate(linesB):
			if word in line:
				lineAppearance.append(i+1)

		if not lineAppearance:
			output.write('"' + word + '" does not exist\n')
		else:
			output.write('"' + word + '" exist in line ')
			for x in range (len(lineAppearance)):
				output.write(str(lineAppearance[x]) + ' ')
			output.write('\n')