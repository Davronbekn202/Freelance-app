from main import *

while True:
    choose = input('choose the number: ')
    if choose == 'add':
        worker()
    elif choose == 'see':
        to_see()
    elif choose == 'del':
        remove()
    elif choose == 'update':
        update()
    else:
        print('please write valid command')
    try:
        if type(choose) == int:
            raise 'the type of choose is int write in str type'

    except Exception as errors:
        print(errors)
