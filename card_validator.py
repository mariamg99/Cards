class Card_Validator(object):

    def __init__(self, previous_card, current_card):
        self.previous_card = previous_card
        self.current_card = current_card

    @staticmethod
    def is_ok_septica(previous_card, current_card):
        if len(current_cards) == 0:
            current_cards.append(card)
            return 1

        if card[0] == '2':  # Must have same color
            if current_cards[-1][1] == card[1] or current_cards[-1][0] == '2':
                return 1

        if card[0] == '7' and current_cards[-1][0] != '2':
            return 1

        if current_cards[-1][0] == '7':
            return 1

        if current_cards[-1][1] == card[1] or current_cards[-1][0] == card[0]:
            return 1

        return 0