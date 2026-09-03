#!/bin/env/python3

import sys
import re

logfile = sys.argv[1]


with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        print(line.strip())
