import sys, getopt
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report

argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv,"hi:",["ifile="])
except getopt.GetoptError:
    print ('StatCalculator.py -i <inputfile>')
    sys.exit(2)


inputFile = ""

for o, a in opts:
    if o in ("-i", "--input"):
        inputFile = a


if (len(opts) == 0 or inputFile==""):
    print ('StatCalculator.py -i <inputfile>')
    sys.exit(2)



df = pd.read_csv(inputFile, sep="\t")
P = df['P'].values
GS = df['GS'].values
#P  GS

y_pred = np.array(P)
y_true = np.array(GS)

allLabels = np.concatenate((y_pred,y_true))

labels = list(set(allLabels))
labels.sort()

print(classification_report(y_true, y_pred, target_names=labels,zero_division=0))
