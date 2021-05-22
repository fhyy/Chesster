from enum import Enum

class COLOR(Enum):
    WHITE = 1
    BLACK = -1
class PIECE(Enum):
    NONE = 0
    WHITE_PAWN = 1
    WHITE_KNIGHT = 3
    WHITE_BISHOP = 4
    WHITE_ROOK = 5
    WHITE_QUEEN = 9
    WHITE_KING = 100
    BLACK_PAWN = -1
    BLACK_KNIGHT = -3
    BLACK_BISHOP = -4
    BLACK_ROOK = -5
    BLACK_QUEEN = -9
    BLACK_KING = -100

UP = -8
DOWN = 8
LEFT = -1
RIGHT = 1
    
def getColor(piece):
    if piece < 0:
        return COLOR.BLACK
    return COLOR.WHITE

def getIndexFromPosTuple(letterNumTuple):
    return getIndexFromPos(letterNumTuple[0:1], int(letterNumTuple[1:2]))
   
def getIndexFromPos(letter, number):
    letterVal = ord(letter.lower()) - 97
    numberVal = number - 1
    return numberVal*8 + letterVal

def getPieceOnPosition(posIndex, boardState):
    # TODO
    return PIECE.WHITE_PAWN
    
def getValidMovesFromPosition(posIndex, boardState):
    piece = getPieceOnPosition(posIndex, boardState)
    if piece == PIECE.WHITE_PAWN or piece == PIECE.BLACK_PAWN:
        return getValidMovesFromPosition_pawn(getColor(piece), posIndex, boardState)
    if piece == PIECE.WHITE_KNIGHT or piece == PIECE.BLACK_KNIGHT:
        return getValidMovesFromPosition_knight(getColor(piece), posIndex, boardState)
    if piece == PIECE.WHITE_BISHOP or piece == PIECE.BLACK_BISHOP:
        return getValidMovesFromPosition_bishop(getColor(piece), posIndex, boardState)
    if piece == PIECE.WHITE_ROOK or piece == PIECE.BLACK_ROOK:
        return getValidMovesFromPosition_rook(getColor(piece), posIndex, boardState)
    if piece == PIECE.WHITE_QUEEN or piece == PIECE.BLACK_QUEEN:
        return getValidMovesFromPosition_queen(getColor(piece), posIndex, boardState)
    if piece == PIECE.WHITE_KING or piece == PIECE.BLACK_KING:
        return getValidMovesFromPosition_king(getColor(piece), posIndex, boardState)
    return []
    
def getValidMovesFromPosition_pawn(color, posIndex, boardState):
    valid = []
    if color == COLOR.BLACK:
        if isInside(getX(posIndex), getY(posIndex)+1):
            if getPieceOnPosition(posIndex+DOWN) == PIECE.NONE:
                valid.append(posIndex+DOWN)
            if (isInside(getX(posIndex)-1, getY(posIndex)+1) and
                getPieceOnPosition(posIndex+DOWN+LEFT) != NONE and
                getColor(getPieceOnPosition(posIndex+DOWN+LEFT)) == COLOR.WHITE):
                valid.append(posIndex+DOWN+LEFT)
            if (isInside(getX(posIndex)+1, getY(posIndex)+1) and
                getPieceOnPosition(posIndex+DOWN+RIGHT) != NONE and
                getColor(getPieceOnPosition(posIndex+DOWN+RIGHT)) == COLOR.WHITE):
                valid.append(posIndex+DOWN+RIGHT)
    else:
        if isInside(posIndex, UP):
            if getPieceOnPosition(getX(posIndex), getY(posIndex)-1) == PIECE.NONE:
                valid.append(posIndex+UP)
            if (isInside(getX(posIndex)-1, getY(posIndex)-1) and
                getPieceOnPosition(posIndex+UP+LEFT) != NONE and
                getColor(getPieceOnPosition(posIndex+UP+LEFT)) == COLOR.BLACK):
                valid.append(posIndex+UP+LEFT)
            if (isInside(getX(posIndex)+1, getY(posIndex)-1) and
                getPieceOnPosition(posIndex+UP+RIGHT) != NONE and
                getColor(getPieceOnPosition(posIndex+UP+RIGHT)) == COLOR.BLACK):
                valid.append(posIndex+UP+RIGHT)
    return valid    
def getValidMovesFromPosition_knight(color, posIndex, boardState):
    # TODO
    return []    
def getValidMovesFromPosition_bishop(color, posIndex, boardState):
    # TODO
    return []    
def getValidMovesFromPosition_rook(color, posIndex, boardState):
    # TODO
    return []    
def getValidMovesFromPosition_queen(color, posIndex, boardState):
    # TODO
    return getValidMovesFromPosition_bishop(color, posIndex, boardState)
    + getValidMovesFromPosition_rook(color, posIndex, boardState)
def getValidMovesFromPosition_king(color, posIndex, boardState):
    # TODO
    return []
    
def checkIfValidMove(fromPos, toPos, boardState):
    # TODO
    return False
    
def isInside(x, y):
    return x >= 0 and x < 8 and y >= 0 and y < 8
    
def getX(posIndex):
    return posIndex - 8*getY(posIndex)
    
def getY(posIndex):
    return floor(posIndex/8)
    
def isInCheck(color, boardState):
    # TODO
    return False