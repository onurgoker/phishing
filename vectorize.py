
import os, argparse, sys, time, string, operator

def generateVectors(path):
	mailType = path.replace("data/output/", "").rstrip("/")

	if mailType == "ham":
    		mailNo = 1
	else:
    		mailNo = 0

	for f in arr:
		if ".txt" in f:
			try:
				file = open(path + f, 'r')
				words = list(file.read().lower().split())
				words = [word.strip(string.punctuation) for word in words]
			except UnicodeDecodeError:
				continue

			# vecfile.write('%s ' % f)
			# create vector with weights multiplied by the occurrence count in the words list
			for w in v:
				vecfile.write('%s ' % str(round(w[1]*words.count(w[0]),3)))
			vecfile.write(str(mailNo) + '\n')

print("Starting job: Vectorizing")
time.sleep(2)

# Define Paths
parser = argparse.ArgumentParser()

parser.add_argument('-ham', dest='ham')
parser.add_argument('-phishing', dest='phishing')
parser.add_argument('-output', dest='output')
parser.add_argument('-dict', dest='dict')

results = parser.parse_args()
hamInputPath = results.ham
phishingInputPath = results.phishing
outputPath = results.output
dictPath = results.dict
wordCount = 300
# End of Path Definition

ignored = {"dict.txt"}
arr = [x for x in os.listdir(hamInputPath) if x not in ignored]

mailCount = len(os.listdir(hamInputPath))-1

# read dict.txt to d
d = {}
with open(dictPath) as f:
    for line in f:
       (key, val) = line.split()
       d[key.lower()] = round(float(val),3)

# sort dictionary by weight
sorted_x = sorted(d.items(), key=operator.itemgetter(1))
# take the first 300
v = sorted_x[0:wordCount]

directory = "output/vector/wtfidf/"

if not os.path.exists(directory):
    os.makedirs(directory)

mailName = str(mailCount)

if mailName.count("0") == 3:
	mailName = mailName.replace("000","k")
elif mailName.count("0") == 4:
	mailName = mailName.replace("0000","0k")

# read a file and split into 'words'
vecfile = open(directory + "v" + mailName + ".txt", 'w+')
vecfile.truncate()

generateVectors(hamInputPath)
generateVectors(phishingInputPath)