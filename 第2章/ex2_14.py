f = open("Sample.txt", "r", encoding="utf-8")
for line in f:
    line = line.rstrip()
    print(line)
f.close()