from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
from website import create_app as init


# app = Flask(__name__)
# app.secret_key = 'ticket selling site'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'crud'

# mysql = MySQL(app)

@init.app.route('/')
def Index():
    cur = init.mysql.connection.cursor()
    cur.execute("SELECT * FROM accounts")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', accounts=data)


@init.app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        cur = init.mysql.connection.cursor()
        cur.execute("INSERT INTO accounts (name, password, email, phone) VALUES (%s, %s, %s, %s)", (name, password, email, phone))
        init.mysql.connection.commit()
        return redirect(url_for('Index'))

@init.app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = init.mysql.connection.cursor()
    cur.execute("DELETE FROM accounts WHERE id=%s", (id_data,))
    init.mysql.connection.commit()
    return redirect(url_for('Index'))



@init.app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = init.mysql.connection.cursor()
        cur.execute("""
        UPDATE accounts SET name=%s, email=%s, phone=%s
        WHERE id=%s
        """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        return redirect(url_for('Index'))




if __name__ == "__main__":
    init.app.run(debug=True)
