import sys
import os
import re

def cd(path=None):
    # print os.getcwd()
    try:
        if(path!=None):
            os.chdir(path)
        else:
            os.chdir(os.path.expanduser("~"))
    except:
        print "OOPS..! you entered something wrong *_*"
    # print os.getcwd()

def pwd():
    try:
        print os.getcwd()
    except:
        print "Something went wrong... :("

def ls(path=None):
    try:
        if path==None:
            path=os.getcwd()
        if path=="~":
            path=os.path.expanduser("~")
        
        file_list = os.listdir(path)
        for name in file_list:
            if name[0]!='.':
                print name
    except:
        print "Something went wrong... :("

def touch(files):
    if(len(files)<2):
        print "Wrong number of arguments"
        return

    try:
        for file in files:
            if file=="touch":
                continue
            
            # lslash = file.rfind('/')
            # dirname = file[:lslash+1]
            # print dirname
            # if os.path.isdir(dirname):
            try:
                with open(file, 'a'):
                    os.utime(file, None)
            except:
                print "Error in path... :( " + file
    except:
        print "Something went wrong... :("
        
def head(files):
    if(len(files)<2):
        print "Wrong number of arguments"
        return

    multiple=0
    if len(files)>2:
        multiple=1
    try:
        for file in files:
            if file=="head":
                continue
            
            if os.path.isfile(file):
                try:
                    with open(file) as f:
                        lines=f.readlines()

                        if multiple==1:
                            print "==> "+file+" <=="
                        for i in range(min(10,len(lines))):
                            print lines[i],
                        print
                except:
                    print "Error in "+file
    except:
        print "Something went wrong... :("

def tail(files):
    if(len(files)<2):
        print "Wrong number of arguments"
        return

    multiple=0
    if len(files)>2:
        multiple=1
    try:
        for file in files:
            if file=="head":
                continue
            
            if os.path.isfile(file):
                try:
                    with open(file) as f:
                        lines=f.readlines()
                        # lines.reverse()
                        if multiple==1:
                            print "==> "+file+" <=="
                        loop=min(10,len(lines))
                        for i in range(len(lines)-loop,len(lines)):
                            print lines[i],
                        print
                except:
                    print "Error in "+file
    except:
        print "Something went wrong... :("
    
def tr(args):
    if(len(args)<3):
        print "Wrong number of arguments"
        return

    change_from = args[1]
    change_to = args[2]
    map = {}
    for i in range(len(change_from)):
        if i>len(args[2])-1:
            cto=change_to[len(args[2])-1]
        else:
            cto=change_to[i]

        map[change_from[i]]=cto

    print "Press $ to exit tr"
    while 1:
        inp = raw_input()
        if inp=='$':
            break

        for i in inp:
            if i in map.keys():
                sys.stdout.write(map[i])
            else:
                sys.stdout.write(i)
        print

def grep(command):
    try:
        l = [pos for pos, char in enumerate(command) if char == '"']
        pattern = command[l[0]+1:l[1]]
        text = command[l[2]+1:l[3]]
        sub = [m.start() for m in re.finditer(pattern, text)]
        if len(sub)<1:
            return

        count=0
        for i in range(len(text)):
            if i in sub:
                count=len(pattern)
                sys.stdout.write('\033[91m\033[1m')
            sys.stdout.write(text[i])
            count=count-1
            if count==0:
                sys.stdout.write('\033[0m')

        print
    except:
        print "Something went wrong... :("

def sed(command):
    try:
        l = [pos for pos, char in enumerate(command) if char == '"']
        first = command[l[0]+1:l[1]]
        text = command[l[2]+1:l[3]]
        l = [pos for pos, char in enumerate(first) if char == '/']
        change_from = first[l[0]+1:l[1]]
        change_to = first[l[1]+1:l[2]]
        ls = text.split(change_from)
        sub = change_to.join(ls)
        print sub
    except:
        print "Something went wrong... :("

sys.stdout.write('\033[92m\033[1m'+"You are in Python Shell now:"+'\033[0m\n')
while 1:
    cwd = os.getcwd()
    prompt = cwd+"$ "
    sys.stdout.write('\033[94m\033[1m'+prompt+'\033[0m')
    raw_command=raw_input()
    command=raw_command.strip().split()
    # print command

    if command[0]=="cd":
        if len(command)>1:
            cd(command[1])
        else:
            cd()
    elif command[0]=="ls":
        if len(command)>1:
            ls(command[1])
        else:
            ls()
    elif command[0]=="pwd":
        if len(command)>1:
            print "pwd takes no arguments..."
        else:
            pwd()
    elif command[0]=="touch":
        touch(command)
    elif command[0]=="grep":
        grep(raw_command)
    elif command[0]=="head":
        head(command)
    elif command[0]=="tail":
        tail(command)
    elif command[0]=="tr":
        tr(command)
    elif command[0]=="sed":
        sed(raw_command)
    elif command[0]=="diff":
        pass
    elif command[0]=="exit":
        exit()
    else:
        print "Wrong command... :("