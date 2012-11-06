# written by Tom Plaskon

# location of your kindle's clippings file
inputFile = 'My Clippings.txt'

# location of file to output to
outputFile = 'counts.csv'

# contains the types of points of interest to count
# remove the corresponding item to skip it
itemsToCount = ['Highlight', 'Note', 'Bookmark']

# contains the page number of each chapter
chapterLocations = [345, 610, 889, 1092, 1315, 1608, 1971, 2423, 2783, 3018, 3563, 4020, 4335, 4816]

# Do Not Edit Past This Point
pointsOfInterest = 0
counts = {}
onResource = None

def updateChapterCount(resource, chapter):
    if resource not in counts:
        counts[resource] = {}

    if chapter not in counts[resource]:
        counts[resource][chapter] = 1
    else:
        counts[resource][chapter] += 1

def getChapterFromLocation(location):    
    for i in range(0, len(chapterLocations)):
        if int(location) < int(chapterLocations[i]):
            return i
    return len(chapterLocations)

f = open(inputFile, 'r')

for line in f:
    words = line.split()

    if len(words) == 1 and words[0] == '==========':
        onResource = None
    if len(words) > 1:
        if onResource == None:
            onResource = line.rstrip()
        elif words[0] == '-' and words[1] in itemsToCount and words[2] == 'Loc.':
            startPage = words[3].split('-')[0]
            updateChapterCount(onResource, getChapterFromLocation(startPage))
            pointsOfInterest += 1

f.close()

f = open(outputFile, 'w')

for resource in sorted(counts.keys()):
    f.write(resource + '\t')
    for i in range(0, len(chapterLocations)+1):
        if i in counts[resource]:
            f.write(str(counts[resource][i]) + '\t')
        else:
            f.write('0\t')
    f.write('\n')

f.close()        

print 'Found', pointsOfInterest, 'points of interest'
print 'Outputted to \'' + outputFile + '\''
            
        
