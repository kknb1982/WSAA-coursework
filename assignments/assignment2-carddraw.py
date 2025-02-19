# This is designed to use the decks of cards API to draw a hand of cards and display them. Five cards will be drawn and displayed.

# Author: Kirstin Barnett
import requests
import json

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

# Create an empty dictionary to store the value counts
value_counts = {} 

# Shuffle the deck
url = "https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
data = response.json()

# Get the deck id
deck_id = data["deck_id"]

# Use the deck id to draw 5 cards
url2 = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5" 
response2 = requests.get(url2)
cards = response2.json()

# Print the value, suit and code of each card drawn
print("\nYou have drawn the following cards:")
for card in cards["cards"]:
    print(f"{card['value']} of {card['suit']}")

# Get the value of the cards
values = [card["value"] for card in cards["cards"]]

# Count the number of cards with the same value
for value in values:
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

# Print the number of cards with the same value
for value, count in value_counts.items():
    if count > 1:
        print(f"\nCongratulations, {count} cards have the value {value}")
        
# Sorts the values according to the value mapping
sorted_values = sorted(values, key=lambda x: value_mapping[x]) 

# Check for a straight
is_straight = True

for i in range(len(sorted_values) - 1):
    if value_mapping[sorted_values[i]] + 1 != value_mapping[sorted_values[i + 1]]: 
        is_straight = False
        break

if is_straight:
    print("\nCongratulations! The hand is a straight.")

# Check all of the same suit
suits = [card["suit"] for card in cards["cards"]]
if all(suit == suits[0] for suit in suits):
    print("\n Congratulations! All cards are of the same suit.")



