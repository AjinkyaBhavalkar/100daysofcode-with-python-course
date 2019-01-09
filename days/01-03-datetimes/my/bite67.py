""" Working with Datetimes.
1. We kicked our datetime on March 30th 2017 calculate what date we finish full 100 days. (modification) If you start your 100 days anyday, calculate when you will finish.
Accepted inputs are date or today.
2. PyBites was founded on 19th December 2016 and Pycon is on 8th May 2018. How many days from pybites' inception to pycon ?
"""

from datetime import datetime
from datetime import timedelta

# 1. 100 days from any day as input.     

rawDate = input("Enter the Start date in this format: yyyy/mm/dd : " )
split_date = rawDate.split("/")
start = datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))
diff = timedelta(100)

finish = start + diff
print("Your 100 days of coding in Python will complete on", finish) 


# 2. difference between two dates

rawDate = input("Enter the start date in this format: yyyy/mm/dd : ")
split_date = rawDate.split("/")
start = datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))

rawDate = input("Enter the end date in this format: yyyy/mm/dd : ")
split_date = rawDate.split("/")
end = datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))

daysinbetween = str(end - start)
print("There were ", daysinbetween, "in between")
