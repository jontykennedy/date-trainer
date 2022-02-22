import sys

month_codes = {
    1: 6,
    2: 2,
    3: 2,
    4: 5,
    5: 0,
    6: 3,
    7: 5,
    8: 1,
    9: 4,
    10: 6,
    11: 2,
    12: 4,
}

century_codes = {
    100: 1,
    200: 3,
    300: 5,
    0: 0,
}

weekday_codes = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
}

def calculate_day_code(day):
    return day % 7

def calculate_month_code(month):
    return month_codes.get(month)

def calculate_century_code(century):
    century = century % 40
    return century_codes.get(century)

def calculate_full_year_code(full_year):
    year = full_year % 100
    century = full_year - year

    year_code = (year + (year // 4)) % 7
    century_code = calculate_century_code(century)

    return year_code + century_code

def leap_year_adjustment(month, full_year):
    year = full_year % 100
    
    if (year == 0 and full_year % 400 == 0):
        print(f"Note, {full_year} is a leap year")
        if (month ==  1 or month == 2):
            return -1
    elif (full_year % 4 == 0):
        print(f"Note, {full_year} is a leap year")
        if (month ==  1 or month == 2):
            return -1
    else:
        print(f"Note, {full_year} is not a leap year")
    return 0

def main():
    full_date  = sys.argv[1]
    date = full_date.split(".")
    day = int(date[0])
    month = int(date[1])
    full_year = int(date[2])

    day_code = calculate_day_code(day)
    print(f"Day Code: {day_code}")

    month_code = calculate_month_code(month)
    print(f"Month Code: {month_code}")

    full_year_code = calculate_full_year_code(full_year)
    print(f"Year Code: {full_year_code}")

    weekday_code = (day_code + month_code + full_year_code + leap_year_adjustment(month, full_year)) % 7
    print(f"Full Date: {weekday_codes.get(weekday_code)}")
    
if __name__ == "__main__":
    main()
