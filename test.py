import psycopg2
from colorama import *

conn = psycopg2.connect(host='localhost', database='MVD_db', user='postgres', password='123', port='5432')

cur = conn.cursor()
cur.execute('SELECT mem_name FROM members ')
usernames = [r[0] for r in cur.fetchall()]
usernames.sort()  # Ensure the list is sorted

username = input('Log in:')
Found = False
low, high = 0, len(usernames) - 1

while low <= high and not Found:
    mid = (low + high) // 2
    if usernames[mid] == username:
        print(Fore.GREEN + 'Already in the list' + Style.BRIGHT + Style.RESET_ALL)
        Found = True
    elif usernames[mid] < username:
        low = mid + 1
    else:
        high = mid - 1

if not Found:
    print(Fore.RED + 'Doesn\'t exist' + Style.BRIGHT + Style.RESET_ALL)

conn.commit()
cur.close()
conn.close()
