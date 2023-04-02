# Ask the user to input their full name.
name = input('Please enter your full name')
length = len(name)
print(length)

# Validation checks on users name.
if length < 2:
    print('You haven’t entered anything. Please enter your full name')
elif length < 4:
    print('Please make sure that you have entered your name and surname.”')
elif length > 25:
    print('Please make sure that you have only entered your full name.')
else:
    print('Thank you for entering your full name')





