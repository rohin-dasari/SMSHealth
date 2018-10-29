from flask import Flask,render_template,request
from twilio.rest import Client
from flask_sqlalchemy import sqlalchemy 

app = Flask(__name__)



@app.route('/send',methods=['GET','POST'])

def send():

    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dateofbirth']
        pnum = request.form['phonenum']     # for future
        v1 = request.form.get('vaccinations1')
        v2 = request.form.get('vaccinations2')
        v3 = request.form.get('vaccinations3')

        
        
        if v1 == "Flu" and v2 == "Tetanus" and v3 == "Vaccine_n":
            text1 = "Great! Looks like you're all caught up on your vaccinations. You played a part in taking charge of your health and preventing an outbreak. Pass this along to get your friends and family vaccinated as well."
        if v1 == "Flu" and v2 != "Tetanus" and v3 != "Vaccine_n":
            text1 = "Great looks like you got your Flu Vaccine. You played a part in taking charge of your health and preventing an outbreak. Pass this along to get your friends and family vaccinated as well. Shots still required: Tetanis, Vaccine_n."
        if v1 == "Flu" and v2 != "Tetanus" and v3 == "Vaccine_n":
            text1 = "You played a part in taking charge of your health and preventing an outbreak. Pass this along to get your friends and family vaccinated as well. Shots still required: Tetanus."
        if v1 == "Flu" and v2 == "Tetanus" and v3 != "Vaccine_n":
            text1 = "You played a part in taking charge of your health and preventing an outbreak. Pass this along to get your friends and family vaccinated as well. Shots still required: Vaccine_n."

        if v1 != "Flu" and v2 == "Tetanus" and v3 == "Vaccine_n":
            text1 = "Shots still required: Flu."
        if v1 != "Flu" and v2 == "Tetanus" and v3 != "Vaccine_n":
            text1 = "Shots still required: Flu, Vaccine_n."
        if v1 != "Flu" and v2 != "Tetanus" and v3 != "Vaccine_n":
            text1 = "Shots still required: Flu, Tetanus, Vaccine_n."
        
        
        
        
        yr1 = dob[5]
        yr2 = dob[6]
        yr3 = '19'
        yr = yr3+yr1+yr2
        yr = int(yr)
        age = 2018 - yr
        agedif = 21-age
        agediff = str(agedif)
        if agedif >= 1:
            text2 = " Vaccination_n deadline coming up in " + agediff + " year(s)."
        
        else:
            text2 = ""
        
        Body = "Hello " + name + ". " + text1
        full  = Body+text2

        account_sid = "****************"
        auth_token = "******************"

        client = Client(account_sid,auth_token)
        client.messages.create(to="+1**********",from_ = "+1**********",body = full)
        
        return render_template('age.html',dateofbirth = age)

    


    return render_template('index.html')

    

if __name__ == "__main__":
    app.run()

    
