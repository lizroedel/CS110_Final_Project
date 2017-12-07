import player

class Ghost(player):
    # Change the speed of the ghost
    def changespeed(self,list,ghost,turn,steps,l):
        '''
        Changes the speed of the player
        param list: (int, int) x, y:
        return: (none)
        '''
        try:
            z=list[turn][2]
            if steps < z:
                self.change_x=list[turn][0]
                self.change_y=list[turn][1]
                steps+=1
            else:
                if turn < l:
                    turn+=1
                elif ghost == "orange_ghost":
                    turn = 2
                else:
                    turn = 0
                    self.change_x=list[turn][0]
                    self.change_y=list[turn][1]
                    steps = 0
            return [turn,steps]
        except IndexError:
            return [0,0]
