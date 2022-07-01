y = 0
x = 0
fin = open("0014words.txt")
for line in fin :
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        if "e" not in w:
            x = x + 1
            print(w)
        else:
            y = y + 1
allw = x + y
print("all words:",allw)
print("words without e:",x )
print("words with e:",y)
pe = (100 * x)/allw
ip = int(pe)
print("procent of words without e:", ip,"%")
