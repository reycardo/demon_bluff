from api.game_setup.game_disposition import GameDisposition
from .base import Card, Alignment, CardType
import random

class Banana(Card):
    def __init__(self):
        super().__init__(
            image="banana.png",
            name="Banana",
            alignment=Alignment.GOOD,
            type=CardType.VILLAGER,
            template="",
            description="Say Banana if not corrupted, else say Split",
            is_corrupted=False,
            is_lying=False
        )    

    def get_template(self, this_card_position: int, game_disposition: GameDisposition, lying: bool = False) -> str:
        if lying:
            template = "I say Split"
        else:   
            template = "I say Banana"
        return template