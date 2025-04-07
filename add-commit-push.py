import subprocess 
import sys 

print("Add Commit Push")
print("Executing \" Git Status\":")
print("")

resultGitStatus = subprocess.run(["git", "status"], capture_output=True, text=True)

print(resultGitStatus.stdout) 

print("Executing \"git add -A\":")

resultGitAdd = subprocess.run(["git", "add" "-A"], capture_output=True, text=True)
print(resultGitAdd.stdout) 
print("")

print("Executing \"git commit -m\":")
print("")

message = "\"Update files.\""
if len(sys.argv) ==3:
    message = sys.argv[2]
    print (message)

resultGitCommit = subprocess.run(["git", "commit" "-m", message], capture_output=True, text=True)
print(resultGitCommit.stdout)
print("")

print("Executing \"git push\":")
print("")

resultGitPush = subprocess.run(["git", "push"], capture_output=True, text=True)
print(resultGitPush.stdout)
print("")