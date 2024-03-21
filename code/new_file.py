import os
import time
path = os.getcwd()
number = 0
for d in [f for f in os.listdir(path) if os.path.isfile(f)]:
    if d[-3:] == ".md" and d[0] == "p":
        tmp = int(d[d.find("_")+1:-3])
        number = tmp if tmp > number else number

with open(f"prof_{number+1}.md", "w") as fout:
    fout.write(f"<!--{time.asctime()}-->")
    print(fout.name)
