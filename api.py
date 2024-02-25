from cryptography import fernet
from cryptography.fernet import Fernet
from parameters import *
import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def first_time()-> bool:
    """Check if was the first lauching 

    Returns:
        bool: True if was the first
    """
    if (path_system / 'permission').exists():
        return False
    else:
        return True


def init_salt()-> str:
    """Generate the salt and save it 

    Returns:
        str: the salt
    """
    salt = os.urandom(16)
    edit_data(path_system, 'permission', str(salt).lstrip("b").strip("'"))
    return str(salt).lstrip("b").strip("'")


def init_password(key: Fernet):
    """initialize password 

    Args:
        key: the decryption key
    """
    edit_data(path_system, 'exec', 'Mot de passe valide')
    with open(path_system / 'exec', "rb") as f:
        mdp = f.read()
        with open(path_system / 'exec', "wb") as a:
            a.write(key.encrypt(mdp))


def load_salt()-> str:
    """Load the salt

    Returns:
        str: the salt 
    """
    with open(path_system / 'permission', 'r') as f:
        return f.read()


def define_password(input_user: str, salt: str)-> Fernet:
    """Generate the decryption key

    Args:
        input_user : user's password
        salt : the salt

    Returns:
        Fernet: the decryption key
    """
    password = bytes(input_user, "utf-8")
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=bytes(salt, 'utf-8'),iterations=480000)
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return fernet.Fernet(key)


def check_password(key: Fernet)-> bool: #type: ignore
    """Check if it's the good password

    Args:
        key : the decryption key

    Returns:
        bool: True if it's the good password
    """
    try:
        if decrypt_data(path_system, 'exec', key) == 'Mot de passe valide':
            return True
    except fernet.InvalidToken: 
        return False


def edit_data(path: Path, name: str, mdp: str):
    """Create a file with the password

    Args:
        path : path file
        name : name of the file
        mdp : data store in file
    """
    if not (path / name).exists():
        (path / name).touch()

    with open(path / name, "w") as f:
        f.write(mdp)


def load_data(path: Path, key: Fernet)-> dict:
    """Load all the data

    Args:
        path : path file
        key : the decryption key

    Returns:
        dict : all the data in dict
    """
    all_data = {}
    for file in path.iterdir():
        account_name = file.name.replace(".json", "").capitalize()
        password = decrypt_data(path, account_name, key)
        all_data[account_name] = password
    return all_data
        

def delete_data(name: str):
    """Delete a file

    Args:
        name : name of the file
    """
    if (path_data / name).exists():
        (path_data / name).unlink()


def encrypt_data(path: Path, name: str, key: Fernet):
    """Encrypt the data in file

    Args:
        path : path of the file
        name : name of the file
        key : the decryption key
    """
    with open(path / name, "rb") as f:
        mdp = f.read()
        with open(path / name, "wb") as a:
            a.write(key.encrypt(mdp))


def decrypt_data(path: Path, name: str, key: Fernet) -> str:
    """Decrypte data in file and return data

    Args:
        path : path of the file
        name : name of the file
        key : the decryption key

    Returns:
        str: the decrypt data
    """
    with open(path / name, "rb") as f:
        return str(key.decrypt(f.read())).lstrip("b").strip("'")

