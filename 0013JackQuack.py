pre = "JKLMNOPQ"
suf = "ack"
for letter in pre:
    if letter == "O":
        print(letter + "u" + suf)
    elif letter == "Q":
        print(letter + "u" + suf)
    else:
        print (letter + suf)
