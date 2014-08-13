__author__ = 'xiejiati'

import re
path = r'I:\Source_1900\assem\src\exp\AsmExpViewUtil.cpp'

p1 = re.compile(r'.*\(.*\).*')
p2 = re.compile(r'(\s*)\}\s*')
p3 = re.compile(r'(\s*)\{\s*')

lines = []
with open(path, 'r') as f:
    lines = f.readlines()

count = len(lines)
i = 0
while i < count:
    j = 0
    if lines[i].strip() == '{' and p1.search(lines[i-1]):
        m1 = p3.search(lines[i])
        while True:
            m2 = p2.search(lines[i+j+1])
            if m2 and m1.group(1) == m2.group(1):
                break
            j += 1
        if j <= 5 and (not lines[i-1].strip().startswith('inline')):
            lines[i-1] = 'inline '+lines[i-1]
    i += j+1


with open(path, 'w') as f:
    f.writelines(lines)

