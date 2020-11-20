import os
import re
import sys

result={}

for file in os.listdir("ft_fun"):
    f = open("ft_fun/"+file, 'r')
    r = f.read()
    line = re.search(r'//file([0-9]*)', r) 
    nb = int(line.group(1))
    result[nb] = r
    f.close()

with open("script.c", 'w') as file:
    sys.stdout = file

    for _, value in sorted(result.items()):
        print(value)

    file.close()