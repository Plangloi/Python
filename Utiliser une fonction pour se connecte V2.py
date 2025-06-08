# Utiliser une fonction pour se connecter
import mysql.connector
from mysql.connector import Error

# Fonction de connexion
def maConnexion(hostname, compte, motDePasse, db):
    connexion = None
    try:
        connexion = mysql.connector.connect(
            host=hostname,
            user=compte,
            passwd=motDePasse,
            database= db
        )
        print('Connexion établie !! ')
        return connexion
    except Error as err:
        print(f"Erreur de connexion: '{err}'")
        return None
##############################################################

# Fonction pour exécuter la requête
def maRequete(connexion, requete):
    try:
        monCurseur = connexion.cursor()  # ou dictionary=True
        monCurseur.execute(requete)
        employes = monCurseur.fetchall()
        monCurseur.close()
        return employes
    except Error as err:
        print(f"Erreur lors de l'exécution de la requête: '{err}'")
        return None

# Mes paramètres
hostname = '127.0.0.1:3333'
compte = 'miloud'
motDePasse = 'miloud'
db = 'db1'

# Appel de la 1ere fonction puis la 2e fonction
connexion = maConnexion(hostname, compte, motDePasse, db)
if connexion:
    req = 'SELECT * FROM employes'
    EMP = maRequete(connexion, req)
    if EMP:
        for empl in EMP:
            print(empl)
    connexion.close()
else:
    print("Impossible d'établir la connexion à la base de données.")