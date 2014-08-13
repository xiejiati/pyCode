__author__ = 'xiejiati'

from re import *

reToBeRepl = r'for_each\(allof\((.*)\),(.*)'
reRepl = r'for ('r'auto iter = \1.begin(); iter != \1.end(); ++iter)'

filePath = r'D:\Users\xiejiati\Desktop\New Text Document.txt'

p = compile(reToBeRepl, I)

f = open(filePath, 'r')

lines = f.readlines()

i = -1
hitCount = 0
for line in lines:
    i += 1
    if p.search(line):
        lines[i] = p.sub(reRepl, line)
        hitCount += 1
        pass

f.close()

#write back to the file
f = open(filePath, 'w')

f.writelines(lines)

f.close()
print(hitCount)














