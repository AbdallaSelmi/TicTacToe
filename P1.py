# ALL ME (Abdalla)
def display_board(board):
    
    print('\n   1   2   3')
    print('A  ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('  ---|---|---')
    print('B  ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('  ---|---|---')
    print('C  ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2]) 


def check_win(board):
    for row in board: 
        if row[0] == row[1] == row[2] and row[0] != ' ': #checks rows fro win
            return row[0] 
    
    for col in range(3): #checks columns for win
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ': #checks diagonals for win
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    return None #if there's no winner yet


def check_draw(board):
    for row in board:
        if ' ' in row: #if there's an empty space (no draw)
            return False
    return True #if there's no empty spaces and no winner (draw) 

def get_player_move(board, player_symbol):
    while True:
        move = input(f"Player '{player_symbol}', enter your move (A1, B3, etc.): ").strip().upper() #strip and upper to keep all inputs consistent
        if len(move) != 2 or move[0] not in 'ABC' or move[1] not in '123':
            print('Invalid move. please try again in the following format (A1, B3, etc.).')
            continue 
        
        row = 'ABC'.index(move[0])# row calculation
        col = int(move[1]) - 1 # column calculation, and '-1' to maintain python indexing
        if board[row][col] != ' ':
            print('That space is already taken. choose another.')
            continue
        
        return row, col


def play_game(user1, user2):

    board = []
    for _ in range(3):
        board.append([' ', ' ', ' '])
    
    player_symbols = {user1: 'X', user2: 'O'}
    turn = 0 # variable that'll keep track of turns between players
    
    print('\nStarting a new game of Tic Tac Toe!')
    display_board(board) #showing the empty board
    
    while True:
        current_user = user1 if turn % 2 == 0 else user2 #it is user1's turn when turn is even, and user2's turn when odd
        player_symbol = player_symbols[current_user] #retrieval of the current player's symbol
        
        print(f"\nIt is {current_user}'s turn.")
        row, col = get_player_move(board, player_symbol) 
        board[row][col] = player_symbol #places player's symbol in the chosen space
        
        display_board(board) #shows the updated board
        
        winner = check_win(board)# call to check for win
        if winner:
            print(f'\nCongratulations, {current_user}! You win!')
            return current_user, 'win' 
        
        if check_draw(board): #call to check for draw
            print('\nThis game is a draw!')
            return None, 'draw'
        
        turn += 1 
