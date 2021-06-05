import chess as chs
import assets as ass

yLabels = "87654321"
xLabels = "ABCDEFGH"

def getAssetFromPiece(piece: chs.Piece):
    if piece.color == chs.COLOR.WHITE and piece.piece == chs.PIECE.PAWN:
        return ass.whitePawn
    elif piece.color == chs.COLOR.WHITE and piece.piece == chs.PIECE.BISHOP:
        return ass.whiteBishop
    elif piece.color == chs.COLOR.WHITE and piece.piece == chs.PIECE.KNIGHT:
        return ass.whiteKnight
    elif piece.color == chs.COLOR.WHITE and piece.piece == chs.PIECE.ROOK:
        return ass.whiteRook
    elif piece.color == chs.COLOR.WHITE and piece.piece == chs.PIECE.QUEEN:
        return ass.whiteQueen
    elif piece.color == chs.COLOR.WHITE and piece.piece == chs.PIECE.KING:
        return ass.whiteKing
    elif piece.color == chs.COLOR.BLACK and piece.piece == chs.PIECE.PAWN:
        return ass.blackPawn
    elif piece.color == chs.COLOR.BLACK and piece.piece == chs.PIECE.BISHOP:
        return ass.blackBishop
    elif piece.color == chs.COLOR.BLACK and piece.piece == chs.PIECE.KNIGHT:
        return ass.blackKnight
    elif piece.color == chs.COLOR.BLACK and piece.piece == chs.PIECE.ROOK:
        return ass.blackRook
    elif piece.color == chs.COLOR.BLACK and piece.piece == chs.PIECE.QUEEN:
        return ass.blackQueen
    elif piece.color == chs.COLOR.BLACK and piece.piece == chs.PIECE.KING:
        return ass.blackKing
    else:
        return None


def getAssetForPos(x, y, boardstate):
    piece = chs.getPieceOnCoordinates(x, y, boardstate)
    if piece.piece == chs.PIECE.NONE:
        if (x+y)%2 == 0:
            return ass.whiteSquare
        return ass.blackSquare
    return getAssetFromPiece(piece)

def getBoardString(boardState):
    boardString = "```prolog" + '\n'
    for y in range(8):
        boardString = boardString + yLabels[y]
        for x in range(8):
            boardString = boardString + " " + getAssetForPos(x, y, boardState)
        boardString = boardString + '\n'
    boardString = boardString + "."
    for x in range(8):
        boardString = boardString + " " + xLabels[x]
    boardString = boardString + '\n'
    boardString = boardString + "```"
    return boardString