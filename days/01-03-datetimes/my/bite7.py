'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime, timedelta
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
       
    stamp = line.split()
    datetimestamp = stamp[1].split("T")
    # datetimestamp string 
    datestamp = datetimestamp[0].split("-")
    timestamp = datetimestamp[1].split(":")
    dt = datetime(int(datestamp[0]), int(datestamp[1]), int(datestamp[2]), int(timestamp[0]), int(timestamp[1]), int(timestamp[2]))
       
    return dt


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
       
    shutdown_lines = []
    # text processor that searches for lines with "shutdown initiated" string. 
    for line in loglines:
        if (line.find(SHUTDOWN_EVENT) != -1 ):
            print("Hurray")
            shutdown_lines.append(line)
            
    
    print(shutdown_lines)
    # Use the convert_to_datetime function on that string to get datetimestamp. 
    return convert_to_datetime(shutdown_lines[-1]) - convert_to_datetime(shutdown_lines[0])       



       
      
