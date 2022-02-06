import os
import pandas as pd
from tabulate import tabulate

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

for source in sources:
    finArr = []
    finArr.append(words)
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
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df = pd.DataFrame(finArr)
    print(tabulate(df, headers='keys', tablefmt='pretty'))



"""
Make 3 seperate tables for each author. X Axis has words, Y axis has occurences. Do this for each author
"""
