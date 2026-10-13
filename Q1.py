# Q1: Username Validation System

# Accept the username from the user
username = input("Enter a username: ")

# Rule checks (each stored as a Boolean for clarity)
only_spaces = username.strip() == ""            # empty or spaces only
too_short = len(username) < 5                   # fewer than 5 characters
is_admin = username.lower() == "admin"          # ignore upper/lower case

# Check order matters: spaces first so " " gets the most meaningful reason
if only_spaces:
    print("Invalid username: it cannot contain only spaces.")
elif too_short:
    print("Invalid username: it must contain at least 5 characters.")
elif is_admin:
    print("Invalid username: 'admin' is reserved (case is ignored).")
else:
    print("Valid username:", username)
