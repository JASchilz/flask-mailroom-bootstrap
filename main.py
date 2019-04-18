import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/make_donation')
def make_donation():
    return 'This is the donation create page, but I haven\'t made it yet.'

@app.route('/donations/')
def all():
    try:
        donor_name = request.args['donor']
        donations = Donation.select().join(Donor).where(Donor.name == donor_name)
    except KeyError:
        donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

