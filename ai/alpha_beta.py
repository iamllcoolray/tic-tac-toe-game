def best_move(board, player):
    node_count = 0
    opponent = 'O' if player == 'X' else 'X'

    def alpha_beta(b, depth, alpha, beta, is_maximizing):
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
            max_eval = -float('inf')
            for i in range(9):
                if b[i] == "":
                    b[i] = player
                    eval = alpha_beta(b, depth + 1, alpha, beta, False)
                    b[i] = ""
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(9):
                if b[i] == "":
                    b[i] = opponent
                    eval = alpha_beta(b, depth + 1, alpha, beta, True)
                    b[i] = ""
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval

    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == "":
            board[i] = player
            score = alpha_beta(board, 0, -float('inf'), float('inf'), False)
            board[i] = ""
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
