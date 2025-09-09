import random
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
        # based on the game_disposition, check the adjacent positions to see if there are any EVIL cards
        adjacent_positions = game_disposition.get_adjacent_positions(this_card_position)
        evil_count = 0
        for pos in adjacent_positions:
            card = game_disposition.get_card_at(pos)
            if card and card.alignment == Alignment.EVIL:
                evil_count += 1

        # get evils in game disposition
        total_evil = sum(1 for card in game_disposition.get_all_cards() if card.alignment == Alignment.EVIL)
        
        def neighbor_text(n):
            return f"Evil neighbor{'s' if n != 1 else ''}"

        if self.is_corrupted or self.is_lying:
            # Lie about the number of adjacent evil cards
            possible_lies = [i for i in range(0, total_evil + 1) if i != evil_count]
            if possible_lies:
                lie = random.choice(possible_lies)
                template = f"I have {lie} {neighbor_text(lie)}"
            else:
                template = f"I have {evil_count} {neighbor_text(evil_count)}"
        else:
            template = f"I have {evil_count} {neighbor_text(evil_count)}"
        
        self.template = template
        return self.template