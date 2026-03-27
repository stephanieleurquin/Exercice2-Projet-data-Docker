# exercice2.py
import pandas as pd

# Création du dataset
data = {
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'Salaire': [50000, 60000, 70000, 80000, 65000]
}

df = pd.DataFrame(data)

# Afficher le dataset complet
print("Dataset complet :")
print(df)

# Calculer l'âge moyen
print("\nÂge moyen :", df['Age'].mean())

# Filtrer les salariés avec un salaire supérieur à 60000
high_salary = df[df['Salaire'] > 60000]
print("\nSalariés avec salaire > 60000 :")
print(high_salary)