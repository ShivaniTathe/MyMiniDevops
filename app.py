from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Sample Tarot cards data
tarot_cards = [
    {"name": "The Fool", "meaning": "New beginnings, adventure, spontaneity."},
    {"name": "The Magician", "meaning": "Skill, confidence, action, concentration."},
    {"name": "The High Priestess", "meaning": "Intuition, mystery, spirituality."},
    # Add more cards as needed
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/draw')
def draw_card():
    card = random.choice(tarot_cards)
    return render_template('card.html', card=card)

if __name__ == '__main__':
    app.run(debug=True)
