def days_in_month(month):
    monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return monthdays[month - 1]
            
def daysBetweenDates(birthyear, birthmonth, birthday, year, month, day):
    days = day - birthday
    wyear = year
    if month > 2:
        while wyear >= birthyear:
            if wyear%4 == 0 and wyear%100 != 0 or wyear%400 == 0:
                if birthmonth < 2 or birthmonth == 2 and birthday != 29:
                    days = days + 1
                else:
                    if wyear > birthyear:
                        days = days + 1
            wyear = wyear - 1                
    else: #month is less than or equal to 2
        while wyear > birthyear:
            if (wyear - 1)%4 == 0 and (wyear - 1)%100 != 0 or (wyear - 1)%400 == 0:
                if birthmonth < 2 or birthmonth == 2 and birthday != 29:
                    days = days + 1
                else:
                    if wyear - 1 > birthyear:
                        days = days + 1
            wyear = wyear - 1                
    while month + (year - birthyear)*12 > birthmonth:
        days = days + days_in_month(month - 1)
        if month > 1:
            month = month - 1
        else:
            month = 12
            year = year - 1
    return days 


def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
