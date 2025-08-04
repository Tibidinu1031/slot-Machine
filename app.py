from flask import Flask, render_template, request, jsonify, session
import random
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Game symbols matching your original code
pacanea = ["7", "🍉", "🍋", "🍇", "🍒", "⭐", "🟣", "🍊"]

# Card game data for double down
cards = {"Rosie": ["♥️", "♦️"], "Neagra": ["♠️", "♣️"]}

class SlotMachine:
    def __init__(self):
        self.hand = []
        self.budget = 0
        self.bet = 0
        self.cards_dealt = []
    
    def generate_hand(self):
        """Generate a new 3x5 slot machine hand"""
        self.hand = []
        for i in range(15):
            symbol = random.choice(pacanea)
            self.hand.append(symbol)
        return self.hand
    
    def check_winnings(self):
        """Check for winning combinations and return multiplier"""
        hand = self.hand
        
        # Check for x10 wins (5 in a row)
        if (hand[0] == hand[1] == hand[2] == hand[3] == hand[4] or 
            hand[5] == hand[6] == hand[7] == hand[8] == hand[9] or 
            hand[10] == hand[11] == hand[12] == hand[13] == hand[14] or 
            hand[0] == hand[6] == hand[12] == hand[8] == hand[4] or 
            hand[10] == hand[6] == hand[2] == hand[8] == hand[14]):
            return 10
        
        # Check for x5 wins (4 in a row)
        elif (hand[0] == hand[1] == hand[2] == hand[3] or 
              hand[5] == hand[6] == hand[7] == hand[8] or 
              hand[10] == hand[11] == hand[12] == hand[13] or 
              hand[0] == hand[6] == hand[12] == hand[8] or 
              hand[10] == hand[6] == hand[2] == hand[8]):
            return 5
        
        # Check for x3 wins (3 in a row)
        elif (hand[0] == hand[1] == hand[2] or 
              hand[5] == hand[6] == hand[7] or 
              hand[10] == hand[11] == hand[12] or 
              hand[0] == hand[6] == hand[12] or 
              hand[10] == hand[6] == hand[2]):
            return 3
        
        # Check for cherry pairs (x2)
        elif ((hand[0] == hand[1] and hand[0] == "🍒") or 
              (hand[5] == hand[6] and hand[5] == "🍒") or 
              (hand[10] == hand[11] and hand[10] == "🍒") or 
              (hand[0] == hand[6] and hand[0] == "🍒") or 
              (hand[10] == hand[6] and hand[10] == "🍒")):
            return 2
        
        # Check for star combinations
        elif hand.count("⭐") == 3:
            return 3
        elif hand.count("⭐") == 4:
            return 4
        elif hand.count("⭐") == 5:
            return 5
        
        return 0
    
    def play_double_down(self, choice):
        """Play the double down card game"""
        # Generate random card
        all_suits = ["♥️", "♦️", "♠️", "♣️"]
        card = random.choice(all_suits)
        self.cards_dealt.append(card)
        
        # Check if guess was correct
        if choice.lower() == 'rosie' and card in cards["Rosie"]:
            return True, card
        elif choice.lower() == 'neagra' and card in cards["Neagra"]:
            return True, card
        else:
            return False, card

@app.route('/')
def index():
    if 'budget' not in session:
        session['budget'] = 0
        session['bet'] = 10
        session['cards_dealt'] = []
    return render_template('index.html')

@app.route('/set_budget', methods=['POST'])
def set_budget():
    data = request.get_json()
    session['budget'] = int(data['budget'])
    session['bet'] = int(data['bet'])
    session['cards_dealt'] = []
    return jsonify({'success': True})

@app.route('/spin', methods=['POST'])
def spin():
    if session['budget'] < session['bet']:
        return jsonify({'error': 'Insufficient budget'})
    
    slot_machine = SlotMachine()
    slot_machine.budget = session['budget']
    slot_machine.bet = session['bet']
    slot_machine.cards_dealt = session.get('cards_dealt', [])
    
    # Generate new hand and check for wins
    hand = slot_machine.generate_hand()
    multiplier = slot_machine.check_winnings()
    
    # Deduct bet from budget
    session['budget'] -= session['bet']
    
    result = {
        'hand': hand,
        'multiplier': multiplier,
        'budget': session['budget'],
        'bet': session['bet'],
        'prize': session['bet'] * multiplier if multiplier > 0 else 0
    }
    
    return jsonify(result)

@app.route('/collect_prize', methods=['POST'])
def collect_prize():
    data = request.get_json()
    prize = data.get('prize', 0)
    session['budget'] += prize
    return jsonify({'budget': session['budget']})

@app.route('/double_down', methods=['POST'])
def double_down():
    data = request.get_json()
    choice = data.get('choice')
    current_prize = data.get('prize', 0)
    
    slot_machine = SlotMachine()
    slot_machine.cards_dealt = session.get('cards_dealt', [])
    
    won, card = slot_machine.play_double_down(choice)
    session['cards_dealt'] = slot_machine.cards_dealt
    
    if won:
        new_prize = current_prize * 2
        result = {
            'won': True,
            'card': card,
            'new_prize': new_prize,
            'cards_dealt': session['cards_dealt'][-5:]  # Show last 5 cards
        }
    else:
        result = {
            'won': False,
            'card': card,
            'new_prize': 0,
            'cards_dealt': session['cards_dealt'][-5:]  # Show last 5 cards
        }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
