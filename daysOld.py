# Find the number of days between two dates, a birthdate
# and the current date, accounting for leap years.

def days_in_month(month):
    monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return monthdays[month - 1]

def get_numbers(date):
    end_day = date.find("/")
    end_month = date.find("/", end_day + 1)
    year = int(date[end_month + 1:])
    month = int(date[end_day + 1:end_month])
    day = int(date[0: end_day])
    return day, month, year
            
def days_since_birth(birthdate, date):
    birthday, birthmonth, birthyear = get_numbers(birthdate)
    day, month, year = get_numbers(date)
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
    else: 
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

print days_since_birth('28/10/1999','28/10/1999')
#0
print days_since_birth('28/10/1999','29/10/1999')
#1
print days_since_birth('28/10/1999','1/11/1999')
#4
print days_since_birth('28/10/1999','30/11/1999')
#33
print days_since_birth('28/10/1999','31/1/2000')
#95
print days_since_birth('28/10/1999','29/2/2000')
#124
print days_since_birth('28/10/1999','31/1/2001')
#461
print days_since_birth('28/10/1999','31/1/2015')
#5574

