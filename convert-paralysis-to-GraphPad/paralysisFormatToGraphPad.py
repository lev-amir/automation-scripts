### by Amir Levine, 2015
### Description
# This script takes in a .csv file in which there are 5 columns:
# 1. Day
# 2. # Alive, present and non-paralyzed
# 3. # Missing
# 4. # Paralyzed
# 5. treatment
# It creates a csv with the same data in a format needed for the creation of a
# survival plot and log-rank test in the Prism GraphPad statistical software

###############################################################################
### Import packages
# module to manipulate .csv files
import csv

# module import to access  file paths relative to acript file
import os
scriptFileDirectory = os.path.dirname(__file__)

###############################################################################
### Functions
def paralysis(reader):
	lastAge = 0
	missingCounter = 0
	alive = 0

	# for each row in inputCSV, check and write to new .csv whether each animal
	# is paralyzed as a single charachter '1' and the
	# day that was recorded.
	# At the end of each treatment, all missing / dead / alive remaining worms
	# are save as '0' corresponding to the last day of of the experiment.
	# Each row is a single worm, described as a vector
	# [day, paralyzed('1') or not('0'), treatment] for example: [16, 0, 'daf-2']
	for row in reader:
		try:
			# 'day of adulthood' increases each row, and reset to a lower number
			# when a new treatment is analyzed. To keep track of the current
			# treatment, compare the current row's day of adulthood to the
			# previous row (lastAge), in order to determine if a new treatment
			# is analyzed.
			# In the last day of each treatment save all remaining alive and
			# missing worms througout the experiment
			if int(row[0]) <= int(lastAge):
				for _ in range(lastAlive + missingCounter):
					writer.writerow([lastAge, '0', lastTreatment])
				missingCounter = 0

			# Add a row with the number '1' and day - indicating one paralyzed
			# worm on that day,  for each worm that was logged as dead
			# row[0] is the day of adulthood
			# '1' indicates paralyzed
			# row[4] is the treatment
			# row[3] is the number of worms logged as paralyzed
			for _ in range(int(row[3])):
				writer.writerow([row[0], '1', row[4]])

			# Add to count the number of worms logged as missing / dead up to
			# this day of the experiment.
			# row[2] is the number of worms logged as missing
			missingCounter += int(row[2])

			# save the current row's day of adulthood to compare in the next
			# iteration to its day of adulthood, in order to determine if a new
			# treatment has started.
			# Save the number of alive animals in case this is the last day of
			# the experiment for that treatment, and then all alive worms will
			# be saved as '0' for that day.
			# row[0] is the day of adulthood
			# row[4] is the treatment
			# row[1] is the number of alive animals.
			lastAge = row[0]
			lastTreatment = row[4]
			lastAlive = int(row[1])

		# ignores errors that occur from column string titles and possible empty
		# rows
		except ValueError:
			pass

	# Same procedure as the one in the above for loop, which adds the remaining
	# alive, missing, and dead worms from the LAST treatment
	for _ in range(lastAlive + missingCounter):
		writer.writerow([lastAge, '0', lastTreatment])

###############################################################################
### Variables
# path to input paralysis.csv file
inputParalysisPath = os.path.join(scriptFileDirectory, "paralysisTemplatePasteDataHere.csv")

# path to output paralysis.csv file
outputParalysisPath = os.path.join(scriptFileDirectory, "paralysisReformattedOutput.csv")

###############################################################################
### Main script

# create the output.csv file as writeable
outputCSV = open(outputParalysisPath,"w",newline='')
writer = csv.writer(outputCSV)

# Add titles to the columns
writer.writerow(['Day of adulthood','Status','Treatment'])

# open the input paralysis.csv file
with open(inputParalysisPath, "r") as inputCSV:
	reader = csv.reader(inputCSV)
	paralysis(reader)

# close the paralysis.csv file
outputCSV.close()
