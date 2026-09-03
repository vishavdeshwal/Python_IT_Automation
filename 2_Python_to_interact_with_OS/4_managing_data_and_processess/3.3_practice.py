import re
import csv
import sys

file = sys.argv[1]
pattern1 = r"(\([a-zA-Z]+\))"
pattern2 = r""

username = {}
with open(file) as f:
    for line in f:
        if "CRON" in line:
            result = re.search(pattern1, line)
            if result != None:
                name = result[1]
                username[name] = username.get(name, 0) + 1
    
print(username)


"""
username = {}
names = ["Alice", "Bob", "Alice", "Alice", "Bob", "Charlie"]

for name in names:
    username[name] = username.get(name, 0) + 1

print(username)

{'Alice': 3, 'Bob': 2, 'Charlie': 1}

"""


