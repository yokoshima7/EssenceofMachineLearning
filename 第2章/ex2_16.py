with open("output.txt", "w", encoding="utf-8") as fw:
    with open("sample.txt", "r", encoding="utf-8") as fr:
        for line in fr:
            print(line, end="", file=fw)