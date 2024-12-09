from flask import Flask, render_template, url_for, flash, redirect, request, session
from game_data import games
from game_data import game_data, all_games  # Import game data
from search import search_games
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_random_secret_key'  # Set your secret key here

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
