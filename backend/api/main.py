from api.game_setup.deck_preparation import card_selection, prepare_deck
from api.game_setup.dump_to_frontend import dump_to_frontend


if __name__ == "__main__":
    deck = prepare_deck()
    game = card_selection(deck=deck, evil_quantity=1, good_quantity=2)
    dump_to_frontend(game_cards=game)
