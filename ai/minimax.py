import random
def best_move(board, player):
    node_count = 0
    opponent = 'O' if player == 'X' else 'X'

    def minimax(b, is_maximizing):
        nonlocal node_count
        node_count += 1
        winner = check_winner(b)
        if winner == player:
            return 1
        elif winner == opponent:
            return -1
        elif "" not in b:
            return 0

        if is_maximizing:
            best = -float('inf')
            for i in range(9):
                if b[i] == "":
                    b[i] = player
                    score = minimax(b, False)
                    b[i] = ""
                    best = max(score, best)
            return best
        else:
            best = float('inf')
            for i in range(9):
                if b[i] == "":
                    b[i] = opponent
                    score = minimax(b, True)
                    b[i] = ""
                    best = min(score, best)
            return best

    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == "":
            board[i] = player
            score = minimax(board, False)
            board[i] = ""
            if score == best_score:
                random_num = random.randint(1, 12)
                if random_num % 4 == 0:
                    best_score = score
                    move = i
            if score > best_score:
                best_score = score
                move = i

    board[move] = player
    return board, move, node_count

def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for x,y,z in wins:
        if b[x] and b[x] == b[y] == b[z]:
            return b[x]
    return None
