from flask import Flask, render_template, redirect, url_for, request
import os
import sqlite3

ctf = 'CTF_{' + 'SQL_INJECTION' + '}'
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html')

# Route for handling the login page logic
@app.route('/login', methods=['POST'])
def login():
    connection = sqlite3.connect('db/data.db')
    # create a database cursor
    cur = connection.cursor()
    
    try:
        # use prepare statement to avoid any sql injection
        #cur.execute('SELECT count(*) FROM users WHERE username = ? AND password = ?;', (request.form['username'], request.form['password']))

        # vulnerable to sql injection attacks
        query = "SELECT count(*) FROM users WHERE username = '%s' AND password = '%s'" % (request.form['username'], request.form['password'])
        #print(query)
        cur.execute(query)
        result = cur.fetchone()
        #print(result[0])
        if int(result[0]) > 0:
            connection.close()
            return render_template('ctf.html', ctf=ctf)

    except sqlite3.OperationalError:
        print(query)
    connection.close()
    error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

def main():
    port=int(os.environ.get("PORT", 8080))
    app.run(debug=False, host="0.0.0.0", port=port)

if __name__ == '__main__':
    main()
