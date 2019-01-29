import os
import sys
import datetime

def createCommit(filename, commitmessage):
    os.system('cd C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam & git init & echo test > C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam\\' + filename + '.txt & git add . & git commit -m \"' + commitmessage + '\" & git remote -v & git push origin master')

def setDate(date):
    os.system("date " + (str(date.month) + "-" + str(date.day)  + "-" + str(date.year)))
    print((str(date.month) + "-" + str(date.day)  + "-" + str(date.year)))

def deleteFiles(directory):
    filelist = [ f for f in os.listdir(directory) if f.endswith(".txt") ]
    for f in filelist:
        os.remove(os.path.join(directory, f))

def spamCommits(date):
    deleteFiles("C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam")
    for i in range(1, 366 * 3):
        setDate(date)
        createCommit(str(i), "created new file")
        date += datetime.timedelta(days=1)
    os.system("W32tm /resync /force")

date = datetime.date(2011, 4, 26) # year, month, day

spamCommits(date)
