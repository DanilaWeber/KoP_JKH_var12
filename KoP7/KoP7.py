import pandas as pd 
import numpy as np

studentsPerfDF = pd.read_csv('')

studentWithBadReadingScore = studentsPerfDF[studentsPerfDF['reading score']<=studentsPerfDF['reading score'].mean()]
print(studentWithBadReadingScore)

f = lambda x: str(x[len(x)//2:]) + str(x[:len(x)//2-1])
