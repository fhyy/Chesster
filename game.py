import chess as chs

class Game:
    def __init__(self, gameId):
        self.whitePlayer = None
        self.blackPlayer = None
        self.turn = chs.COLOR.WHITE
        self.boardState = chs.startingBoardState()
        self.gameId = gameId

    def setPlayer(player : Player):
        if player.color == chs.COLOR.WHITE:
            self.whitePlayer = player
        else:
            self.blackPlayer = player


class Player:
    def __init__(self):
        self.color = chs.COLOR.WHITE
        self.playerId = None # Keep as None to play agains bot
