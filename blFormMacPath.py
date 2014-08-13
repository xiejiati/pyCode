__author__ = 'xiejiati'

import re
import os

macPath = r"I:\Source_1900\Macro\InHouse\CAD\Tutorials\CADFundamentals\CdIferChk1.mac"

lstPath = macPath.split('\\')
lstPath[1] = 'Binary'

name = re.sub(r'(\w+)\.mac', r'\1', lstPath[-1])

dirPath = '\\'.join(lstPath[:-1])

filePath = ''
num = 0
for dir in os.listdir(dirPath):
    dir = dirPath+'\\'+dir
    if os.path.isfile(dir) and dir.endswith('.bl'):
         m = re.search(name+r'\.?(\d)?', dir)
         if not m:
             continue

         if not m.group(1):
             filePath = dir
             break
         tmpNum = int(m.group(1))
         if tmpNum > num:
             num = tmpNum
             filePath = dir

filePath = dirPath+'\\'+filePath

try:
    os.startfile(filePath)
except:
    pass

pass



















