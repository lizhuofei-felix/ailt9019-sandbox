import os
import sys

name = sys.argv[1] if len(sys.argv) > 1 else "AILT9019_PRACTICE_FLAG"
print(name in os.environ)
