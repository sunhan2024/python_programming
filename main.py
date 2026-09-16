import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DATA_FILE = "data/Crash_Analysis_System_(CAS)_data.csv"
CONDITION = "fine"

def read_csv_data(filename: str, columns: list[str]) -> list[tuple]:
    """
    IMPORTANT NOTE: When completing parts 1 and 2 of the project you do NOT need to understand how this function works.
    Reads in data from the CSV file with the specified filename.
    Returns columns of data in the order specified by columns.
    """
    df = pd.read_csv(filename)
    desired_columns = df[columns]
    return list(desired_columns.itertuples(index=False, name=None))

def menu_select(options: list[str]) -> int:
    """
    Prints a list of enumerated options and collects the user's choice.
    The user is prompted until they enter a valid menu index.
    Returns a valid user selection.
    """
    prompt = f"0-{len(options) - 1}:: "
    i = 0
    while i < len(options):
        print(f'[{i}] {options[i]}')
        i += 1

    selection = int(input(prompt))
    while selection < 0 or selection >= len(options):
        print(f'{selection} is not a valid option\nTry again')
        selection = int(input(prompt))
    return selection


def unique_values(table: list, col_index: int) -> list:
    """
    Given a list of tuples returns a sorted list of unique values of a given column.
    Example:
    animals = [
        ("cat", "dog"),
        ("bird", "dog"),
        ("fish", "fish")
    ]

    print(unique_values(animals, 0))
    ['bird', 'cat', 'fish']

    print(unique_values(animals, 1))
    ['dog', 'fish']
    """
    out = []
    for row in table:
        if row[col_index] not in out:
            out.append(row[col_index])
    out.sort()
    return out


def print_crash_severity_report(year_of_interest: int, speed_of_interest: int) -> None:
    """Prints a table outlining the number of crashes in a given year for a given speed limit."""
    data = read_csv_data(DATA_FILE, ["crashYear", "temporarySpeedLimit", "crashSeverity"])
    severity_types = unique_values(data, 2)
    print_record =[]
    for severity_type in severity_types:
        count = 0
        for year, speed_limit, crash_type in data:
            if year == year_of_interest and speed_limit == speed_of_interest and crash_type == severity_type:
                count += 1
        print_record.append(count)
    if sum(print_record) == 0:
        print()
        print("No crashes found for this year and temporary speed limit.")
    else:
        print("Crash Severity by Classification")
        print(f"Temporary Speed Limit: {speed_of_interest}")
        print(f"Year: {year_of_interest}")
        print()
        for severity_type in severity_types:
            count = 0
            for year, speed_limit, crash_type in data:
                if year == year_of_interest and speed_limit == speed_of_interest and crash_type == severity_type:
                    count += 1
            print(f"{severity_type}: {count}")    

def print_crash_severity_report_allyear(speed_of_interest: int) -> None:
    """Prints a table outlining the number of crashes in a given year for a given speed limit."""
    data = read_csv_data(DATA_FILE, ["crashYear", "temporarySpeedLimit", "crashSeverity"])
    severity_types = unique_values(data, 2)
    all_years = unique_values(data, 0)
    print_record =[]
    for year in all_years:
        for severity_type in severity_types:
            count = 0
            for year_data, speed_limit, crash_type in data:
                if year_data == year and speed_limit == speed_of_interest and crash_type == severity_type:
                    count += 1
            print_record.append(count)
    if sum(print_record) == 0:
        print()
        print("No records found for this temporary speed limit.")
    else:
        print("Crash Severity by Classification for all years")
        print(f"Temporary Speed Limit: {speed_of_interest}")
        print()
        for year in all_years:
            print(f"Year: {year}")
            for severity_type in severity_types:
                count = 0
                for year_data, speed_limit, crash_type in data:
                    if year_data == year and speed_limit == speed_of_interest and crash_type == severity_type:
                        count += 1
                print(f"{severity_type}: {count}")
            print()

def main():
    """Small application that presents tables and graphs based on crash data"""
    menu_options = [
        "Crash Severity Report",
        "Crash Severity Report for all years",
        "Crash Reports Graph for a given year and temporary speed limit",
        "Crash Reports Graph for all years for a given temporary speed limit",
        "Exit"
    ]
    option = menu_select(menu_options)
    if option == 0:
        year = read_int("Year: ")
        speed_limit = read_int("Temporary Speed Limit: ")
        print_crash_severity_report(year, speed_limit)
    elif option == 1:
         speed_limit = read_int("Temporary Speed Limit: ")
         print_crash_severity_report_allyear(speed_limit)
    elif option == 2:
        year = read_int("Year: ")
        speed_limit = read_int("Temporary Speed Limit: ")
        generate_graph(year, speed_limit)
    elif option == 3:
        speed_limit = read_int("Temporary Speed Limit: ")
        generate_graph_allyear(speed_limit)
    elif option == 4:
        print("Bye!")

def read_int(prompt):
    """Prompts the user for a valid int and returns it."""
    # YOUR CODE HERE (Hint: you already wrote this one earlier.)
    generic = None
    while generic is None:
        generic_str = input(prompt)
        if generic_str.isnumeric():
            generic = int(generic_str)
        else:
            print("Please enter an integer.")
    return generic

def generate_graph(year_of_interest, speed_of_interest):
    """Generate a graph of Crash Reports over time for #5"""
    data = read_csv_data(DATA_FILE, ["crashYear", "temporarySpeedLimit", "crashSeverity"])
    severity_types = unique_values(data, 2)
    severity_count = []
    for severity_type in severity_types:
        count = 0
        for year, speed_limit, crash_type in data:
            if year == year_of_interest and speed_limit == speed_of_interest and crash_type == severity_type:
                count += 1
        severity_count.append(count)
    axes = plt.axes()
    axes.bar(severity_types, severity_count)
    axes.set_xlabel("Crash Severity")
    axes.set_ylabel("Number of Crashes")
    axes.set_title(f"Crash Reports for {year_of_interest} with temporary speed limit of {speed_of_interest}")
    plt.show()

def generate_graph_allyear(speed_of_interest):
    """Generate a graph of Crash Counts over all years for a given temporary speed limit"""
    data = read_csv_data(DATA_FILE, ["crashYear", "temporarySpeedLimit", "crashSeverity"])
    all_years = unique_values(data, 0)
    count_of_each_year = []
    for year in all_years:
        count = 0
        for year_data, speed_limit, crash_type in data:
            if year_data == year and speed_limit == speed_of_interest:
                count += 1
        count_of_each_year.append(count)
    axes = plt.axes()
    axes.bar(all_years, count_of_each_year)
    axes.set_xlabel("Year")
    axes.set_ylabel("Number of Crashes")
    axes.set_title(f"Crash Counts for all years with temporary speed limit of {speed_of_interest}")
    plt.show()

print(DATA_FILE)
main()
