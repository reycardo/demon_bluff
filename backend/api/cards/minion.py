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
        self.template = f"NOT IMPLEMENTED"