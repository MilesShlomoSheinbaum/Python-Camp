while True:

    leapYear = int(input("Input a year"))
    
    if leapYear % 400 == 0 and leapYear % 100 == 0:
        print ( f"{leapYear} is a leap year")
    elif leapYear == "stop" or "no more":
        break
    
    else:
        print(f"{leapYear} is not a leap year.")
