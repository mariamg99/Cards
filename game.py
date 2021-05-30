class Game:
    cards = ['2R', '2N', '2T', '2C',
             '3R', '3N', '3T', '3C', '4R', '4N', '4T', '4C',
             '5R', '5N', '5T', '5C', '6R', '6N', '6T', '6C',
             '7R', '7N', '7T', '7C', '8R', '8N', '8T', '8C',
             '9R', '9N', '9T', '9C', 'zR', 'zN', 'zT', 'zC',
             'jR', 'jN', 'jT', 'jC', 'qR', 'qN', 'qT', 'qC',
             'kR', 'kN', 'kT', 'kC', 'aR', 'aN', 'aT', 'aC']

    def __init__(self, playersno, cardsno, cper_player):
        self.p = playersno
        self.c = cardsno
        self.cper_player = cper_player
        self.current_cards = Game.cards
        self.dropped_cards = []

    @staticmethod
    def validate_card(current_cards, card):

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