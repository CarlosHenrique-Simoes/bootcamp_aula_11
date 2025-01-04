import random  # noqa: D100


def deal_card() -> int:
    """Returns a random card from the deck.

    The deck contains values from 2 to 11, with 10 repeated to represent
    the face cards (Jack, Queen, King) which also have a value of 10.
    """  # noqa: D401
    # List of possible card values in a deck
    cards: list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Randomly select a card from the deck
    card: int = random.choice(cards)  # noqa: S311
    return card


user_cards = []
computer_cards = []
IS_GAME_OVER = False
TWENTY_ONE = 21
ELEVEN = 11
TWO = 2

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


def calculate_score(cards: list) -> int:
    """Take a list of cards and return the score calculated from the cards.

    If the score is a BlackJack (21) and only 2 cards are in the list,
    return 0.
    If the score is over 21 and contains an Ace (11), change the Ace to 1 and
    recalculate the score.
    """
    if sum(cards) == TWENTY_ONE and len(cards) == TWO:
        # BlackJack
        return 0
    if ELEVEN in cards and sum(cards) > TWENTY_ONE:
        # Replace Ace with 1 (if over 21)
        cards.remove(11)
        cards.append(1)
    return sum(cards)
