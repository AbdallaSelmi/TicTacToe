from P1 import play_game
from P2 import load_users, save_users, login_user, register_user, update_scores

def main_menu(): # Abdalla
    print('\nWelcome to Tic Tac Toe!') #navigation menu
    print('1. Login')
    print('2. Register')
    print('3. Play Game')
    print('4. View Scores')
    print('5. Exit')

def view_scores(users): # Abdalla
    print('\nScores:')
    print('Username    Wins   Losses   Draws')
    print('---------------------------------')
    for username, data in users.items(): # retrieval of data
        print(f'{username:<12}{data["wins"]:<7}{data["losses"]:<8}{data["draws"]}')

def main(): # Tayyab
    users = load_users('user.txt')
    current_user = None

    while True:
        main_menu()
        choice = input('\nEnter your choice (1-5): ').strip()

        if choice == '1': #login
            current_user = login_user(users)
        elif choice == '2':  #register
            current_user = register_user(users)
        elif choice == '3':  #play game
            if not current_user:
                print('You need to login or register before playing!')
                continue
            
            opponent = input('Enter the username of the opponent: ').strip() 
            if opponent not in users:
                print(f'User "{opponent}" does not exist.')
                continue

           
            result_user, result = play_game(current_user, opponent)
            if result == 'win': #winner's score updated
                update_scores(users, result_user, 'win')
                loser = current_user if result_user == opponent else opponent #loser's score updated
                update_scores(users, loser, 'loss')
            elif result == 'draw': #draw updated into scores
                update_scores(users, current_user, 'draw')
                update_scores(users, opponent, 'draw')
        elif choice == '4':  #view scores
            view_scores(users)
        elif choice == '5':  #exit
            save_users(users, 'user.txt')
            print('Thanks for playing! Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
