#!/usr/bin/env python3

import re
import sys

file=sys.argv[1]

pattern=r"User \'(\w+)\'$"
with open(file, 'r') as f:
  for line in f:
    if re.search(pattern, line):
      print(line.strip())
