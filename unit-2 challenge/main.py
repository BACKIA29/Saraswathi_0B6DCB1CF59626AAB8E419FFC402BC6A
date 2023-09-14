#Implementation of a class called Player that represents a cricket player

class Player:
    def play(self):
        print("The player is playing cricket.")
      
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")
      
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")
      
batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()