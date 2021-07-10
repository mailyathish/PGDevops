#!/usr/bin/env 
import paramiko
import socket
import sys
import os
import tarfile
from scp import SCPClient


if sys.argv[1]=="" or sys.argv[2]=="":
   print("missing arguments ")	
   exit()

file = open(r"./host.txt","r")
jmeter_path = "/home/centos/apache-jmeter-5.1.1.zip"
current_dir = os.path.dirname(os.path.abspath(__file__))

folderCopy = sys.argv[1]
output_filename = sys.argv[2]
output_file = sys.argv[2]
scriptPath=""
createDir = "cd 2021_Prod_Release_Validation_Scripts;mkdir "+output_filename+" ;cd "+output_filename+"/"+" ;pwd"
#print("Create Dir"+createDir)



#print(sys.argv[1])
if os.path.isdir(folderCopy):
   #print("folder:"+folderCopy)
   #print("file:"+output_filename)
   def make_tarfile(output_filename, folderCopy):
        with tarfile.open(output_filename+".tar.gz", "w:gz") as tar:
            tar.add(folderCopy, arcname=os.path.basename(folderCopy))
            print("Created :"+output_filename)

print("Zipping Source Files :")		
make_tarfile(output_filename, folderCopy)

#print("Tar files :"+output_filename)
output_filename+=".tar.gz"
#print("Tar files :"+output_filename) 

for server_name in file:
    try:
            #Paramiko.SSHClient can be used to make connections to the remote server and transfer files
        print("Establishing ssh connection: "+server_name)

        key = paramiko.RSAKey.from_private_key_file("experiment_user.pem.txt")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("connecting:"+server_name)
        client.connect( hostname = server_name, username = "centos", pkey = key )
        print("Connected to the server:"+server_name)
	
        # Define progress callback that prints the current percentage completed for the file
	def progress(filename, size, sent):
    		sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )

	# SCPCLient takes a paramiko transport and progress callback as its arguments.
	scp = SCPClient(client.get_transport(), progress=progress)	
	

	def progress4(filename, size, sent, peername):
	    sys.stdout.write("(%s:%s) %s's progress: %.2f%%   \r" % (peername[0], peername[1], filename, float(sent)/float(size)*100) )
	scp = SCPClient(client.get_transport(), progress4=progress4)

	

	scp.put('apache-jmeter-5.1.1.zip', '/home/centos/apache-jmeter-5.1.1.zip')
	print("")


	
	def FolderCreator():    
   	     bash_script = open("script.sh").read()
    	     # read the BASH script content from the file
             # execute the BASH script
             stdin, stdout, stderr = client.exec_command(bash_script)
             #stdin, stdout, stderr = client.exec_command(createDir)
             # read the standard output and print it
             print(stdout.read().decode())
             # print errors if there are any
             err = stderr.read().decode()
             if err:
                print(err)
	     

	     stdin, stdout, stderr = client.exec_command(createDir)
	     scriptPath = stdout.read()	
             scriptPath = scriptPath.rstrip()
             scriptPath = scriptPath+ os.path.sep
             print("changed :"+scriptPath)
             print(stdout.read().decode())
	     if err:
	        print(err)
             scp.put(output_filename,scriptPath)
             print("")


	FolderCreator()
	VarExtractor = "cd 2021_Prod_Release_Validation_Scripts/"+output_file+"; tar -xzf"+output_filename+"; chmod -R 777 /home/centos/2021_Prod_Release_Validation_Scripts/"
	def TarExtractor():
	    #print(VarExtractor)
	    stdin, stdout, stderr = client.exec_command(VarExtractor)
            print(stdout.read().decode())		
	
	TarExtractor()


    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials")
    except paramiko.SSHException as sshException:
        print("Could not establish SSH connection: %s" % sshException)
    except socket.timeout as e:
        print("Connection timed out")
    except Exception,e:
        print("Exception in connecting to the server")
        print("PYTHON SAYS:",e)

    finally:
        client.close()
	
