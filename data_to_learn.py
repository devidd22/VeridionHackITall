import json

w = "word"
cw = "counter-word"

words = [{w : "Feather", cw : "Rock"},
         {w : "Coal", cw : "Peddle"},
         {w : "Pebble", cw : "Leaf"},
         {w : "Leaf", cw : "Rock"},
         {w : "Paper", cw : "Sword"},
         {w : "Rock", cw : "Paper"},
         {w : "Water", cw : "Paper"},
         {w : "Twig", cw : "Rock"},
         {w : "Sword", cw : "Shield"},
         {w : "Shield", cw : "Gun"},
         {w : "Gun", cw : "Laser"},
         {w : "Flame", cw : "Water"},
         {w : "Rope", cw : "Sword"},
         {w : "Disease", cw : "Cure"},
         {w : "Cure", cw : "Bacteria"},
         {w : "Bacteria", cw : "Flame"},
         {w : "Shadow", cw : "Light"},
         {w : "Light", cw : "Shield"},
         {w : "Virus", cw : "Cure"},
         {w : "Sound", cw : "Shield"},
         {w : "Time", cw : "Coal"},
         {w : "Fate", cw : "Logic"},
         {w : "Earthquake", cw : "Time"},
         {w : "Storm", cw : "Time"},
         {w : "Vaccine", cw : "Logic"},
         {w : "Logic", cw : "Karma"},
         {w : "Gravity", cw : "Light"},
         {w : "Robots", cw : "Time"},
         {w : "Stone", cw : "Earthquaks"},
         {w : "Echo", cw : "Shield"},
         {w : "Thunder", cw : "Time"},
         {w : "Karma", cw : "Fate"},
         {w : "Wind", cw : "Shield"},
         {w : "Ice", cw : "Flame"},
         {w : "Sandstorm", cw : "Time"},
         {w : "Laser", cw : "Star"},
         {w : "Magma", cw : "Time"},
         {w : "Peace", cw : "Flame"},
         {w : "Explosion", cw : "Shield"},
         {w : "War", cw : "Time"},
         {w : "Enlightenment", cw : "Karma"},
         {w : "Nuclear Bomb", cw : "Time"},
         {w : "Volcano", cw : "Nuclear Bomb"},
         {w : "Whale", cw : "Disease"},
         {w : "Earth", cw : "Time"},
         {w : "Moon", cw : "Time"},
         {w : "Star", cw : "Gravity"},
         {w : "Tsunami", cw : "Nuclear bomb"},
         {w : "Supernova", cw : "Gravity"},
         {w : "Antimatter", cw : "Supernova"},
         {w : "Plague", cw : "Cure"},
         {w : "Rebirth", cw : "Gun"},
         {w : "Tectonic Shift", cw : "Time"},
         {w : "Gamma-Ray Burst", cw : "Water"},
         {w : "Human Spirit", cw : "Fate"},
         {w : "Apocalyptic Meteor", cw : "Human Spirit"},
         {w : "Earth's Core", cw : "Nuclear Bomb"},
         {w : "Neutron Star", cw : "Neutron Star"},
         {w : "Supermassive Black Hole", cw : "Supermassive Black Hole"},
         {w : "Entropy", cw : "Logic"}, # set de date de la ADȘ
         {w : "Bottle", cw : "Sword"},
         {w : "Laptop", cw : "Sword"},
         {w : "Book", cw : "Sword"},
         {w : "Sand", cw : "Flame"},
         {w : "Purse", cw : "Sword"},
         {w : "Beens", cw : "Rock"},
         {w : "Clothes", cw : "Sword"},
         {w : "Car", cw : "Flame"},
         {w : "Human", cw : "Gun"},
         {w : "God", cw : "Fate"},
         {w : "Building", cw : " Earthquake"},
         {w : "Juice", cw : "Rock"},
         {w : "Brick" , cw : "Earthquake"},
         {w : "Cloud", cw : "Storm"},
         {w : "River", cw : "Pebble"},
         {w : "Antibiotic", cw : "Bacteria"},
         {w : "Silence", cw : "Sound"},
         {w : "Eternity", cw : "Time"},
         {w : "Free Will", cw : "Fate"},
         {w : "Calm", cw : "Storm"},
         {w : "Anti-gravity", cw : "Gravity"},
         {w : "Flood", cw : "Sandstorm"},
         {w : "Fire", cw : "Ice"},
         {w : "Ignorance", cw : "Enlightenment"},
         {w : "Matter", cw : "Antimatter"},
         {w : "Destruction", cw : "Rebirth"},
         {w : "Stability", cw : "Tectonic Shift"},
         {w : "Order", cw : "Entropy"},
         {w : "Outer Space", cw : "Earth's Core"}]