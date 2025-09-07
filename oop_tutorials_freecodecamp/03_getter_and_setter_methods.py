


# Getter and Setter Methods
from datetime import datetime
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        return self._email
    
    def set_email(self, new_email):
        if '@' in new_email:
            self._email = new_email
            print(f"Email changed to {new_email} at {datetime.now()}")
        


user5 = User("Vinay", 'nvinay1303@gmail.com', '1232*223')
user5.set_email('n.vinay@gridx.de')
print(user5.get_email())

user1 = User("Aruni", 'nvinay1303@gmail.com', 'sdfsfss')
user1.set_email('sdfs@faf')

# Getter and setter methods are providing a controlled way to access emails. Helps to improve integrity of data.
# Access and modify data in a controlled way
# This is how it's done in Java.. it's very verbose.. python has a simpler way