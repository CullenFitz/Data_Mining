import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

words = [" ", "charge", "glass", "faith", "then", "alone", "passion",
         "corner", "must", "somewhat", "dropped", "difficult", "one",
         "seemed", "give", "flower"]

DickensBooks = ["A Tale of Two Cities", "Barnaby Rudge", "Bleak House", "David Copperfield", "Dombey and Son",
         "Great Expectations", "Hard Times", "Little Dorrit", "Martin Chuzzlewit", "Nicholas Nickleby",
         "Oliver Twist", "Our Mutual Friend", "The Mystery of Edwin Drood", "The Old Curiosity Shop",
         "The Posthumous Papers of The Pickwick Club"]

EliotBooks = ["Adam Bede", "Daniel Deronda", "Felix Holt, the Radical",
         "Middlemarch", "Romola", "Silas Marner", "The Mill on the Floss"]

HardyBooks = ["A Laodicean", "A Pair of Blue Eyes",
         "Deperate Remedies", "Far From the Madding Crowd", "Jude the Obscure", "Tess of the d'Urbervilles",
         "The Hand of Ethelberta", "The Mayor of Casterbridge", "The Return of the Native", "The Trumpet-Major",
         "The Well-Beloved", "The Woodlanders", "Two on a Tower", "Under the Greenwood Tree"]

books = []
books.append(DickensBooks)
books.append(EliotBooks)
books.append(HardyBooks)

finArr = []
finArr.append(words)
sources = []

dickens = r"C:\Users\Cullen\Downloads\AABooks\Charles Dickens - cleared"
eliot = r"C:\Users\Cullen\Downloads\AABooks\George Eliot - cleared"
hardy = r"C:\Users\Cullen\Downloads\AABooks\Thomas Hardy - cleared"

sources.append(dickens)
sources.append(eliot)
sources.append(hardy)
count = 0
for source in sources:
    for filename in os.listdir(source):
        count += 1;
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
#print(df)


"""
Make 3 seperate tables for each author. X Axis has words, Y axis has occurences. Do this for each author
"""
