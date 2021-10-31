from flask import Blueprint, jsonify

cornList = [
    ["Minecraft", ["PC", "Playstation", "XBox", "Nintendo Switch", "Mobile"], ["Mojang"], ["2011"]],
    ["Fortnite", ["PC", "Playstation", "XBox", "Nintendo Switch", "Mobile"], ["Epic games"], ["2017"]],
    ["Valorant", ["PC"], ["Riot Games"], ["2020"]],
    ["Dead By Daylight", ["PC", "Playstation", "XBox", "Nintendo Switch", "Mobile"], ["Behaviour Interactive"], ["2016"]],
    ["Overwatch", ["PC", "Playstation", "XBox", "Nintendo Switch"], ["Blizzard Entertainment"], ["2016"]],
    ["Grand Theft Auto V", ["PC", "Playstation", "XBox"], ["Rockstar Games"], ["2013"]]
]
print(cornList[2][2])