'''
File: main.py
Created Date: Friday August 27th 2021 - 02:35pm
Author: Ammar Mian
Contact: ammar.mian@univ-smb.fr
-----
Last Modified: Mon Aug 30 2021
Modified By: Ammar Mian
-----
Copyright (c) 2021 Université Savoie Mont-Blanc
'''
import matplotlib.pyplot as plt
from image import Image
from reconnaissance import reconnaissance_chiffre, lecture_modeles

if __name__ == '__main__':

    # Variables utiles
    path_to_assets = '../assets/'
    plt.ion()  # Mode interactif de matplotlib our ne pas bloquer l'éxécutions lorsque l'on fait display

    # ==============================================================================
    # Lecture image et affichage
    # ==============================================================================
    image = Image()
    image.load(path_to_assets + 'test1.JPG')
    image.display("Exemple d'image")

    # ==============================================================================
    # Binarisation de l'image et affichage
    # ==============================================================================
    S = 70
    image_binarisee = image.binarisation(S)
    image_binarisee.display("Image binarisee")

    # ==============================================================================
    # Localisation de l'image et affichage
    # ==============================================================================
    image_localisee = image_binarisee.localisation()
    image_localisee.display("Image localisee")

    # ==============================================================================
    # Redimensionnement de l'image et affichage
    # ==============================================================================
    image_resizee = image_localisee.resize(100, 500)
    image_resizee.display("Image redimensionee")

    # ==============================================================================
    # Lecture modeles et reconnaissance
    # ==============================================================================
    liste_modeles = lecture_modeles(path_to_assets)
    chiffre = reconnaissance_chiffre(image, liste_modeles, 255)
    print("Le chiffre reconnu est : ", chiffre)

    fichiers = [('test1.jpg', 4), ('test2.jpg', 1), ('test3.jpg', 2), ('test4.jpg', 2), ('test5.jpg', 2),
                ('test6.jpg', 4), ('test7.jpg', 5),
                ('test10.jpg', 6)]
    liste_imgs = []
    for fichier, nbr in fichiers:
        model = Image()
        model.load(path_to_assets + fichier)
        liste_imgs.append((model, nbr))

    res = []
    for s in range(0, 256, 10):
        l = []
        for img, nbr in liste_imgs:
            chiffre = reconnaissance_chiffre(image, liste_modeles, 255)
            l.append(chiffre == nbr)
        res.append(l)

    res_sim = []
    for s in res:
        res_sim.append(sum(s))

    print(res_sim)
