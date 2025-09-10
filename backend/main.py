from api.game_setup.deck_preparation import card_selection, prepare_deck, shuffle_deck
from api.game_setup.game_disposition import GameDisposition
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from any origin (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get the backend directory
current_dir = Path(__file__).parent
# Go up one level to workspace root, then into frontend/public/game.json
frontend_public_path = (current_dir.parent / 'frontend' / 'public' / 'game.json').resolve()

@app.post("/api/game_disposition")
def generate_game_disposition():
    deck = prepare_deck()
    game = card_selection(deck=deck, evil_quantity=1, good_quantity=4)
    game = shuffle_deck(game)
    game_disposition = GameDisposition(positions={i: card for i, card in enumerate(game)})
    # Set templates for each card based on their position and the overall game disposition
    for position, card in game_disposition.positions.items():
        # mask if the card is a Minion
        if hasattr(card, 'mask') and callable(getattr(card, 'mask')):
            card.mask(this_card_position=position, game_disposition=game_disposition)
        template = card.get_template(this_card_position=position, game_disposition=game_disposition, lying=card.is_lying)
        card.template = template
    return game_disposition.dump_to_dict()
