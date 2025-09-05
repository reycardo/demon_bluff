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
    def set_template(self, this_card_position: int, game_disposition: "GameDisposition") -> None:
        """
        Placeholder for setting the card's template based on its position and the game disposition.
        Should be overridden by subclasses.
        """
        pass
    image: str
    name: str
    alignment: Alignment
    type: CardType
    template: str
    is_corrupted: bool
    is_lying: bool
    description: str = ""

    def __post_init__(self):
        # Always prepend the image path
        self.image = f"images/{self.image}"

    def to_dict(self):
        return {
            "image": self.image,
            "name": self.name,
            "alignment": self.alignment.value if hasattr(self.alignment, 'value') else str(self.alignment),
            "type": self.type.value if hasattr(self.type, 'value') else str(self.type),
            "template": self.template,
            "description": self.description
        }

    def corrupt(self):
        self.is_corrupted = True

    @staticmethod
    def dump_to_json(cards, filename="game.json"):
        import json
        data = [card.to_dict() for card in cards]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)