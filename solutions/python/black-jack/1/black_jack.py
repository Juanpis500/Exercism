"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """
    face_card = ['J','Q','K']
    ace_card = 'A'
    default_card = '23456789'
    
    if card == '10':
        return 10
    if card in face_card:
        return 10
    if card == ace_card:
        return 1
    if card in default_card:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    if value_of_card(card_one) > value_of_card(card_two):
        return str(card_one)
    if value_of_card(card_one) < value_of_card(card_two):
        return str(card_two)
    if value_of_card(card_one) == value_of_card(card_two):
        return str(card_one), str(card_two)

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """
    
    if card_one == 'A' or card_two == 'A':
        return 1
    if (value_of_card(card_one) + value_of_card(card_two)) > 10:
        return 1
    else:
        return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """
    face_card = ['J','Q','K']

    if (card_one in face_card and card_two == 'A') or (card_one == 'A' and card_two in face_card):
        return True
        
    if (card_one == '10' and card_two == 'A') or (card_one == 'A' and card_two == '10'):
        return True
        
    if (value_of_card(card_one) + value_of_card(card_two)) == 21:
        return True
        
    return False
    


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if value_of_card(card_one) == value_of_card(card_two):
        return True
        
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    numbers =[9, 10, 11]

    if card_one =='A' or  card_two == 'A':
        if card_one =='A':
            if (value_of_ace(card_one,card_two) + value_of_card(card_two)) in numbers:
                return True
        if card_two =='A':
            if (value_of_ace(card_one,card_two) + value_of_card(card_one)) in numbers:
                return True

    if (value_of_card(card_one) + value_of_card(card_two)) in numbers:
        return True
        
    return False
