import argparse


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def validate_year(year):
    return 0 <= year <= 2999


def validate_month(month):
    return 1 <= month <= 12


def validate_day(year, month, day):
    leap_year = is_leap_year(year)
    if day < 1:
        return False
    if leap_year and month == 2:
        if day <= 29:
            return True
    if month == 2 and day <= 28:
        return True
    if month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
        return True
    elif month in [4, 6, 9, 11] and day <= 30:
        return True
    return False


def validate_date(year, month, day):
    if year < 100:
        year += 2000
    return validate_year(year) and validate_month(month) and validate_day(year, month, day)


def get_earliest_date(dates):
    dates.sort(key=lambda x: (x[0], x[1], x[2]))
    return dates[0]


def create_all_variations(num_1, num_2, num_3):
    combinations = [[num_1, num_2, num_3], [num_1, num_3, num_2],
                    [num_2, num_1, num_3], [num_2, num_3, num_1],
                    [num_3, num_2, num_1], [num_3, num_1, num_2]]
    return combinations


def date(date_file):
    with open(date_file) as f:
        date_input = f.read()
    date_list = date_input.split("/")
    try:
        date_list = [int(number) for number in date_list]
    except ValueError:
        print("Wrong input data")
        return
    possible_dates = []
    for comb in create_all_variations(date_list[0], date_list[1], date_list[2]):
        if validate_date(comb[0], comb[1], comb[2]):
            year = comb[0] + 2000 if comb[0] < 100 else comb[0]
            month = comb[1]
            day = comb[2]
            possible_dates.append([year, month, day])
    if not possible_dates:
        return f"{date_input} is illegal"
    earliest_date = get_earliest_date(possible_dates)
    return "{:04d}-{:02d}-{:02d}".format(earliest_date[0], earliest_date[1], earliest_date[2])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("date_file")
    args = parser.parse_args()
    input_file = args.date_file
    print(date(input_file))
