# just a basic login in program.

sname = 1234
spasword = 1234
name = input("enter your login name: ")
password = input("enter you password: ")


def add_me(name, password, sname, spasword):
    if int(name) == int(sname) and int(password) == int(spasword):
        print("user name correct")
        print("password correct, you are logged in.")
    else:
        print("Login failed")


add_me(name, password, sname, spasword)
