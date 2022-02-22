import sys

century_codes = {
    100: 1,
    200: 3,
    300: 5,
    0: 0,
}

def calculate_century_code(century):
    century = century % 40
    return century_codes.get(century)

def  calculate_full_year_code(full_year):
    year = full_year % 100
    century = full_year - year

    if (year == 0 and full_year % 400 == 0):
        print("Note, " + str(full_year) + " is a leap year")
    elif (full_year % 4 == 0):
        print("Note, " + str(full_year) + " is a leap year")
    else:
        print("Note, " + str(full_year) + " is not a leap year")

    year_code = (year + (year // 4)) % 7
    century_code = calculate_century_code(century)

    full_year_code = year_code + century_code
    print("Year Code: " + str(full_year_code))


def main():
    full_year = int(sys.argv[1])
    calculate_full_year_code(full_year)
    
if __name__ == "__main__":
    main()
