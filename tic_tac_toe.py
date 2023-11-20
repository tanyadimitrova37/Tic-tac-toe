from random import randrange

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
first_row = " +-------+-------+-------+\n"
lines = "|       |       |       |\n"
pluses = "+-------+-------+-------+\n"
last_row = "+-------+-------+-------+"

def display_board(board):
    print(first_row,
          lines,
          "|  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], "  |\n",
          lines,
          pluses,
          lines,
          "|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], "  |\n",
          lines,
          pluses,
          lines,
          "|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |\n",
          lines,
          last_row)

def enter_move(board):
    print("Enter your move: ", end=" ")
    move_player = int(input())
    if 0 > move_player or move_player > 9:
        print("Move not valid")
        return enter_move(board)

    field_taken = True

    for i in range(0, len(board)):
        for m in range(0, len(board[i])):
            if board[i][m] == move_player:
                board[i][m] = "O"
                field_taken = False
    if field_taken:
        print("Field taken")
        enter_move(board)
        return
    else:
        return display_board(board)

def computer_move(board):
    comp_move = randrange(1, 10)
    field_taken = True

    for i in range(0, len(board)):
        for m in range(0, len(board[i])):
            if board[i][m] == comp_move:
                board[i][m] = "X"
                field_taken = False
    if field_taken:
        computer_move(board)
    else:
        display_board(board)
        return

def make_list_of_free_fields(board):
    available_fields = True
    free_fields_list = []
    for i in range(0, len(board)):
        for m in range(0, len(board[i])):
            if type(board[i][m]) == int:
                free_fields_list.append((i, m))

    return free_fields_list

def victory_for(board, sign):
    if sign == "X" and ((board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or
                        (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or
                        (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or
                        (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or
                        (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or
                        (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") or
                        (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or
                        (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X")):
        print("Computer won!")
        return True
    elif sign == "O" and ((board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or
                          (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or
                          (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or
                          (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or
                          (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or
                          (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O") or
                          (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or
                          (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O")):
        print("You won!")
        return True
    else:
        return False

def draw_move(board):
    computer_move(board)
    print("It's a draw")
    return

def play():
    display_board(board)
    while True:
        free = make_list_of_free_fields(board)
        if len(free) == 0:
            print("It's a draw")
            break
        else:
            enter_move(board)
            if (victory_for(board, "O")):
                break
            else:
                computer_move(board)
                if (victory_for(board, "X")):
                    break

 play()
