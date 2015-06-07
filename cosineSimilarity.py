import math

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

vektors=formVector('/Users/rgupta/Downloads/stock-similarity/stock2.data')
matrix = [[0 for i in xrange(len(vektors))] for i in xrange(len(vektors))]

for item1 in vektors:
    for item2 in vektors:
        if item1 != item2:
            matrix[item1][item2] = cosineSimilarity(item1, item2, vektors)
print matrix