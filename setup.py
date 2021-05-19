import discord
def resetBoard():  
    string = ""
    for x in range(4):
        string = "x o x o x o x o \n" + "o x o x o x o x \n"
    return string