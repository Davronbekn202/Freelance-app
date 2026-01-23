from base.database2 import add_to_job, add_to_portfolio
from main import *

print("""
1 - add personal info
2 - see info
3 - remove info
4 - update info
5 - add work
""")
while True:
    choose = int(input('choose the number: '))
    if choose == 1:
        if worker():
            if add_portfolio():
                add_job()

    elif choose == 2:
        to_see()
    elif choose == 3:
        remove()
    elif choose == 4:
        update()
    elif choose == 5:
        adding_works()
    else:
        print('please write valid command')
