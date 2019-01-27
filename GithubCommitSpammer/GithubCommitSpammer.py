import os
import sys
import datetime

def createCommit(filename, commitmessage):
    os.system('cd C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam & git init & echo test > C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam\\' + filename + '.txt & git add . & git commit -m \"' + commitmessage + '\" & git remote -v & git push origin master')


githubURL = "https://github.com/Rishabhja101/Spam.git"
localURL = "C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam"


date = datetime.date(1943,3, 31)
date += datetime.timedelta(days=1)
print (str(date.month) + "-" + str(date.day)  + "-" + str(date.year))

os.system("date 04/01/18")
