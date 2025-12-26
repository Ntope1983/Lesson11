# the structure in a program must be Static variables-?global variables-> def functions-->main function->main()
# Play tic-tac-toe
player1 = "X"
player2 = "O"

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

available_positions = {(x, y) for x in range(3) for y in range(3)}


def player_choice(player):  # Chose an index in the board
    while True:
        try:
            row = int(input(f"Δώσε μία  θέση player {player}"))
            column = int(input(f"Δώσε μία  θέση player {player}"))
            if row not in range(3) or column not in range(3):
                print("Λάθος: η θέση πρέπει να είναι 0, 1 ή 2.")
                continue
            x = (row, column)
            while x not in available_positions:
                row = int(input(f"Δώσε μία έγκυρη θέση player {player}"))
                column = int(input(f"Δώσε μία έγκυρη θέση player {player}"))
                x = (row, column)
            available_positions.remove(x)
            board[row][column] = player
            break
        except ValueError:
            print("Λάθος εισαγωγή ακεραίου")
            continue


def print_board(board2):  # Εκτύπωσή board
    print("\n    0   1   2")
    for i, row in enumerate(board2):
        print(f"{i}   " + " | ".join(row))
        if i < 2:
            print("   ---+---+---")


def check_win(player):  # Check if we have a winner
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    else:
        return False


def switch_player(turn_to_play):  # turn player
    if turn_to_play == player1:
        return player2
    else:
        return player1


def main():
    turn = player1
    for round in range(9):
        print(f"Γύρος:{round + 1}")
        print_board(board)
        player_choice(turn)
        print_board(board)
        if check_win(turn):
            print(f"Συγχαρητήρια κέρδισε ο παίχτης :{turn}")
            break
        turn = switch_player(turn)
    print("Ισοπαλία")


main()
