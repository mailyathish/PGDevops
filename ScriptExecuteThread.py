#!/usr/bin/env 
import paramiko
import socket
import sys
import os
import JConfig

file = open(os.path.abspath(sys.argv[1]),"r")
current_dir = os.path.dirname(os.path.abspath(__file__))

def ScriptExe():

    
    for line in file:
        try:
            currentline = line.split(",")

            print(currentline[0])
            print(currentline[1])
            print(currentline[2])

            scriptpath =JConfig.SPath+sys.argv[2]+JConfig.ScriptFolder+currentline[1]
            JMeterScript ="nohup  "+JConfig.JPath+" -Jthreads="+currentline[2]+" -n -t "+scriptpath+" > /dev/null 2>&1 & "
            JMeterScript = JMeterScript.replace("\n","") 
            print("script path :"+JMeterScript)
     
            

            #Paramiko.SSHClient can be used to make connections to the remote server and transfer files
            print("Establishing ssh connection: "+currentline[0])
            print("script1:"+currentline[1])
            key = paramiko.RSAKey.from_private_key_file("experiment_user.pem.txt")
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print("connecting:"+currentline[0])
            client.connect( hostname = currentline[0], username = "centos", pkey = key )
            print("Connected to the server:"+currentline[0])
            

        
            scriptpath =JConfig.SPath+sys.argv[2]+JConfig.ScriptFolder+currentline[1]
            print(scriptpath)
            print("Starting Execution  :"+scriptpath)
            #currentline[1] = currentline[1].rstrip("\n")
            JMeterScript ="nohup "+JConfig.JPath+" -Jthreads="+currentline[2]+" -n -t "+scriptpath+" > /dev/null 2>&1 & "
            JMeterScript = JMeterScript.replace("\n","") 
            print("script path :"+JMeterScript)

            stdin, stdout, stderr = client.exec_command(JMeterScript)
            print(stdout.read().decode())
            Process = "ps -eo pid,comm,lstart,etime,time,args | grep "+currentline[1]
            print(Process)
            stdin, stdout, stderr = client.exec_command('ps -ef | grep -v grep | grep java | awk \'{print $2}\'')
            stdin, stdout, stderr = client.exec_command(Process)
            pid = stdout.readline()
            print("Started : " + pid)
            scriptpath=""
            JMeterScript=""
            

        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials")
        except paramiko.SSHException as sshException:
            print("Could not establish SSH connection: %s" % sshException)
        except socket.timeout as e:
            print("Connection timed out")
        except Exception:
            print("Exception in connecting to the server")
            print("PYTHON SAYS:",e)

        finally:
            client.close()
            


def main():
        
    ScriptExe()

    #root.mainloop()


if __name__ == "__main__":


    
    main()
	
