import assets
def resetBoard():  
    string = ""
    for x in range(4):
        string += assets.blackSquare + assets.whiteSquare +  assets.blackSquare + assets.whiteSquare +  assets.blackSquare + assets.whiteSquare +  assets.blackSquare + assets.whiteSquare  + "\n" +
        assets.whiteSquare +  assets.blackSquare + assets.whiteSquare +  assets.blackSquare + assets.whiteSquare +  assets.blackSquare + assets.whiteSquare  + assets.blackSquare
    return string

print(resetBoard())
