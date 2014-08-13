__author__ = 'xiejiati'

from re import *

reTobeRepl = r'for_each\(allof\((\w+)(.*)'
reRepl = r'for ('r'auto iter = \1.begin(); iter != \1.end(); ++iter)'

filePath = r''

p = compile(reTobeRepl, I)
pElementDot = compile(r'element[.]', I)
pElement = compile(r'element', I)
pEnd = compile(r'[}][)][;]')

f = open(filePath, 'r')

lines = f.readlines()

i = -1
hitCount = 0
enterScope = False
for line in lines:
    i += 1
    if (not enterScope) and p.search(line):
        lines[i] = p.sub(reRepl, line)
        hitCount += 1
        enterScope = True
        continue

    if (enterScope and pElementDot.search(line)):
        lines[i] = pElementDot.sub(r'iter->', line)
        continue

    if (enterScope and pElement.search(line)):
        lines[i] = pElement.sub(r'*iter', line)
        continue

    if (enterScope and pEnd.search(line)):
        lines[i] = pEnd.sub(r'}', line)
        enterScope = False
        continue

f.close()

#write back to the file
f = open(filePath, 'w')

f.writelines(lines)

f.close()
print(hitCount)














