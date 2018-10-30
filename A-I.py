# This is a version of the A.I that uses rules to choose the best move rather than hard coding

class AI():
    """This is the class of the A.I that the player will play against. """
    def __init__(self, opHand, myHand, start):
        self._opHand = opHand
        self._myHand = myHand
        self.start = start

    def _calcOdds(self, state="destroy"):
        combos = []
        for myHand in self._myHand:
            for opHand in self._opHand:
                if myHand + opHand == 5:
                    combos.append([self._myHand.index(myHand), self.opHand.index(opHand)])
        return combos


    def attack(self):
        """This function dictates what to do if the AI decides it wants to attack"""
        attacking = []
        if self.start == True:
            attacking = ['attack', 'left', 'left']
            return attacking

        else:
            movesToDestroy = self._calcOdds(state="destroy")
            if len(movesToDestroy) != 0:
