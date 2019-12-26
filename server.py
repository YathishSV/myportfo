from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:navigate>')
def html_page(navigate):
    return render_template(navigate)


@app.route('/submit-form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except :
            return "There is something wrong with saving data"
    else:
        return "There is something wrong . Please check"


def write_to_file(data):
    details = data['email'] + ',' + data['subject'] + ',' + data['message']
    with open('database.txt', 'a') as my_file:
        my_file.write('\n' + details)


def write_to_csv(data):
    # email = data["email"]
    # subject = data["subject"]
    # message = data["message"]
    field_names = ['email','subject','message']
    with open('csv_db.csv', 'a',newline='') as my_csv:
       # csv_writer = csv.writer(my_csv, delimiter=",")
        csv_writer = csv.DictWriter(my_csv,fieldnames=field_names)
        csv_writer.writerow(data)
