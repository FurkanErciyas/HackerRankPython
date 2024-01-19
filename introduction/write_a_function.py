def is_leap(year):
    leap = False

    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
        else:
            if year % 4 == 0:
                is_leap = True
    
    return leap

year = int(input("Year = "))

print(is_leap(year))