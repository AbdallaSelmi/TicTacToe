# Whole file made by TAYYAB
def load_users(file_name='users.txt'):
    # reads user data from the file and returns it as a dictionary
    users = {}
    with open(file_name, 'r') as file:
        for line in file:
            username, password, wins, losses, draws = line.strip().split('|')
            users[username] = {
                'password': password,
                'wins': int(wins),
                'losses': int(losses),
                'draws': int(draws)
            }
    return users

def save_users(users, file_name='users.txt'):
    # writes user dictionary back to file
    with open(file_name, 'w') as file:
        for username, data in users.items():
            line = f'{username}|{data["password"]}|{data["wins"]}|{data["losses"]}|{data["draws"]}\n'
            file.write(line)


def login_user(users):
    # prompts user to log in w/ username & password
    # returns username if login is successful
    print('\nLogin:')
    username = input('Enter username: ').strip()
    password = input('Enter password: ').strip()

    if username in users and users[username]['password'] == password:
        print(f'Welcome back, {username}!')
        return username
    else:
        print('Invalid username or password. Please try again.')
        return None


def register_user(users):
    # allows a new user to register by putting in a unique username and password
    # returns the username of new user    
    print('\nRegister:')
    while True:
        username = input('Enter your username: ').strip()
        if username in users:
            print('Username already exists. Please try a different one.')
            continue

        password = input('Enter your password: ').strip()
        users[username] = {'password': password, 'wins': 0, 'losses': 0, 'draws': 0}
        print(f'User "{username}" registered successfully!')
        return username


def update_scores(users, username, result):
    # updates user's score based on result of the game.
    # reults include win, loss or draw
    if username not in users:
        print(f'Error: User "{username}" not found.')
        return

    if result == 'win':
        users[username]['wins'] += 1
    elif result == 'loss':
        users[username]['losses'] += 1
    elif result == 'draw':
        users[username]['draws'] += 1

