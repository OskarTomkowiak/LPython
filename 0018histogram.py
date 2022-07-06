def histogram(s):
    di = dict()
    for le in s:
        di[le] = di.get(le,0) +1
    print(di)
histogram("brontosaurus")
