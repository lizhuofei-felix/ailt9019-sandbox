import os
import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = "AILT9019_PRACTICE_FLAG"

exists = name in os.environ

print(exists)
