from app.hash import HashTest


new_pass = input('Please enter a password: ')
hashed_password = HashTest.hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')
if HashTest.check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')
