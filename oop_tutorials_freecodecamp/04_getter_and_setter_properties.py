# Instead of getter and setter methods above, we can use properties which are less verbose and more effective

class User:
    def __init__(self, username, password, email):
        self.name = username
        self.password = password
        self._email = email # protected attribute (should not be accessed directly outside the class)

    # Read-only property
    @property
    def email(self):
        return self._email + '123'
    
    # Updateable property
    # Exposing public email property while keeping email attribute protected
    @email.setter # standard python way of creating setter properties
    def email(self, new_email):
        if '@' in new_email: # simple validation logic
            self._email = new_email
            print(f"Email changed to {self.email}")
        else:
            print('Invalid email')




user1 = User("Nikhil", '123141', 'nik@gmail.com')
user1.email = 'bull@' #triggers setter property
print(user1.email) # public email property while keeping email attribute protected




