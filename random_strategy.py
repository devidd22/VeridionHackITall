import requests
from time import sleep
import random

host = ""
post_url = f"{host}/submit-word"
get_url = f"{host}/get-word"
status_url = f"{host}/status"

NUM_ROUNDS = 5

#dictionar unde e 

word_costs = {
    1: ["Feather", "Coal", "Pebble"],
    2: ["Leaf", "Paper", "Rock"],
    3: ["Water", "Twig"],
    4: ["Sword", "Shield"],
    5: ["Gun", "Flame", "Rope"],
    6: ["Disease", "Cure", "Bacteria"],
    7: ["Shadow", "Light", "Virus"],
    8: ["Sound", "Time", "Fate"],
    9: ["Earthquake", "Storm", "Vaccine"],
    10: ["Logic", "Gravity", "Robots"],
    11: ["Stone", "Echo"],
    12: ["Thunder", "Karma"],
    13: ["Wind", "Ice", "Sandstorm"],
    14: ["Laser", "Magma", "Peace"],
    15: ["Explosion", "War", "Enlightenment"],
    16: ["Nuclear Bomb", "Volcano"],
    17: ["Whale", "Earth", "Moon"],
    18: ["Star", "Tsunami"],
    19: ["Supernova", "Antimatter"],
    20: ["Plague", "Rebirth"],
    21: ["Tectonic Shift"],
    22: ["Gamma-Ray Burst"],
    23: ["Human Spirit"],
    24: ["Apocalyptic Meteor"],
    25: ["Earth’s Core"],
    26: ["Neutron Star"],
    35: ["Supermassive Black Hole"],
    45: ["Entropy"]
}


def what_beats(word):
    sleep(random.randint(1, 3))
    return random.randint(1, 60)

def play_game(player_id):
    for round_id in range(1, NUM_ROUNDS+1):
        round_num = -1
        while round_num != round_id:
            response = requests.get(get_url)
            print(response.json())
            sys_word = response.json()['word']
            round_num = response.json()['round']

            sleep(1)

        if round_id > 1:
            status = requests.get(status_url)
            print(status.json())

        choosen_word = what_beats(sys_word)
        data = {"player_id": player_id, "word_id": choosen_word, "round_id": round_id}
        response = requests.post(post_url, json=data)
        print(response.json())