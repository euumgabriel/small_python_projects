import datetime

DAYS = (
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
)
MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)


def main():
    year = get_year()
    month = get_month()
    calendar_text = get_calendar(year, month)
    save_calendar(calendar_text, year, month)

    print(calendar_text)


def get_year():
    while True:
        year = input("Enter the year for the calendar: ")

        if year.isdecimal() and int(year) > 0:
            return int(year)

        print("Please enter a numeric year, like 2022.")


def get_month():
    while True:
        month = input("Enter the month for the calendar (1 - 12): ")

        if not month.isdecimal():
            print("Please enter a numeric month, like 3 for March.")
            continue

        month = int(month)

        if 1 <= month <= 12:
            return month

        print("Please enter a number from 1 to 12.")


def get_calendar(year, month):
    calendar_text = ""

    calendar_text += (" " * 34) + MONTHS[month - 1] + " " + str(year) + "\n"

    calendar_text += "...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n"

    week_separator = ("+----------" * 7) + "+\n"

    blank_row = ("|          " * 7) + "|\n"

    current_date = datetime.date(year, month, 1)

    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:
        calendar_text += week_separator

        day_number_row = ""

        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += "|" + day_number_label + (" " * 8)

            current_date += datetime.timedelta(days=1)

        day_number_row += "|\n"

        calendar_text += day_number_row

        for i in range(3):
            calendar_text += blank_row

        if current_date.month != month:
            break

    calendar_text += week_separator

    return calendar_text


def save_calendar(calendar_text, year, month):
    calendar_filename = f"calendar_{year}_{month}.txt"

    with open(calendar_filename, "w") as file_obj:
        file_obj.write(calendar_text)

    print(f"Saved to {calendar_filename}")


if __name__ == "__main__":
    main()
