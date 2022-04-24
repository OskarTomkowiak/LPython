def computepay(hours, rate) :
    print("In computepay")
    print(hours,"hours")
    print(rate, "$ rate")

sh = input ("Enter Hours: ")
sr = input ("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()
computepay (fh,fr)
if fh > 40:
    print("Overtime")
    reg = fh *  fr
    otp = (fh - 40.0) * (fr * 0.5)
    print(reg,"+",otp)
    xp = reg + otp
elif fh < 5:
    print("Below normal work time")
    reg = fh * fr
    now = (fr / 2.0)
    print(reg,"-",now)
    xp = reg - now
else:
    print("regular")
    xp = fh * fr
print("Pay",xp, "$")
