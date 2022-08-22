import sys
arg = sys.argv[1]
if "-a" == arg:
    with open('test.txt','a') as f:
        arg = sys.argv[2]
        f.write(arg)
        f.write("\n")
        arg = sys.argv[3]
        f.write(arg)
        f.write("\n")
    
else:
    with open('test.txt','w') as f:
        arg = sys.argv[1]
        f.write(arg)
        f.write("\n")
        arg = sys.argv[2]
        f.write(arg)
        f.write("\n")