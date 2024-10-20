from flask import Flask, render_template, url_for, flash, redirect, request, session
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf import FlaskForm
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm
from game_data import games
from flask_sqlalchemy import SQLAlchemy
from extensions import db  # Make sure this is imported at the top
from mysql.connector import Error
from game_data import game_data, all_games  # Import game data
from search import search_games
from flask_mail import Mail,Message
import os


# Database configuration
db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'Allied,1978',  # Your MySQL password here
    'database': 'pirate'
}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_random_secret_key'  # Set your secret key here
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"


# Initialize the database
db.init_app(app)  # Initialize SQLAlchemy with the app

# Initialize database and create contacts table if it does not exist
def init_contact_db():
    connection = mysql.connector.connect(**db_config)
    try:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            message TEXT NOT NULL
        )''')
        connection.commit()
    finally:
        cursor.close()
        connection.close()

init_contact_db()

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save to database
        connection = mysql.connector.connect(**db_config)
        try:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)', (name, email, message))
            connection.commit()
            flash('Message sent successfully!', 'success')
            return redirect(url_for('contact'))

        except Exception as e:

            flash(f'Error: {str(e)}', 'error')
        finally:
            cursor.close()
            connection.close()

    return render_template('contact.html')


# Database setup for user registration
def init_db():
    with app.app_context():  # Make sure to use app context
        db.create_all()  # Create database tables if they don't exist

init_db()

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  # Create an instance of the RegistrationForm
    if form.validate_on_submit():  # Use form's validation method
        username = form.username.data
        email = form.email.data
        password = form.password.data
        hashed_password = generate_password_hash(password)

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Check if the email is already registered
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
            user = cursor.fetchone()

            if user:
                flash('Email already registered!')
                return redirect(url_for('register'))

            # Insert new user into the database
            cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                           (username, email, hashed_password))
            connection.commit()

            flash('Registration successful! You can now log in.')
            return redirect(url_for('login'))

        except Error as e:
            flash(f'An error occurred: {e}')
            return redirect(url_for('register'))

        finally:
            # Ensure that the cursor and connection are closed
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    return render_template('register.html', form=form)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash('Please fill out both fields.')
            return redirect(url_for('login'))

        try:
            # Database connection
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Checking if user exists
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
            user = cursor.fetchone()

            if user and check_password_hash(user[3], password):  # Assuming the password is in the 4th column
                session['user_id'] = user[0]  # User ID
                session['username'] = user[1]  # Username
                flash('Login successful!')
                return redirect(url_for('home'))
            else:
                flash('Invalid email or password. Please try again.')

        except Error as e:
            flash(f'Error: {str(e)}')

        finally:
            # Ensure the cursor and connection are closed
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    return render_template('login.html')



# About page route
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about2')
def about2():
    return render_template('aboutt.html')

# Home route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/game/<int:game_id>')
def game_page(game_id):
    game = game_data.get(game_id)  # Get game details by ID
    if game:
        return render_template('game_page.html', game=game)
    else:
        return "Game not found", 404

# Route for the games list page
@app.route('/Games')
def games_list():
    # Example data for pagination (replace with actual pagination logic)
    current_page = request.args.get('page', 1, type=int)
    games_per_page = 10
    total_games = len(all_games)  # Assuming `all_games` contains all game data
    total_pages = (total_games + games_per_page - 1) // games_per_page
    
    # Slice games for the current page
    start = (current_page - 1) * games_per_page
    end = start + games_per_page
    paginated_games = all_games[start:end]

    # Pass `current_page`, `total_pages`, and `games_per_page` to the template
    return render_template('games.html', 
                           games=paginated_games,
                           current_page=current_page, 
                           total_pages=total_pages,
                           games_per_page=games_per_page)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure the tables are created before starting the app
    app.run(debug=True)
