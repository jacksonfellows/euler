import random
from collections import defaultdict

class MonopolySquare:
    def __init__(self, pos):
        # a number from 0 to 39
        self.pos = pos

    def land(self):
        return self.pos

    def __str__(self):
        return "pos: %d" % self.pos

class ReferralSquare(MonopolySquare):
    def __init__(self, pos, referral):
        MonopolySquare.__init__(self, pos)
        self.referral = referral

    def land(self):
        # print("using referral square")
        return self.referral

    def __str__(self):
        return MonopolySquare.__str__(self) + ", ref: %d" % self.referral

class CardsSquare(MonopolySquare):
    def __init__(self, pos, cards):
        MonopolySquare.__init__(self, pos)
        self.cards = cards
        self.i = 0

    def land(self):
        return self.cards.draw(self.pos)
    
    def __str__(self):
        return MonopolySquare.__str__(self) + ", cards: " + str([str(c) for c in self.cards.cards])

class Cards:
    def __init__(self, cards):
        self.cards = cards
        random.shuffle(self.cards)
        self.i = 0

    def draw(self, pos):
        card = self.cards[self.i]
        self.i = (self.i+1) % len(self.cards)
        if card == "nop":
            return pos

        if isinstance(card,ActionCard):
            # print("using action card " + str(card))
            return card.action(pos)
        return card


class ActionCard(Cards):
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def __str__(self):
        return self.name

board = list(map(MonopolySquare, range(40))) # start out with all normal squares
# a little helper to replace these normal squares
def replace(i, square_type, *args):
    board[i] = square_type(i, *args)

# set up the "referral" squares
replace(30, ReferralSquare, 10)

# set up the "card" squares
cc_cards = Cards([0,10] + ["nop"]*14)
replace(2, CardsSquare, cc_cards)
replace(17, CardsSquare, cc_cards)
replace(33, CardsSquare, cc_cards)

# setup the actions
def goto_next(locs): # assume locs are static squares
    def next_(pos):
        gs = list(filter(lambda x: x > pos, locs))
        if len(gs) == 0:
            return locs[0] # wrap around
        return min(gs)
    return next_
next_RR = ActionCard("next RR", goto_next([5,15,25,35]))
next_U = ActionCard("next U", goto_next([12,28]))
back_3 = ActionCard("back 3", lambda pos: (pos - 3) % len(board))

ch_cards = Cards([0, 10, 11, 24, 39, 5, next_RR, next_RR, next_U, back_3] + ["nop"]*6)
replace(7, CardsSquare, ch_cards)
replace(22, CardsSquare, ch_cards)
replace(36, CardsSquare, ch_cards)

results = defaultdict(int)

square = board[0]
results[0] = 1
num_results = 1

conseq_doubles = 0
# print(square)
for _ in range(1000000):
    a = random.choice(range(1,5)) #random.choice(range(1,7))
    b = random.choice(range(1,5)) #random.choice(range(1,7))
    if a == b:
        conseq_doubles += 1
    else:
        conseq_doubles = 0

    if conseq_doubles == 3:
        i = 10 # go to jail
    else:
        roll = a + b
        # print("rolled: %d" % roll)
        i = board[(square.pos + roll) % len(board)].land()

    results[i] += 1
    num_results += 1
    square = board[i]
    # print(square)

# print(num_results)
# print(results)

sorted_results = list(map(lambda kv: (kv[0],kv[1]/num_results), sorted(results.items(), key = lambda kv: kv[1], reverse = True)))
# print(sorted_results)
print("%0.2d%0.2d%0.2d" % (sorted_results[0][0], sorted_results[1][0], sorted_results[2][0]))
