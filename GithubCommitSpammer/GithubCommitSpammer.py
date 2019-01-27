import os
import sys
import datetime
import pywin32

def createCommit(filename, commitmessage):
    os.system('cd C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam & git init & echo test > C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam\\' + filename + '.txt & git add . & git commit -m \"' + commitmessage + '\" & git remote -v & git push origin master')

def _win_set_time(time):
    dayOfWeek = datetime.datetime(time).isocalendar()[2]
    pywin32.SetSystemTime( time[:2] + (dayOfWeek,) + time[2:])

githubURL = "https://github.com/Rishabhja101/Spam.git"
localURL = "C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam"

startTime = ( 2018, # Year
              1, # Month
              1, # Day
              0, # Hour
              0, # Minute
              0, # Second
              0, # Millisecond
          )

_win_set_time(startTime)

#for i in range(1, 365):
#    createCommit(i, "test commit")
