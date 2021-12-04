from itertools import accumulate

boards = []
draw_order = []
data=[]
with open("input.txt", "r") as f:
    data = f.read().splitlines()
    draw_order = data[0].split(",")
num_boards = int((len(data[2:]) + 1)/6)

# increment all values so that I can set to 0 if theyre correct. decrement at the end
boards = [[[int(val) + 1 for val in row.strip().split()] for row in data[board_index*6 + 2:(board_index*6 + 2)+5]] for board_index in range(0, num_boards)]
# boards[board_id][row][column]


def find_winner(boards):
    for i, board in enumerate(boards):
        for x in range(0, 5):
            horizontal_sum = board[x][0] + board[x][1] + board[x][2] + board[x][3] + board[x][4]
            vertical_sum = board[0][x] + board[1][x] + board[2][x] + board[3][x] + board[4][x]
            if horizontal_sum == 0 or vertical_sum == 0:
                return board
    return False


for draw_index, draw_number in enumerate(draw_order):
    boards = [[[0 if val == (int(draw_number) + 1) else val for val in row] for row in board] for board in boards]
    winner = find_winner(boards)
    if winner:
        winner = [[val-1 if val != 0 else val for val in row] for row in winner]

        total_sum = list(accumulate(list(accumulate(winner))[-1]))[-1] # lol
        print(f"Winning score is {int(draw_number) * total_sum}")
        break


