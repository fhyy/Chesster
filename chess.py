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

def getIndexFromCoords(x, y):
    return y*8 + x
    
def getPieceOnCoordinates(x, y, boardState):
    posIndex = getIndexFromCoords(x,y)
    return boardState[posIndex]
def getPieceOnPosition(posIndex, boardState):
    return boardState[posIndex]
    
def getValidMovesFromPosition(posIndex, boardStates):
    x = getX(posIndex)
    y = getY(posIndex)
    piece = getPieceOnPosition(posIndex, boardStates)
    if piece == PIECE.WHITE_PAWN or piece == PIECE.BLACK_PAWN:
        return getValidMovesFromPosition_pawn(getColor(piece), x, y, boardStates)
    if piece == PIECE.WHITE_KNIGHT or piece == PIECE.BLACK_KNIGHT:
        return getValidMovesFromPosition_knight(getColor(piece), x, y, boardStates)
    if piece == PIECE.WHITE_BISHOP or piece == PIECE.BLACK_BISHOP:
        return getValidMovesFromPosition_bishop(getColor(piece), x, y, boardStates)
    if piece == PIECE.WHITE_ROOK or piece == PIECE.BLACK_ROOK:
        return getValidMovesFromPosition_rook(getColor(piece), x, y, boardStates)
    if piece == PIECE.WHITE_QUEEN or piece == PIECE.BLACK_QUEEN:
        return getValidMovesFromPosition_queen(getColor(piece), x, y, boardStates)
    if piece == PIECE.WHITE_KING or piece == PIECE.BLACK_KING:
        return getValidMovesFromPosition_king(getColor(piece), x, y, boardStates)
    return []
    
def getValidMovesFromPosition_pawn(color, x, y, boardStates):
    posIndex = getIndexFromCoords(x, y)
    valid = []
    if color == COLOR.BLACK:
        if isInside(x, y+1):
            if getPieceOnPosition(posIndex+DOWN, boardStates[0]) == PIECE.NONE:
                valid.append(posIndex+DOWN)
                if y == 6 and getPieceOnPosition(posIndex+DOWN+DOWN, boardStates[0]) == PIECE.NONE:
                    valid.append(posIndex+DOWN+DOWN)
            if (isInside(x-1, y+1) and
                getPieceOnPosition(posIndex+DOWN+LEFT, boardStates[0]) != NONE and
                getColor(getPieceOnPosition(posIndex+DOWN+LEFT, boardStates[0])) == COLOR.WHITE):
                valid.append(posIndex+DOWN+LEFT)
            if (isInside(x+1, y+1) and
                getPieceOnPosition(posIndex+DOWN+RIGHT, boardStates[0]) != NONE and
                getColor(getPieceOnPosition(posIndex+DOWN+RIGHT, boardStates[0])) == COLOR.WHITE):
                valid.append(posIndex+DOWN+RIGHT)
    else:
        if isInside(x, y-1):
            if getPieceOnCoordinates(x, y-1, boardStates[0]) == PIECE.NONE:
                valid.append(posIndex+UP)
                if y == 1 and getPieceOnPosition(posIndex+UP+UP, boardStates[0]) == PIECE.NONE:
                    valid.append(posIndex+UP+UP)
            if (isInside(x-1, y-1) and
                getPieceOnPosition(posIndex+UP+LEFT, boardStates[0]) != NONE and
                getColor(getPieceOnPosition(posIndex+UP+LEFT, boardStates[0])) == COLOR.BLACK):
                valid.append(posIndex+UP+LEFT)
            if (isInside(x+1, y-1) and
                getPieceOnPosition(posIndex+UP+RIGHT, boardStates[0]) != NONE and
                getColor(getPieceOnPosition(posIndex+UP+RIGHT, boardStates[0])) == COLOR.BLACK):
                valid.append(posIndex+UP+RIGHT)
    return valid    
def getValidMovesFromPosition_knight(color, x, y, boardStates):
    valid = []
    for i in [-1,1]:
        for j in [-1,1]:
            piece = getPieceOnCoordinates(x+(i*2), y+j, boardStates[0])
            if piece == PIECE.NONE or getColor(piece) != color:
                valid.append(getIndexFromCoords(x+(i*2), y+j))
            piece = getPieceOnCoordinates(x+i, y+(j*2), boardStates[0])
            if piece == PIECE.NONE or getColor(piece) != color:
                valid.append(getIndexFromCoords(x+i, y+(j*2)))
    return valid
def getValidMovesFromPosition_bishop(color, x, y, boardStates):
    valid = []
    for dx in [-1,1]:
        for dy in [-1,1]:
            for d in range(7):
                if isInside(x+dx*d, y+dy*d):
                    if getPieceOnCoordinates(x+dx*d, y+dy*d, boardStates[0]) == PIECE.NONE:
                        valid.append(getIndexFromCoords(x+dx*d, y+dy*d))
                        continue
                    elif getColor(getPieceOnCoordinates(x+dx*d, y+dy*d, boardStates[0])) != color:
                        valid.append(getIndexFromCoords(x+dx*d, y+dy*d, boardStates[0]))
                    break
                break
    return valid
def getValidMovesFromPosition_rook(color, x, y, boardStates):
    valid = []
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        for d in range(7):
            if isInside(x+dx*d, y+dy*d):
                if getPieceOnCoordinates(x+dx*d, y+dy*d, boardStates[0]) == PIECE.NONE:
                    valid.append(getIndexFromCoords(x+dx*d, y+dy*d))
                    continue
                elif getColor(getPieceOnCoordinates(x+dx*d, y+dy*d, boardStates[0])) != color:
                    valid.append(getIndexFromCoords(x+dx*d, y+dy*d))
                break
            break
    return valid
def getValidMovesFromPosition_queen(color, x, y, boardStates):
    return getValidMovesFromPosition_bishop(color, x, y, boardStates)
    + getValidMovesFromPosition_rook(color, posIndex, boardStates)
def getValidMovesFromPosition_king(color, x, y, boardStates):
    # TODO: castling
    valid = []
    for dx, dy in [(-1,1),(0,1),(1,1),
                   (-1,0),      (1,0),
                   (-1,-1),(0,-1),(1,-1)]:
        if isInside(x+dx, y+dy):
            piece = getPieceOnCoordinates(x+dx, y+dy, boardStates[0])
            if piece == PIECE.NONE or getColor(piece) != color:
                valid.append(getIndexFromCoords(x+dx, y+dy))
    return []
    
def checkIfValidMove(fromPos, toPos, boardStates):
    return toPos in getValidMovesFromPosition(fromPos, boardStates)
    
def isInside(x, y):
    return x >= 0 and x < 8 and y >= 0 and y < 8
    
def getX(posIndex):
    return posIndex - 8*getY(posIndex)
    
def getY(posIndex):
    return floor(posIndex/8)
    
def isInCheck(color, boardState):
    # TODO
    return False
    
def addBoardState(newBoardstate, boardStates):
    boardStates.insert(0, newBoardstate)