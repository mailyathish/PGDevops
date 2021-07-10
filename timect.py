#!/usr/bin/env python
import os
import sys

import time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

import splunklib.client as client
import splunklib.results as results
import csv
import datetime
import urllib2
import base64
from datetime import date,timedelta
import ssl


HOST = "lenlspksrhp01.jcpenney.com"
PORT = 8089
USERNAME = "yningapp"
PASSWORD = base64.b64decode("QmFuZ2Fsb3JlNjYwJCQ=")



#date_time = '29.08.2011 11:05:02'  -- Format of date
Env = sys.argv[1]   ## Environment 
Ftstamp = sys.argv[2]  ## From
Ttstamp = sys.argv[3]  ## Time
Release = sys.argv[4]


pattern = '%d.%m.%Y %H:%M:%S'
Fepoch = int(time.mktime(time.strptime(Ftstamp, pattern)))
print Fepoch

Tepoch = int(time.mktime(time.strptime(Ttstamp, pattern)))
print Tepoch


#os.environ['TZ']='UTC'
#epoch = int(time.mktime(time.strptime(tstamp,pattern)))
#print epoch

# Establish Splunk Connection
service = client.connect(
   host=HOST,
   port=PORT,
   username=USERNAME,
   password=PASSWORD)




file = open(r"./queries.txt","r")
path = "/home/centos/auto/inputdir/"

def get_filename_datetime(filename):
    # Use current date to get a text file name.
       return  filename + Release+".csv"


for line in file:
       currentline = line.split("~")
       name = get_filename_datetime(str(currentline[0]+"-Perf-Run-"))
       Query = "search index=dp-cloud host=*"+Env+"* earliest="+str(Fepoch)+" latest="+str(Tepoch)+" "+str(currentline[1])
       print(Query)
       job = service.jobs.create(Query, **{"exec_mode": "blocking",'status_buckets': '0'})
       search_results = job.results(**{"output_mode": "csv"})
       print (name)
       f = open(path+name, 'a')
       f.write(search_results.read())






