
# !/usr/bin/python



import os
from os import walk
fileDirectory = '\home\centos\auto\inputdir'

outputDirectory = '/home/centos/auto/outputdir/'
for root, dirs, files in os.walk("/home/centos/auto/inputdir/", topdown=False):
    for file in files:
        print(file)
        headerCopied = False
        with open(root + file, "r") as input:
            with open(outputDirectory + file, "w") as output:
                for line in input:
                    if not line.startswith('Endpoint'):
                        output.write(line)
                    else:
                        if not headerCopied:
                            output.write(line)
                            headerCopied = True
