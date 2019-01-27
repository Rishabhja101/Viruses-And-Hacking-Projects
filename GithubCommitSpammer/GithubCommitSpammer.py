import subprocess
import os


def createCommit(filename):
    os.system('cd C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam & git init & echo test > C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam\\' + filename + '.txt & git add . & git commit -m \"test commit\" & git remote -v & git push origin master')

githubURL = "https://github.com/Rishabhja101/Spam.git"
localURL = "C:\\Users\\risha\\OneDrive\\Documents\\GitHub\\Spam"

createCommit('0')
