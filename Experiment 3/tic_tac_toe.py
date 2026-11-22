board = [" "] * 9

def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner():
    win = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for line in win:
        a, b, c = line
        if board[a] == board[b] == board[c] != " ":
            return True
    return False

player = "X"

for turn in range(9):
    display()
    position = int(input("Player " + player + ", enter position (1-9): ")) - 1

    if board[position] == " ":
        board[position] = player
    else:
        print("Position already occupied!")
        continue

    if check_winner():
        display()
        print("Player", player, "wins!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

else:
    display()
    print("Draw!")
