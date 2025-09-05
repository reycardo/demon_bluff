from api.cards.base import Card

class GameDisposition:
    def __init__(self, positions=None):
        # positions: dict of position (int) -> card instance
        self.positions = positions if positions is not None else {}

    def add_card(self, card: Card, position: int):
        """
        Add a card to a specific numbered position.
        """
        if position is None:
            raise ValueError("Position must be specified for numbered disposition.")
        self.positions[position] = card

    def get_card_at(self, position: int):
        return self.positions.get(position)

    def get_all_cards(self):
        """
        Return all card instances in the disposition.
        """
        return list(self.positions.values())
    
    def get_adjacent_positions(self, position: int):
        """
        Return a list of positions adjacent to the given position.
        Adjacency is circular: position 0 is adjacent to 1 and N-1, position N-1 is adjacent to N-2 and 0.
        """
        keys = sorted(self.positions.keys())
        if position not in keys:
            raise ValueError(f"Position {position} not found in disposition.")
        idx = keys.index(position)
        n = len(keys)
        left = keys[(idx - 1) % n]
        right = keys[(idx + 1) % n]
        return [left, right]    
    
    def dump_to_frontend(self, filename: str):
        """
        Dump the game disposition to a JSON file for the frontend, including position info for each card.
        """
        cards_with_position = []
        for position, card in self.positions.items():
            card_data = card.to_dict() if hasattr(card, 'to_dict') else card.__dict__.copy()
            card_data['position'] = position
            cards_with_position.append(card_data)
        import json
        with open(filename, 'w') as f:
            json.dump(cards_with_position, f, indent=2)