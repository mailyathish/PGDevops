

#!/usr/bin/env
import paramiko
import socket
import sys
import os
import tarfile

folderCopy = sys.argv[1]
output_filename = sys.argv[2]

#print(sys.argv[1])
print(folderCopy)
if os.path.isdir(folderCopy):
    print("folder:"+folderCopy)
    print("file:"+output_filename)
    def make_tarfile(output_filename, folderCopy):
        with tarfile.open(output_filename+".tar.gz", "w:gz") as tar:
            tar.add(folderCopy, arcname=os.path.basename(folderCopy))

make_tarfile(output_filename, folderCopy)
