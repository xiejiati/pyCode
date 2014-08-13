__author__ = 'xiejiati'

import re
path = r'I:\Source_1900\driver\Settings\Default\Environment-2\Controls\Controls.zcui'

p = re.compile(r'name="GROUP(\d+)"')

length = 0
with open(path, 'r') as f:
    for line in f:
        m = p.search(line)
        if not m: continue

        num = m.group(1)
        if int(num) > length:
            length = int(num)

print length