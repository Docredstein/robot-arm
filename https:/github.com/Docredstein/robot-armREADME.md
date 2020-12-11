# robot-arm
c'est un programme pour controller un bras robotique à 6 servos 
--------------------------nécessite--------------------------------------
python 3.6 ou supérieur
la librairie Serial et TKinter
--------------------------utilisation------------------------------------
programmez l'arduino avec le programme "6ServoArm.ino"
lancez le programme "bras gui.py", tapez "n", rentrez les différents paramètres (2 000 000 de bauds et 0 ms d'écart entre chaque paquet par défauts) 
ensuite chaque slider contrôle un servo
--------------------------explication------------------------------------
le programme arduino est fait pour qu'il attende 6 bytes qui représentent chacun la position en degré d'un servo.
















testé sur : https://www.gotronic.fr/art-bras-robotique-joy-it-robot02-26637.htm 
