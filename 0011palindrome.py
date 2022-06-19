pal = input("Enter a word: ")
npal = len(pal)
def palindrome(pal):
    if pal[0] == pal[-1]:
        if npal <= 3:
            print("True")
        else:
            if pal[1] == pal[-2]:
                if npal >= 7:
                        if pal[2] == pal[-3]:
                            print("True")
                        else:
                            print("False")
                else:
                    print("True")
            else:
                print("False")
    else:
        print("False")
palindrome(pal)
