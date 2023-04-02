from flask import Flask, request, render_template
from twilio.rest import Client
import geocoder

app = Flask(__name__)

# initialize Twilio client with your account SID and auth token
client = Client("ACf23d3a0c0e95b07c82f43964dc9f0965", "b2cd229ed473284df9352000790d5be5")

# define message to be sent
message = "Emergency! Please help! My location is: "

# define emergency contacts
contacts = {"Dharcha": "+919025740216", "Shiva": "+917010480901"}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # name = request.form['name']
        # phone_number = request.form['phone_number']

        # get current location
        g = geocoder.ip('me')
        location = g.latlng

        # add location to message
        message_with_location = message + str(location)

        # send message to emergency contacts
        for name, number in contacts.items():
            client.messages.create(
                to=number, 
                from_="+15855221700", 
                body="Emergency alert from " + name + "! " + message_with_location
            )

        return 'Emergency alert sent to contacts!'

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)