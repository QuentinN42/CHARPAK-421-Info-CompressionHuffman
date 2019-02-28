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


class Feuille(Arbre):
    def __init__(self, frequence, symbole):
        """ Construit une feuille

            frequence: int
            symbole: str
        """
        Arbre.__init__(self, frequence, None, None)
        self.symbole = symbole

    def affiche(self, prefixes=['    ']):
        """ Affiche la feuille """
        print("".join(prefixes[:-1]) + '|___' +
              str(self.frequence) +
              '(' + self.symbole + ')')

class Huffman:
    """ Algorithme de construction de l'arbre de Huffman """
    def __init__(self, frequences):
        """ Constructeur

            frequences: dictionnaire des fréquences
        """
        self.foret = []

def encode(c: str) -> str:
    """
    code un caractere en ascii 8 bit

    :param c: str
    :return: str

    >>> encode('b')
    '01100010'
    """
    return "{:08b}".format(ord(c))

def encode_ascii(txt):
    """
    permet d'encoder en ascii

    :arg txt: str chaine de caracteres a coder
    :return code: str mots binaires joints

    >>> encode_ascii('bonjour')
    '01100010011011110110111001101010011011110111010101110010'
    """
    return ''.join([encode(c) for c in txt])


def frequences(txt : str) -> dict:
    """
    permet d'etablir la frequence de chaque lettre q'une chaine de carracteres
    :param txt: str chaine de carracteres
    :return d: dict dictrionaire des frequences
    >>> frequences('ABRACADABRA')
    {'A': 5, 'B': 2, 'R': 2, 'C': 1, 'D': 1}
    """
    d = {}
    for c in txt:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


if __name__ == "__main__":
    A = Arbre(18,
              Arbre(8,
                    Arbre(3,
                          Feuille(1, 'd'),
                          Feuille(2, 'c')),
                    Feuille(5, 'b')),
              Feuille(10, 'a'))
    A.affiche()

