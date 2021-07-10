
import os
import sys
import numpy as np
import pandas as pd


filename1="/Users/yningapp/Documents/automation/data/Search-Perf-Run-R4-Release-May10.csv"
filename2="/Users/yningapp/Documents/automation/Search-Perf-Run-ECOM193-27MAY.csv"



firstProductSet = pd.read_csv(filename1)
df1 = pd.DataFrame(firstProductSet,columns= ['Endpoint', 'StatusCode','TPS','P95'])

#print(df1)

secondProductSet = pd.read_csv(filename2) 
df2 = pd.DataFrame(secondProductSet,columns= ['Endpoint', 'StatusCode','TPS','P95'])



#print(df2)

output1 = pd.merge(df1, df2, on=["StatusCode","Endpoint"],how='outer',suffixes=('-R4', '-R5'))





  
# displaying result
print(output1)