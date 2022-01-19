import subprocess

subprocess.run(['ls','-la'])
#subprocess.run('ls -la',shell=True)    #If we set shell = true, no need to give args in a list

var = subprocess.run(['ls','-la'])
print(var)                          # CompletedProcess(args=['ls', '-la'], returncode=0)


# Directing the terminal output to the file
with open('shell_commands.txt','w') as fhandle:
    subprocess.run(['ls','-la'],stdout=fhandle,text=True) #text=True reqd else data is printed in binary format

# Chaining the input to the output
#inp = subprocess.run(['cat','shell_commands.txt'],stdout=subprocess.PIPE,text=True)
inp = subprocess.run(['cat','shell_commands.txt'],capture_output=True,text=True)
#print(inp.stdout)

out = subprocess.run(['grep','-n','IMG.jpg'],capture_output=True,text=True,input=inp.stdout)
print(out.stdout)


# Chaining the input to the output| another way
onetime = subprocess.run('cat shell_commands.txt | grep -n IMG.jpg',capture_output=True,text=True,shell=True)
print(onetime.stdout)
print(onetime.returncode)

# Printing error to standard output
err = subprocess.run(['ls','-la','unknownfile'],capture_output=True,text=True)
print(err.stderr)
print(err.returncode)

# Sending error to Dev NULL
devnull = subprocess.run(['ls','-la','unknownfile'],stderr=subprocess.DEVNULL)
print(devnull.stderr)