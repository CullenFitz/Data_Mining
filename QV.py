import numpy as np
import os
import matplotlib.pyplot as plt

words = ["charge", "glass", "faith", "then", "alone", "passion",
         "corner", "must", "somewhat", "dropped", "difficult", "one",
         "seemed", "give", "flower"]

finArr = []
sources = []

dickens = r"C:\Users\Cullen\Downloads\AABooks\Charles Dickens - cleared"
eliot = r"C:\Users\Cullen\Downloads\AABooks\George Eliot - cleared"
hardy = r"C:\Users\Cullen\Downloads\AABooks\Thomas Hardy - cleared"

sources.append(dickens)
sources.append(eliot)
sources.append(hardy)

for source in sources:
    #print(source)
    for filename in os.listdir(source):
        f = os.path.join(source, filename)
        if os.path.isfile(f):
            #print(f)
            prob = []
            with open(f, encoding="utf8") as file:
                long_description = file.read()
                split = long_description.split()
                wordCount = len(split)
                for i in words:
                    occ = long_description.count(i)
                    prob.append(occ / wordCount)
                finArr.append(prob)

for i in finArr:
    print(i)

plt.imshow(finArr)
plt.colorbar()
plt.show()
