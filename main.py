from database import *
def worker():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    add_account(name,surname,email,password)
def to_see():
    show_result()

to_see()