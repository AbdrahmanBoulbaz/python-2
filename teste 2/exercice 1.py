def inverser_case(lettre):
    if lettre.islower():
        return lettre.upper()
    elif lettre.isupper():
        return lettre.lower()
    else:
        return lettre
texte = input("enter une phrase  ")
nouveau_texte = ''.join(inverser_case(lettre) for lettre in texte)
print(nouveau_texte)
