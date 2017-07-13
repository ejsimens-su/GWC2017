# Define the fields and methods for your object here.
#create instance of new users
class User:
    def init(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.user_connections = []
# Define the fields and methods for your object here.
# Define the program flow for your user interface here.
#class Network:

def main():
    users = []
    user_name = input('Please enter a username:')
    user_id = input('Enter in a user ID:')

    user1 = User(user_name, user_id)

    user_name.append(users)
    print('Users:', users)

# Runs your program.
if __name__ == '__main__':
    main():
