"""
Don't use scripts like this in production!
"""

import sys
import time


result = int(sys.argv[1]) + 5


if result < 10:
    print(result)
    time.sleep(5)  # Simulate a delay while the script works.
