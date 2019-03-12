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
    def __init__(self, freq):
        """ Constructeur

            freq: dictionnaire des fréquences
        """
        print(freq)
        self.foret = []


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


def encode_ascii(txt):
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


def _test_dict(dico,func) -> list:
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
    A = Arbre(18,
              Arbre(8,
                    Arbre(3,
                          Feuille(1, 'd'),
                          Feuille(2, 'c')),
                    Feuille(5, 'b')),
              Feuille(10, 'a'))
    A.affiche()
