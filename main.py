import psycopg2

conn = psycopg2.connect(host = 'localhost', database = 'amir', user = 'postgres', password = '123', port = '5432')

cur = conn.cursor()
cur.execute('SELECT first_name FROM actor')
usernames = [r[0] for r in cur.fetchall()]
username = input('Log in:')
while not Found:
   if username in usernames:
      print('Alredy in list')
      Found = True
   else:
      print('Don`t exist')

conn.commit()
cur.close()
conn.close()
   
   