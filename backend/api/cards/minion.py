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

    def set_template(self, this_card_position: int, game_disposition: GameDisposition):
        # This card will select a random card present in game_disposition and switch its image, 
        # to the one it randomly selected and then it will use it's set_template method
        total_positions = len(game_disposition.positions)
        random_position = random.choice([pos for pos in range(total_positions) if pos != this_card_position])
        random_card: Card = game_disposition.get_card_at(random_position)

        self.template = random_card.set_template(this_card_position=this_card_position, game_disposition=game_disposition)
        self.image=random_card.image
        self.name=random_card.name
        return self.template