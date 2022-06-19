n = input("Enter a number: ")
inn = int(n)
def fibonocci(inn):
    if inn == 0:
        return 0
    elif inn == 1:
        return 1
    else:
        return fibonocci(inn-1)+fibonocci(inn-2)
result = fibonocci(inn)
print(result)
