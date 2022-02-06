import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd

words = ["charge", "glass", "faith", "then", "alone", "passion",
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
authInd = 0
for source in sources:
    authInd += 1
    bookInd = 0
    #print(authInd)
    for filename in os.listdir(source):
        bookInd += 1
        #print(bookInd)
        f = os.path.join(source, filename)
        if os.path.isfile(f):
            prob = []
            #prob.append(books[authInd][bookInd])
            with open(f, encoding="utf8") as file:
                long_description = file.read()
                split = long_description.split()
                wordCount = len(split)
                for i in words:
                    occ = long_description.count(i)
                    prob.append(occ / wordCount)
                finArr.append(prob)

#for i in finArr:
    #print(i)

print(pd.DataFrame(finArr))

