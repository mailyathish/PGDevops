#!/usr/bin/env
import paramiko
import socket
import sys
import os
import tarfile
from scp import SCPClient



file = open(r"./scripts.txt","r")
current_dir = os.path.dirname(os.path.abspath(__file__))

scriptpath=""
JMeterScript=""


for line in file:
    try:

        currentline = line.split(",")
            #Paramiko.SSHClient can be used to make connections to the remote server and transfer files
        print("Establishing ssh connection: "+currentline[0])
        print("script1:"+currentline[1])
        key = paramiko.RSAKey.from_private_key_file("experiment_user.pem.txt")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("connecting:"+currentline[0])
        client.connect( hostname = currentline[0], username = "centos", pkey = key )
        print("Connected to the server:"+currentline[0])

	def ScriptKill():

	    #Process = "ps -ef pid | grep "+currentline[1]
            #print(Process)
            stdin, stdout, stderr = client.exec_command('ps -ef | grep -v grep | grep java | awk \'{print $2}\'')
            pid = stdout.readline().strip()
            print "PID of the remote process: " + pid
	    stdin, stdout, stderr = client.exec_command('kill -9 '+pid)
	    print(stdout.readline())
            

        ScriptKill()

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
