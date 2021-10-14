import subprocess

def run(*args):
    return subprocess.check_call(['git'] + list(args))


run("status")
run("add", ".")
run("commit", "-m", "Testing Purpose - 3")
run("push")
