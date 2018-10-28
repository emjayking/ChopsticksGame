# Simple A.I

class A.I:
    def __init__(self, hand, opHand, start=False , turnNo , enemyMove):
        self.hand = hand # [Left Hand, Right Hand]
        self.opHand = opHand # [Left Hand, Right Hand]
        self.start = start
        self.attack = [1, 1] #[attacking, attacking with]
        self.opHand = opHand  [left hand, Right Hand]
        self.turnNo = turnNo
        self.eMove = enemyMove

    # what does the code need to do?
        # control two variables (left and right hand)

        # If the number on each hand is <= 5 then the hand must be removed from play

        # make a play to remove an oponents hand or to split our own hand
     def choose(self):
         pass
         # choose between split or attack

    def split(self):
        pass
        #doing some stuff

    def attack(self):
        if self.start is True:
            self.attack = [1, 1]
        else:
            if self.turnNo == 2 # in other words if we are going second
                if self.hand ==  [1, 2]:
                    self.attack == [1, 2]
                else:
                    self.attack == [1, 1]

            if self.turnNo == 3
                if self.eMove == "attack"
                    if self.opHand == [2, 1]: # if they have 2 in their left and 1 in their right
                        if self.hand == [3, 1]: # and we have 3 in our left
                            self.attack = [1, 1] # attack their left with our left
                        elif self.hand == [2, 2]: # or if we have 2, 2
                            self.attack = [2 ,1] # attack their right with either one
                        else:
                            self.attack = [2, 2] # attack with our Right because it must be 3


                    if self.opHand == [1, 2]: # if they have 2 in their right
                        if self.hand == [3, 1]: # and we have 3 in our left
                            self.attack = [2, 1] # attack with our left
                        elif self.hand == [2, 2]: # or if we have 2 ,2
                            self.attack = [1, 2] # attack their left with either one

                        else:
                            self.attack = [2, 2] # attack with our Right because is must be 3


                if self.eMove == "pass":







        #doing some other stuff
