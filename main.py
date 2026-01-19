from base.database import *
from base.database2 import *
from updates import *


def worker():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    add_account(name, surname, email, password)


def to_see():
    show_result()


def remove():
    pick_up = input('Enter id: ')
    delete_info(pick_up)
    print('information deleted successfully')

def update():
    print("""
    1 - name
    2 - surname
    3 - email
    4 - password
    0 - stop updating
    """)
    while True:
        options = int(input('Which you want to update: '))
        if options == 1:
            from_which_id = int(input("Enter id: "))
            what_name = input("Enter name: ").title()

            update_name(what_name, from_which_id)
            print("information updated successfully")
        elif options == 2:
            from_which_id = int(input("Enter id: "))
            what_surname = input("Enter surname: ").title()
            update_surname(what_surname, from_which_id)
            print("information updated successfully")
        elif options == 3:
            from_which_id = int(input("Enter id: "))
            what_email = input("Enter email: ").title()
            update_email(what_email, from_which_id)
            print("information updated successfully")
        elif options == 4:
            from_which_id = int(input("Enter id: "))
            what_password = input("Enter password: ").title()
            update_password(what_password, from_which_id)
            print("information updated successfully")
        elif options == 0:
            break
        else:
            print('Invalid option')

def add_job():
    occupation = input("Enter your occupation: ")
    experience = input("Enter your experience: ")
    portfolio_id = int(input("Enter portfolio id: "))
    accounts_id = int(input("Enter accounts id: "))
    add_to_job(occupation,experience,portfolio_id,accounts_id)


def add_portfolio():
    title = input("Enter the title: ").title()
    description = input("Enter the description: ").capitalize()
    created_at = input("Enter the created at: ")
    accounts_id = int(input("Enter accounts id: "))