def trick_score(trick, trump_suit):
    """
        Returns score of a trick using card values and trump suit

        Args:
            trick: set of four cards
            trump_suit: one of the suits

        Returns:
            Returns score

        Raises:
            ValueError: If trick does not have 4 cards
            TypeError: If trump_suit not a valid suit
        """

    suits = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
    trump_values = {'Jack': 20, '9': 14, 'Ace': 11, '10': 10, 'King': 4,
                    'Queen': 3, '8': 0, '7': 0}
    non_trump_values = {'Jack': 2, '9': 0, 'Ace': 11, '10': 10, 'King': 4,
                        'Queen': 3, '8': 0, '7': 0}

    if len(trick) != 4:  # if not exactly 4 trick cards
        raise ValueError

    if trump_suit not in suits:  # if trump suit not valid
        raise TypeError

    score = 0

    for card, suit in trick:  # for each pair of card and suit
        if card not in trump_values:  # raise error if card not appropriate
            raise ValueError
        if suit not in suits:
            raise ValueError

        if suit == trump_suit:  # use trump values if trump suit
            score += trump_values[card]
        else:  # use non_trump values if not trump suit
            score += non_trump_values[card]

    return score
