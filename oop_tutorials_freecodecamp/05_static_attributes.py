# Static attrbutes
# Static attributes are attributes that are shared among all instances of a class.
# They are defined within the class but outside any instance methods.
# Static attributes are accessed using the class name rather than the instance name.

class User:
    # Static attribute
    user_count = 0

    def __init__(self, username):
        self.username = username
        User.user_count += 1  # Increment the static attribute when a new user is created

    def display_user(self):
        print(f"Username: {self.username}")
        print(f"Total Users: {User.user_count}")

# Creating instances of the User class
user1 = User("Alice")
user2 = User("Bob")
user3 = User("Charlie")
print(User.user_count)  # Output: 3
print(user1.user_count)  # Output: 3
user1.display_user()
# static attributes are indented once but install methods are indented twice

# when to use static attributes
# Use static attributes when you want to keep track of information that is shared among all instances of a class.
# Examples include counting the number of instances created, storing configuration settings, or maintaining a shared resource.