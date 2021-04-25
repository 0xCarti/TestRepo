import datetime

display = [["O"] * 53 for _ in range(7)]
dates = [["O"] * 53 for _ in range(7)]


def read_year_file(filename: str):
    display.clear()
    try:
        with open(filename, 'r') as file:
            for line in file:
                display.append(list(line.strip()))
    except FileNotFoundError:
        print(f"The file {filename} was not found.")


def write_year_file(filename: str):
    try:
        with open(filename, 'w') as file:
            for row in display:
                file.write(''.join(row) + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def generate_year_array(start_row: int = 0, start_col: int = 0):
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2021, 12, 31)
    date_of_range = [start_date + datetime.timedelta(days=delta) for delta in range((end_date - start_date).days + 1)]
    for date in date_of_range:
        display[start_row][start_col] = "X"
        dates[start_row][start_col] = str(date)
        if start_row + 1 == len(display):
            start_row = 0
            start_col += 1
        else:
            start_row += 1


if __name__ == "__main__":
    selected_dates = []
    generate_year_array(5,0)
    #write_year_file("2021.txt")
    read_year_file("2021.txt")
    for i in range(len(display)):
        for j in range(len(display[i])):
            if display[i][j] == "#":
                selected_dates.append(dates[i][j])
            print(display[i][j], end="")
        print("")

    for s_date in selected_dates:
        print(s_date)