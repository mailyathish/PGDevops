import os,re
import glob
import pandas as pd
#from os import walk
import os.path
from os import path

import pandas as pd

path = "./R5/"
path1 ="./R6/"

"""
allFiles = glob.glob(os.path.join(path,"*.csv"))



li = []

for filename in allFiles:
    ##df = pd.read_csv(filename, index_col=None, header=0)
    ##li.append(df)
    
frame = pd.concat(li, axis=0, ignore_index=True)
print(frame) 


file_location = './R4/promise*.csv'
file_name = os.path.basename(file_location )
print(file_name) 
"""


for root, dirs, files in os.walk(path, topdown=False):
    for file in files:
    	filenname = file.split('-')
    	fname = filenname[0]
    	#print( os.path.abspath(file))
    	for filename in os.listdir('./R5/'):
    		print("")
    		if re.match(fname, filename):    
       		    PreviousRelease = os.path.abspath(path+file)
       		    CurrentRelease = os.path.abspath(path1+filename)
       		    print(PreviousRelease)
       		    print(CurrentRelease)
       		    
       		    firstProductSet = pd.read_csv(PreviousRelease)
       		    
       		    df1 = pd.DataFrame(firstProductSet,columns= ['Endpoint', 'StatusCode', 'Method','TPS','P95'])
       		    secondProductSet = pd.read_csv(CurrentRelease)
       		    df2 = pd.DataFrame(secondProductSet,columns= ['Endpoint', 'StatusCode','Method','TPS','P95'])
       		    output1 = pd.merge(df1, df2, on=["Method","StatusCode","Endpoint"],how='outer',suffixes=('-R4', '-R5'))


       		    output1.to_csv(fname+".csv",header=True, index=False)
       		    output1.to_csv('my_csv.csv', mode='a', header=True, index=False)

       		  








