#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
UE Radiofrequence :
DM Huffman
Compression et decompression via l'arbre de huffman.

@author : Quentin Lieumont
@date : Mar 2019
"""


class Arbre:
    def __init__(self, frequence, gauche, droit):
        """ Construit un Arbre

            frequence: int
            gauche, droit: Arbre
        """
        self.frequence = frequence
        self.gauche = gauche
        self.droit = droit

    def affiche(self, prefixes=['    ']):
        """ Affiche l'arbre """
        print(''.join(prefixes[:-1]) + '|___' + str(self.frequence))
        prefixes.append('|   ')
        self.gauche.affiche(prefixes)
        prefixes.pop()
        prefixes.append('    ')
        self.droit.affiche(prefixes)
        prefixes.pop()
    
    def __add__(self, other):
        return Arbre(self.frequence + other.frequence, self, other)

    def __eq__(self, other):
        """
        egal ou non ?
        :param other:
        :return: Bool
        
        >>> Arbre(1, Feuille(0), Feuille(1)) == Arbre(1, Feuille(0), Feuille(1))
        True
        >>> Arbre(1, Feuille(0), Feuille(1)) == Arbre(1, Feuille(1), Feuille(0))
        False
        """
        if type(other) != type(self):
            return False
        elif self.frequence == other.frequence and self.gauche == other.gauche and self.droit == other.droit:
            return True
        else:
            return False

    def __ne__(self, other):
        """
        pas egal ?
        :param other:
        :return:
        
        >>> Arbre(1, Feuille(0), Feuille(1)) != Arbre(1, Feuille(0), Feuille(1))
        False
        >>> Arbre(1, Feuille(0), Feuille(1)) != Arbre(1, Feuille(1), Feuille(0))
        True
        """
        return not self == other

    def __contains__(self, item):
        """
        pour le if item in Arbre:
        :param item: quelque chose
        :return: bool
        
        >>> Arbre(1, Feuille(0), Feuille(1)) in Arbre(1, Feuille(0), Feuille(1))
        False
        >>> Feuille(0) in Arbre(1, Feuille(0), Feuille(1))
        True
        """
        return item == self.droit or item == self.gauche or item in self.droit or item in self.gauche
    
    def code(self, symb) -> str:
        """
        descend l'arbre pour trouver le code d'une feuille
        :param symb: symbole d'une Feuille
        :return code: str
        
        >>> Arbre(1, Arbre(1, Feuille(0,'A'), Feuille(1,'B')), Arbre(1, Feuille(0,'C'), Feuille(1,'D'))).code('C')
        '10'
        """
        f_type = type(Feuille(0))
        if symb not in self:
            raise "symbole {} n'est pas dans l'arbre {}".format(symb, self)
        code = ""
        selected = self
        while type(selected) != f_type:
            if symb in selected.gauche:
                selected = selected.gauche
                code += "0"
            else:
                selected = selected.droit
                code += "1"
        return code
    
    def table_de_codage(self, symboles) -> dict:
        """
        associe a chaque symbole son code
        :param symboles: liste des symboles
        :return d: dictionnaire des codage
        """
        d = {}
        for s in symboles:
            d[s] = self.code(s)
        return d


class Feuille(Arbre):
    def __init__(self, frequence, symbole = ''):
        """
        Construit une feuille

        frequence: int
        symbole: str
        """
        Arbre.__init__(self, frequence, None, None)
        self.symbole = symbole

    def affiche(self, prefixes=[' '*4]):
        """ Affiche la feuille """
        print("".join(prefixes[:-1]) + '|___' +
              str(self.frequence) +
              '(' + self.symbole + ')')
    
    def __eq__(self, other):
        """
        egal ou non ?
        :param other:
        :return: Bool
        """
        if type(other) != type(self):
            return False
        elif self.frequence == other.frequence and self.symbole == other.symbole:
            return True
        else:
            return False

    def __contains__(self, item):
        return item == self.symbole


#Huffman


class Huffman:
    """ Algorithme de construction de l'arbre de Huffman """
    
    def pop_min(self) -> Feuille:
        """
        trie le tableau
        pop le premier element
        
        :return Feuille: la moins frequente des feuilles
        
        >>> Huffman(frequences('a'*5+'b'*2), debug = True).pop_min() == Feuille(2,'b')
        True
        """
        self.foret.sort(key = lambda x: x.frequence)
        return self.foret.pop(0)

    def fusion(self) -> bool:
        """
        fusionne si possible les deux plus petits arbres
        
        :return bool: fusion possible ?
        """
        if len(self.foret) > 1:
            e1 = self.pop_min()
            e2 = self.pop_min()
            self.foret.append(e1 + e2)
            return True
        else:
            return False

    def arbre(self) -> Arbre:
        """
        Cree un arbre de huffman
        tourne tant que fusion est vrai
        
        :return Arbre: L'arbre cree
        """
        return self.foret[0]

    def affiche(self) -> None:
        """
        affiche l'arbre de huffman
        
        :return None:
        """
        self.arbre().affiche()

    def compresse(self, texte: str) -> str:
        """
        code un texte avec le dictionnaire precedement genere
        
        :param texte: texte a coder
        :return: str
        """
        dico = self.arbre().table_de_codage(self.symboles)
        code = ''
        for car in texte:
            if car not in dico:
                raise "{} not in {}".format(car, dico)
            else:
                code += dico[car]
        return code
    
    def decompresse(self, code: str) -> str:
        """
        decode le code en descendat l'arbre
        thx to SilentGhost pour le dico inverse :
        https://stackoverflow.com/questions/483666/python-reverse-invert-a-mapping
        
        :param code: str
        :return texte: str
        >>> H = Huffman(frequences("ABRACADABRA"))
        >>> H.decompresse("01101110100010101101110")
        'ABRACADABRA'
        """
        dico = self.arbre().table_de_codage(self.symboles)
        inv_dico = {v: k for k, v in dico.items()}
        texte = ""
        
        while code is not "":
            nb = 1
            while code[0:nb] not in inv_dico.keys():
                nb += 1
            texte += inv_dico[code[0:nb]]
            code = code[nb:]
        return texte
    
    def __init__(self, freq, debug = False):
        """
        Constructeur

        :param freq: dictionnaire des fréquences
        :param debug: debug mode
        """
        self.symboles = freq.keys()
        self.foret = [Feuille(freq[symbole], symbole) for symbole in freq.keys()]
        if not debug:
            while self.fusion():
                pass


#Fonctions


def encode(c: str) -> str:
    """
    code un caractere en ascii 8 bit

    :param c: str
    :return: str

    >>> encode('b')
    '01100010'
    """
    return "{:08b}".format(ord(c))


def encode_ascii(txt: str) -> str:
    """
    permet d'encoder en ascii

    :arg txt: str chaine de caracteres a coder
    :return code: str mots binaires joints

    >>> encode_ascii('bonjour')
    '01100010011011110110111001101010011011110111010101110010'
    """
    return ''.join([encode(c) for c in txt])


def frequences(txt: str) -> dict:
    """
    permet d'etablir la frequence de chaque lettre q'une chaine de carracteres

    :param txt: str chaine de carracteres
    :return d: dict dictrionaire des frequences

    >>> frequences('ABRACADABRA') == {'A': 5, 'B': 2, 'R': 2, 'C': 1, 'D': 1}
    True
    """
    d = {}
    for c in txt:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


#Tests pytest


def decorated_test(func):
    def inner(*args, **kwargs):
        before = "\n"*3+"="*10
        print(before, func.__name__, before[::-1])
        res = func(*args, **kwargs)
        return res
    return inner


def _test_dict(dico, func) -> list:
    """
    test une fonction pour chaque element d'un dictionnaire
    
    :param dico: dictionnaire input, expected output
    :param func: fonction a tester
    :return: tableau des resultats des tests
    """
    tab = []
    for key in dico.keys():
        print('Input :', key)
        expected = dico[key]
        result = func(key)
        print('Expected output :', expected)
        print('Returned output :', result)
        tab.append(expected == result)
    return tab


@decorated_test
def test_encode():
    """
    test toutes les lettres de l'alphabet contenues dans le fichier usefull.py
    """
    from usefull import alphabet
    for test in _test_dict(alphabet, encode):
        assert test


@decorated_test
def test_frequences():
    """
    test les combinaisons de str/frequences presentes dans usefull.py
    """
    from usefull import freqTest
    for test in _test_dict(freqTest, frequences):
        assert test


if __name__ == "__main__":
    from test_parsearg import parse_arguments
    from usefull import cmode, dmode
    
    args = parse_arguments()

    Mode = args.Mode
    InputFile = args.InputFile

    config = args.config
    
    output_a = args.AppendOutput
    output_w = args.Output
    
    if Mode.lower() in cmode:
        if config is None:
            config = InputFile
        
        with open(config, 'r') as f:
            h = Huffman(frequences(f.read()))
        with open(InputFile, 'r') as f:
            raw_txt = f.read()
            txt = h.compresse(raw_txt)
        
        print("Le texte a ete compresse avec le facteur suivant : {}\n\n".format(100*len(txt)/(8*len(raw_txt))))
        
    elif Mode.lower() in dmode:
        if config is None:
            raise FileNotFoundError("Comment decoder ce message ?\nUtiliser -c CONFIG\n --help pour plus d'info")
        
        with open(config, 'r') as f:
            h = Huffman(frequences(f.read()))
        with open(InputFile, 'r') as f:
            txt = h.decompresse(f.read())

        print("Le texte a ete decompresse avec succes. Il fait {} caracteres :\n\n".format(len(txt)))
        
    else:
        raise KeyError("Mode must be in {} or in {}".format(cmode, dmode))

    if output_a is not None:
        with open(output_a, 'a') as f:
            f.write(txt)
        print("Ecriture a la suite reussie")
    elif output_w is not None:
        with open(output_w, 'w') as f:
            f.write(txt)
        print("Ecrasement effectué")
    else:
        print(txt)
