from flask import Flask, render_template, request, jsonify
from ai.minimax import best_move as minimax_move
from ai.alpha_beta import best_move as alpha_beta_move
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ai-move', methods=['POST'])
def ai_move():
    data = request.get_json()
    board = data['board']
    player = data.get('player', 'X')
    difficulty = data.get('difficulty', 'hard')

    if difficulty == 'easy':
        possible_moves = [i for i, val in enumerate(board) if val == ""]
        move = random.choice(possible_moves)
        board[move] = player
        node_count = 0
    elif difficulty == 'medium':
        board, move, node_count = minimax_move(board, player)
    else:
        board, move, node_count = alpha_beta_move(board, player)

    next_player = 'O' if player == 'X' else 'X'
    return jsonify({'board': board, 'player': next_player, 'nodesExplored': node_count})

if __name__ == '__main__':
    app.run(debug=True)
