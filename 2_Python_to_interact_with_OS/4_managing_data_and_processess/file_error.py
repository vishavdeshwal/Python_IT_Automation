#!/usr/bin/env python3

import os
import sys

fileName=sys.argv[1]

if not os.path.exists(fileName):
     with open(fileName, "w") as f:
       f.write("New File created\n")
else: 
   print("Error, the file {} already exists ".format(fileName))
   sys.exit(1)
