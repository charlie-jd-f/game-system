from hangman import play_hangman

LINE = '-'*60
USERS = "user_lib/users.txt"

class User:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def add_user(self):
        
        # open the file in append mode
        with open(USERS, 'a') as file:
            
            # add the username and password to the file
            file.write(f"{self.username},{self.password},\n")
            
    def password_checker(self, new_password):
        boolean = True if self.password == new_password else False
        return boolean
    
    
    
    def username_password_match(self):
        
        # open the file in read mode
        with open(USERS, 'r') as file:

            # loop through each line in the file, store the username
            # and password in a list
            user_info = []
            for line_no, line in enumerate(file):
                if self.username in line:
                    user_info = line.split(',')
                    break
        
        # Check if password or username are correct
        if user_info == []:
            print("Error! Username does not exist! Please try again.")
            boolean = False
        elif user_info[1] != self.password:
            print("Error: Incorrect password! Please try again.")
            boolean = False
        else:
            boolean = True
        
        return boolean            
                
def log_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    user = User(username,password)
    logged_in = user.username_password_match()
    return logged_in
        

def create_new_user():
    
    # Ask user for username and password
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    password_check = input("Enter your password again: ")
    new_user = User(username,password)
    
    if new_user.password_checker(password_check) == True:
        new_user.add_user()
    else:
        print(LINE + "\nError: Passwords did not match! Please try again.\n")
            
            
if __name__ == "__main__":

    print("Welcome to [working title]!.")

    while True:
        
        # Log-in menu
        print(LINE+"\nSelect an option from the list:\n"\
            "0. Exit\n"\
            "1. Log in\n"\
            "2. Create an account\n" + LINE)
        
        login_choice = input("Enter an option number: ")
        print(LINE)
        
        # Exit
        if login_choice == "0":
            print("Thank you for playing today!")
            break
        
        # Log in
        if login_choice == "1":
            
            logged_in = log_in()
            if logged_in == True:
                
                while True:
                    
                    # Main Menu
                    print(LINE + "\nSelect an option from the list:\n"\
                        "0. Go Back\n"\
                        "1. Play a game\n"\
                        "2. Leaderboard\n"\
                        "3. Game Statistics\n"+LINE)
                    
                    menu_option = input("Enter an option number: ")
                    print(LINE)
                    
                    if menu_option == "0":
                        break
                    elif menu_option == "1":
                        
                        # Game Menu
                        print("Select an option from the list:\n"\
                            "0. Go Back\n"\
                            "1. Hangman\n"+LINE)
                        
                        game_option = input("Enter an option number: ")
                        print(LINE)
                        
                        if game_option == "0":
                            break
                        elif game_option == "1":
                            
                            score = play_hangman()
                            
                        else:
                            print("Error! Invalid input! Please try again.")
                        
                    elif menu_option == "2":
                        print("leaderboard")
                    elif menu_option == "3":
                        print("game stats")
                    else:
                        print("Error! Invalid input! Please try again.")
                    
        # Create an account
        elif login_choice == "2":
            
            create_new_user()
          
        else:
            print("Error: Invalid Input! Please try again.")