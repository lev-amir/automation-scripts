# Takes in .txt file w/ list of journal names, seperated by Newline (/n).
# next few lines are not needed
import os
os.getcwd() # Return the current working directory
os.chdir('C:\Google Drive\PubMed Journal Search Project') # Change current working directory

InFile = 'CombinedTop10% (AgingQ3)' + '.txt'

names = []

# Transfers each journal name,

with open(InFile, 'r') as f:
	for line in f:
		if line.strip() not in names:
			names.append(line.strip())

# Saves each journals with added strings in new file in the format:
# "<journal1>"[tiab] OR "<journal2>"[tiab] ...

OutFile = open('New' + InFile, 'w+')

for i in range(len(names)):
	OutFile.write('"' + str(names[i]) + '"' + '[ta]')
	if i != len(names) - 1:
		OutFile.write(' OR ')
	else:
		OutFile.write('\n\nNumber of unique journals = ' + str(len(names)))

OutFile.seek(0)
print(OutFile.read())