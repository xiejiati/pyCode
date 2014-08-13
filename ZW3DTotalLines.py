__author__ = 'xiejiati'

import os

startPath = r''
filterType = []
filterType.append('h')
filterType.append('hpp')
filterType.append('c')
filterType.append('cpp')

def countZW3D(startPath, lineCount):
    if os.path.islink(startPath) or startPath == '..' or startPath == '.':
        return
    lstDir = os.listdir(startPath)
    for dir in lstDir:
        dir = startPath+'\\'+dir
        if os.path.isfile(dir) and dir.rpartition('.')[-1] in filterType:
            inComment = False

            with open(dir, 'r') as f:
                for line in f:

                    line = line.strip()

                    if line == '':
                        continue

                    if line.startswith('//'):
                        continue

                    if line.startswith('/*'):
                        if not line.endswith('*/'):
                            inComment = True
                        continue

                    if line.endswith('*/'):
                        inComment = False
                        continue


                    if not inComment:
                        lineCount[0] += 1

        elif os.path.isdir(dir):
            countZW3D(dir, lineCount)


lineCount = []
lineCount.append(0)

countZW3D(startPath, lineCount)

print(lineCount[0])








