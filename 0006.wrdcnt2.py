while True:
    file = input("Enter file name: ")
    if file == "clown":
        file = '0003clown.txt'
        break
    elif file == "intro":
        file = '0004intro.txt'
        break
    else:
        print("Bad file name...")
hand = open (file)
di = dict()
for lines in hand:
    lines = lines.rstrip()
    words = lines.split()
    for word in words:
        di[word] = di.get(word,0) +1
largest = -1
theword = None
for k,v in di.items() :
    print(k,v)
    if v > largest :
        largest = v
        theword = k
print('The most common word is','|',theword,'|',largest,'|' )
