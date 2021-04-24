class Card:
    _rank_to_str = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
    _suit_to_str = {'C': 'Clubs', 'H': 'Hearts', 'S': 'Spades', 'D': 'Diamonds'}

    # initialise the cards into rank and suit
    def __init__(self, rank: int, suit: str):

        assert 2 <= rank <= 14
        assert suit.upper() in {'C', 'H', 'S', 'D'}

        self.rank = rank
        self.suit = suit

    # gives back the cards in printable representation
    def __repr__(self):

        rank_to_str = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
        suit_to_str = {'C': 'Clubs', 'H': 'Hearts', 'S': 'Spades', 'D': 'Diamonds'}

        return_rank = ""
        if self.rank in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            return_rank += str(self.rank)
        else:
            return_rank += rank_to_str[self.rank]

        return_suit = suit_to_str[self.suit]

        return str(return_rank) + " of " + str(return_suit)

    # all overloading functions below tells if one card is greater than the other in gameplay
    def __lt__(self, other):

        return self.rank < other.rank
        pass

    def __gt__(self, other):

        return self.rank > other.rank
        pass

    def __le__(self, other):

        return self.rank <= other.rank
        pass

    def __ge__(self, other):

        return self.rank >= other.rank
        pass

    def __eq__(self, other):

        return self.rank == other.rank
        pass


""" The class Deck takes care of shuffling the card, dealing the card and resetting the card."""


class Deck:
    # set initial condition
    def __init__(self, shuffled=False):
        self.shuffled = shuffled
        self.cards = [Card(2, "D"), Card(3, "D"), Card(4, "D"), Card(5, "D"), Card(6, "D"), Card(7, "D"), Card(8, "D"),
                      Card(9, "D"), Card(10, "D"), Card(11, "D"), Card(12, "D"), Card(13, "D"), Card(14, "D"),
                      Card(2, "C"), Card(3, "C"), Card(4, "C"), Card(5, "C"), Card(6, "C"), Card(7, "C"), Card(8, "C"),
                      Card(9, "C"), Card(10, "C"), Card(11, "C"), Card(12, "C"), Card(13, "C"), Card(14, "C"),
                      Card(2, "S"), Card(3, "S"), Card(4, "S"), Card(5, "S"), Card(6, "S"), Card(7, "S"), Card(8, "S"),
                      Card(9, "S"), Card(10, "S"), Card(11, "S"), Card(12, "S"), Card(13, "S"), Card(14, "S"),
                      Card(2, "H"), Card(3, "H"), Card(4, "H"), Card(5, "H"), Card(6, "H"), Card(7, "H"), Card(8, "H"),
                      Card(9, "H"), Card(10, "H"), Card(11, "H"), Card(12, "H"), Card(13, "H"), Card(14, "H")]
        self.cards.reverse()

    # Shuffle the cards using random module
    def shuffle(self):

        self.shuffled = True
        import random
        random.shuffle(self.cards)

    # gives the top card from the list
    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            self.shuffled = False
            return None

    # Reset the cards into non-shuffled condition
    def reset(self):
        self.shuffled = False
        self.cards = [Card(2, "D"), Card(3, "D"), Card(4, "D"), Card(5, "D"), Card(6, "D"), Card(7, "D"), Card(8, "D"),
                      Card(9, "D"), Card(10, "D"), Card(11, "D"), Card(12, "D"), Card(13, "D"), Card(14, "D"),
                      Card(2, "C"), Card(3, "C"), Card(4, "C"), Card(5, "C"), Card(6, "C"), Card(7, "C"), Card(8, "C"),
                      Card(9, "C"), Card(10, "C"), Card(11, "C"), Card(12, "C"), Card(13, "C"), Card(14, "C"),
                      Card(2, "S"), Card(3, "S"), Card(4, "S"), Card(5, "S"), Card(6, "S"), Card(7, "S"), Card(8, "S"),
                      Card(9, "S"), Card(10, "S"), Card(11, "S"), Card(12, "S"), Card(13, "S"), Card(14, "S"),
                      Card(2, "H"), Card(3, "H"), Card(4, "H"), Card(5, "H"), Card(6, "H"), Card(7, "H"), Card(8, "H"),
                      Card(9, "H"), Card(10, "H"), Card(11, "H"), Card(12, "H"), Card(13, "H"), Card(14, "H")]
        self.cards.reverse()

    def __repr__(self):

        return "Deck(dealt " + str(52 - len(self.cards)) + ", shuffled=" + str(self.shuffled) + ")"
