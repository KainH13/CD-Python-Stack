from . import deck

class Player:

    def __init__(self, name):
        self.name = name
        self.deck = deck.Deck()
        self.deck.shuffle()
        self.score = 0
        self.current_card = None

    def flip_card(self):
        card = self.deck.cards[0]
        self.deck.cards.pop(0)
        print(f"Player {self.name} flipped {card.string_val}")
        self.current_card = card
        return self


if __name__ == "__main__":
    player = Player("Kai")
    player.flip_card()