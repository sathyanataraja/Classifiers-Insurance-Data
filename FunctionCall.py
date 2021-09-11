import pandas as pd
from ClassifiersUtils import *

df = pd.read_csv('heart.csv')

df1 = df.copy()
del df1['Target']

KNN = RunKNN(df1, df['target'], 0.25, 40, 5)

DT = RunDecisionTree(df1, df['target'], 0.25, 40,15)

RF = RunRandomForest(df1, df['target'], 0.25, 40,5)

GB = RunGradientBoostingClassifier(df1, df['target'], 0.25, 40)

XGB = RunXGBOOST(df1, df['Status'], 0.33, 45)


