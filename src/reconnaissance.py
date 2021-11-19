from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    for model in liste_modeles:
        model = model.binarisation(S)
        model = model.localisation()
        
    image = image.binarisation(S)
    image = image.localisation()
    
    simis = []
    for model in liste_modeles:
        simis.append(image.similitude(model))
        
    best_ind = 0
    best = 0
    for i, simi in enumerate(simis):
        if simi > best:
            best_ind = i
            best = simi
            
    return best_ind

