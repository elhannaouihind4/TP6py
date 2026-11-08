import unittest
from film import Film


class TestFilm(unittest.TestCase):

    # Tester la création d'un film
    def test_creation(self):
        film = Film("Titanic", "James Cameron", 1997, 9.5)
        self.assertEqual(film.titre, "Titanic")

    # Tester le film classique
    def test_classique(self):
        film = Film("Titanic", "James Cameron", 1997, 9.5)
        self.assertTrue(film.est_classique())

    # Tester un film récent
    def test_recent(self):
        film = Film("Avatar", "James Cameron", 2009, 8.5)
        self.assertFalse(film.est_classique())

    # Tester la conversion JSON
    def test_json(self):
        film = Film("Titanic", "James Cameron", 1997, 9.5)
        donnees = film.to_json()
        self.assertIn("Titanic", donnees)

    # Tester le chargement JSON
    def test_from_json(self):
        film = Film("Titanic", "James Cameron", 1997, 9.5)
        nouveau = Film.from_json(film.to_json())
        self.assertEqual(film, nouveau)

    # Tester une note invalide
    def test_note_invalide(self):
        with self.assertRaises(ValueError):
            Film("Titanic", "James Cameron", 1997, 15)

    # Tester un titre vide
    def test_titre_vide(self):
        with self.assertRaises(ValueError):
            Film("", "James Cameron", 1997, 9.5)

    # Tester une année invalide
    def test_annee_invalide(self):
        with self.assertRaises(ValueError):
            Film("Titanic", "James Cameron", -1997, 9.5)

    # Tester la comparaison
    def test_comparaison(self):
        film1 = Film("Titanic", "James Cameron", 1997, 9.5)
        film2 = Film("Avatar", "James Cameron", 2009, 8.5)
        self.assertFalse(film1 < film2)


if __name__ == "__main__":
    unittest.main()