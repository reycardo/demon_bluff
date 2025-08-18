from .base import Card, Alignment, CardType

class Lover(Card):
    def __init__(self):
        super().__init__(
            image="lover.png",
            name="Lover",
            alignment=Alignment.GOOD,
            type=CardType.VILLAGER,
            template=""
        )

    def set_template(self, number_of_adjacent_evils: int):
        self.template = f"{number_of_adjacent_evils} Evil adjacent to me"
