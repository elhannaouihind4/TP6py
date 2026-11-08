from dataclasses import dataclass, asdict, replace
import json


@dataclass(frozen=True, slots=True)
class Livre:

    titre: str
    auteur: str
    annee: int
    prix: float

    # Convertir le livre en JSON
    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    # Créer un nouveau livre avec un prix réduit
    def promo(self, prix_reduit):
        return replace(self, prix=prix_reduit)

    # Charger un livre depuis JSON
    @classmethod
    def from_json(cls, chaine):
        donnees = json.loads(chaine)
        return cls(**donnees)

    # Comparer deux livres selon leur prix
    def __lt__(self, autre):
        return self.prix < autre.prix



livre1 = Livre("1984", "George Orwell", 1949, 9.90)

# Affichage JSON
print(" Livre en JSON :")
print(livre1.to_json())

# Promotion
livre2 = livre1.promo(7.50)

print("\n Livre après promotion :")
print(livre2)

# Afficher le livre original
print("\n Livre original :")
print(livre1)

# Chargement depuis JSON
livre3 = Livre.from_json(livre1.to_json())

print("\n4. Livre chargé depuis JSON :")
print(livre3)

# Comparaison des prix
print("\n Comparaison des prix :")
print(livre2 < livre1)