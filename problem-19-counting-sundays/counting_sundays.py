DAYS_PER_YEAR = 365.25
DAYS_OF_WEEK = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
MONTHS = ["JAN", "FEB", "MAR", "APR", \
          "MAY", "JUN", "JUL", "AUG", \
          "SEP", "OCT", "NOV", "DEC"]
THIRTY_DAY_MONTHS = ["APR", "JUN", "SEP", "NOV"]
THIRTY_ONE_DAY_MONTHS = filter(lambda m : \
    m not in THIRTY_DAY_MONTHS and m is not "FEB", MONTHS)

def is_leap_year(yyyy):
    is_century = yyyy % 100 == 0

    if is_century:
        return yyyy % 400 == 0
    else:
        return yyyy % 4 == 0

def days_in_month(mm, yyyy):
    month_name = MONTHS[mm - 1]

    if month_name == "FEB":
      if is_leap_year(yyyy):
        return 29
      else:
        return 28
    elif month_name in THIRTY_DAY_MONTHS:
        return 30
    else:
        return 31

def day_ranges_for_months(yyyy):
    day_ranges = {}
    day_number = 1

    for mm in range(1, len(MONTHS) + 1):
        month_name = MONTHS[mm-1]
        day_ranges[month_name] = (day_number, day_number+days_in_month(mm,yyyy))
        day_number += days_in_month(mm, yyyy)

    return day_ranges

def n_days_away_from_xday(number_of_days, day_of_week, ago=True, after=False):
    assert ago ^ after
    day = DAYS_OF_WEEK.index(day_of_week)
    offset = number_of_days * (-1 if ago else 1)

    return DAYS_OF_WEEK[(day + offset) % len(DAYS_OF_WEEK)] 

def days_in_year(yyyy):
    if is_leap_year(yyyy):
        return int(DAYS_PER_YEAR) + 1
    else:
        return int(DAYS_PER_YEAR)

class Date:
    def __init__(self, dd, mm, yyyy):
        self.day = dd
        self.month = mm
        self.year = yyyy

    def to_day_number(self):
        day_count = 0

        for mm in range(1, self.month):
            day_count += days_in_month(mm, self.year)

        day_count += self.day

        return day_count

    @staticmethod
    def day_number_to_date(day_number, yyyy):
        assert 1 <= day_number <= days_in_year(yyyy)

        day_ranges_for_months_in_given_year = day_ranges_for_months(yyyy)
        day_count = 0

        for month_name in MONTHS:
            days_range = day_ranges_for_months_in_given_year[month_name]
            start_day_number, end_day_number = days_range

            if day_number in range(start_day_number, end_day_number):
                dd = day_number - day_count
                mm = MONTHS.index(month_name) + 1
                return Date(dd, mm, yyyy)
            else:
                day_count += days_in_month(MONTHS.index(month_name) + 1, yyyy) 

    def days_away_from(self, date2):
        dates = sorted([self, date2], key=lambda d: (d.year, d.month, d.day))
        start_date, end_date = dates

        if start_date.year == end_date.year:
            return end_date.to_day_number() - start_date.to_day_number()
        else:
            day_count = 0

            for year in range(start_date.year + 1, end_date.year):
                day_count += days_in_year(year)

            day_count += days_in_year(start_date.year) - start_date.to_day_number() + 1
            day_count += end_date.to_day_number() - 1

            return day_count

    def __repr__(self):
        return repr("-".join(map(str,[self.month, self.day, self.year])))

def find_num_sundays_that_fall_on_first_of_each_month_between_years():
    YEAR_START = 1901
    YEAR_END = 2000
    REFERENCE_DATE = Date(31, 12, 2013)
    REFERENCE_DAY_OF_WEEK = "TUE"
    TARGET_DAY = "SUN"

    num_matches = 0

    for yyyy in range(YEAR_START, YEAR_END + 1):
        for i in range(1, days_in_year(yyyy) + 1):
            date_i = Date.day_number_to_date(i, yyyy)
            day_difference = REFERENCE_DATE.days_away_from(date_i)
            yday = n_days_away_from_xday(day_difference, REFERENCE_DAY_OF_WEEK)

            if yday is TARGET_DAY and date_i.day is 1:
                num_matches += 1

    return num_matches

print find_num_sundays_that_fall_on_first_of_each_month_between_years()

