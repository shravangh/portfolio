from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def name():
    return render_template('index.html')

@app.route("/<string:name>")
def names(name):
    return render_template(name)

def write_to_data(data):
    with open('database.txt',mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{email},\n{subject},\n{message}')

def write_to_csv(data):
    with open('database2.csv',newline='',mode='a') as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database2, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route("/submit_form",methods=['get','POST'])
def submit_form():
    if request.method=='POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thank-you.html')
    else:
        return 'sorry try again'