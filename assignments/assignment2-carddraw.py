# This is designed to use the decks of cards API to draw a hand of cards and display them. Five cards will be drawn and displayed.

# Author: Kirstin Barnett
import requests
import json

url = "https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

response = requests.get(url)
data = response.json()

deck_id = data["deck_id"] # This will get the deck id from the json response
print(deck_id)

url2 = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5" # This will draw 5 cards from the deck
print (url2)
response2 = requests.get(url2)
cards = response2.json()


for card in cards["cards"]:
    print(card["value"], card["suit"], card["code"]) # This will print the value, suit and code of each card drawn

# Get the value of the cards
values = [card["value"] for card in cards["cards"]]

value_counts = {} # Create an empty dictionary to store the value counts

# Count the number of cards with the same value
for value in values:
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

# Print the number of cards with the same value
for value, count in value_counts.items():
    if count > 1:
        print(f"{count} cards have the value {value}")
        
# Check for a straight

## Set a mapping for the values
value_mapping = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "JACK": 11,
    "QUEEN": 12,
    "KING": 13,
    "ACE": 14
}

sorted_values = sorted(values, key=lambda x: value_mapping[x]) # sorts the values according to the value mapping
print(f"The sorted values are: {sorted_values}")

for i in range(len(sorted_values) - 1):
    if value_mapping[sorted_values[i]] + 1 != value_mapping[sorted_values[i + 1]]: # checks if the next value is one more than the current value
        print("The hand is not a straight.")    
        break
else:
    print("The hand is not a straight.")

# Check all of the same suit
suits = [card["suit"] for card in cards["cards"]]
if all(suit == suits[0] for suit in suits):
    print("All cards are of the same suit.")
else:
    print("Not all cards are of the same suit.")
    
# Check for pair, triple, straight or all of the same suit