import os

import glob

for f in glob.glob('./R4/*.csv'):
    TargetttedFiles = os.path.split(f)[-1]
    print(TargetttedFiles)


for filename in os.listdir('./R5/'):
    if filename.startswith(TargetttedFiles):
        #print(filename)


"""for f in glob.glob('./R5/*.csv'):
    print(os.path.split(f)[-1]). """