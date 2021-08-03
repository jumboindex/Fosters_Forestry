from flask import Flask, redirect, url_for, render_template, request
import smtplib

app = Flask(__name__, static_url_path='', static_folder='Resources/')

@app.route("/home/")
def home():
    return render_template("index.html", methods=['GET'])


@app.route("/submit", methods=['POST'])
def form():

    
    # grab form data after sumbission  
    contact = request.form["name"]
    email = request.form["email"]
    number = request.form["phone"]
    customerMessage = request.form['message']
   
    # create message
    emailMessage = contact + "  " + email + "  " + number + "  " + customerMessage
    print(emailMessage)
    #email to psudeo mail server
    #server = smtplib.SMTP("smtp.gmail.com", 587)
    #server.starttls()
    #server.login("sales@fostersforestry.co.uk", "NOTAPASSWORD")
    #server.sendmail("norepy@fostersforestry.co.uk", "sales@fostersforestry.co.uk", emailMessage)
    
    return redirect(url_for("home"))
  

if __name__ == "__main__":
    app.run()

