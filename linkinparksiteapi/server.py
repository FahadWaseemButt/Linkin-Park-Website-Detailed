from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = '172.18.0.3'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Test@1234'
app.config['MYSQL_DB'] = 'linkinparksite'

mysql = MySQL(app)

# Members API Route
@app.route("/members")
def members():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM members")
    data = cur.fetchall()
    cur.close()
    return {"members": [member[1] for member in data]}  # Assuming member name is in the second column

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')