import sys

century_codes = {
    100: 1,
    200: 3,
    300: 5,
    0: 0,
}

def calculate_day_code(day):
    return day % 7

def calculate_century_code(century):
    century = century % 40
    return century_codes.get(century)

def calculate_full_year_code(full_year):
    year = full_year % 100
    century = full_year - year

    if (year == 0 and full_year % 400 == 0):
        print(f"Note, {full_year} is a leap year")
    elif (full_year % 4 == 0):
        print(f"Note, {full_year} is a leap year")
    else:
        print(f"Note, {full_year} is not a leap year")

    year_code = (year + (year // 4)) % 7
    century_code = calculate_century_code(century)

    return year_code + century_code


def main():
    date = sys.argv[1].split(".")
    day = int(date[0])
    month = int(date[1])
    full_year = int(date[2])

    day_code = calculate_day_code(day)
    print(f"Day Code: {day_code}")

    full_year_code = calculate_full_year_code(full_year)
    print(f"Year Code: {full_year_code}")
    
if __name__ == "__main__":
    main()
