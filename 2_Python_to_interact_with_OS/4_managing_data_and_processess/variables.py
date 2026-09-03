#!/usr/bin/env python3

import os

# Now it says if env variable "HOME" or "SHELL" or "FRUIT" is there then print it, else print empty string ""
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

