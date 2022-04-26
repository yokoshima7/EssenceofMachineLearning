with open("sample.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip()
        print(line)
