# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        #print year, month, day + 1
        return year, month, day + 1
    else:
        if month == 12:
            #print year + 1, 1, 1
            return year + 1, 1, 1
        else:
            #print year, month + 1, 1
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def isLeapYear(year):
    if year%4 != 0:
        return False
    else:
        if year%100 != 0:
           return True
        else:
            if year%400 != 0:
                return False
            else:
                return True

def daysInMonth(year, month):
    days = 31
    if month == 2:
        if isLeapYear(year):
            days = 29
            #print days
        else:
            days = 28
        #print days
    if month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
        #print days
    return days

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days = days + 1
        # print days
    print days
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
