from tkinter.filedialog import askopenfilename
import os

# get script containing folder path
dir = os.path.dirname(__file__)

print(dir)

# ScreenFilename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

ScreenGenes = open(os.path.join(dir,"ScreenList.txt"),'r')
MyGenes = open(os.path.join(dir,"MyGenes.txt"),'r')

MyGenesList = MyGenes.read().split('\n')
ScreenList = ScreenGenes.read().split('\n')

Overlaps = []
Unique = []

for gene in MyGenesList:
	for target in ScreenList:
		if gene in target and gene not in Overlaps:
			# print('Mine:' + gene + '\tScreen:' + target)
			# ^ Showed the target list entire row when messy, not informative
			Overlaps.append(gene)
	if gene not in Unique and gene not in Overlaps:
		Unique.append(gene)

if Overlaps:
	print('\n\tOverlaps between the two lists:\n')
	for gene in Overlaps:
		print(gene)
else:
	print('\n\tThere are no overlaps between the two lists!')

# present unique genes that aren't present in screen list if user wishes it:
uniqueGenesDesire = input('Would you like to view the unique values from your gene list? [Y/N]: ').lower()
if  uniqueGenesDesire == 'y':
	print('\n\tValues that are unique to the query list:\n')
	for gene in Unique:
		print(gene)
