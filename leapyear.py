def leapyear(year, birthdate, date):
    birthday, birthmonth, birthyear = get_numbers(birthdate)
    day, month, year1 = get_numbers(date)
    ldays = 0
    year = year1
    while year > birthyear:
        if year%4 == 0:
            if month > 2:
                ldays = ldays + 1
            if month < 2 or month == 2 and day != 29:
                if year1 - 1 > birthyear:
                    if (year1 - 1)%4 == 0:
                        ldays = ldays + 1
        year = year - 1
    if birthyear%4 == 0:
        if birthmonth < 3 and (month != 2 or day != 29):
            ldays = ldays + 1
    return ldays
