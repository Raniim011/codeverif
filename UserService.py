# UserService.py - Fichier de test pour DevGuard AI

import json
import sqlite3

class UserService:
    def __init__(self):
        # Violation DIP : instanciation directe en dur de la base de données
        self.db_path = "users.db"
        self.current_user = None

    def register_user(self, username, email, password):
        # Violation SRP : La classe gère à la fois la logique métier, la validation, le hachage et la persistance SQL
        if not username or "@" not in email:
            print("Erreur : Données invalides")
            return False
        
        # Connexion directe à la base de données (couplage fort)
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, email TEXT, password TEXT)")
            # Faille potentielle : pas de hachage de mot de passe, vulnérable aux injections SQL si mal nettoyé
            query = f"INSERT INTO users (username, email, password) VALUES ('{username}', '{email}', '{password}')"
            cursor.execute(query)
            connection.commit()
            print(f"Utilisateur {username} enregistré avec succès !")
            return True
        except Exception as e:
            # Gestion d'erreur trop générique
            print(f une erreur est survenue: {e})
            return False
        finally:
            connection.close()

    def send_welcome_email(self, email):
        # Violation SRP : L'envoi d'e-mail n'a rien à faire dans une classe de gestion de données utilisateur
        print(f"Envoi d'un e-mail de bienvenue à {email}...")
        # Simulation d'envoi...
        return True
