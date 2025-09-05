import os
from api.cards.base import Card

def dump_to_frontend(game_cards):
    """
    Dump the selected game cards to a JSON file for the frontend.
    """

    from pathlib import Path
    # Get the backend/api/game_setup directory
    current_dir = Path(__file__).parent
    # Go up three levels to the workspace root, then into frontend/public/game.json
    frontend_public_path = (current_dir.parent.parent.parent / 'frontend' / 'public' / 'game.json').resolve()

    Card.dump_to_json(game_cards, filename=str(frontend_public_path))
    print(f"Game cards dumped to {frontend_public_path}")