from collections import Counter
import os
import sys

def read_history(history):
     cont = []
     with open(history) as f:
        for line in f.readlines():
            if not line.split():
                continue
            cont.append(line.split()[0])
     return cont

history = os.environ["HOME"] + "/.bash_history"
try: 
    history = sys.argv[1]
except:
    pass
command_list = read_history(history)
counter = Counter(command_list)
print("Stats")
stats = (_ for _ in counter.most_common() if _[1] > 1)
for _ in stats:
    print(_)

