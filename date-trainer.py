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
    100: 5,
    200: 3,
    300: 1,
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

def validate_and_extract_date(full_date):
    date = full_date.split(".")
    day = int(date[0])
    month = int(date[1])
    full_year = int(date[2])
    if (day < 1 or day > 31 or month < 1 or month > 12 or full_year < 0):
        sys.exit("Invalid date")
    if ((month == 4 or month == 6 or month == 9 or month == 11) and day > 30):
        sys.exit("Invalid date")
    if (not(is_a_leap_year(full_year)) and month == 2 and day > 28):
        sys.exit("Invalid date")
    if (is_a_leap_year(full_year) and month == 2 and day > 29):
        sys.exit("Invalid date")

    return day,month,full_year

def calculate_day_code(day):
    return day % 7

def calculate_month_code(month):
    return month_codes.get(month)

def calculate_century_code(century):
    century = century % 400
    return century_codes.get(century)

def calculate_full_year_code(full_year):
    year = full_year % 100
    century = full_year - year

    year_code = (year + (year // 4)) % 7
    century_code = calculate_century_code(century)

    return year_code + century_code

def is_a_leap_year(full_year):
    year = full_year % 100
    if (year == 0 and full_year % 400 == 0):
        return True
    elif (full_year % 4 == 0):
        return True
    else:
        return False


def leap_year_adjustment(month, full_year):
    year = full_year % 100
    
    if (is_a_leap_year(full_year) and (month ==  1 or month == 2)):
        return -1
    return 0

def calculate_day(full_date):
    day, month, full_year = validate_and_extract_date(full_date)
    day_code = calculate_day_code(day)
    month_code = calculate_month_code(month)
    full_year_code = calculate_full_year_code(full_year)
    weekday_code = (day_code + month_code + full_year_code + leap_year_adjustment(month, full_year)) % 7

    return day_code, month_code, full_year_code, weekday_code

def quiz():
    print("\nQUIZ:")
    answered_year_code = input("Year code? ")
    answered_month_code = input("Month code? ")
    answered_day_code = input("Day code? ")
    answered_leap_year = input("Leap year? ")
    answered_day = input("What day? ")
    return answered_day_code, answered_month_code, answered_year_code, answered_leap_year, answered_day

def score(day_code, month_code, full_year_code, weekday_code, leap_year, answered_day_code, answered_month_code, 
answered_year_code, answered_leap_year, answered_day):
    print("\nRESULTS:")
    print(f"Answered day code: {answered_day_code}, actual day code: {day_code}")
    print(f"Answered month code: {answered_month_code}, actual month code: {month_code}")
    print(f"Answered year code: {answered_year_code}, actual year code: {full_year_code}")
    print(f"Answered leap year: {answered_leap_year}, actual leap year: {leap_year}")
    print(f"Answered day: {answered_day}, actual day: {weekday_codes.get(weekday_code)}")

def main():
    while(True):
        print("--------------------------------------------")
        full_date = input("Enter a date (dd.mm.yyyy): ")
        day_code, month_code, full_year_code, weekday_code = calculate_day(full_date)
        answered_day_code, answered_month_code, answered_year_code, answered_leap_year, answered_day = quiz()
        score(day_code, month_code, full_year_code, weekday_code, is_a_leap_year(int(full_date.split(".")[2])), 
        answered_day_code, answered_month_code, answered_year_code, answered_leap_year, answered_day)
    
if __name__ == "__main__":
    main()
