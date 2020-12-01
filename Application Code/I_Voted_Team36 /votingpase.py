import sqlite3

conn=sqlite3.connect('votingbase.db')
print('Database created')
conn.execute('CREATE TABLE IF NOT EXISTS voter_records (name TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL, vp_count INTEGER, gs_count INTEGER,cs_count INTEGER, ms_count INTEGER )')
print("Table created successfully!")
'''
name='Ravi Sharma'
email='ravi12@gmail.com'
passes='ravi1'
for i in range(1):
	conn.execute('INSERT INTO voter_records values(?,?,?,?,?,?,?)',(name,email,passes,0,0,0,0))
print("inserted")
'''

#conn.execute('INSERT INTO voter_records VALUES ()')
conn.execute('CREATE TABLE IF NOT EXISTS president (name TEXT NOT NULL,email TEXT NOT NULL, branch TEXT NOT NULL,post TEXT NOT NULL, agenda TEXT NOT NULL, vote_count INTEGER )')
conn.execute('CREATE TABLE IF NOT EXISTS g_sec (name TEXT NOT NULL,email TEXT NOT NULL, branch TEXT NOT NULL,post TEXT NOT NULL, agenda TEXT NOT NULL, vote_count INTEGER )')
conn.execute('CREATE TABLE IF NOT EXISTS cultural (name TEXT NOT NULL,email TEXT NOT NULL, branch TEXT NOT NULL,post TEXT NOT NULL, agenda TEXT NOT NULL, vote_count INTEGER )')
conn.execute('CREATE TABLE IF NOT EXISTS mess_sec (name TEXT NOT NULL,email TEXT NOT NULL, branch TEXT NOT NULL,post TEXT NOT NULL, agenda TEXT NOT NULL, vote_count INTEGER )')
conn.execute('CREATE TABLE IF NOT EXISTS admin_records (email TEXT NOT NULL,password TEXT NOT NULL)')
conn.commit()
cur=conn.cursor()
cand_email='b@gmail.com'
'''
cur.execute('UPDATE president set vote_count=?',(0,))
cur.execute('UPDATE g_sec set vote_count=?',(0,))
cur.execute('UPDATE cultural set vote_count=?',(0,))
cur.execute('UPDATE mess_sec set vote_count=?',(0,))
cur.execute('UPDATE voter_records set vp_count=?',(0,))
cur.execute('UPDATE voter_records set gs_count=?',(0,))
cur.execute('UPDATE voter_records set cs_count=?',(0,))
cur.execute('UPDATE voter_records set ms_count=?',(0,))
'''
cur.execute('SELECT email,password FROM voter_records')
data=cur.fetchall()
print(data)
conn.close()