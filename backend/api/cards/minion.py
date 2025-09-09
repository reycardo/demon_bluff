import random
from api.game_setup.game_disposition import GameDisposition
from .base import Card, Alignment, CardType

class Minion(Card):
    def __init__(self):
        super().__init__(
            image="minion.png",
            name="Minion",
            alignment=Alignment.EVIL,
            type=CardType.MINION,
            template="",
            description="I always lie",
            is_corrupted=False,
            is_lying=True
        )

    def get_template(self, this_card_position: int, game_disposition: GameDisposition, lying: bool = True) -> str:
        # This card will select a random card present in game_disposition and switch its image, 
        # to the one it randomly selected and then it will use it's set_template method
        total_positions = len(game_disposition.positions)
        random.seed()
        random_position = random.choice([pos for pos in range(total_positions) if pos != this_card_position])
        random_card: Card = game_disposition.get_card_at(random_position)

        template = random_card.get_template(this_card_position=this_card_position, game_disposition=game_disposition, lying=lying)
        self.image=random_card.image
        self.name=random_card.name
        return template