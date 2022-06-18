def print_n  (s,n):
    if n < 0 :
        print("Number have to be positive")
    elif n <= 0:
        return
    else:
        print(s)
        print_n (s,n - 1)
Word = input ("Choose word... ")
Number = input ("Choose number... ")
NumberF = float(Number)
print_n(Word,NumberF)
print("Number of the words:",Number)
