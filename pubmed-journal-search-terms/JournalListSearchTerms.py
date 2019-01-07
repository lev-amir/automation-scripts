InFile = "C:\Google Drive - Work\PubMed Journal Search Keywords (Skill-improvement)\.2016-10 agingQ1.txt"

with open(InFile, 'r') as f:
	names = [line.strip() for line in f]

# print(names)

s = ""
for i in range(len(names)):
	s += '"' + str(names[i]) + '"' + '[ta]'
	if i != len(names) - 1:
		s += ' OR '

# print(s)

open('C:\Google Drive - Work\PubMed Journal Search Keywords (Skill-improvement)\.newSaved.txt', 'w').write(s)
