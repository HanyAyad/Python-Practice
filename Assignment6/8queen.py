def draw_board(queens):
    board_size = len(queens)
    board = [['.'] * board_size for _ in range(board_size)]
    for row, col in enumerate(queens):
        board[col][row] = 'Q'
    print('+-----------------+')
    for row in board:
        print('| ' + ' '.join(row) + ' |')
    print('+-----------------+')

if __name__=="__main__":
    queens=[0,4,7,5,2,6,1,3]
    draw_board(queens)