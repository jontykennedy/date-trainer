import datetime
import random
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

num_to_month = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


def validate_and_extract_date(full_date):
    date = full_date.split("/")
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

    return day, month, full_year


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

    year_code = year + (year // 4)
    century_code = calculate_century_code(century)

    return (year_code + century_code) % 7


def is_a_leap_year(full_year):
    year = full_year % 100
    if (year == 0 and full_year % 400 == 0):
        return True
    elif (full_year % 4 == 0):
        return True
    else:
        return False


def leap_year_adjustment(month, full_year):
    if (is_a_leap_year(full_year) and (month == 1 or month == 2)):
        return -1
    return 0


def calculate_day_components(full_date):
    day, month, full_year = validate_and_extract_date(full_date)
    day_code = calculate_day_code(day)
    month_code = calculate_month_code(month)
    full_year_code = calculate_full_year_code(full_year)
    weekday_code = (day_code + month_code + full_year_code +
                    leap_year_adjustment(month, full_year)) % 7

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
    print(
        f"Answered day code: {answered_day_code}, actual day code: {day_code}")
    print(
        f"Answered month code: {answered_month_code}, actual month code: {month_code}")
    print(
        f"Answered year code: {answered_year_code}, actual year code: {full_year_code}")
    print(
        f"Answered leap year: {answered_leap_year}, actual leap year: {leap_year}")
    print(
        f"Answered day: {answered_day}, actual day: {weekday_codes.get(weekday_code)}")


def generate_random_date(start, end):
    return start + (end - start) * random.random()


def full_quiz_mode():
    start = datetime.date(year=1, month=1, day=1)
    end = datetime.date(year=3000, month=12, day=31)
    full_date = generate_random_date(start, end)
    sanitised_year = full_date.strftime("%Y").lstrip("0")
    full_date_num = full_date.strftime(f"%d/%m/{sanitised_year}")
    full_date_string = full_date.strftime(f"%d %B {sanitised_year}")
    print(f"Target: {full_date_string}")

    day_code, month_code, full_year_code, weekday_code = calculate_day_components(
        full_date_num)
    answered_day_code, answered_month_code, answered_year_code, answered_leap_year, answered_day = quiz()
    score(day_code, month_code, full_year_code, weekday_code, is_a_leap_year(int(full_date_num.split("/")[2])),
          answered_day_code, answered_month_code, answered_year_code, answered_leap_year, answered_day)


def year_code_quiz_mode():
    random_year = random.randint(0, 3000)
    print(f"Target: {random_year}")
    answered_year_code = input("Year code? ")
    full_year_code = calculate_full_year_code(int(random_year)) % 7
    print(
        f"Answered year code: {answered_year_code}, actual year code: {full_year_code}")


def month_code_quiz_mode():
    random_month = random.randint(1, 12)
    print(f"Target: {num_to_month.get(random_month)}")
    answered_month_code = input("Month code? ")
    month_code = calculate_month_code(random_month)
    print(
        f"Answered month code: {answered_month_code}, actual month code: {month_code}")


def day_code_quiz_mode():
    random_day = random.randint(1, 31)
    print(f"Target: {random_day}")
    answered_day_code = input("Day code? ")
    day_code = calculate_day_code(random_day)
    print(
        f"Answered day code: {answered_day_code}, actual day code: {day_code}")


def century_code_quiz_mode():
    random_century = random.randint(1, 3000) // 100 * 100
    print(f"Target: {random_century}")
    answered_century_code = input("Century code? ")
    century_code = calculate_century_code(random_century)
    print(
        f"Answered century code: {answered_century_code}, actual century code: {century_code}")


def leap_year_quiz_mode():
    random_year = random.randint(1, 3000)
    answer = input(f"Is {random_year} a leap year? (yes/no) ")
    actual = "yes" if is_a_leap_year(random_year) else "no"
    if (answer.lower() == actual):
        print("Correct")
        return
    print("Incorrect")


def day_calculator():
    full_date = input("Enter a date (dd/mm/yyyy): ")
    _, _, _, weekday_code = calculate_day_components(full_date)
    print(f"{weekday_codes.get(weekday_code)}")


def main():
    while(True):
        print("-------------------------------------------------")
        print("MODES:\n(1) Full Quiz \n(2) Year Code Quiz \n(3) Month Code Quiz \n"
              + "(4) Day Code Quiz \n(5) Leap Year Quiz \n(6) Century Code Quiz \n(7) Day Calculator\n(8) Exit")
        selection = input("Mode: ")
        print("-------------------------------------------------")
        if (selection == "1"):
            enter_loop(full_quiz_mode)
        elif (selection == "2"):
            enter_loop(year_code_quiz_mode)
        elif (selection == "3"):
            enter_loop(month_code_quiz_mode)
        elif (selection == "4"):
            enter_loop(day_code_quiz_mode)
        elif (selection == "5"):
            enter_loop(leap_year_quiz_mode)
        elif (selection == "6"):
            enter_loop(century_code_quiz_mode)
        elif (selection == "7"):
            day_calculator()
            input("\nPress enter to return to home...")
        elif (selection == "8"):
            print("Goodbye\n-------------------------------------------------")
            sys.exit()


def enter_loop(mode):
    while(True):
        mode()
        option = input(
            "Press enter to restart or X to return to the home menu: ")
        if (option.lower() == "x"):
            break
        print("")


if __name__ == "__main__":
    main()
