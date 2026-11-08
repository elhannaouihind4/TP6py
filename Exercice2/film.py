from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True, slots=True)
class Film:

    titre: str
    realisateur: str
    annee: int
    note: float

    
    def __post_init__(self):

        if not isinstance(self.titre, str) or not self.titre.strip():
            raise ValueError("Titre invalide.")

        if not isinstance(self.realisateur, str) or not self.realisateur.strip():
            raise ValueError("Réalisateur invalide.")

        if type(self.annee) != int or self.annee <= 0:
            raise ValueError("Année invalide.")

        if not isinstance(self.note, (int, float)) or isinstance(self.note, bool):
            raise ValueError("La note doit être numérique.")

        if self.note < 0 or self.note > 10:
            raise ValueError("La note doit être entre 0 et 10.")

    # Convertir le film en JSON
    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    # Vérifier si le film est un classique
    def est_classique(self):
        return self.annee < 2000

    # Charger un film depuis JSON
    @classmethod
    def from_json(cls, chaine):
        donnees = json.loads(chaine)
        return cls(**donnees)

    # Comparer deux films selon leur note
    def __lt__(self, autre):
        return self.note < autre.note



film1 = Film("Titanic", "James Cameron", 1997, 9.5)
film2 = Film("Avatar", "James Cameron", 2009, 8.5)

print(" Informations du film :")
print(film1)

print("\n Film en JSON :")
print(film1.to_json())

print("\n Film classique :")
print(film1.est_classique())

print("\n Chargement depuis JSON :")
film3 = Film.from_json(film1.to_json())
print(film3)

print("\n Comparaison des notes :")
print(film1 < film2)