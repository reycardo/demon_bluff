import random
from api.game_setup.game_disposition import GameDisposition
from .base import Card, Alignment, CardType

class Lover(Card):
    def __init__(self):
        super().__init__(
            image="saint.png",
            name="Saint",
            alignment=Alignment.GOOD,
            type=CardType.VILLAGER,
            template="",
            description="Learn if a card is Good or Evil",
            is_corrupted=False,
            is_lying=False
        )

    def get_template(self, this_card_position: int, game_disposition: GameDisposition, lying: bool = False) -> str:
        # based on the game_disposition, check if a random selected card is EVIL or GOOD
        total_positions = len(game_disposition.positions)
        random.seed()  # Seed with system time or entropy source
        random_position = random.choice([pos for pos in range(total_positions) if pos != this_card_position])
        random_card: Card = game_disposition.get_card_at(random_position)

        if random_card:
            template = f"#{random_position} is {random_card.alignment.name.lower()}."

        if lying:
            # Lie about the alignment of the selected card
            if random_card.alignment == Alignment.GOOD:
                template = f"#{random_position} is evil."
            else:
                template = f"#{random_position} is good."
        
        return template