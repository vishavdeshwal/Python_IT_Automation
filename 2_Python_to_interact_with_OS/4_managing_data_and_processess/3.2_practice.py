import re
import csv
import sys

file = sys.argv[1]
pattern1 = r"(\([a-zA-Z]+\))"
pattern2 = r""

count = 0
count2 = 0
with open(file) as f:
    for line in f:
        if "CRON" in line:
            result = re.search(pattern1, line)
            if result != None:
                count += 1
                print(result[1])


print(count)
