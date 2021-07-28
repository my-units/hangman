class Card:
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, v, s):
        """suit 和 values 的值都为整型数"""
        self.value = v
        self.suit = s

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v


# card1 = Card(10, 1)
# card2 = Card(10, 3)
# print(card1, '\n', card2)
# print(card1 > card2)
