import assets
def resetBoard():  
    string = ""
    for x in range(4):
        string += assets.checkerBoard + assets.checkerBoard +  assets.checkerBoard + assets.checkerBoard + "\n"
    return string

print(resetBoard())