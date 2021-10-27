#import textdistance
import json
from scipy.spatial import distance
import pandas as pd
import nltk
def similarity1(x, y):
    return distance.jaccard(x, y) #textdistance.jaccard(string1 , string2)

def similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

def nltkSim(x,y):
    return (1-nltk.jaccard_distance(x, y))

f = open(
    "data/data2.json",
)
data = json.load(f)
outMat = []
prodList = [0]
for i in data:
    prodList.append(i["display_name"])
    row = [i["display_name"]]
    for j in data:
        try:
            row.append(nltkSim(set(i["display_name"].split()),set(j["display_name"].split())))
        except Exception as e:
            print(set(i["display_name"]),set(j["display_name"]))
            exit()
    outMat.append(row)

df = pd.DataFrame(outMat)

headerList = prodList
df.to_csv("output/scores2.csv", header=headerList, index=False)