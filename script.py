import subprocess, re
from datetime import datetime

def run(*args):
    return subprocess.check_call(['git'] + list(args))


run("add", ".")
commitMessage = ""
status = subprocess.getoutput('git status')

if re.search('Your branch is ahead of', status):
    print("Already Commited - Just Pushing :)")
    run("push")
    exit()
    
elif checkIfNecessary := re.search('nothing to commit, working tree clean', status):
    print("Nothing to commit :(")
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

print("Pushing Process - Started.")

run("commit", "-m", commitMessage)

print(commitMessage)
#run("push")

print("Pushing Process - Done.")

exit()
