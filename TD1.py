import numpy as np

class MotLong:

    def __init__(self):
        self.score_ = {"A":1,"E":1,"I":1,"L":1,"N":1,"O":1,"R":1,"S":1,"T":1,"U":1,"D":2,"G":2,"M":2,"B":3,"C":3,"P":3,"F":4,"H":4,"V":4,"J":8,"Q":8,"K":10,"W":10,"X":10,"Y":10,"Z":10}


    def score(self,lettre):
        return self.score_[lettre.upper()]

    def mot_possibles(self,tirage,lexique):
        joker = False
        if "?" in tirage:
            joker = True
        L = []
        tirage_copy = tirage.copy()
        for mot in lexique:
            valide = True
            for lettre in mot:
                if lettre not in tirage_copy :
                    if joker:
                        joker = False
                    else:
                        valide = False
                else:
                    tirage_copy.remove(lettre)
            if valide == True:
                L.append(mot)
            tirage_copy = tirage.copy()
        print(L)
        return L

    def mot_possibles2(self,tirage,lexique):
        L = []
        tirage_copy = tirage.copy()
        for mot in lexique:
            joker = False
            if "?" in tirage:
                joker = True
            valide = True
            score_mot = 0
            for lettre in mot:
                if lettre not in tirage_copy :
                    if joker:
                        joker = False
                    else:
                        valide = False
                else:
                    tirage_copy.remove(lettre)
                    score_mot+=self.score(lettre.upper())
            if valide == True:
                L.append([mot,score_mot])
            tirage_copy = tirage.copy()
        print(L)
        return np.array(L)

    def ex4(self,tirage,lexique):
        mots_possibles = self.mot_possibles2(tirage, lexique)
        mot_choisi = mots_possibles[0,0]
        score_mot_choisi = mots_possibles[0,1]
        for mot in mots_possibles:
            if mot[1]>score_mot_choisi:
                score_mot_choisi = mot[1]
                mot_choisi = mot[0]
        return mot_choisi,score_mot_choisi

    def ex1(self,tirage,lexique):
        mots_possibles = self.mot_possibles(tirage,lexique)
        mot_choisi = mots_possibles[0]
        for mot in mots_possibles:
            if len(mot)>len(mot_choisi):
                mot_choisi=mot
        return mot_choisi

    def score_mot(self,mot):
        score = 0
        for lettre in mot:
            score += self.score(lettre)
        return score

    def ex2(self,tirage,lexique):
        mots_possibles = self.mot_possibles(tirage,lexique)
        mot_choisi = mots_possibles[0]
        score_mot_choisi = self.score_mot(mot_choisi)
        for mot in mots_possibles:
            score_mot = self.score_mot(mot)
            if score_mot > score_mot_choisi:
                mot_choisi = mot
                score_mot_choisi = score_mot
        return [mot_choisi,score_mot_choisi]


if __name__ == "__main__":
    L = open("mots.sansaccent.txt", "r").read().splitlines()
    motLong = MotLong()
    tirage = ['a','b',"c","?"]
    print(motLong.ex1(tirage,L))
    print(motLong.score_mot("cab"))
    print(motLong.ex2(tirage,L))
    print(motLong.ex4(tirage, L))
    #utiliser 1 joker



