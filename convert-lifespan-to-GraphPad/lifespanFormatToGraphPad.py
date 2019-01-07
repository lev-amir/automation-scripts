### by Amir Levine, 2015
### Description
# This script takes in a .csv file in which there are 4 columns:
# 1. Day
# 2. # Missing
# 3. # dead
# 4. treatment
# It creates a csv with the same data in a format needed for the creation of a
# survival plot and log-rank test in the Prism GraphPad statistical software

###############################################################################

# module to manipulate .csv files
import csv

# module import to access  file paths relative to acript file
import os
scriptFileDirectory = os.path.dirname(__file__)

### Variables
# path to input lifespan.csv file
inputLifespanPath = os.path.join(scriptFileDirectory, "lifespanTemplatePasteDataHere.csv")

# path to output lifespan.csv file
outputLifespanPath = os.path.join(scriptFileDirectory, "lifespanReformattedOutput.csv")

###############################################################################

# create the output .csv file as writeable
outputCSV = open(outputLifespanPath,"w",newline='')
writer = csv.writer(outputCSV)
# Add titles to the columns
writer.writerow(['Day of adulthood','','Treatment'])

# open the lifespan.csv file
with open(inputLifespanPath, "r") as inputCSV:
	reader = csv.reader(inputCSV)

	# iterable variable that will increase in size to determine the current
	# column to write the dead/missing number, based on the assumed treatmentCounter
	# that's currently analyzed
	treatmentCounter = 1
	lastAge = 10000

	# for each row in the lifespan.csv check and write to new .csv the number of dead
	#   and number of missing animals per day as a single charachter '1'/'0' respectively.
	# each row is [day, dead/missing, treatment]. ex. [16, 0, 'daf-2']
	for row in reader:
		try:
			# compare current row's day of adulthood to the previous row's in
			# order to determine if a new treatment has started
			if int(row[0]) <= int(lastAge):
				treatmentCounter += 1

			# Add a row with the number '0' and day - indicating one missing
			# worm on that day
			for _ in range(int(row[1])):
				writer.writerow([row[0], '0', row[3]])

			# Add a row with the number '1' and day - indicating one dead worm
			# on that day.
			for _ in range(int(row[2])):
				writer.writerow([row[0], '1', row[3]])

			# save the current row's day of adulthood to compare in the next
			# iteration to its day of adulthood, in order to determine if a new
			# treatment has started.
			lastAge == row[0]

		# ignores errors that occur from column string titles.
		except ValueError:
			pass

# close the lifespan.csv file
outputCSV.close()
