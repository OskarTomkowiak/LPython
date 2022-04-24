while True:
    fname = input ('Enter File:')
    if fname == "clown" :
        fname = 'clown.txt'
        break
    elif fname == "intro" :
        fname = 'intro.txt'
        break
    else:
        print("No file with this name")
hand = open (fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        print(w)
        if w in di:
            di[w] = di[w] +1
            print('**Existing**')
        else:
            di[w] = 1
            print('**NEW**')
        print("number of this words",di[w])
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
largest = -1
theword = None
for k,v in di.items() :
    print (k,v)
    if v > largest :
        largest = v
        theword = k
print('=======================================')
print("The most common word is |",theword,"|",largest,"|")
print('=======================================')
