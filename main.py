def display_game_state(state):
    print("---------")
    print(f"| {state[0][0]} {state[0][1]} {state[0][2]} |")
    print(f"| {state[1][0]} {state[1][1]} {state[1][2]} |")
    print(f"| {state[2][0]} {state[2][1]} {state[2][2]} |")
    print("---------")


def process_move(state):
    move_checked = 0

    while move_checked == 0:
        move = input("Please enter your move as coordinates, such as '1 1'")

        if move[0].isnumeric() and move[2].isnumeric():  # ensure move is numerical
            row = int(move[0]) - 1
            column = int(move[2]) - 1

            if column not in range(0, 3) or row not in range(0, 3):  # ensure move is within range 1:3
                print("Coordinates should be from 1 to 3!")

            elif state[row][column] != ' ':  # ensure cell is empty
                print("This cell is occupied! Choose another one!")

            else:
                move_checked = 1

                return row, column

        else:
            print("You should enter numbers!")


def victory_checker(state, player):
    # check for horizontal victory
    if state[0][0] == state[0][1] == state[0][2] == player:
        return 1
    elif state[1][0] == state[1][1] == state[1][2] == player:
        return 1
    elif state[2][0] == state[2][1] == state[2][2] == player:
        return 1

    # check for vertical victory
    elif state[0][0] == state[1][0] == state[2][0] == player:
        return 1
    elif state[0][1] == state[1][1] == state[2][1] == player:
        return 1
    elif state[0][2] == state[1][2] == state[2][2] == player:
        return 1

    # check for diagonal victory
    elif state[0][0] == state[1][1] == state[2][2] == player:
        return 1
    elif state[0][2] == state[1][1] == state[2][0] == player:
        return 1

    # check for draw
    elif ' ' not in state[0] and ' ' not in state[1] and ' ' not in state[2]:
        return 2


def game():
    game_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    victory = 0
    turns = 0
    player = 'X'

    while victory == 0:
        display_game_state(game_state)  # display game board

        row, column = process_move(game_state)  # request move and check move is legal
        turns += 1

        game_state[row][column] = player  # replace chosen cell with player mark (X or 0)

        if turns == 9:
            victory = victory_checker(game_state, player)  # check if victory/draw has occurred

        if victory == 1:
            display_game_state(game_state)  # display game board
            print(f"{player} wins")
        elif victory == 2:
            display_game_state(game_state)  # display game board
            print("Draw")
        else:
            if player == 'X':
                player = 'O'
            else:
                player = 'X'


if __name__ == "__main__":
    game()