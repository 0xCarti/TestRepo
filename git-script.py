import datetime
import os
import sys

display = [["O"] * 53 for _ in range(7)]
dates = [["O"] * 53 for _ in range(7)]
selected_dates = []


def read_year_file(filename: str):
    display.clear()
    try:
        with open(filename, 'r') as file:
            for line in file:
                display.append(list(line.strip()))
        print('Finished reading file.')
    except FileNotFoundError:
        print(f"The file {filename} was not found.")


def write_year_file(filename: str):
    try:
        with open(filename, 'w') as file:
            for row in display:
                file.write(''.join(row) + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def write_year_to_file(filename: str, date: str):
    try:
        with open(filename, 'w') as file:
            print(f'Wrote to {date}')
            file.write(date + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def generate_year_array(start_row: int = 0, start_col: int = 0):
    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date(2000, 12, 31)
    date_of_range = [start_date + datetime.timedelta(days=delta) for delta in range((end_date - start_date).days + 1)]
    date_of_range = [date for date in date_of_range if not (date.month == 2 and date.day == 29)]
    for date in date_of_range:
        display[start_row][start_col] = "X"
        dates[start_row][start_col] = str(date)
        if start_row + 1 == len(display):
            start_row = 0
            start_col += 1
        else:
            start_row += 1

def populate_github():
    print("starting git commits")
    os.system(f'git add 2021.txt')
    for date in selected_dates:
        write_year_to_file(f"date.txt", date)
        os.system(f'git add date.txt')
        os.system(f'git commit -a --date={date} --message={date}')
        print(f'Commit made and pushed for {date}')
    os.system(f'git push test master')

def display_menu():
    print(f'1: Write year to file.')
    print(f'2: Read design from year file.')
    print(f'3: Populate GitHub.')
    print(f'4: Show Array.')
    print(f'5: Exit')
    return input("Please enter a number: ")

if __name__ == "__main__":
    year_file = "2001.txt"
    generate_year_array(1, 0)
    while True:
        user_input = display_menu()
        if user_input == "1":
            write_year_file(year_file)
        elif user_input == "2":
            read_year_file(year_file)
            for i in range(len(display)):
                for j in range(len(display[i])):
                    if display[i][j] == "#":
                        selected_dates.append(dates[i][j])
        elif user_input == "3":
            populate_github()
        elif user_input == "4":
            for i in range(len(display)):
                for j in range(len(display[i])):
                    print(display[i][j], end="")
                print('')
        elif user_input == "5":
            sys.exit()
        else:
            print("Please enter an appropraite choice.")