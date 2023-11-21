from blog.models import Equipement, Character
from django.db import Error

def move(id_character,id_lieu):

    try:
        chara = Character.objects.get(id_character = id_character)
        try:
            but = Equipement.objects.get(id_equip=id_lieu)

            if(but.disponibilite == 'disponible'):
                if((but.id_equip == 'marais' and chara.type == 'marais') or (but.id_equip == 'konoha' and chara.type == 'ninja') or (but.id_equip == 'zone51' and chara.type == 'anomalie')):
                    if(chara.etat == 'paisible' or chara.etat == 'repos'):
                        chara.lieu.disponibilite = 'disponible'
                        chara.lieu.save()
                        chara.lieu = but
                        chara.etat = 'repos'
                        chara.save()
                        return ""
                    else:
                        return "Ce shrek risque de perturber la paix de ce lieu..."
                elif(but.id_equip == 'zone51' or but.id_equip == 'marais' or but.id_equip == 'konoha'):
                    return "Ce shrek ne peut pas aller là bas..."
                else:
                    chara.lieu.disponibilite='disponible'
                    chara.lieu.save()
                    chara.lieu=but
                    if(but.id_equip == 'psy' or but.id_equip == 'chasse'):
                        chara.etat='paisible'
                        but.disponibilite = 'occupe'
                    if(but.id_equip == 'champ_de_bataille'):
                        chara.etat='frenesie'
                    chara.save()
                    but.save()
                    return ""
            else:
                return "Ce lieu est déjà occupé... "

        except Error:
            return "Ce lieu n'apparait pas sur la carte..."

    except Error:
        return "Ce shrek n'est pas répertorié..."
