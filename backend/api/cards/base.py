# cards/base.py
from dataclasses import dataclass
from enum import Enum

class Alignment(Enum):
    GOOD = "good"
    EVIL = "evil"

class CardType(Enum):
    VILLAGER = "villager"
    MINION = "minion"
    DEVIL = "devil"



@dataclass
class Card:
    def get_template(self, this_card_position: int, game_disposition: "GameDisposition", lying: bool = False) -> str:
        """
        Placeholder for setting the card's template based on its position and the game disposition.
        Should be overridden by subclasses.
        """
        return ""
    image: str
    name: str
    alignment: Alignment
    type: CardType
    template: str
    is_corrupted: bool
    is_lying: bool
    is_dead: bool = False
    description: str = ""
    masked_card: "Card" = None

    def __post_init__(self):
        # Always prepend the image path
        self.image = f"images/cards/{self.image}"

    def to_dict(self):
        return {
            "image": self.image,
            "name": self.name,
            "alignment": self.alignment.value if hasattr(self.alignment, 'value') else str(self.alignment),
            "type": self.type.value if hasattr(self.type, 'value') else str(self.type),
            "template": self.template,
            "description": self.description,
            "masked_card": self.masked_card.to_dict() if self.masked_card else None
        }

    def corrupt(self):
        self.is_corrupted = True

    def kill(self):
        self.is_dead = True
        if self.alignment == Alignment.EVIL:
            return 0
        else:
            return 5

    @staticmethod
    def dump_to_json(cards, filename="game.json"):
        import json
        data = [card.to_dict() for card in cards]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)