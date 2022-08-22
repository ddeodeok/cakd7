import sys
result = 1
args = sys.argv

for i in args[1:6]:
    result *=int(i)
print(result)