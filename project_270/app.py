# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define route and Verify_otp() function below
@app.route('/login',methods=['POST'])
def verify_otp():
	username=request.form['username']
	password=request.form['password']
	mobile_number=request.form['number']
	if username=='verify' and password=='12345':
		account_sid='AC7a0a20f5856f98da085f1e7661c186b4'
		auth_token='98c0daf366b7a7fcea1817f573bace9f'
		client=Client(account_sid,auth_token)



		verification = client.verify \
			.services('VA0fcfc2efa468aae047d1c28a30ce6616') \
			.verifications \
			.create(to=mobile_number, channel='sms')

		print(verification.status)
		return render_template('otp_verify.html')
	else:
		return "Entered User ID or Password is wrong"





if __name__ == "__main__":
    app.run()

