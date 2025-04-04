import requests
from time import sleep
import random
# import tensorflow as tf
import json
from word_choice import *
from kmeans import *
#from lista_cuvinte import *
# Assuming you have the trained model and JSON data
#model = tf.keras.models.load_model('lista_cuvinte.py')  # Load the pre-trained model


# Define URLs
host = "http://172.18.4.158:8000"
post_url = "http://172.18.4.158:8000/submit-word"
get_url = "http://172.18.4.158:8000/get-word"
status_url = "http://172.18.4.158:8000/status"

NUM_ROUNDS = 5
NUMAR = 0
def what_beats(sys_word):    
    return predict_counter_word_most_frequent(sys_word)

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
            print(f"Status after round {round_id}: {status.json()}")
        choosen_word = what_beats(sys_word)
        print(f"Player: {player_id}, Runda: {round_id}, Sys_word: {choosen_word}")
        data = {"player_id": player_id, "word_id": choosen_word, "round_id": round_id}
        response = requests.post(post_url, json = data)
        print(response.json())        
        
if __name__=="__main__":
    play_game("JEZRVRmDMj")