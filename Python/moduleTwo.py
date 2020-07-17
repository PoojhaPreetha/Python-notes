def isVowel(p):
    if len(p)>1:
        return "Only one char is allowed"
    p=p.upper()
    if p in ["A","E","I","O","U"]:
        return "Its a vowel"
    else:
        return "Its not a vowel"
