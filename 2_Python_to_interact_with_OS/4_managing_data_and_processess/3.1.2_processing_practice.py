import re
import sys 


file=sys.argv[1]
pattern=r"\'(\w+)\'"
with open(file) as f:
    for line in f:
        if re.search(pattern, line):
            result = re.search(pattern, line)
            print(result[1])
        else:
            print("No match found in line: ")