Le but du code est de calculer les nombres de la duration de déplacement augmenté par un quart d'heure par utilisateurs membre et nonmembre.

Commande pour executer ce programme:
!python PMV_BIXI_Duration.py data/2017 > output_PMV_BIXI_duration.txt

Chaque ligne dans le output fichier denote
[nombreQuartheure,membre/nonMembre] nombreDeplacement
par exemple: [2, 0]	74105 
Ça veut dire que 74105 déolacements sont fait pendant 2017 par non membres dont les durations de déplacement sont entre 30mins et 45 mins.