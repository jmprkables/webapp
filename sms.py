import sys
from phant import Phant
from twilio.rest import TwilioRestClient
from time import sleep
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ""
auth_token  = ""
client = TwilioRestClient(account_sid, auth_token)

p = Phant(public_key='', fields=[''], private_key='')

while(True):
	data = p.get()
	print("Latest Loudness Value is: {}".format(data[0]['temp']))
	if float(data[0]['temp']) > 1500:
		message = client.messages.create(body="{}".format(data[0]['']),
		    to="",    # Replace with your phone number
		    from_="") # Replace with your Twilio number
		print (message.sid)
	sleep(15)
