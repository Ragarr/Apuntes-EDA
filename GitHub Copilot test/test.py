import datetime
def DaysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    return abs(date2 - date1).day