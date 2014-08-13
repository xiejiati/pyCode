__author__ = 'xiejiati'

import  re

logFilePath = r''

p = re.compile(r'failed.*(\[I:\\.*\.mac\])', re.I)

lines = []
fileName = ''
with open(logFilePath, 'r') as f:
    for line in f:
        m = p.search(line)
        if not m: continue

        lines.append(m.group(1)+'\n')
        if fileName != '': continue
        fileName = m.group(1)[:-5].rpartition('\\')[-1]

fileRecPath = r'D:\Users\xiejiati\Desktop' + '\\' + fileName + 'FailedMacs.txt'

f = open(fileRecPath, 'w+')
f.writelines(lines)
f.close()
