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

    def set_template(self, this_card_position: int, game_disposition: GameDisposition):
        # based on the game_disposition, check if a random selected card is EVIL or GOOD
        total_positions = len(game_disposition.positions)
        random_position = random.choice([pos for pos in range(total_positions) if pos != this_card_position])
        random_card: Card = game_disposition.get_card_at(random_position)

        if random_card:
            template = f"The card at position {random_position} is {random_card.alignment.name.lower()}."

        if self.is_corrupted or self.is_lying:
            # Lie about the alignment of the selected card
            if random_card.alignment == Alignment.GOOD:
                template = f"The card at position {random_position} is evil."
            else:
                template = f"The card at position {random_position} is good."

        self.template = template
        return self.template