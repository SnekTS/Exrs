import psycopg2
from colorama import *

conn = psycopg2.connect(host = 'localhost', database = 'MVD_db', user = 'postgres', password = '123', port = '5432')

cur = conn.cursor()
cur.execute('SELECT mem_name FROM members ')
usernames = [r[0] for r in cur.fetchall()]
username = input('Log in:')
Found = False
while not Found:
   if username in usernames:
      print(Fore.GREEN + 'Alredy in list' + Style.BRIGHT + Style.RESET_ALL)
      Found = True
   else:
      print(Fore.RED + 'Don`t exist' + Style.BRIGHT + Style.RESET_ALL)
      break
   
conn.commit()
cur.close()
conn.close()
   
   