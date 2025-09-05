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

    def set_template(self, this_card_position: int, game_disposition: GameDisposition):
        self.template = f"NOT IMPLEMENTED"
