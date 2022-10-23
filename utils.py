pass_log = []
details = []


def signup(email, name, username, password):
    global pass_log, details
    if username in pass_log:
        print("username is already taken")
        print("enter details:")
        signup(email, name, username, password)
    elif len(password) < 10 or password.isdigit():
        print("Password should have minimum of 10 characters and should contain at least one number")
        print("enter details:")
        signup(email, name, username, password)
    else:
        details.append([email, name, username, password])
        pass_log.append([username, password])
        print("you have successfully signed up")


def login(username, password):
    inp = [username, password]
    if inp in pass_log:
        print("logged in successfully")
    else:
        print("The username and password do not match")
        print("enter the username and password:")
        login(username, password)
