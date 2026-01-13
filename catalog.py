from main import *
print("""
1 - add
2 - see
3 - remove
3 - update
""")
while True:
    choose = int(input('choose the number: '))
    if choose == 1:
        worker()
    elif choose == 2:
        to_see()
    elif choose == 3:
        remove()
    elif choose == 4:
        update()
    else:
        print('please write valid command')

