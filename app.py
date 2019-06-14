from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'flask'
app.config['MYSQL_DATABASE_PASSWORD'] = 'LeMotDePasseDeFlask'
app.config['MYSQL_DATABASE_DB'] = 'LeMarche'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)


@app.route('/fruits', methods=['GET', 'POST'])
def index():
    cur = mysql.connect()
    conn = cur.cursor()
    conn.execute("SELECT * FROM fruits")
    row = conn.fetchall()
    payload = []
    for result in row:
        content = {"id": result[0], 'nom': result[1]}
        payload.append(content)
    if request.method == "POST":
        fruit = request.form
        nomDuFruit = fruit['nom']
        conn.execute("INSERT INTO fruits(nom) VALUES (%s)", (nomDuFruit))
        cur.commit()
        cur.close()
        conn.close()
        print('Le fruit a bien ?t? ins?r? en bdd')
        return redirect('./fruits')

    return render_template('index.html', fruits=payload)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
