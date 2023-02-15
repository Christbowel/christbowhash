import pyfiglet
import hashlib
from termcolor import colored

#Banner

ascii_text = pyfiglet.figlet_format("christbowHash", font="starwars")
ascii_text += "\n\033[38;2;255;153;51m\033[2mby christbowel\033[0m"
print(ascii_text)


def crack_hash(hash_value, wordlist_path, hash_type, verbose):
 
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        num_passwords = sum(1 for line in f)
        f.seek(0)

        print(colored(f"Bruteforcing en cours pour le hash {hash_value} (type de hachage: {hash_type})...", 'yellow'))

        
        for i, password in enumerate(f):
            password = password.strip()  
            
            if hash_type == 'md5':
                hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            elif hash_type == 'sha1':
                hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
            elif hash_type == 'sha256':
                hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            else:
                print(colored(f"Type de hachage invalide: {hash_type}", 'red'))
                return

            
            if hashed_password == hash_value:
                print(colored(f"Mot de passe trouvé: {password}", 'green'))
                return

            
            if verbose and i % 100 == 0:
                print(colored(f"{i}/{num_passwords} mots de passe testés.", 'cyan'))

            print(colored("Aucun mot de passe trouvé dans la wordlist.", 'red'))

hash_type = input("Entrez le type de hachage (md5, sha1 ou sha256) : ")
hash_value = input("Entrez le hash à déchiffrer : ")
wordlist_path = input("Entrez le chemin d'accès à la wordlist (si vous n'en avez pas entrer passwords.txt ): ")
verbose = input("Voulez-vous afficher des informations de progression ? (o/n) : ").lower() == 'o'


crack_hash(hash_value, wordlist_path, hash_type, verbose)
