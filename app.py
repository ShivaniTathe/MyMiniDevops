from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Sample Tarot cards data
tarot_cards = [
    {"name": "The Fool", "meaning": "New beginnings, adventure, spontaneity.", "image": "static/images/the_fool.jpg"},
     {"name": "The Magician", "meaning": "Skill, confidence, action, concentration.", "image": "static/images/the_magician.jpg"},
     {"name": "The High Priestess", "meaning": "Intuition, mystery, spirituality.", "image": "static/images/the_high_priestess.jpg"},
     {"name": "The Empress", "meaning": "Fertility, abundance, nurturing.", "image": "static/images/the_empress.jpg"},
     {"name": "The Emperor", "meaning": "Authority, structure, control.", "image": "static/images/the_emperor.jpg"},
    {"name": "The Hierophant", "meaning": "Tradition, conformity, morality.", "image": "static/images/the_hierophant.jpg"},
    {"name": "The Lovers", "meaning": "Love, harmony, relationships.", "image": "static/images/the_lovers.jpg"},
    {"name": "The Chariot", "meaning": "Determination, willpower, victory.", "image": "static/images/the_chariot.jpg"},
    {"name": "Strength", "meaning": "Courage, patience, inner strength.", "image": "static/images/strength.jpg"},
    {"name": "The Hermit", "meaning": "Introspection, solitude, guidance.", "image": "static/images/the_hermit.jpg"},
    {"name": "Wheel of Fortune", "meaning": "Change, cycles, fate.", "image": "static/images/wheel_of_fortune.jpg"},
    {"name": "Justice", "meaning": "Fairness, truth, law.", "image": "static/images/justice.jpg"},
    {"name": "The Hanged Man", "meaning": "Suspension, letting go, new perspectives.", "image": "static/images/the_hanged_man.jpg"},
    {"name": "Death", "meaning": "Endings, transformation, transition.", "image": "static/images/death.jpg"},
    {"name": "Temperance", "meaning": "Balance, moderation, purpose.", "image": "static/images/temperance.jpg"},
    {"name": "The Devil", "meaning": "Bondage, addiction, materialism.", "image": "static/images/the_devil.jpg"},
    {"name": "The Tower", "meaning": "Upheaval, sudden change, revelation.", "image": "static/images/the_tower.jpg"},
    {"name": "The Star", "meaning": "Hope, inspiration, serenity.", "image": "static/images/the_star.jpg"},
    {"name": "The Moon", "meaning": "Illusion, fear, anxiety.", "image": "static/images/the_moon.jpg"},
    {"name": "The Sun", "meaning": "Joy, success, positivity.", "image": "static/images/the_sun.jpg"},
    # {"name": "Judgement", "meaning": "Reflection, reckoning, awakening.", "image": "static/images/judgement.jpg"},
    # {"name": "The World", "meaning": "Completion, accomplishment, travel.", "image": "static/images/the_world.jpg"},
    # {"name": "Ace of Wands", "meaning": "Inspiration, new opportunities, growth.", "image": "static/images/ace_of_wands.jpg"},
    # {"name": "Two of Wands", "meaning": "Planning, making decisions, progress.", "image": "static/images/two_of_wands.jpg"},
    # {"name": "Three of Wands", "meaning": "Expansion, foresight, overseas opportunities.", "image": "static/images/three_of_wands.jpg"},
    # {"name": "Four of Wands", "meaning": "Celebration, harmony, home.", "image": "static/images/four_of_wands.jpg"},
    # {"name": "Five of Wands", "meaning": "Conflict, competition, tension.", "image": "static/images/five_of_wands.jpg"},
    # {"name": "Six of Wands", "meaning": "Victory, success, public recognition.", "image": "static/images/six_of_wands.jpg"},
    # {"name": "Seven of Wands", "meaning": "Challenge, competition, perseverance.", "image": "static/images/seven_of_wands.jpg"},
    # {"name": "Eight of Wands", "meaning": "Speed, action, swift change.", "image": "static/images/eight_of_wands.jpg"},
    # {"name": "Nine of Wands", "meaning": "Resilience, persistence, test of faith.", "image": "static/images/nine_of_wands.jpg"},
    # {"name": "Ten of Wands", "meaning": "Burden, responsibility, hard work.", "image": "static/images/ten_of_wands.jpg"},
    # {"name": "Page of Wands", "meaning": "Exploration, excitement, freedom.", "image": "static/images/page_of_wands.jpg"},
    # {"name": "Knight of Wands", "meaning": "Energy, passion, inspired action.", "image": "static/images/knight_of_wands.jpg"},
    # {"name": "Queen of Wands", "meaning": "Courage, determination, joy.", "image": "static/images/queen_of_wands.jpg"},
    # {"name": "King of Wands", "meaning": "Natural leader, vision, entrepreneur.", "image": "static/images/king_of_wands.jpg"},
    # {"name": "Ace of Cups", "meaning": "Love, new relationships, compassion.", "image": "static/images/ace_of_cups.jpg"},
    # {"name": "Two of Cups", "meaning": "Partnership, unity, love.", "image": "static/images/two_of_cups.jpg"},
    # {"name": "Three of Cups", "meaning": "Celebration, friendship, creativity.", "image": "static/images/three_of_cups.jpg"},
    # {"name": "Four of Cups", "meaning": "Meditation, contemplation, apathy.", "image": "static/images/four_of_cups.jpg"},
    # {"name": "Five of Cups", "meaning": "Regret, failure, disappointment.", "image": "static/images/five_of_cups.jpg"},
    # {"name": "Six of Cups", "meaning": "Revisiting the past, childhood memories.", "image": "static/images/six_of_cups.jpg"},
    # {"name": "Seven of Cups", "meaning": "Opportunities, choices, illusion.", "image": "static/images/seven_of_cups.jpg"},
    # {"name": "Eight of Cups", "meaning": "Disappointment, abandonment, withdrawal.", "image": "static/images/eight_of_cups.jpg"},
    # {"name": "Nine of Cups", "meaning": "Contentment, satisfaction, gratitude.", "image": "static/images/nine_of_cups.jpg"},
    # {"name": "Ten of Cups", "meaning": "Happiness, fulfillment, emotional stability.", "image": "static/images/ten_of_cups.jpg"},
    # {"name": "Page of Cups", "meaning": "Creative opportunities, intuitive messages.", "image": "static/images/page_of_cups.jpg"},
    # {"name": "Knight of Cups", "meaning": "Romance, charm, imagination.", "image": "static/images/knight_of_cups.jpg"},
    # {"name": "Queen of Cups", "meaning": "Compassion, calm, comfort.", "image": "static/images/queen_of_cups.jpg"},
    # {"name": "King of Cups", "meaning": "Emotional balance, control, generosity.", "image": "static/images/king_of_cups.jpg"},
    # {"name": "Ace of Swords", "meaning": "Breakthrough, clarity, sharp mind.", "image": "static/images/ace_of_swords.jpg"},
    # {"name": "Two of Swords", "meaning": "Indecision, choices, stalemate.", "image": "static/images/two_of_swords.jpg"},
    # {"name": "Three of Swords", "meaning": "Heartbreak, sorrow, grief.", "image": "static/images/three_of_swords.jpg"},
    # {"name": "Four of Swords", "meaning": "Rest, relaxation, recovery.", "image": "static/images/four_of_swords.jpg"},
    # {"name": "Five of Swords", "meaning": "Conflict, disagreement, defeat.", "image": "static/images/five_of_swords.jpg"},
    # {"name": "Six of Swords", "meaning": "Transition, change, rite of passage.", "image": "static/images/six_of_swords.jpg"},
    # {"name": "Seven of Swords", "meaning": "Betrayal, deception, getting away with something.", "image": "static/images/seven_of_swords.jpg"},
    # {"name": "Eight of Swords", "meaning": "Isolation, self-imposed restriction, imprisonment.", "image": "static/images/eight_of_swords.jpg"},
    # {"name": "Nine of Swords", "meaning": "Anxiety, worry, fear.", "image": "static/images/nine_of_swords.jpg"},
    # {"name": "Ten of Swords", "meaning": "Painful endings, deep wounds, betrayal.", "image": "static/images/ten_of_swords.jpg"},
    # {"name": "Page of Swords", "meaning": "New ideas, curiosity, thirst for knowledge.", "image": "static/images/page_of_swords.jpg"}
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
