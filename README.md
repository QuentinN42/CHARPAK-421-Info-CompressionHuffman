# Compression Huffman
DM S4 Radiofrequence \
Institut Villebon Georges Charpak


#### Utitlisation du programe
Le programme s'execute de la maniere suivante : `python Base.py ARGS args_optionnels`
* Arguments
    * Mode : `C` pour coder un texte et `D` pour le décoder.
    * Input : Le fichier à coder/décoder.
* Arguments optionnels
    * Help `--help` : Affiche l'aide.
    * Version `--version` Affiche la version du programme.
    * Configuration `--config` : Fichier de configuration des frequences.\
    Obligatoire pour le decodage de fichier.
    * Sortie : Si aucun de ces arguments n'est appellé, le script va print la sortie.
        * `-o` : Ecrase le fichier de sortie.
        * `-oa` : Ecrit a la suite du fichier de sortie.


#### Utilisation de codes externes :
Inversion de dictionnaire : [Stack overflow : 483666][483666] \
Parseur : [Stack overflow : 28479543][28479543]






[483666]: https://stackoverflow.com/questions/483666/python-reverse-invert-a-mapping
[28479543]: https://stackoverflow.com/questions/28479543/run-python-script-with-some-of-the-argument-that-are-optional