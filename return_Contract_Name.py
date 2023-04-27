
def returnName(longstring):
    index = longstring.index('contract')
    Bracket_index = longstring.index('{')
    word = longstring[index+8:Bracket_index].strip()

    return word
