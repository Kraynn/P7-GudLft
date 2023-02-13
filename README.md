# Güdlft - Projet #11
__________________________

Le programme a pour objet la création d'une plateforme de réservation de compétitions sportives.
Un utilisateur peut à ses fins:

- Se connecter selon son club et voir le solde des points chaque club.
- Echanger les points de son club pour inscrire un athlète à une compétition.

______________
HOW TO INSTALL
--------------

Importation des scripts:
---------------------------

Télécharger et extaire le contenu du repertoire https://github.com/Kraynn/P7-GudLft/ dans le répertoire local. 
> 
Puis déplacer le contenu dans le repertoire local voulu.


Ou cloner le répertoire via github en utilisant la commande:
> git clone github.com/Kraynn/P7-GudLft/


__________________________________________________________
Création de l'environnement virtuel:
------------------------------------
Exectuer les commandes suivantes dans l'invité de commande au sein du répertoire local voulu:
>
>python -m venv gudlft

>gudlft\Scripts\activate.bat

>pip install -r requirements.txt

___________________________________________________



Lancer le serveur :
----------------------

A partir de l'environnement virtuel créé, exécuter les commandes suivante:
>
>set FLASK_APP=server.py
> flask run


Lancer les tests :
----------------------

Executer les commandes suivantes:
>
Tests avec pytest:
>
>pytest tests\

Coverage test:
>
>coverage run -m pytest
>coverage html

Locust stress test:
>
> cd tests\performance_test
> locust -f locust.py


***************************








