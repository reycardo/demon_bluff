from .base import Card, Alignment, CardType

class Hunter(Card):
    def __init__(self):
        super().__init__(
            image="hunter.png",
            name="Hunter",
            alignment=Alignment.GOOD,
            type=CardType.VILLAGER,
            template="",
            description="Learn how far from me is the nearest Evil"
        )

    def set_template(self, number_of_adjacent_evils: int):
        self.template = f"I am {number_of_adjacent_evils} card away from closest Evil"
