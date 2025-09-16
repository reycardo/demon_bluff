import random
from api.game_setup.game_disposition import GameDisposition
from .base import Card, Alignment, CardType

class Lover(Card):
    def __init__(self):
        super().__init__(
            image="tsuki.png",
            name="Tsuki",
            alignment=Alignment.GOOD,
            type=CardType.VILLAGER,
            template="",
            description="Can't die, if corrupted takes 4 additional dmg",
            is_corrupted=False,
            is_lying=False
        )

    def get_template(self, this_card_position: int, game_disposition: GameDisposition, lying: bool = False) -> str:
        template = "I Can't die"
        return template
    
    def kill(self):
        self.is_dead = True
        if self.is_corrupted:
            return 9  # Takes 5+4 additional damage if corrupted
        return 0  # Normal damage if not corrupted