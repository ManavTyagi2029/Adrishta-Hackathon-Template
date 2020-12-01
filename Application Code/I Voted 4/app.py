from flask import Flask,render_template,request,redirect,url_for,session
import sqlite3

app=Flask(__name__)
app.config['SECRET_KEY']='ivotexyz'
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

with sqlite3.connect('votingbase.db') as conn:
	cur=conn.cursor()
	cur.execute('SELECT * from president')
	data1=cur.fetchall()
	cur.execute('SELECT * from g_sec')
	data2=cur.fetchall()
	cur.execute('SELECT * from cultural')
	data3=cur.fetchall()
	cur.execute('SELECT * from mess_sec')
	data4=cur.fetchall()

@app.route('/')
def index():
	msg=''
	return render_template('login.html',msg=msg)

@app.route('/admin')
def admin():
	with sqlite3.connect('votingbase.db') as conn:
		cur=conn.cursor()
		cur.execute('SELECT * from president')
		data1=cur.fetchall()
		cur.execute('SELECT * from g_sec')
		data2=cur.fetchall()
		cur.execute('SELECT * from cultural')
		data3=cur.fetchall()
		cur.execute('SELECT * from mess_sec')
		data4=cur.fetchall()
	return render_template('admin.html',username=session['username'],op1=data1,op2=data2,op3=data3,op4=data4)

@app.route('/cform',methods=['POST','GET'])
def cform():
	if request.method=='POST':
		candidate=request.form
		name=candidate['name']
		email=candidate['email']
		branch=candidate['b_select']
		motive=candidate['agenda']
		post=candidate['post_select']
		img=candidate['image_input']
		val=0
		if(post=='VP'):
			k=1
		elif (post=='G.sec'):
			k=2
		elif (post=='C.sec'):
			k=3
		else:
			k=4
		if k==1:
			with sqlite3.connect('votingbase.db') as conn:
				cur=conn.cursor()
				cur.execute("INSERT INTO president VALUES(?,?,?,?,?,?,?)",(name,email,branch,post,motive,val,img))
				conn.commit()
		elif k==2:
			with sqlite3.connect('votingbase.db') as conn:
				cur=conn.cursor()
				cur.execute("INSERT INTO g_sec VALUES(?,?,?,?,?,?,?)",(name,email,branch,post,motive,val,img))
				conn.commit()
		elif k==3:
			with sqlite3.connect('votingbase.db') as conn:
				cur=conn.cursor()
				cur.execute("INSERT INTO cultural VALUES(?,?,?,?,?,?,?)",(name,email,branch,post,motive,val,img))
				conn.commit()
		else:
			with sqlite3.connect('votingbase.db') as conn:
				cur=conn.cursor()
				cur.execute("INSERT INTO mess_sec VALUES(?,?,?,?,?,?,?)",(name,email,branch,post,motive,val,img))
				conn.commit()
		return redirect(url_for('admin'))
	return render_template('Cform.html')

@app.route('/dform',methods=['POST','GET'])
def dform():
	if request.method=='POST':
		del_cand=request.form
		name=del_cand['name']
		email=del_cand['email']
		post=del_cand['post_select']
		if(post=='VP'):
			k=1
		elif (post=='G.sec'):
			k=2
		elif (post=='C.sec'):
			k=3
		else:
			k=4
		if k==1:
			with sqlite3.connect('votingbase.db') as conn:
				cur=conn.cursor()
				cur.execute("DELETE FROM president WHERE email=? and name=?",(email,name))
				conn.commit()
		elif k==2:
			with sqlite3.connect('votingbase.db') as conn:
				cur=conn.cursor()
				cur.execute("DELETE FROM g_sec WHERE email=? and name=?",(email,name))
				conn.commit()
		elif k==3:
			with sqlite3.connect('votingbase.db') as conn:
				cur=conn.cursor()
				cur.execute("DELETE FROM cultural WHERE email=? and name=?",(email,name))
				conn.commit()
		else:
			with sqlite3.connect('votingbase.db') as conn:
				cur=conn.cursor()
				cur.execute("DELETE FROM mess_sec WHERE email=? and name=?",(email,name))
				conn.commit()
		return redirect(url_for('admin'))
	return render_template('Dform.html')

@app.route('/voter')
def voter():
	with sqlite3.connect('votingbase.db') as conn:
		cur=conn.cursor()
		cur.execute('SELECT * from president')
		data1=cur.fetchall()
		cur.execute('SELECT * from g_sec')
		data2=cur.fetchall()
		cur.execute('SELECT * from cultural')
		data3=cur.fetchall()
		cur.execute('SELECT * from mess_sec')
		data4=cur.fetchall()
	return render_template('voter.html',msg='',username=session['username'],op1=data1,op2=data2,op3=data3,op4=data4)

@app.route('/gvoter')
def gvoter():
	with sqlite3.connect('votingbase.db') as conn:
		cur=conn.cursor()
		cur.execute('SELECT * FROM g_sec')
		data2=cur.fetchall()
	return render_template('gvoter.html',msg='',op2=data2)

@app.route('/login',methods=['POST','GET'])
def login():
	if request.method=='POST':
		log_info=request.form
		emailid=log_info['email']
		password=log_info['password']
		user=log_info['client_select']
		if (user=='V'):
			with sqlite3.connect('votingbase.db') as conn:
				cur=conn.cursor()
				cur.execute('SELECT email,password FROM voter_records')
				data=cur.fetchall()
				for i in data:
					if (i[0]==emailid) and (i[1]==password):
						k=1
						break
					else:
						k=2
				if k==1:
					session['username']=log_info['email']
					return redirect(url_for('voter'))
				else:
					msg="Try Again"
					return redirect(url_for('index',msg=msg))
		elif (user=='A'):
			with sqlite3.connect('votingbase.db') as conn:
				cur=conn.cursor()
				cur.execute('SELECT * FROM admin_records')
				data=cur.fetchall()
				for i in data:
					if (i[0]==emailid) and (i[1]==password):
						k=1
					else:
						k=2
				if k==1:
					session['username']=log_info['email']
					print(session['username'])
					return redirect(url_for('admin'))
				else:
					msg="Try Again"
					return redirect(url_for('index',msg=msg))
	return render_template('login.html')

@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username',None)
	return redirect(url_for('index'))

@app.route('/results')
def results():
	username=session['username']
	with sqlite3.connect('votingbase.db') as conn:
		cur=conn.cursor()
		cur.execute('SELECT vote_count FROM president ORDER BY vote_count DESC')
		d1=cur.fetchall()
		cur.execute('SELECT vote_count FROM g_sec ORDER BY vote_count DESC')
		d2=cur.fetchall()
		cur.execute('SELECT vote_count FROM cultural ORDER BY vote_count DESC')
		d3=cur.fetchall()
		cur.execute('SELECT vote_count FROM mess_sec ORDER BY vote_count DESC')
		d4=cur.fetchall()
		if (d1[0][0]>0) and (d2[0][0]>0) and (d3[0][0]>0) and (d4[0][0]>0):
			cur.execute('SELECT * FROM president ORDER BY vote_count DESC')
			data1=cur.fetchall()
			cur.execute('SELECT * FROM g_sec ORDER BY vote_count DESC')
			data2=cur.fetchall()
			cur.execute('SELECT * FROM cultural ORDER BY vote_count DESC')
			data3=cur.fetchall()
			cur.execute('SELECT * FROM mess_sec ORDER BY vote_count DESC')
			data4=cur.fetchall()
			return render_template('result.html',op1=data1[0],op2=data2[0],op3=data3[0],op4=data4[0],msg='',username=username)
		else:
			msg="No voting Yet"
			return render_template('result.html',msg=msg,username=username)

@app.route('/vpvoting',methods=['POST','GET'])
def vpvoting():
	if request.method=='POST':
		user_email=session['username']
		cand_email=request.form['vp_name']
		with sqlite3.connect('votingbase.db') as conn:
			cur=conn.cursor()
			cur.execute('UPDATE president SET vote_count=vote_count + ? where email=?',(1,cand_email))
			cur.execute('UPDATE voter_records SET vp_count=vp_count +? where email=?',(1,user_email))
			msg="Voted"
			return redirect(url_for('gvoter'))
	return render_template('voter.html')

@app.route('/gsecvoting',methods=['POST','GET'])
def gsecvoting():
	if request.method=='POST':
		user_email=session['username']
		cand_email=request.form['vp_name']
		with sqlite3.connect('votingbase.db') as conn:
			cur=conn.cursor()
			cur.execute('UPDATE g_sec SET vote_count=vote_count + ? where email=?',(1,cand_email))
			cur.execute('UPDATE voter_records SET gs_count=gs_count +? where email=?',(1,user_email))
			msg="Voted"
			return redirect(url_for('cvoter'))
	return render_template('gvoter.html')

@app.route('/cvoter')
def cvoter():
	with sqlite3.connect('votingbase.db') as conn:
		cur=conn.cursor()
		cur.execute('SELECT * FROM cultural')
		data3=cur.fetchall()
	return render_template('cvoter.html',msg='',op3=data3)

@app.route('/csecvoting',methods=['POST','GET'])
def csecvoting():
	if request.method=='POST':
		user_email=session['username']
		cand_email=request.form['vp_name']
		with sqlite3.connect('votingbase.db') as conn:
			cur=conn.cursor()
			cur.execute('UPDATE cultural SET vote_count=vote_count + ? where email=?',(1,cand_email))
			cur.execute('UPDATE voter_records SET cs_count=cs_count +? where email=?',(1,user_email))
			msg="Voted"
			return redirect(url_for('mvoter'))
	return render_template('cvoter.html')


@app.route('/mvoter')
def mvoter():
	with sqlite3.connect('votingbase.db') as conn:
		cur=conn.cursor()
		cur.execute('SELECT * FROM mess_sec')
		data4=cur.fetchall()
	return render_template('mvoter.html',msg='',op4=data4)

@app.route('/messvoting',methods=['POST','GET'])
def messvoting():
	if request.method=='POST':
		user_email=session['username']
		cand_email=request.form['vp_name']
		with sqlite3.connect('votingbase.db') as conn:
			cur=conn.cursor()
			cur.execute('UPDATE mess_sec SET vote_count=vote_count + ? where email=?',(1,cand_email))
			cur.execute('UPDATE voter_records SET ms_count=ms_count +? where email=?',(1,user_email))
			msg="Voted"
			return redirect(url_for('logout'))
	return render_template('cvoter.html')





