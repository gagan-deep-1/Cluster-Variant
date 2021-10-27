import json
import nltk
import csv


def nltkSim(x, y):
    return (1-nltk.jaccard_distance(x, y))


def createCluster(prodList):
    i = 0
    cluster = {}
    while i < len(prodList):
        set1 = set(prodList[i].split())
        j = i+1
        cluster[prodList[i]] = []
        while j < len(prodList):
            if nltkSim(set1, prodList[j].split()) > 0.6:
                cluster[prodList[i]].append(prodList[j])
                del prodList[j]
            else:
                j += 1
        i += 1
    return cluster


f = open(
    "data/data.json",
)
data = json.load(f)
prodList = []
for i in data:
    prodList.append(i["display_name"])

cluster = createCluster(prodList)

with open("output/cluster.csv", "w") as outfile:
    writer = csv.writer(outfile)
    for i in cluster:
        writer.writerow([i, cluster[i]])
