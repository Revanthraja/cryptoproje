from flask import Flask, render_template, session, redirect, url_for,request,send_file
import os
import json 
from cipher import cipher_text


app = Flask(__name__)


app.secret_key = 'wanna_change'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app.config['static'] = './static'

params = None

with open("config.json",'r') as c:
	params = json.load(c)["params"]


@app.route('/')
def authentication():
	if('user' in session and session['user'] == params['user']):
		return redirect('dashboard')

	return render_template('login-page.html',change= False,status=-1,keyValidation=False)


@app.route('/login',methods = ['POST','GET'])
def login():
	if('user' in session and session['user'] == params['user']):
		return redirect('dashboard')

	if request.method=="POST":
		email = request.form.get('emailaddress')
		password = request.form.get('pass')
		if(password == params['admin_pass']):
			session['user'] = email
			return redirect('dashboard')

	return redirect('/')


@app.route('/change-password',methods = ['GET','POST'])
def change_password():
	if(request.method == 'POST'):
		email = request.form.get('emailaddress')
		if(email in params['user']):
			secretKey = request.form.get('secretKey')
			if(secretKey == params['secret_key']):
				new_pwd = request.form.get('pass')
				if(len(new_pwd)!=0):
					with open("config.json",'r+') as file:
						json_data = json.load(file)
						json_data['params']['admin_pass'] = new_pwd
						file.seek(0)
						json.dump(json_data,file)
						file.truncate()
						file.close()
					return render_template('login-page.html',status = 1,change= True,keyValidation=True)
			return render_template('login-page.html',status = -1,change= True,keyValidation=False)
		return render_template('login-page.html',change= True,status = 0,keyValidation=True)
	return render_template('login-page.html',change= True,status = -1,keyValidation=True)



@app.route('/dashboard',methods=['POST','GET'])
def dashboard():
	if('user' in session and session['user'] == params['user']):
		if(request.method=='POST'):
			check_data = request.form.get('fileType')
			info = request.form.get('text')
			file = request.files['file']
			fileType = request.form.get('fileType')
			key = request.form.get('key')
			file.save(os.path.join(app.config['static'],'userImage'))

			obj = cipher_text('userImage')
			obj.encryption(fileType,info,key)
			print(type(info))
			
			os.remove(os.path.join(app.config["static"],'userImage'))

			return redirect('download')
		return render_template('dashboard.html')
	else:
		return redirect('/')




@app.route('/decryption',methods = ['GET','POST'])
def decryption():
	data = False
	if('user' in session and session['user'] == params['user']):
		return render_template('decryption.html',data = data)

	return redirect('/')





@app.route('/decrypt-data',methods=['GET','POST'])
def decrypt_data():
	data = None
	if('user' in session and session['user'] == params['user']):
		if(request.method == 'POST'):
			file = request.files['file']
			key = request.form.get('key')
			file.save(os.path.join(app.config["static"],'userImage1.png'))

			obj = cipher_text(file.filename)
			data = obj.decryption(key)
			
			return render_template('decryption.html',data = data)



@app.route('/download')
def download_image():
	if('user' in session and session['user'] == params['user']):
		return render_template("download image.html")

	return redirect('/')



@app.route('/download-image')
def fetch_image():
	return send_file('static/userImage1.png',attachment_filename='EncryptedImage.png',as_attachment = True)



@app.route('/logout')
def logout():
	if('user' in session):
		session['user'] = None
	
	return redirect('/')

if __name__ == '__main__':
	app.run()