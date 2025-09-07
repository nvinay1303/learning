class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # make a data attribute protected by prefixing it with an underscore (_).. don't read attr. outside of its class/subclasses..it'a convention
        self.password = password

    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")

    def get_email(self):
        return self._email
    
    def clean_email(self):
        return self._email.lower().strip()


user1 = User('Nikhil', '  nivnay1303@gmail.com ', '23232343')
user2 = User('Aruni', 'aruni12@gmail.com', '23213123')

user1.say_hi_to_user(user2)

# print(user1._email) # still accessible from outside the class but not supposed to use outside the class (python convention for developers)
# user1._email = '234324' # poor python etiquette
# print(user1.clean_email()) # this is okay but not the above use where we access the attribute from outside the class

# The consenting adults philosophy; but attributes can be made private using double underscore (__)
# python does name mangling (change the name of attributes; make variables private) when __ is used so that attributes cannot be 

'''
Protected (_) vs Private (__) variables
- protected variables can be accessed outside the class but you're not supposed to but private variables 
cannot be accessed outside the class. theyoffer better readability and flexibility making them the preferred 
choice.
'''