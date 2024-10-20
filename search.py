def search_games(query):
    # Assuming you have a list of games
    games = ['Game1', 'Game2', 'Game3']  # Replace with your actual game data
    results = [game for game in games if query.lower() in game.lower()]
    return results
