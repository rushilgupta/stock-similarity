import math
import argparse

def formVector(filePath):
    vektors = {}
    with open(filePath, "r") as lines:
        for line in lines:
            content = line.split(':')
            if int(content[0]) not in vektors:
                vektors[int(content[0])] = {}
            vektors[int(content[0])][int(content[1])] = int(content[2])
    return vektors

def cosineSimilarity(item1, item2, vektors):
    v1 = vektors[item1]
    v2 = vektors[item2]
    dot_product = 0
    for key in v1:
        if key in v2:
            dot_product += v1[key]*v2[key]
    return dot_product/(magnitude(v1)*magnitude(v2))

def magnitude(vektor):
    magnitude = 0
    for key in vektor:
        magnitude += vektor[key]*vektor[key]
    return math.sqrt(magnitude)

def sortedSimilarity(item, matrix):
    print 'printing similarity order for %s ' %(item)
    item_map = {}
    for i in xrange(len(matrix)):
        item_map[matrix[item][i]] = i

    keylist = item_map.keys()
    keylist.sort(reverse=True)
    for key in keylist:
        #print "%s: %s" % (key, item_map[key])
        print("%s," % (item_map[key])),
    print ''

parser = argparse.ArgumentParser()
# usage: python cosineSimilarity.py --path  /Users/rgupta/Downloads/stock-similarity/stock.data
parser.add_argument('--path', help='path to file in format item:user:rating')
args = parser.parse_args()

vektors=formVector(args.path)
matrix = [[0 for i in xrange(len(vektors))] for i in xrange(len(vektors))]

for item1 in vektors:
    for item2 in vektors:
        if item1 != item2:
            matrix[item1][item2] = cosineSimilarity(item1, item2, vektors)

for item in vektors:
    sortedSimilarity(item, matrix)