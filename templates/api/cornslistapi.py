from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

info = []
info_list = [
    ["Minecraft", ["PC", "Playstation", "XBox", "Nintendo Switch", "Mobile"], "Mojang", "2011"],
    ["Fortnite", ["PC", "Playstation", "XBox", "Nintendo Switch", "Mobile"], "Epic games", "2017"],
    ["Valorant", ["PC"], "Riot Games", "2020"],
    ["Dead By Daylight", ["PC", "Playstation", "XBox", "Nintendo Switch", "Mobile"], "Behaviour Interactive", "2016"],
    ["Overwatch", ["PC", "Playstation", "XBox", "Nintendo Switch"], "Blizzard Entertainment", "2016"],
    ["Grand Theft Auto V", ["PC", "Playstation", "XBox"], "Rockstar Games", "2013"]
]



def _find_next_id():
    return max(info["id"] for inf in info_list) + 1


def _init_info():
    id = 1
    # Creating the questions list which will store all the data to be converted to json
    for inf in info_list:
        info.append({"id": id, })
        id += 1


# Converts questions to json
@api_bp.route('/games/')
def get_games():
    if len(games) == 0:
        _init_games()
    return jsonify(games)


if __name__ == "__main__":
    for item in info_list:
        print(item[0], print(item[1]))