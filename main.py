#### Fonction secondaire

"""cette fonction permet de savoir si un mot ou une phrase est un palindrome"""
def ispalindrome(p):
    """cette fonction permet de savoir si un mot ou une phrase est un palindrome"""
    p=str.lower(p)
    ent = "àçéèëêiôù-'^!§:/;.,?&#([-|_)]=)"
    sor = "aceeeeiou                      "
    trans = str.maketrans(ent,sor)
    mot = p.translate(trans)
    motsansaccent = mot.replace(" ", "")
    for i in range (len(motsansaccent)//2):
        if motsansaccent[i]!=motsansaccent[-i-1]:
            return False
    return True
#### Fonction principale

def main():
    """cette fonction principale permet d'effectuer des appels de la fonction ispalindrome"""

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
