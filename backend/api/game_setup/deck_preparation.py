import importlib
import os
import random
from api.cards.base import Card
from typing import List, Optional

# Prepare deck by searching for all non-base card classes
def prepare_deck() -> List[Card]:
    deck: List[Card] = []
    cards_dir = os.path.join(os.path.dirname(__file__), '..', 'cards')
    cards_dir = os.path.abspath(cards_dir)
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

def card_selection(deck: List[Card], evil_quantity: int = 1, good_quantity: int = 2) -> List[Card]:
    """
    Select a specified quantity of EVIL and GOOD cards from the deck.
    """
    evil_cards = [card for card in deck if getattr(card, 'alignment', None) and card.alignment.name == 'EVIL']
    good_cards = [card for card in deck if getattr(card, 'alignment', None) and card.alignment.name == 'GOOD']

    selected_evil: List[Card] = random.sample(evil_cards, evil_quantity) if len(evil_cards) >= evil_quantity else evil_cards
    selected_good: List[Card] = random.sample(good_cards, good_quantity) if len(good_cards) >= good_quantity else good_cards

    game: List[Card] = selected_evil + selected_good
    return game