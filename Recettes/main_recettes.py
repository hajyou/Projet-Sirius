#coding:utf-8

import sqlite3
import os
import time

boucles1 = True

while boucles1 == True:
    log = "test"
    login = input("Entrez votre mot de passe \n>>")
    if login != log:
        print("Ce n'est pas le bon mot de passe !")
        time.sleep(2)
        continue
    else:
        pass

    print("\n-------------- Version 1.0 --------------")
    print("[SYSTEM Y.H ] : Programme (Recette) lancé !")
    print("_________________________________________\n")
    boucles = True
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()

    while boucles == True:

        new_values = (time.strftime("%d/%m/%Y"), input("\nEntrer votre désignation \n>>"), float(input("\nEntrer vos revenues \n>>")))

        cursor.execute('INSERT INTO tt_donnees_r VALUES(?, ?, ?)', new_values)
        connection.commit()
        req2 = cursor.execute('SELECT * FROM tt_donnees_r')
        print("\n_________Base de données__________\n")
        for row in req2.fetchall():
            print(row)
            print("\n__________________________________\n")
        demande = input("Voulez-vous |nettoyer| votre base de données ? o/n \n>>")
        if demande == "o":
            verif = input("Etes-vous sûrs de vouloir nettoyer votre base de données ? o/n ?\ncela effacera toutes les données !\n>>")
            while 1:    
                if verif == 'o':
                    req = 'DELETE FROM tt_donnees_r'
                    cursor.execute(req)
                    connection.commit()
                    time.sleep(1)
                    print("Votre base de données a bien été nettoyer .. \n")
                    print("\n____________________________ Base de données _____________________________\n")
                    print("\n____________  Vide (Tapez Ctrl + z + entrer pour quitter !)  _____________\n")
                    time.sleep(2)
                    break
                    while 1:   
                        mess2 = input("Avez-vous d'autres données ? y/n\n>>")
                        if mess2 == 'y':
                            boucles = True
                            break
                        elif mess2 == 'n':
                            print("Fermeture en cours ...")
                            time.sleep(2)
                            connection.close()
                            boucles1 = False
                            break
                        else:
                            print("Vous devez soit confirmer par 'y' pour oui soit par 'n' pour non")
                            continue
                elif verif == 'n':
                    break
                else:
                    print("Vous vous étes surment tromper retaper soit 'n' pour non soit 'o' pour oui")
                    continue
        else:
            while 1:   
                mess = input("Avez-vous d'autres données ? y/n")
                if mess == 'y':
                    boucles = True
                    break
                elif mess == 'n':
                    print("Fermeture en cours ...")
                    time.sleep(2)
                    connection.close()
                    boucles1 = False
                    break
                else:
                    print("Vous devez soit confirmer par 'y' pour oui soit par 'n' pour non")
                    continue


os.system('pause')
