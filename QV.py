import pandas as pd
import numpy as np
import nltk
import os

words = ["charge", "glass", "faith", "then", "alone", "passion",
         "corner", "must", "somewhat", "dropped", "one",
         "seemed", "give", "flower"]

finArr = [["charge", "glass", "faith", "then", "alone", "passion",
         "corner", "must", "somewhat", "dropped", "one",
         "seemed", "give", "flower"]]
with open(r'C:\Users\Cullen\Downloads\AABooks\Charles Dickens - cleared/BARNABY RUDGE.txt', encoding="utf8") as file:
    long_description = file.read()
    split = long_description.split()
    wordCount = len(split)

prob = []
for i in words:
    occ = long_description.count(i)
    prob.append(occ/wordCount)
    finArr.append(prob)
for i in finArr:
    print(i)