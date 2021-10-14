import subprocess, re
from datetime import datetime

def run(*args):
    return subprocess.check_call(['git'] + list(args))


commitMessage = ""

status = subprocess.getoutput('git status')
if checkIfNecessary := re.search('nothing to commit, working tree clean', status):
    exit()

else:
    searchModified = re.findall('modified:(.*)\n', status)
    for modified in searchModified:
        commitMessage += "Modified: " + modified.strip() + "\n"

    searchAdded = re.findall('added:(.*)\n', status)
    for added in searchAdded:
        commitMessage += "Added: " + added.strip() + "\n"


    searchDeleted = re.findall('deleted:(.*)\n', status)
    for deleted in searchDeleted:
        commitMessage += "Removed: " + deleted.strip() + "\n"


    searchRenamed = re.findall('renamed:(.*)\n', status)
    for renamed in searchRenamed:
        commitMessage += "Renamed: " + renamed.strip() + "\n"
        
run("add", ".")
run("commit", "-m", commitMessage)
run("push")
exit()
