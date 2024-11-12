from flask import Flask, render_template, request, redirect
import mysql.connector
import os

# Create Flask app instance with the current directory as the template folder
app = Flask(__name__, template_folder=os.getcwd())

# Database connection details
db_config = {
    'host': 'sql12.freesqldatabase.com',
    'user': 'sql12743987',
    'password': 'tkcDiHZp4V',
    'database': 'sql12743987',
    'port': 3306  # default MySQL port
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']

        # Insert into database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "INSERT INTO contacts (name, phone) VALUES (%s, %s)"
        cursor.execute(query, (name, phone))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect('/')

    return render_template('index.html')  # Flask will now look in the current directory

if __name__ == '__main__':
    app.run(debug=True)
