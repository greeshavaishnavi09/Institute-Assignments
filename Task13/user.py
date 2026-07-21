class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  

user1 = User("Greesha", "sdfghjy123")

# name mangling 
print(f"Username: {user1.username}")
print(f"Mangled Password Access: {user1._User__password}")
