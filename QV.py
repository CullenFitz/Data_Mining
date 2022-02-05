import pandas as pd
import numpy as np
import nltk
import os

words = ["charge", "glass", "faith", "then", "alone", "passion",
         "corner", "must", "somewhat", "dropped", "one",
         "seemed", "give", "flower"]

finArr = []
prob = []
sources = []

dickens = r"C:\Users\Cullen\Downloads\AABooks\Charles Dickens - cleared"
eliot = r"C:\Users\Cullen\Downloads\AABooks\George Eliot - cleared"
hardy = r"C:\Users\Cullen\Downloads\AABooks\Thomas Hardy - cleared"

sources.append(dickens)
sources.append(eliot)
sources.append(hardy)

for source in sources:
    for filename in os.listdir(source):
        f = os.path.join(source, filename)
        if os.path.isfile(f):
            with open(f,
                      encoding="utf8") as file:
                long_description = file.read()
                split = long_description.split()
                wordCount = len(split)

                for i in words:
                    occ = long_description.count(i)
                    prob.append(occ / wordCount)
                finArr.append(prob)

print(finArr)