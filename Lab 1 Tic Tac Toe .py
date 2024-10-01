import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Human player
    computer_player = "O"

    print("Welcome to Tic-Tac-Toe!")
    print("Board positions:")
    print(" 0 | 1 | 2")
    print("-----------")
    print(" 3 | 4 | 5")
    print("-----------")
    print(" 6 | 7 | 8")

    while True:
        print_board(board)

        if current_player == "X":
            move = input(f"Player {current_player}, enter your move (0-8): ")
            try:
                move = int(move)
                row, col = divmod(move, 3)
                if board[row][col] != " ":
                    print("Invalid move. Cell already occupied. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 0 and 8.")
                continue
        else:
            # Computer's turn
            available_moves = get_available_moves(board)
            row, col = random.choice(available_moves)
            print(f"Computer ({computer_player}) chooses: {row * 3 + col}")

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = computer_player if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
