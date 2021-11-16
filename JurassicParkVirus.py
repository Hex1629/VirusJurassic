import os
import sys
import time
from time import sleep
#BLACK = '\033[30m'
#RED = '\033[31m'
#GREEN = '\033[32m'
#YELLOW = '\033[33m'
#BLUE = '\033[34m'
#MAGENTA = '\033[35m'
#CYAN = '\033[36m'
#WHITE = '\033[37m'
#UNDERLINE = '\033[4m'
#RESET = '\033[0m'
def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3.0/90)
slowprints('\033[32mJurassic Park System Security Interface')
slowprints('Version 4.0.5 Alpha E')
slowprints('Ready...')
slowprints('''$: system raptors''')
slowprints('''Raptor containment enclosure.....''')
slowprints('''Security               [ok]''')
slowprints('''Fence                  [ok]''')
slowprints('''Feeding Pavillion      [ok]''')
slowprints('''System Halt!''')
slowprints('''$: access security''')
slowprints('''access: PERMISSION DENTED.''')
slowprints('''$: access security grid''')
slowprints('''access: PERMISSION DENTED.''')
slowprints('''$: access main security grid''')
slowprints('''access: PERMISSION DENTED....and....''')
while True:
			print("YOU DIDN'T SAY THE MAGIC WORD!")
			time.sleep(0.6)