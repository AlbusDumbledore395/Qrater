from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {'yesh': '123', 'ravana': 'eesalacupnamde'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        return redirect(url_for('success'))
    else:
        return redirect(url_for('failure'))

@app.route('/success')
def success():
    return render_template('home.html')

@app.route('/failure')
def failure():
    return "Login failed!"

if __name__ == '__main__':
    app.run(debug=True)
