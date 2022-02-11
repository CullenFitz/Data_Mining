import os
import pandas as pd
from tabulate import tabulate
import numpy as np

words = [" ", "charge", "glass", "faith", "then", "alone", "passion",
         "corner", "must", "somewhat", "dropped", "difficult", "one",
         "seemed", "give", "flower"]

sources = []

dickens = r"C:\Users\Cullen\Downloads\AABooks\Charles Dickens - cleared"
eliot = r"C:\Users\Cullen\Downloads\AABooks\George Eliot - cleared"
hardy = r"C:\Users\Cullen\Downloads\AABooks\Thomas Hardy - cleared"

sources.append(dickens)
sources.append(eliot)
sources.append(hardy)

datDickens = []
datEliot = []
datHardy = []

authCount = 0
for source in sources:
    finArr = []
    finArr.append(words)
    authCount += 1
    for filename in os.listdir(source):
        f = os.path.join(source, filename)
        if os.path.isfile(f):
            prob = []
            prob.append(filename)
            with open(f, encoding="utf8") as file:
                long_description = file.read()
                split = long_description.split()
                wordCount = len(split)
                count = 0;
                for i in words:
                    count += 1
                    if count == 1:
                        continue
                    else:
                        occ = long_description.count(i)
                        prob.append(occ / wordCount)
                finArr.append(prob)
                if authCount == 1:
                    new = prob.copy()
                    new.pop(0)
                    datDickens.append(new)
                elif authCount == 2:
                    new = prob.copy()
                    new.pop(0)
                    datEliot.append(new)
                else:
                    new = prob.copy()
                    new.pop(0)
                    datHardy.append(new)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df = pd.DataFrame(finArr)
    print(tabulate(df, headers='keys', tablefmt='pretty'))

datDickens = np.transpose(datDickens)
datEliot = np.transpose(datEliot)
datHardy = np.transpose(datHardy)

dicRes = list(map(sum, datDickens))
eliRes = list(map(sum, datEliot))
harRes = list(map(sum, datHardy))

print(dicRes)
print(eliRes)
print(harRes)
#For each author, find the words that occur the most for that author



