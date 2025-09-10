import random
from api.game_setup.game_disposition import GameDisposition
from .base import Card, Alignment, CardType

class Lover(Card):
    def __init__(self):
        super().__init__(
            image="lover.png",
            name="Lover",
            alignment=Alignment.GOOD,
            type=CardType.VILLAGER,
            template="",
            description="Learn how many Evil characters I am adjacent to",
            is_corrupted=False,
            is_lying=False
        )

    def get_template(self, this_card_position: int, game_disposition: GameDisposition, lying: bool = False) -> str:
        # Count adjacent evils (0, 1, or 2)
        adjacent_positions = game_disposition.get_adjacent_positions(this_card_position)
        evil_count = sum(
            1 for pos in adjacent_positions
            if game_disposition.get_card_at(pos) and game_disposition.get_card_at(pos).alignment == Alignment.EVIL
        )

        def neighbor_text(n):
            return f"Evil{'s' if n != 1 else ''} adjacent to me"

        if lying:
            # Lie: pick from 0, 1, 2 but never the actual evil_count
            # Ensure max range takes maximum evil in game_disposition
            possible_lies = [i for i in range(0, 3) if i != evil_count]
            random.seed()
            lie = random.choice(possible_lies)
            template = f"I have {lie} {neighbor_text(lie)}"
        else:
            template = f"I have {evil_count} {neighbor_text(evil_count)}"
        
        return template