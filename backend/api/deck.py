import importlib
import os
import random
from api.cards.base import Card

# Prepare deck by searching for all non-base card classes

def prepare_deck():
    deck = []
    cards_dir = os.path.dirname(__file__) + '/cards'
    for filename in os.listdir(cards_dir):
        if filename.endswith('.py') and filename != 'base.py':
            module_name = f"api.cards.{filename[:-3]}"
            module = importlib.import_module(module_name)
            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, type) and issubclass(obj, Card) and obj is not Card:
                    card_instance = obj()
                    deck.append(card_instance)
    return deck

# Example usage
if __name__ == "__main__":
    deck = prepare_deck()
    # Select 1 EVIL card and 2 GOOD cards
    evil_cards = [card for card in deck if getattr(card, 'alignment', None) and card.alignment.name == 'EVIL']
    good_cards = [card for card in deck if getattr(card, 'alignment', None) and card.alignment.name == 'GOOD']
    selected_evil = random.choice(evil_cards) if evil_cards else None
    selected_good = random.sample(good_cards, 2) if len(good_cards) >= 2 else good_cards
    game = [selected_evil] + selected_good if selected_evil else selected_good
    # Dump selected game cards to game.json        
    frontend_public_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend/public/game.json'))
    Card.dump_to_json(game, filename=frontend_public_path)
