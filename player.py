class Players:
    def __init__(self, label: str, hand: list = None) -> None:
        if hand is None:
            hand = []
        self.label = label
        self.hand = hand

    def add_card(self, card: int) -> None:
        self.hand.append(card)