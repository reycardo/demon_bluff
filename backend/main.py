from api.game_setup.deck_preparation import card_selection, prepare_deck
from api.game_setup.game_disposition import GameDisposition

from pathlib import Path
# Get the backend directory
current_dir = Path(__file__).parent
# Go up one level to workspace root, then into frontend/public/game.json
frontend_public_path = (current_dir.parent / 'frontend' / 'public' / 'game.json').resolve()


if __name__ == "__main__":
    deck = prepare_deck()
    game = card_selection(deck=deck, evil_quantity=1, good_quantity=2)
    game_disposition = GameDisposition(positions={i: card for i, card in enumerate(game)})
    game_disposition.dump_to_frontend(filename=str(frontend_public_path))
