game_list = [[" "] * 3 for i in range(0, 9, 3)]
write = "X"


def result():
    condition = ""

    if game_list[0][0] == game_list[1][1] == game_list[2][2] != " " or game_list[0][2] == game_list[1][1] == game_list[2][0] != " ":
        condition = f"{game_list[0][0]} wins"
    else:
        for row in game_list:
            if len(set(row)) == 1 and set(row) != {" "}:
                condition = f"{row[0]} wins"

        for column in range(3):
            column_data = []
            for row in range(3):
                column_data.append(game_list[row][column])
            if len(set(column_data)) == 1 and set(column_data) != {" "}:
                condition = f"{column_data[0]} wins"

        if condition == "":
            if " " not in game_list[0] and " " not in game_list[1] and " " not in game_list[2]:
                condition = "Draw"
    return condition


def print_game():
    print("-" * 9)
    for n in range(3):
        print("|", *game_list[n], "|")
    print("-" * 9)


print_game()

while True:
    try:
        coordinates = list(
            map(int, input("Enter the coordinates:").strip().split()))
        if coordinates[0] > 3 or coordinates[1] > 3 or coordinates[0] < 1 or coordinates[1] < 1:
            print("Coordinates should be from 1 to 3!")
        else:
            if game_list[-1 * coordinates[1]][coordinates[0] - 1] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                game_list[-1 * coordinates[1]][coordinates[0] - 1] = write
                write = "O" if write == "X" else "X"
                print_game()
                if result() != "":
                    print(result())
                    break
    except ValueError:
        print("You should enter numbers!")
