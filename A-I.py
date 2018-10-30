# This is a version of the A.I that uses rules to choose the best move rather than hard coding
import itertools

class AI():
    """This is the class of the A.I that the player will play against. """
    def __init__(self, opHand, myHand, start):
        self._opHand = opHand
        self._myHand = myHand
        self.start = start

    def _calcMoves(self):
        desCombos = []
        combos = []
        # loop through each combination of my hand and the enemy hand
        # if that combination allows for the destruction of an opponenents hand
        # append it to a list
        for r in itertools.product(_myHand, _opHand):
            if r[0] + r[1] >= 5:
                desCombos.append(r)
            elif r[0] + r[1] + r[0] < 5:
                combos.append(r)

        if len(desCombos) != 0:
            return desCombos
        else:
            return combos.sort(key=combos[0] + combos[1])



    def attack(self):
        """This function dictates what to do if the AI decides it wants to attack"""
        attacking = []
        if self.start == True:
            attacking = ['attack', 'left', 'left']
            return attacking

        else:
            movesToDestroy = self._calcMoves(state="destroy")
            if len(movesToDestroy) != 0: # if we can't destroy an opponets hand
