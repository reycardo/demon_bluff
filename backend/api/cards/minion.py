from .base import Card, Alignment, CardType

class Minion(Card):
    def __init__(self):
        super().__init__(
            image="minion.png",
            name="Minion",
            alignment=Alignment.EVIL,
            type=CardType.MINION,
            template=""
        )

    def set_template(self):
        self.template = f""
