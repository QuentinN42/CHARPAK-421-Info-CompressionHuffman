from huffman import encode, frequences

#Tests pytest


def decorated_test(func):
    def inner(*args, **kwargs):
        before = "\n" * 3 + "=" * 10
        print(before, func.__name__, before[::-1])
        res = func(*args, **kwargs)
        return res
    
    return inner


def _test_dict(dico, func, p) -> list:
    """
    test une fonction pour chaque element d'un dictionnaire

    :param dico: dictionnaire input, expected output
    :param func: fonction a tester
    :return: tableau des resultats des tests
    """
    tab = []
    for key in dico.keys():
        expected = dico[key]
        result = func(key)
        if p:
            print('Input :', key)
            print('Expected output :', expected)
            print('Returned output :', result)
        tab.append(expected == result)
    return tab


@decorated_test
def test_encode(p = False):
    """
    test toutes les lettres de l'alphabet contenues dans le fichier usefull.py
    """
    from usefull import alphabet
    for test in _test_dict(alphabet, encode, p):
        assert test


@decorated_test
def test_frequences(p = True):
    """
    test les combinaisons de str/frequences presentes dans usefull.py
    """
    from usefull import freqTest
    for test in _test_dict(freqTest, frequences, p):
        assert test

