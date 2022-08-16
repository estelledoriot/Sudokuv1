######################
# grille et correction
######################

# grille du sudoku
grille1 = [[7, 0, 8, 0, 1, 9, 5, 0, 0], 
           [0, 9, 3, 0, 7, 6, 8, 0, 0],
           [0, 5, 0, 3, 0, 0, 0, 0, 9], 
           [0, 0, 0, 0, 4, 1, 0, 6, 7],
           [0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [9, 4, 0, 7, 6, 0, 0, 0, 0],
           [2, 0, 0, 0, 0, 5, 0, 8, 0], 
           [0, 0, 9, 6, 3, 0, 4, 1, 0],
           [0, 0, 6, 4, 2, 0, 9, 0, 5]]

# correction du sudoku
correction = [[7, 6, 8, 2, 1, 9, 5, 4, 3], 
              [4, 9, 3, 5, 7, 6, 8, 2, 1],
              [1, 5, 2, 3, 8, 4, 6, 7, 9], 
              [3, 8, 5, 9, 4, 1, 2, 6, 7],
              [6, 2, 7, 8, 5, 3, 1, 9, 4], 
              [9, 4, 1, 7, 6, 2, 3, 5, 8],
              [2, 3, 4, 1, 9, 5, 7, 8, 6], 
              [5, 7, 9, 6, 3, 8, 4, 1, 2],
              [8, 1, 6, 4, 2, 7, 9, 3, 5]]

###########
# affichage
###########

def affiche(grille : list):
    """affiche une grille de sudoku avec les délimitations des carrés

    Args:
        grille (list): une grille de sudoku
    """
    for i in range(9):
        if i % 3 == 0:
            print("-" * 25)
        for j in range(9):
            if j % 3 == 0:
                print("|", end=' ')
            print(grille[i][j], end=' ')
        print("|")
    print("-" * 25)

###########
# fonctions
###########

def finie(grille : list) -> bool:
    """détermine si une grille de sudoku est finie (il ne reste plus de 0)

    Args:
        grille (list): une grille de sudoku

    Returns:
        bool: True si la grille est finie
    """
    for i in range(9):
        for j in range(9):
            if grille[i][j] == 0:
                return False
    return True

assert finie(correction)
assert not finie(grille1)

def cherche_ligne(grille : list, ligne : int, chiffre : int) -> bool:
    """teste si un chiffre est présente dans une ligne 

    Args:
        grille (list): une grille de sudoku
        ligne (int): numéro de la ligne
        chiffre (int): chiffre à rechercher

    Returns:
        bool: True si chiffre est dans la ligne n°ligne de grille
    """
    trouvé = False
    for j in range(9):
        if grille[ligne][j] == chiffre:
            trouvé = True
    return trouvé

assert cherche_ligne(grille1, 0, 8)
assert not cherche_ligne(grille1, 0, 2)

def test_lignes(grille : list) -> bool:
    """teste si chaque ligne est correctement remplie (chaque chiffre entre 1 et 9 est présent une fois)

    Args:
        grille (list): une grille de sudoku

    Returns:
        bool: True si toutes les lignes sont correctement remplies
    """
    correct = True
    for ligne in range(9):
        for chiffre in range(1, 10):
            if not cherche_ligne(grille, ligne, chiffre):
                correct = False
    return correct

assert test_lignes(correction)
assert not test_lignes(grille1)

def cherche_colonne(grille : list, colonne : int, chiffre : int) -> bool:
    """teste si un chiffre est présente dans une colonne 

    Args:
        grille (list): une grille de sudoku
        colonne (int): numéro de la colonne
        chiffre (int): chiffre à rechercher

    Returns:
        bool: True si chiffre est dans la colonne n°colonne de grille
    """
    trouvé = False
    for i in range(9): 
        if grille[i][colonne] == chiffre:
            trouvé = True
    return trouvé

assert cherche_colonne(grille1, 0, 2)
assert not cherche_colonne(grille1, 0, 1)

def test_colonnes(grille : list) -> bool:
    """teste si chaque colonne est correctement remplie (chaque chiffre entre 1 et 9 est présent une fois)

    Args:
        grille (list): une grille de sudoku

    Returns:
        bool: True si toutes les colonnes sont correctement remplies
    """
    correct = True
    for colonne in range(9): 
        for chiffre in range(1, 10):
            if not cherche_colonne(grille, colonne, chiffre):
                correct = False
    return correct  

assert test_colonnes(correction)
assert not test_colonnes(grille1)

def cherche_carré(grille : list, gligne : int, gcolonne : int, chiffre : int) -> bool:
    """teste si un chiffre est présente dans un carré. Chaque carré est repéré par deux coordonnées, sa grande ligne et sa grande colonne 

    Args:
        grille (list): une grille de sudoku
        gligne (int): numéro de la grande ligne (du carré)
        gcolonne (int): numéro de la grande colonne (du carré)
        chiffre (int): chiffre à rechercher

    Returns:
        bool: True si chiffre est dans le carré
    """
    trouvé = False
    for i in range(3 * gligne, 3 * gligne + 3): 
        for j in range(3 * gcolonne, 3 * gcolonne + 3):
            if grille[i][j] == chiffre:
                trouvé = True
    return(trouvé)    

assert cherche_carré(grille1, 1, 1, 6)
assert not cherche_carré(grille1, 1, 1, 5)

def test_carrés(grille : list) -> bool:
    """teste si chaque carré est correctement rempli (chaque chiffre entre 1 et 9 est présent une fois)

    Args:
        grille (list): une grille de sudoku

    Returns:
        bool: True si tous les carrés sont correctement remplis
    """
    correct = True
    for gligne in range (3): 
        for gcolonne in range (3): 
            for chiffre in range(1, 10): 
                if not cherche_carré(grille, gligne, gcolonne, chiffre):
                    correct = False
    return correct  

assert test_carrés(correction)
assert not test_carrés(grille1)

def verification(grille : list) -> bool:
    """vérifie si une grille de sudoku est correctement remplie (si chaque chiffre entre 1 et 9 est présent exactement une fois dans chaque ligne, chaque colonne et chaque carré)

    Args:
        grille (list): une grille de sudoku

    Returns:
        bool: True si la grille est corrrectement remplie
    """
    return test_lignes(grille) and test_colonnes(grille) and test_carrés(grille)

assert verification(correction)
assert not verification(grille1)

##################
# partie de sudoku
##################

def jeu(grille : list):
    """crée un jeu de sudoku dans la console

    Args:
        grille (list): une grille de sudoku
    """
    
    print("Bienvenue dans le jeu de SUDOKU")
    print("-------------------------------")
    print()
    print("Voici la grille à remplir :")
    print()
    affiche(grille)
    print()

    while not finie(grille):
        ligne = input("quelle ligne veux-tu remplir ?")
        colonne = input("quelle colonne veut-tu remplir ?")
        chiffre = input("quel chiffre veux-tu mettre ?")
        if ligne not in "123456789":
            print("Veuillez donner un numéro de ligne entre 1 et 9")
        elif colonne not in "123456789":
            print("Veuillez donner un numéro de colonne entre 1 et 9")
        elif chiffre not in "123456789":
            print("Veuillez donner un chiffre entre 1 et 9")
        elif grille[int(ligne)-1][int(colonne)-1] != 0:
            print("La case est déjà remplie")
        else:
            grille[int(ligne)-1][int(colonne)-1] = int(chiffre)

        affiche(grille)
        print()

jeu(grille1)