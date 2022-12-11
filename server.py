from flask import Flask, render_template, request, send_from_directory, redirect
import csv

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    send_from_directory(app.static_folder, 'favicon.ico')
    return render_template(page_name)

@app.route("/static/favicon.ico")
def fav():
    return send_from_directory(app.static_folder, 'favicon.ico')

def write_to_csv(data):
    with open('database.csv', 'a', encoding='windows-1251') as csvfile:
        names =  ['name', 'email', 'subject', 'message']
        file_writer = csv.DictWriter(csvfile, delimiter = ",", fieldnames=names)
        file_writer.writerow(data)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    return 'Try again.'


app.run('127.0.0.1', debug=True)