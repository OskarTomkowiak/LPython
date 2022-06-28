fin = open('words.txt')
di = dict()
for line in fin:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        if len(w) > 20:
            print(w)
