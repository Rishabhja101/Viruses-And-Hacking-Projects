import os
import sys
import datetime

def createCommit(filename, commitmessage):
    os.system('cd C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam & git init & echo test > C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam\\' + filename + '.txt & git add . & git commit -m \"' + commitmessage + '\" & git remote -v & git push origin master')

def setDate(date):
    os.system("date " + (str(date.month) + "-" + str(date.day)  + "-" + str(date.year)))
    print((str(date.month) + "-" + str(date.day)  + "-" + str(date.year)))

def spamCommits(date):
    for i in range(1, 100):
        setDate(date)
        createCommit(str(i), "created new file")
        date += datetime.timedelta(days=1)

date = datetime.date(2017,1, 1) # year, month, day

#setDate(date)
spamCommits(date)
