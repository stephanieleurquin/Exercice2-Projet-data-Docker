# Mini Projet Docker Data

Ce projet montre comment exécuter un script Python simple avec Docker.  
Le script crée un petit dataset et calcule le salaire moyen. Ce projet est adapté pour un mini-exercice en data.

---

## Contenu du projet

- `exercice.py` : script Python qui crée un dataset et calcule le salaire moyen.  
- `Dockerfile` : fichier pour construire l’image Docker qui exécute le script.  
- `README.md` : ce fichier d’instructions.

---

## Prérequis

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installé et lancé sur votre machine.  
- Git (si vous souhaitez cloner le projet depuis GitHub).  

---

## Installation et utilisation

### Option 1 : Cloner depuis GitHub

bash
git clone https://github.com/stephanieleurquin/Mini-projet-Docker-Data.git
cd Mini-projet-Docker-Data

## Option 2 : Construire l’image Docker
Dans le projet excécuter :
docker build -t mini-docker-data .

##Option 3 : Lancer le script dans Docker
docker run --rm mini-docker-data

##Le script affiche:
Dataset :
       Nom  Age  Salaire
0    Alice   25    50000
1      Bob   30    60000
2  Charlie   35    70000
3    David   40    80000

Salaire moyen : 65000.0


```bash
git clone https://github.com/stephanieleurquin/Mini-projet-Docker-Data.git
cd Mini-projet-Docker-Data
