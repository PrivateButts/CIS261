# Randy Butts  CIS261  Deck of Cards


from random import shuffle


class Card:
    rank: str
    suit: str

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"


class Deck:
    cards: list[Card] = []

    def __init__(self):
        for suit in ["Clubs", "Hearts", "Spades", "Diamonds"]:
            for rank in ["Ace", *range(2, 11), "Jack", "Queen", "King"]:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, amount: int = 1):
        print("Here are your cards:")
        for i in range(amount):
            card = self.cards.pop()
            print(card)

    def printCount(self):
        print(f"There are {len(self.cards)} cards left in the deck.")


if __name__ == "__main__":
    print("Card Dealer")

    deck = Deck()
    deck.shuffle()
    print("I have shuffled a deck of 52 cards.")

    amount = int(input("How many cards would you like?: "))
    print()

    deck.deal(amount)
    print()

    deck.printCount()

    print("\nGood luck!")
