from api.game_setup.game_disposition import GameDisposition
from .base import Card, Alignment, CardType
import random

class Hunter(Card):
    def __init__(self):
        super().__init__(
            image="hunter.png",
            name="Hunter",
            alignment=Alignment.GOOD,
            type=CardType.VILLAGER,
            template="",
            description="Learn how far from me is the nearest Evil",
            is_corrupted=False,
            is_lying=False
        )    

    def set_template(self, this_card_position: int, game_disposition: GameDisposition):
        # set template based on game disposition
        # Hunter card will try to find the nearest card whose alignment is EVIL
        nearest_evil_distance = None
        total_positions = len(game_disposition.positions)
        for distance in range(1, (total_positions // 2) + 1):
            left_position = (this_card_position - distance) % total_positions
            right_position = (this_card_position + distance) % total_positions
            
            left_card: Card = game_disposition.get_card_at(left_position)
            right_card: Card = game_disposition.get_card_at(right_position)
            
            if left_card and left_card.alignment == Alignment.EVIL:
                nearest_evil_distance = distance
                break
            if right_card and right_card.alignment == Alignment.EVIL:
                nearest_evil_distance = distance
                break        

        if self.is_corrupted or self.is_lying:
            # Get all possible distances except the real one
            possible_distances = [d for d in range(1, (total_positions // 2) + 1)]
            if nearest_evil_distance in possible_distances:
                possible_distances.remove(nearest_evil_distance)
            if possible_distances:
                lie_distance = random.choice(possible_distances)
                template = f"I am {lie_distance} card away from closest Evil"
        else:
            if nearest_evil_distance is not None:
                template = f"I am {nearest_evil_distance} card away from closest Evil"
            else:
                template = "No Evil card in range"

        self.template = template
        return template