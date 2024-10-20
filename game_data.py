# Improved dummy data for games
games = [
    # {
    #     'name': 'FarCry 5',
    #     'image': 'FarCry 5.jpg',
    #     'description': 'Adventure through an epic quest in this thrilling game.',
    #     'page_url': 'FarCry 5',
    #     'genre': 'Action-Adventure',
    #     'release_year': 2018,
    #     'rating': 8.5  # Out of 10
    # },
    # {
    #     'name': 'Sniper Elite 3',
    #     'image': 'Sniper Elite 3.jpg',
    #     'description': 'Tactical stealth and sniper skills in World War II.',
    #     'page_url': 'Sniper Elite 3',
    #     'genre': 'Shooter',
    #     'release_year': 2014,
    #     'rating': 8.0
    # },
    # {
    #     'name': 'Sniper Elite 4',
    #     'image': 'Sniper Elite 4.jpg',
    #     'description': 'Tactical stealth and sniper skills in World War II.',
    #     'page_url': 'Sniper Elite 4',
    #     'genre': 'Shooter',
    #     'release_year': 2017,
    #     'rating': 8.2
    # },
    # {
    #     'name': 'Assassin\'s Creed Odyssey',
    #     'image': 'Assassins_Creed_Odyssey.jpg',
    #     'description': 'Embark on an epic journey in ancient Greece.',
    #     'page_url': 'Assassins_Creed_Odyssey',
    #     'genre': 'Action RPG',
    #     'release_year': 2018,
    #     'rating': 9.0
    # },
    # {
    #     'name': 'The Witcher 3: Wild Hunt',
    #     'image': 'Witcher_3.jpg',
    #     'description': 'A vast open-world RPG filled with adventures and choices.',
    #     'page_url': 'Witcher_3',
    #     'genre': 'RPG',
    #     'release_year': 2015,
    #     'rating': 9.7
    # },
    # # Add more games here...
]
#####################################################################################

# game_data.py
game_data = {
    1: {
        'name': 'FarCry 5',
        'image': 'FarCry 5.jpg',
        'description': 'Far Cry 5 is an open-world first-person shooter set in rural Montana, where players must combat a doomsday cult known as Eden\'s Gate, liberating the region and its inhabitants.',
        'min_requirements': ['OS: Windows 7', 'Processor: Intel Core i5', 'Memory: 8 GB RAM','Graphics: NVIDIA GeForce GTX 460 or AMD Radeon R7 260 (768 MB VRAM)','DirectX: DirectX 11','Storage: 30 GB free disk space'],
        'rec_requirements': ['OS: Windows 10', 'Processor: Intel Core i7', 'Memory: 16 GB RAM','Graphics: NVIDIA GeForce GTX 970 or AMD Radeon R9 290 (4 GB VRAM)','DirectX: DirectX 11','Storage: 30 GB free disk space'],
        'screenshots': ['FarCry 5 sh 1.jpg', 'FarCry 5 sh 2.jpg'],
        'download_link': 'https://uploadscloud.com/nnkbfyft73ex/ThePcGames.net_Far_Cry_5.zip.html'
    },

    2: {
        'name': 'Assassin Creed Syndicate',
        'image': 'Assassin Creed Syndicate.jpg',
        'description': 'Assassin\'s Creed Syndicate is an action-adventure game set in Victorian-era London, following the story of twins Jacob and Evie Frye as they fight against the Templar Order and liberate the city from oppression.',
        'min_requirements': ['OS: Windows 8', 'Processor: Intel Core i3', 'Memory: 4 GB RAM','Graphics: NVIDIA GeForce GTX 660 or AMD Radeon HD 7870 (2 GB VRAM)','DirectX: DirectX 10','Storage: 40 GB free disk space'],
        'rec_requirements': ['OS: Windows 10', 'Processor: Intel Core i5', 'Memory: 8 GB RAM','Graphics: NVIDIA GeForce GTX 970 or AMD Radeon R9 290 (4 GB VRAM)','DirectX: DirectX 11','Storage: 40 GB free disk space'],
        'screenshots': ['Assassin Creed Syndicate sh 1.jpg', 'Assassin Creed Syndicate sh 3.png'],
        'download_link': "https://uploadscloud.com/wu5efsr37fza/ThePcGames.net_Assassins_Creed_Syndicate.zip.html"
    },

        3: {
        'name': 'Assassin Creed 2',
        'image': 'Assassin Creed 2.jpg',
        'description': 'Assassin\'s Creed II is an action-adventure game set in Renaissance Italy, following the story of Ezio Auditore da Firenze as he seeks vengeance and uncovers the secrets of the Assassins.',
        'min_requirements': ['OS: Windows XP SP2 or Windows Vista', 'Processor: Intel Core 2 Duo 1.8 GHz or AMD Athlon 64 X2 4000+', 'Memory: 2 GB RAM','Graphics: NVIDIA GeForce 8600 series or ATI Radeon HD 2600 with 256 MB video memory','DirectX: DirectX 9.0c','Storage: 17.6 GB free disk space'],
        'rec_requirements': ['OS: Windows Vista or Windows ', 'Processor: Dual-core CPU 2.5 GHz', 'Memory: 4 GB RAM','Graphics: NVIDIA GeForce GTX 460 or ATI Radeon HD 6850 with 768 MB video memory','DirectX: DirectX 9.0c','Storage: 17.6 GB free disk space'],
        'screenshots': ['Assassin Creed 2 sh 1.jpg', 'Assassin Creed 2 sh 2.jpg'],
        'download_link': "https://uploadscloud.com/3a4jijreh11h/ThePcGames.net_Assassins_Creed_2_v1.01_Repack.zip.html"
    }
}


# Sample data for games
# game_data.py

# featured_games = [
#     {
#         'id': 1,
#         'name': 'Forza Horizon 5',
#         'image': 'Forza_Horizon_5.jpg',
#         'description': 'A thrilling racing game set in an open world.'
#     },
#     {
#         'id': 2,
#         'name': 'Mount And Blade 2 Bannerlord',
#         'image': 'Mount_And_Blade_2_Bannerlord.jpg',
#         'description': 'A medieval action-RPG and strategy game.'
#     },
#     # Add more games as needed
# ]



all_games = [
    {'id': 1, 'name': 'FarCry 5', 'image': 'FarCry 5.jpg', 'description': 'This is FarCry 5 Full Game.'},
    {'id': 2, 'name': 'Assassin Creed Syndicate', 'image': 'Assassin Creed Syndicate.jpg', 'description': 'This is Assassin\'s Creed Syndicate Full Game.'},
    {'id': 3, 'name': 'Assassin 2', 'image': 'Assassin Creed 2.jpg', 'description': 'This is Assassin\'s Creed 2 Full Game.'}
     
]
